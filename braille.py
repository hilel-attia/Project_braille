from gtts import gTTS
import os
brailles = ['⠀', '⠮', '⠐', '⠼', '⠫', '⠩', '⠯', '⠄', '⠷', '⠾', '⠡', '⠬', '⠠', '⠤', '⠨', '⠌', '⠴', '⠂', '⠆', '⠒', '⠲',
            '⠢',
            '⠖', '⠶', '⠦', '⠔', '⠱', '⠰', '⠣', '⠿', '⠜', '⠹', '⠈', '⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚',
            '⠅',
            '⠇', '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', '⠪', '⠳', '⠻', '⠘', '⠸']

asciicodes = [' ', '!', '"', '#', '$', '%', '&', '', '(', ')', '*', '+', ',', '-', '.', '/',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '[', '\\', ']', '^', '_']


def save(txt):
    f = open("Braille.txt", "w", encoding="Utf-8")
    f.write(txt)
    f.close()


def textToBraille(text):
    final_string = ''
    for char in text:
        char = char.lower()

        if char == "a":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "b":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "c":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "d":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "e":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "f":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "g":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "h":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "i":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "j":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "k":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "l":
            final_string = final_string + brailles[asciicodes.index(char)]

        elif char == "m":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "n":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "o":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "p":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "q":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "r":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "s":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "t":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "u":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "v":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "w":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "x":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "y":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == "z":
            final_string = final_string + brailles[asciicodes.index(char)]
        elif char == " ":
            final_string = final_string + brailles[asciicodes.index(char)]

    return (final_string)

def text_to_speech(txt,lg):
    language = lg
    myobj = gTTS(text=txt, lang=language, slow=False)
    myobj.save("output.mp3")
    os.system("start output.mp3")
def textFile_to_speech():
    fh = open("test.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    fh.close()
    os.system("start output.mp3")

def Menu():
		x = -1
		while(x < 1 or x > 6 ):
			print('==============================')
			print('| 1 - text to braille        |')
			print('| 2 - text to speech         |')
			print('| 3 - text file to speech    |')
			print('| 4 - exit 			        |')
			print('==============================')
			x = int(input('\nEnter menu option: '))
			os.system("cls")
		return x


x = Menu()

while (x != 4):
    if (x == 1):
        ch=input("TEXT :")
        save(textToBraille(ch))
    if (x == 2):
        ch = input("TEXT :")
        lg = input("Language :")
        text_to_speech(ch,lg)
    if (x == 3):
        textFile_to_speech()

    x = Menu()

#save(textToBraille("hilel"))
#text_to_speech("hilel from tunisia")
#textFile_to_speech()


