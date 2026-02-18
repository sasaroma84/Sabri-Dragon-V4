'''
SABRI DRAGON V4 - 2060 EDITION
النسخة الغاشمة - جميع أدوات الاختراق
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
import threading
import subprocess
import os

# تعيين الألوان - واجهة الهكر المظلمة
Window.clearcolor = (0.05, 0.05, 0.1, 1)

class TerminalOutput(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output = Label(
            text='[b][color=FFD700]🐉 SABRI DRAGON V4 - TERMINAL[/color][/b]\n' + '='*40 + '\n',
            markup=True,
            size_hint_y=None,
            font_size='14sp',
            halign='left',
            valign='top',
            color=(0, 1, 0, 1)
        )
        self.output.bind(texture_size=self.update_height)
        self.add_widget(self.output)
    
    def update_height(self, *args):
        self.output.height = self.output.texture_size[1]
    
    def append(self, text):
        def update(dt):
            self.output.text = text + '\n' + self.output.text
        Clock.schedule_once(update)

class ToolButton(Button):
    def __init__(self, tool_name, command, **kwargs):
        super().__init__(**kwargs)
        self.tool_name = tool_name
        self.command = command
        self.text = tool_name
        self.size_hint_y = None
        self.height = 50
        self.background_color = (0.2, 0.2, 0.3, 1)
        self.color = (1, 1, 1, 1)
        self.bind(on_press=self.run_tool)
    
    def run_tool(self, instance):
        app = App.get_running_app()
        app.terminal.append(f'[color=FFD700]🚀 تشغيل: {self.tool_name}[/color]')
        
        def run():
            try:
                result = subprocess.getoutput(self.command)
                Clock.schedule_once(lambda dt: app.terminal.append(result))
            except Exception as e:
                Clock.schedule_once(lambda dt: app.terminal.append(f'[color=FF0000]❌ خطأ: {str(e)}[/color]'))
        
        threading.Thread(target=run, daemon=True).start()

class SabriDragonApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        
        # العنوان العلوي
        title = Label(
            text='[b][color=FFD700]🐉 SABRI DRAGON V4 - 2060 EDITION[/color][/b]',
            markup=True,
            size_hint_y=0.1,
            font_size='22sp'
        )
        main_layout.add_widget(title)
        
        # التبويبات للأدوات
        tabs = TabbedPanel(do_default_tab=False, size_hint_y=0.5)
        
        # تبويب الشبكة
        net_tab = TabbedPanelItem(text='Network')
        l1 = BoxLayout(orientation='vertical', padding=10, spacing=5)
        l1.add_widget(ToolButton('🔍 Nmap Scan', 'nmap -sV 127.0.0.1'))
        l1.add_widget(ToolButton('🌍 DNS Lookup', 'nslookup google.com'))
        net_tab.add_widget(l1)
        tabs.add_widget(net_tab)
        
        # تبويب SQL
        sql_tab = TabbedPanelItem(text='SQL')
        l2 = BoxLayout(orientation='vertical', padding=10, spacing=5)
        l2.add_widget(ToolButton('💉 SQLmap Scan', 'sqlmap --version'))
        sql_tab.add_widget(l2)
        tabs.add_widget(sql_tab)
        
        # تبويب Exploit
        exp_tab = TabbedPanelItem(text='Exploit')
        l3 = BoxLayout(orientation='vertical', padding=10, spacing=5)
        l3.add_widget(ToolButton('🎯 Metasploit', 'msfconsole --version'))
        exp_tab.add_widget(l3)
        tabs.add_widget(exp_tab)

        main_layout.add_widget(tabs)
        
        # الطرفية (Terminal) لعرض النتائج
        self.terminal = TerminalOutput(size_hint_y=0.4)
        main_layout.add_widget(self.terminal)
        
        return main_layout

if __name__ == '__main__':
    SabriDragonApp().run()
