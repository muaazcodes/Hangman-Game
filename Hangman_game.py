import PySimpleGUI as sg
from Hangman_solver import HangmanGame   

def hangman_game():
    game = HangmanGame()
    sg.theme("DarkBlue3")

    layout = [
        [sg.Text("Hangman Game", font=("Helvetica", 20), justification="center", expand_x=True)],
        [sg.Text("Word:", size=(8,1)), sg.Text(game.get_display_word(), key="-WORD-", font=("Helvetica", 24))],
        [sg.Text("Stage:")],
        [sg.Multiline(game.get_stage(), size=(30, 10), key="-STAGE-", font=("Courier", 12), disabled=True)],
        [sg.Text("Guess:"), sg.Input(key="-INPUT-", size=(15,1), focus=True), sg.Button("Submit", bind_return_key=False)],
        [sg.Text("", key="-MESSAGE-", size=(50,1), text_color="yellow")],
        [sg.Button("New Game"), sg.Button("Exit")]
    ]

    window = sg.Window("Hangman Game", layout, finalize=True)
    window["-INPUT-"].set_focus()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "New Game":
            game = HangmanGame()
            window["-WORD-"].update(game.get_display_word())
            window["-STAGE-"].update(game.get_stage())
            window["-MESSAGE-"].update("")
            window["-INPUT-"].set_focus()
            continue

        if event == "Submit" and not game.is_over():
            guess = values["-INPUT-"].lower().strip()
            window["-INPUT-"].update("")
            window["-INPUT-"].set_focus()

            if not guess:
                window["-MESSAGE-"].update("Please enter a letter or a word.")
                continue

            if len(guess) == 1:
                game.guess_letter(guess)
            else:
                game.guess_word(guess)

            window["-WORD-"].update(game.get_display_word())
            window["-STAGE-"].update(game.get_stage())
            window["-MESSAGE-"].update(game.get_message())

    window.close()

if __name__ == "__main__":
    hangman_game()
