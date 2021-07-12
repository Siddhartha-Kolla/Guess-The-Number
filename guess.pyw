# Importing some modules needed for the app
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from random import randint

# A App Class
class Guess_The_Number_App(App):

    # A function containing the build of the app
    def build(self):
        # Guess of the Computer
        self.com_guess = randint(1,10)
        # A variable which count the chances
        self.chances = 5

        # Setting the name of the app
        self.title = "Guess The Number"
        Window.size = (800,500)
        self.first_layout = GridLayout(cols=1)

        self.chances_label = Label(text=f"Your chances : {self.chances}",font_size=32)
        self.first_layout.add_widget(self.chances_label)

        self.second_layout = GridLayout(cols=2)

        self.guess_input_label = Label(text="Enter Your Guess here : ",font_size=32)
        self.second_layout.add_widget(self.guess_input_label)

        self.guess_input = TextInput(multiline=False)
        self.second_layout.add_widget(self.guess_input)

        self.first_layout.add_widget(self.second_layout)

        self.submit_button = Button(text="Submit",font_size=32)
        self.submit_button.bind(on_press=self.submit)
        self.first_layout.add_widget(self.submit_button)

        self.result_label = Label(text="",font_size=32)
        self.first_layout.add_widget(self.result_label)

        return self.first_layout
    def submit(self,instance):
        if self.chances > 0:
            self.chances = self.chances-1
            self.chances_label.text = f"Your Chances : {self.chances}"

            if int(self.guess_input.text) == self.com_guess:
                self.result_label.text = "You have won the game"
                self.submit_button.disabled = True
                self.won = True
            elif int(self.guess_input.text) < self.com_guess:
                self.result_label.text = "Your Guess is lesser than the Computer Guess"
            elif int(self.guess_input.text) > self.com_guess:
                self.result_label.text = "Your Guess is greater than the Computer Guess"
            else:
                pass
            self.guess_input.text = ""

        else:
            pass
        if self.chances == 0:
            if not self.won:
                self.submit_button.disabled = True
                self.chances_label.text = "You have lost the game"
            else:
                pass

if __name__ == '__main__':
    Guess_The_Number_App().run()
