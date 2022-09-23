#
import kivy 
kivy.require("2.1.0")
from kivy.app import App
from kivy.uix.label import Label
"""print('hi mama')
print('Greetings: %s'%message)"""
message = 'Hello Mimi Dinosaur!!!! RoaaaaaRRRRRRRRRRR'
# creating a class to inherit from kivy base class 
class MlxApp(App):
    def build(self):
        return Label(text = message)
    
if __name__ == '__main__':
    MlxApp().run()
    
    
