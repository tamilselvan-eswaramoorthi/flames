from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.base import EventLoop
from kivy.config import Config

def flames(str1,str2):
    str1.lower()
    str2.lower()
    str1=sorted(str1)
    str2=sorted(str2)
    tem=[]
    for i in range(0,len(str1)):
        if not str1[i]==' ':
            tem.append(str1[i])
    str1=tem
    tem=[]
    for i in range(0,len(str2)):
        if not str2[i]==' ':
            tem.append(str2[i])
    str2=tem
    tem=[]
    temp=list(set(str1)&set(str2))
    t=(len(str1)+len(str2)-len(temp)-len(temp))-1
    words=["Friends","Love","Affection","Marriage","Enemy","Sibling"]
    index=0
    cntr=0
    while len(words)!=1:
        if cntr==t:
            del words[index]
            cntr=0
        index = (index + 1) % len(words)
        cntr+=1 
    
    btn3=Button(text=words[0],font_size=70)
    pop=Popup(content=btn3, title='You Got !',size_hint=(None, None), size=(400, 300))
    pop.open()
    btn3.bind(on_press=pop.dismiss)

class LoginScreen(GridLayout):
    def on_start(self):
        Logger.info('This is a Simple boredom app which gives Your most probable relationsip')

    def __init__(self):
        super(LoginScreen, self).__init__()
        EventLoop.ensure_window()
        EventLoop.window.title = self.title = 'Rockivy | Kivy App Contest 2014'
        self.rows=3
        self.cols=2

        lbl1=Label(text="Your Name :",italic=True, bold=True)
        lbl2=Label(text="The other Name :",italic=True, bold=True)
        txt1=TextInput(multiline=False, font_size=50)
        txt2=TextInput(multiline=False, font_size=50)
        btn1=Button(text="Exit",italic=True)
        btn1.bind(on_press=lambda *a:App.get_running_app().stop())
        btn2=Button(text="OK",italic=True)
        if not txt1=='' or txt2=='':
            btn2.bind(on_press=lambda *a:flames(txt1.text,txt2.text))
        self.add_widget(lbl1)
        self.add_widget(txt1)
        self.add_widget(lbl2)
        self.add_widget(txt2)
        self.add_widget(btn1)
        self.add_widget(btn2)


class SimpleKivy(App):
    def build(self):
        l = Label(text='Hello world')
        return LoginScreen()

if __name__ == "__main__":
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')  # 16:9
    Config.set('graphics', 'resizable', '0')
    SimpleKivy().run() 