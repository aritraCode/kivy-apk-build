from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.count = 0
        self.button = Button(text="Click Me!", font_size=24, on_press=self.on_button_click)
        layout = BoxLayout()
        layout.add_widget(self.button)
        return layout

    def on_button_click(self, instance):
        self.count += 1
        self.button.text = f"Clicked {self.count} times"

if __name__ == "__main__":
    MyApp().run()
