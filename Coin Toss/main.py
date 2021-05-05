from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import random
from kivymd.color_definitions import colors


class DemoApp(MDApp):
    title = "COIN TOSS"


    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = '300'

        screen = Screen()
        return Builder.load_file('toss.kv')

    def show_MDDialog(self, wrongvalue=None):
        my_dialog = MDDialog(title="Wrong Input", text="Kindly please Enter the right value either HEADS OR TAILS. You have enter "+wrongvalue, size_hint = [.5,.5])
        my_dialog.open()

    def clear(self):
        self.root.ids.result.text = ""
        self.root.ids.actualtoss.text = ""
        self.root.ids.cointoss.text = ""

    def play(self):
        # playing = True
        # while playing == True:
        coin = ["heads", "tails"]
        toss = random.choice(coin)

        selection = self.root.ids.cointoss.text

        if selection != " ":
            if selection.lower() == "heads" or selection.lower() == "tails":

                if selection.lower() == toss:
                    print("The actual toss is", toss)
                    print("You Won")
                    self.root.ids.result.text = "You WON"
                    self.root.ids.actualtoss.text = toss
                else:
                    self.root.ids.result.text = "You LOOSE"
                    self.root.ids.actualtoss.text = toss
            else:
                self.show_MDDialog(selection)
        else:
            self.show_MDDialog(selection)


DemoApp().run()
