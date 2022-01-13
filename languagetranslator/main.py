from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Language translator')
root.geometry("910x300")


def translate_it():
    translatedtext.delete(1.0, END)
    try:
        for key, value in languages.items():
            if value == originalComb.get():
                from_language_key = key

        for key, value in languages.items():
            if value == translateBox.get():
                to_language_key = key

        words = textblob.TextBlob(originaltext.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translatedtext.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)


def clear():
    originaltext.delete(1.0, END)
    translatedtext.delete(1.0, END)


language_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28)


# language list from googletrans
languages = googletrans.LANGUAGES

# converted into a list
language_list = list(languages.values())
print(language_list)


# creating the text boxes


originaltext = Text(root, height =10, width=40)
originaltext.grid(row=0, column=0, pady=20, padx=10)

translateButton = Button(root, text='Translate it!', font=('Helvetica', 24), command=translate_it)
translateButton.grid(row=0, column=1, padx=10)

translatedtext = Text(root, height =10, width=40)
translatedtext.grid(row=0, column=2, pady=20, padx=10)

# drop down lists
originalComb = ttk.Combobox(root, width=50, value=language_list)
originalComb.current(21)
originalComb.grid(row=2, column=0)

translateBox = ttk.Combobox(root, width=50, value=language_list)
translateBox.current(26)
translateBox.grid(row=2, column=2)

# clear button
clearButton = Button(root, text="Clear", command=clear)
clearButton.grid(row=2, column=1)
root.mainloop()
