from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: 10
    padding: 10

    TextInput:
        id: input
        font_size: 32
        multiline: False
        halign: "right"
        size_hint: (1, 0.2)

    GridLayout:
        cols: 4
        spacing: 10
        size_hint: (1, 0.8)

        Button:
            text: "7"
            on_press: input.text += self.text
        Button:
            text: "8"
            on_press: input.text += self.text
        Button:
            text: "9"
            on_press: input.text += self.text
        Button:
            text: "/"
            on_press: input.text += self.text

        Button:
            text: "4"
            on_press: input.text += self.text
        Button:
            text: "5"
            on_press: input.text += self.text
        Button:
            text: "6"
            on_press: input.text += self.text
        Button:
            text: "*"
            on_press: input.text += self.text

        Button:
            text: "1"
            on_press: input.text += self.text
        Button:
            text: "2"
            on_press: input.text += self.text
        Button:
            text: "3"
            on_press: input.text += self.text
        Button:
            text: "-"
            on_press: input.text += self.text

        Button:
            text: "C"
            on_press: input.text = ""
        Button:
            text: "0"
            on_press: input.text += self.text
        Button:
            text: "="
            on_press:
                try: input.text = str(eval(input.text))
                except: input.text = "Error"
        Button:
            text: "+"
            on_press: input.text += self.text
'''

class CalculatorApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    CalculatorApp().run()
