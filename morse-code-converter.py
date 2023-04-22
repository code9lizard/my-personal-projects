import os
import time

art = """
  __  __                              _                              _           
 |  \/  |___ _ _ ___ ___   __ ___  __| |___   __ ___ _ ___ _____ _ _| |_ ___ _ _ 
 | |\/| / _ \ '_(_-</ -_) / _/ _ \/ _` / -_) / _/ _ \ ' \ V / -_) '_|  _/ -_) '_|
 |_|  |_\___/_| /__/\___| \__\___/\__,_\___| \__\___/_||_\_/\___|_|  \__\___|_|  
                                                                                 
"""

morse_dict = {
    ".": "dot",
    "-": "dash",
}

alphabet_morse = {
    "a": [".", "-"],
    "b": ["-", ".", ".", "."],
    "c": ["-", ".", "-", "."],
    "d": ["-", ".", "."],
    "e": ["."],
    "f": [".", ".", "-", "."],
    "g": ["-", "-", "."],
    "h": [".", ".", ".", "."],
    "i": [".", "."],
    "j": [".", "-", "-", "-"],
    "k": ["-", ".", "-"],
    "l": [".", "-", ".", "."],
    "m": ["-", "-"],
    "n": ["-", "."],
    "o": ["-", "-", "-"],
    "p": [".", "-", "-", "."],
    "q": ["-", "-", ".", "-"],
    "r": [".", "-", "."],
    "s": [".", ".", "."],
    "t": ["-"],
    "u": [".", ".", "-"],
    "v": [".", ".", ".", "-"],
    "w": [".", "-", "-"],
    "x": ["-", ".", ".", "-"],
    "y": ["-", ".", "-", "-"],
    "z": ["-", "-", ".", "."],
    "1": [".", "-", "-", "-", "-"],
    "2": [".", ".", "-", "-", "-"],
    "3": [".", ".", ".", "-", "-"],
    "4": [".", ".", ".", ".", "-"],
    "5": [".", ".", ".", ".", "."],
    "6": ["-", ".", ".", ".", "."],
    "7": ["-", "-", ".", ".", "."],
    "8": ["-", "-", "-", ".", "."],
    "9": ["-", "-", "-", "-", "."],
    "0": ["-", "-", "-", "-", "-"],
}

print(art)
print("Welcome to the morse converter program!")
while True:
    morse_visual = ""
    user_input = input("Enter a word: ").lower()

    if user_input != "stop":

        for letter in user_input:
            if letter == " ":
                morse_visual += letter
            elif letter not in alphabet_morse:
                print("One of the letter you entered is not in the morse dictionary, please try again.")
                break
            else:
                morse_visual += ("".join(alphabet_morse[letter]) + " ")

        print(morse_visual)

        for morse in morse_visual:
            if morse == " ":
                time.sleep(0.8)
            else:
                os.system(f"afplay sound/{morse_dict[morse]}.wav")
    else:
        break
