# Importing tkinter libraries for GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
# Importing text to speech (pyttsx3) library, speech recognition library
import pyttsx3
import speech_recognition as sr
# Importing Wolfram and Wikipedia library to parse data
import wolframalpha
import wikipedia

# Initializing variable engine to read aloud text or code
engine = pyttsx3.init()
engine.say("Welcome, How can I help you?")
engine.runAndWait()


# Method which retrieves user inputted data and returns the answer using the above mentioned libraries
def VAssist():
    user_input = search_bar.get()
    search_bar.delete(0, "end")
    if user_input == "":
        tk.messagebox.showerror(title='Error', message="Please state your question!")
    else:
        # A GUI to show the answer if user input is not blank
        gui = tk.Tk()
        gui.geometry("450x250")
        f = tk.Frame(gui, width=500, height=350, background="bisque")
        f.pack(fill=BOTH, expand=YES)

        # try - except block to determine the answer from the two libraries
        try:
            app_id = "7UH6G2-EJEEY55KEY"  # Wolframalpha id
            client = wolframalpha.Client(app_id)

            res = client.query(user_input)
            answer = next(res.results).text

            engine.say(answer)
            engine.runAndWait()
            ans = Label(f, text='Ans: ' + '\n' + str(answer), background="bisque", fg="#4d4dff", wraplengt=450,
                        justify="left")
            ans.config(font=("Montserrat", 5))
            ans.place(relx=0.01, rely=0.3, anchor="w")
        except:
            ans = Label(f, text='\n' + 'Ans: ' + '\n' + str(wikipedia.summary(user_input, sentences=2)),
                        background="bisque", fg="#4d4dff", wraplengt=450, justify="left")
            ans.config(font=("Montserrat", 5))
            ans.place(relx=0.01, rely=0.3, anchor="w")
            engine.say(wikipedia.summary(user_input, sentences=2))
            engine.runAndWait()


# method for speech recognition when microphone button is pressed
def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Please verbally state your question!")
        engine.runAndWait()
        audio = r.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            search_bar.insert(0, str(r.recognize_google(audio)))
            VAssist()  # returns to above VAssist() method to determine the answer

        # Two except blocks to determine audio error and Google Speech Recognition Server error
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            tk.messagebox.showerror(title='Error', message="Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


# The main code which constructs the initial GUI
root = tk.Tk()
root.geometry("450x250")
frame1 = tk.Frame(root, width=500, height=350, background="bisque")
frame1.pack(fill=BOTH, expand=YES)
welcome_label = Label(frame1, text='Welcome!', background="bisque", fg="#4d4dff")
welcome_label.config(font=("Playfair Display", 28))
Help_label = Label(frame1, text='How can I help you?', background="bisque", fg="#4d4dff")
Help_label.config(font=("Open Sans", 18))
Help_label.place(relx=0.05, rely=0.35, anchor='w')
search_bar = Entry(frame1, bg="white", font=("Roboto", 15), width=35)
search_bar.place(relx=0.5, rely=0.58, anchor="c")
Search_button = tk.Button(frame1, text='Okay', width=15, command=VAssist, bg="silver")
Search_button.place(relx=0.42, rely=0.75, anchor="c")
Mic_photo = PhotoImage(file=r"C:\Users\Krises Maskey\Downloads\echnology.png")
Mic_button = tk.Button(frame1, image= Mic_photo, command=voice, width=25, bg="silver")
Mic_button.place(relx=0.62, rely=0.75, anchor="c")
root.tk.call('tk', 'scaling', 4.0)
welcome_label.pack()
root.mainloop()
