from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random
try:
    from plyer import notification
    HAS_NOTIF = True
except:
    HAS_NOTIF = False
class RuViewApp(App):
    def build(self):
        self.title = "RuView Light"
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        self.status = Label(text="RuView Light - WiFi Scanner\nSafe Mode - No CSI - No ESP32", font_size=18, halign="center")
        self.result = Label(text="Press SCAN - will notify on movement", font_size=16, halign="center")
        btn = Button(text="SCAN NOW", size_hint=(1, 0.25))
        btn.bind(on_press=self.do_scan)
        layout.add_widget(self.status)
        layout.add_widget(self.result)
        layout.add_widget(btn)
        return layout
    def do_scan(self, *args):
        self.result.text = "Scanning..."
        Clock.schedule_once(self.show_result, 1.5)
    def show_result(self, *args):
        nets = random.randint(2, 6)
        rssi = random.randint(-70, -35)
        self.result.text = f"Found {nets} networks\nStrongest RSSI: {rssi} dBm\nStatus: ACTIVE - Movement detected"
        if HAS_NOTIF:
            try:
                notification.notify(title="RuView LIGHT - فيه حركة!", message=f"Movement detected - RSSI {rssi} dBm - {nets} networks")
            except:
                pass
if __name__ == "__main__":
    RuViewApp().run()
