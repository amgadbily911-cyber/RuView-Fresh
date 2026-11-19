#!/bin/bash
cd ~/RuView-Fresh
RUN_ID=$(cat .current_run_id)
echo "Watch started for $RUN_ID at $(date)"
while true; do
  STATUS=$(gh run view $RUN_ID --json status,conclusion -q '.status')
  CONCLUSION=$(gh run view $RUN_ID --json status,conclusion -q '.conclusion')
  echo "$(date) status=$STATUS conclusion=$CONCLUSION" >> watch_bg.log
  if [ "$STATUS" = "completed" ]; then
    if [ "$CONCLUSION" = "success" ]; then
      rm -rf apk-download
      mkdir -p apk-download
      gh run download $RUN_ID -n RuView-Light-APK -D apk-download >> watch_bg.log 2>&1
      cp apk-download/*.apk ~/storage/downloads/RuView-Light.apk
      ls -lh ~/storage/downloads/RuView-Light.apk >> watch_bg.log
      termux-notification --title "RuView Light DONE" --content "APK in Downloads - Install now"
      termux-vibrate -d 500
      termux-toast "RuView Light DONE"
      echo "SUCCESS DONE" >> watch_bg.log
      break
    else
      termux-notification --title "RuView BUILD FAILED" --content "Open Termux to see log"
      termux-vibrate -d 1000
      termux-toast "Build FAILED"
      echo "FAILED DONE" >> watch_bg.log
      break
    fi
  fi
  sleep 300
done
