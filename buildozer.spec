[app]
title = RuView Light
package.name = ruviewlight
package.domain = org.ruview.light
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,plyer
orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.permissions = ACCESS_WIFI_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,POST_NOTIFICATIONS,VIBRATE,FOREGROUND_SERVICE
[buildozer]
log_level = 2
warn_on_root = 1
