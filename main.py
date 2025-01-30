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
    print("Вы хотите закодировать или раскодировать текст?"
          "\nЕсли закодировать введите:  1"
          "\nЕсли раскодировать введите: 2")
    a = input()
    if a == "1":
        print("Теперь введите текст")
        text = input()
        encode_to_morse(text)
    elif a == "2":
        print("Теперь введите код")
        code = input()
        decode_from_morse(code)
    else:
        print("Введите 1 или 2")
        return
