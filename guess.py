# Modules that are needed for the App
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from random import randint
from kivy.uix.popup import Popup


# A App Class
class Guess_The_Number_App(App):

    # build of the App
    def build(self):

        # icon of the App
        self.icon = 'logo.png'

        # title of the App
        self.title = "Guess The Number"

        # size of the app
        Window.size = (800, 500)

        # the guess of the computer
        self.com_guess = randint(1, 10)

        # count of the chances
        self.chances = 5

        # setting a boolean for not getting problems in the end
        self.won = False

        # Creating a Grid Layout with 1 column
        self.first_layout = GridLayout(cols=1)

        # show the how many chances are left
        self.chances_label = Label(text=f"Your chances : {self.chances}", font_size=32)
        # adding to the Grid Layout
        self.first_layout.add_widget(self.chances_label)

        # adding a second Grid Layout with 2 columns
        self.second_layout = GridLayout(cols=2)

        # Label for the Users Text Input Box
        self.guess_input_label = Label(text="Enter Your Guess here : ", font_size=32)
        self.second_layout.add_widget(self.guess_input_label)

        # A Text Input Box which takes the input from the user
        self.guess_input = TextInput(multiline=False, font_size=32)
        self.second_layout.add_widget(self.guess_input)

        # adding the second Grid Layout to the first Grid Layout
        self.first_layout.add_widget(self.second_layout)

        # Creating a submit Button and binding it to a function
        self.submit_button = Button(text="Submit", font_size=32)
        self.submit_button.bind(on_press=self.submit)
        self.first_layout.add_widget(self.submit_button)

        # Show the state of the number User gave
        self.result_label = Label(text="", font_size=32)
        self.first_layout.add_widget(self.result_label)

        # displaying the Grid Layout in the App
        return self.first_layout

    # function to check the sate of the User's Input
    def submit(self, instance):
        # Exceptional Handling for Wrong Data Type
        try:
            # Taking the guess input
            self.user_guess = int(self.guess_input.text)
            # checking if the chances are more than zero
            if self.chances > 0:
                # reducing the chances count and updating the chances Label
                self.chances = self.chances - 1
                self.chances_label.text = f"Your Chances : {self.chances}"

                # Checking if the users guess matches to the computers guess
                if self.user_guess == self.com_guess:

                    # setting the result label that the user has won the game
                    self.result_label.text = "You have won the game"
                    # disabling the button so that they won click it again
                    self.submit_button.disabled = True
                    # setting the won boolean to True
                    self.won = True
                    # opening the won label
                    self.popups("won")

                # checking if the users guess is lesser than the computer
                elif self.user_guess < self.com_guess:
                    # setting the result label that the user's guess is lesser than the computer guess
                    self.result_label.text = "Your Guess is lesser than the Computer Guess"

                # checking if the users guess is lesser than the computer
                elif self.user_guess > self.com_guess:
                    # setting the result label that the user's guess is lesser than the computer guess
                    self.result_label.text = "Your Guess is greater than the Computer Guess"
                # creating a else function and setting it to pass
                else:
                    pass
                # Clearing the Guess Input Box
                self.guess_input.text = ""

            # Checking if the player has lost the game
            if self.chances == 0 and not self.won:
                # Disabling the Submit Button
                self.submit_button.disabled = True
                # Informing that the player has lost the game
                self.chances_label.text = "You have lost the game"
                # Open the reset popup
                self.popups("lost")

            # creating a else function and setting it to pass
            else:
                pass
        # Showing a Popup Box that the player has entered a wrong data type
        except:
            self.error_popup_content = BoxLayout(orientation="vertical")
            self.error_label = Label(text="Entered Wrong Data Type.\nPlease Enter a number", font_size=20)
            self.error_ok_button = Button(text="OK", font_size=32)

            self.error_popup_content.add_widget(self.error_label)
            self.error_popup_content.add_widget(self.error_ok_button)

            self.error_popup = Popup(title="Wrong Data Type", content=self.error_popup_content, auto_dismiss=False,
                                     size_hint=(None, None), size=(400, 200))
            self.error_popup.open()

            self.error_ok_button.bind(on_press=self.error_popup.dismiss)
            self.guess_input.text = ""

    # creating a popup function where reset popups are stored
    def popups(self, state):
        # setting a variable with a BoxLayout as its content for the reset popup
        self.reset_popup_content = BoxLayout(orientation="vertical")
        # creating a label to show to reset the game
        self.reset_label = Label(
            text=f"You have {state} the game!\nThe computer guessed {self.com_guess}.\nDo you like to reset the game?",
            font_size=20)
        # creating a Grid Layout withe yes and no buttons
        self.reset_buttons_grid = GridLayout(cols=2)
        self.yes_btn = Button(text="Yes", font_size=20)
        self.no_btn = Button(text="No", font_size=20)

        # adding all widgets to the main content
        self.reset_buttons_grid.add_widget(self.yes_btn)
        self.reset_buttons_grid.add_widget(self.no_btn)
        self.reset_popup_content.add_widget(self.reset_label)
        self.reset_popup_content.add_widget(self.reset_buttons_grid)

        # declaring the popup inside a variable and setting some modules
        self.reset_popup = Popup(title="Reset the Game?", content=self.reset_popup_content, auto_dismiss=False,
                                 size_hint=(None, None), size=(400, 200))

        # binding yes and no button from the popup content to the perspective functions
        self.yes_btn.bind(on_press=self.reset)
        self.no_btn.bind(on_press=self.reset_popup.dismiss)

        # opening the popup
        self.reset_popup.open()

    # creating a reset function to reset the game
    def reset(self, instance):
        # closing the reset popup box
        self.reset_popup.dismiss()
        # clearing the reset label
        self.result_label.text = ""
        # enabling the submit button
        self.submit_button.disabled = False
        # setting the won boolean to False
        self.won = False
        # changing the computer guess
        self.com_guess = randint(1, 10)
        # setting the chances to 5
        self.chances = 5
        # updating the chances label with new chances
        self.chances_label.text = f"Your Chances : {self.chances}"

# running the app
if __name__ == '__main__':
    Guess_The_Number_App().run()
