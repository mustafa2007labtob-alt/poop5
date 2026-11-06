rom kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # 1. إنشاء Layout رئيسي
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 2. إنشاء Label (النص)
        self.label = Label(text="click the button", font_size=20)
        
        # 3. إنشاء Button (الزر)
        btn = Button(text="click here", font_size=18)
        
        # ربط حدث الضغط بدالة معينة (Binding)
        btn.bind(on_press=self.on_button_click)
        
        # إضافة العناصر للـ Layout باستخدام add_widget
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def on_button_click(self, instance):
        # تغيير نص الـ Label برمجياً
        self.label.text ="you are click the button"

if __name__ == '__main__':
    MyApp().run()

