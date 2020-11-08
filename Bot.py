
import PySimpleGUI as sg
from utils import get_meaning, get_synonyms, get_antonyms

greeting = "Hi, I am a word bot. I can help you with words\n"

layout = [
    [sg.Multiline(greeting, font=("Arial", 14), size=(70, 15), key='output')],
    [sg.InputText("", font=("Arial", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Arial", 14), bind_return_key=True, key='meaning'),
     sg.Button("Synonyms", font=("Arial", 14), key='synonym'),
     sg.Button("Antonyms", font=("Arial", 14), key='antonym'),
     sg.Button("Clear", font=("Arial", 14), key='clear')
    ]
]

def display_meaning(word):
    meaning = get_meaning(word)
    window['output'].print("WORD: " + word)
    if meaning:
        window['output'].print("MEANING: ", meaning + ".")
    else:
        display_error("Word is not found in corpus.")

def display_synonyms(word):
    synonyms = get_synonyms(word)
    window['output'].print("WORD: "+ word)
    if synonyms:
        window['output'].print("SYNONYMS: ")
        for synonym in synonyms:
            if synonym != synonyms[-1]:
                window['output'].print(synonym, end =", ")
            else:
                window['output'].print(synonym + ".")
    else:
        display_error("Word is not found in corpus")

def display_antonyms(word):
    antonyms = get_antonyms(word)
    window['output'].print("WORD: "+ word)
    if antonyms:
        window['output'].print("SYNONYMS: ")
        for antonym in antonyms:
            if antonym != antonyms[-1]:
                window['output'].print(antonym, end =", ")
            else:
                window['output'].print(antonym + ".")
    else:
        display_error("Word is not found in corpus")

def display_error(message):
    """
    Displays an error message in the output window
    :param message: string, the error message to be displayed
    """
    window['output'].print("ERROR: " + message, text_color='red')


if __name__ == '__main__':
    window = sg.Window('File Explorer', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonym':
            display_synonyms(values['input'])
        elif event == 'antonym':
            display_antonyms(values['input'])
        elif event == 'clear':
            window.FindElement('output').Update(value = greeting)
    window.Close()