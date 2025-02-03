text = ""
code = ""
MorseCode = {"a": ".-",
             "b": "-...",
             "c": "-.-.",
             "d": "-..",
             "e": ".",
             "f": "..-.",
             "g": "--.",
             "h": "....",
             "i": "..",
             "j": ".---",
             "k": "-.-",
             "l": ".-..",
             "m": "--",
             "n": "-.",
             "o": "---",
             "p": ".--.",
             "q": "--.-",
             "r": ".-.",
             "s": "...",
             "t": "-",
             "u": "..-",
             "v": "...-",
             "w": ".--",
             "x": "-..-",
             "y": "-.--",
             "z": "--.."}

MorseCodeInversion = {".-": "a",
                      "-...": "b",
                      "-.-.": "c",
                      "-..": "d",
                      ".": "e",
                      "..-.": "f",
                      "--.": "g",
                      "....": "h",
                      "..": "i",
                      ".---": "j",
                      "-.-": "k",
                      ".-..": "l",
                      "--": "m",
                      "-.": "n",
                      "---": "o",
                      ".--.": "p",
                      "--.-": "q",
                      ".-.": "r",
                      "...": "s",
                      "-": "t",
                      "..-": "u",
                      "...-": "v",
                      ".--": "w",
                      "-..-": "x",
                      "-.--": "y",
                      "--..": "z"}


def encode_to_morse(text):
    text = text.lower()
    for i in text.split():
        print(*[MorseCode[j] for j in i])


def decode_from_morse(code):
    code = code.lower().split()
    for i in code:
        print(*[MorseCodeInversion[j] for j in i])


def main():
    global text
    global code
    a = input("Вы хотите закодировать или раскодировать текст?"
          "\nЕсли закодировать введите:  1"
          "\nЕсли раскодировать введите: 2")
    print("Введите 1 или 2") if a not in ['1', '2'] else encode_to_morse(input("Теперь введите текст")) if a == "1" \
        else decode_from_morse(input("Теперь введите код"))

