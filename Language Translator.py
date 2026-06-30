#!pip install googletrans==3.1.0a0
#!pip install gTTS
#!pip install tk==0.1.0

from googletrans import Translator
from gtts import gTTS
from tkinter import *

window = Tk()
window.title("Language Translator")
window.geometry("600x280")
window.config(bg = "black")
e1 = Entry(window, bg = "white", fg = "black", font = ("Calibri", 22, "bold" ))
e1.place(x = 20, y = 20)

def convert_language():
    a1 = e1.get()
    t1 = Translator()
    t2 = click_option.get()
    
    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "German":
        convert = "de"
    elif t2 == "French":
        convert = "fr"
    elif t2 == "Spanish":
        convert = "es"
    elif t2 == "Russian":
        convert = "ru"
    elif t2 == "Arabic":
        convert = "ar"
    elif t2 == "Belarusian":
        convert = "be"
    elif t2 == "Bulgarian":
        convert = "bg"
    elif t2 == "Czech":
        convert = "cs"
    elif t2 == "Welsh":
        convert = "cy"
    elif t2 == "Danish":
        convert = "da"
    elif t2 == "Greek":
        convert = "el"
    elif t2 == "Esperanto":
        convert = "eo"
    elif t2 == "Estonian":
        convert = "et"
    elif t2 == "Finnish":
        convert = "fi"
    elif t2 == "Irish":
        convert = "ga"
    elif t2 == "Scottish Gaelic":
        convert = "gd"
    elif t2 == "Hungarian":
        convert = "hu"
    elif t2 == "Armenian":
        convert = "hy"
    elif t2 == "Indonesian":
        convert = "id"
    elif t2 == "Icelandic":
        convert = "is"
    elif t2 == "Italian":
        convert = "it"
    elif t2 == "Japanese":
        convert = "ja"
    elif t2 == "Korean":
        convert = "ko"
    elif t2 == "Lithuanian":
        convert = "lt"
    elif t2 == "Latvian":
        convert = "lv"
    elif t2 == "Mongolian":
        convert = "mn"
    elif t2 == "Moldavian":
        convert = "mo"
    elif t2 == "Nepali":
        convert = "ne"
    elif t2 == "Dutch":
        convert = "nl"
    elif t2 == "Norwegian":
        convert = "nn"
    elif t2 == "Polish":
        convert = "pl"
    elif t2 == "Portuguese":
        convert = "pt"
    elif t2 == "Romanian":
        convert = "ro"
    elif t2 == "Slovak":
        convert = "sl"
    elif t2 == "Albanian":
        convert = "sq"
    elif t2 == "Serbian":
        convert = "sr"
    elif t2 == "Swedish":
        convert = "sv"
    elif t2 == "Thai":
        convert = "th"
    elif t2 == "Turkish":
        convert = "tr"
    elif t2 == "Ukrainian":
        convert = "uk"
    elif t2 == "Vietnamese":
        convert = "vi"
    elif t2 == "Yiddish":
        convert = "yi"
    elif t2 == "Chinese":
        convert = "chi"
    elif t2 == "Marathi":
        convert = "mr"
        
    trans_text = t1.translate(a1, dest = convert)
    trans_text = trans_text.text
    ob1 = gTTS(text = trans_text, slow = False, lang = convert)
    label_2.config(text = trans_text)

choices = [
    "English", 
    "Hindi", 
    "German", 
    "French", 
    "Spanish", 
    "Russian", 
    "Arabic", 
    "Belarusian", 
    "Bulgarian", 
    "Czech", 
    "Welsh", 
    "Danish",
    "Greek",
    "Esperanto",
    "Estonian",
    "Finnish",
    "Irish",
    "Scottish Gaelic",
    "Hungarian",
    "Armenian",
    "Indonesian",
    "Icelandic",
    "Italian",
    "Japanese",
    "Korean",
    "Lithuanian",
    "Latvian",
    "Mongolian",
    "Moldavian",
    "Nepali",
    "Dutch",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Slovak",
    "Albanian",
    "Serbian",
    "Swedish",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Vietnamese",
    "Yiddish",
    "Chinese",
    "Marathi",
]
    
click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices)
list_drop.configure(background = "green", foreground = "white", font = ("Arial", 15, "bold"))
list_drop.place(x = 400,y = 20)

label_2 = Label(window, text = "\t\t\t\t\t\t", bg = "black", fg = "white", font = ("Arial", 40, "bold"))
label_2.place(x = 0,y = 120)
label_2 = Label(window, text = "Translated Text", bg = "black", fg = "white", font = ("Arial", 40, "bold"))
label_2.place(x = 180,y = 120)

Button_1 = Button(window, text = "Translate", bg = "red", fg = "white", font = ("Arial", 25, "bold"), command = convert_language)
Button_1.place(x = 220,y = 200)
        
window.mainloop()