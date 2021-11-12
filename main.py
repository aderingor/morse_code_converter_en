morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def translate():
    morse_list = []
    print("Welcome to the Morse Code Translator (EN)")
    word = input("Please enter the word or a number that you want to translate into morse code: ").upper()
    for letter in word:
        if letter not in morse_dict:
            morse_list.append(letter)
        else:
            morse_list.append([morse_dict[letter]])
    print(f"{morse_list}")
    repeat = input("Do you want to run the translator again? (Write Y or N) ").upper()
    if repeat == "Y":
        translate()
    else:
        print("Thanks for using the Morse Code Translator! Good bye. ")
        pass


translate()
