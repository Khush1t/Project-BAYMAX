from chatterbot import Cbot
from chatterbot.trainers import L_Train
from tkinter import *

# calling the audio recognition library
import pyttsx3 as pp

# initialising the pp function
engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(word):    # accessing voices through speak function from engine variable
    engine.say(word)
    engine.runAndWait()


bot = Cbot("Baymax-bot")    #object Cbot is made

# training the Chatbot with conversation
convo = [
    "Hi"
    "Hello! I am Baymax."
    "Hey there!"
    "How are you?"
    "I am doing great these days."
    "How are college classes going?"
    "I need some help!"
    "Who made you?"
    "Best for Electrical : https://www.youtube.com/channel/UCltVEZ6GecWntoZ19FvaWhQ"
    "All the remaining subjects of group B : https://drive.google.com/drive/u/0/folders/0B6eUQ5fyKy1FNmJsanB4SXNVSEk"
    "I am a bot, made by Khushwant and Ananya."
    "Please elaborate your problem!"
    "No worries I am always here for help ;)"
    "This is for the Drawing subject : https://www.youtube.com/channel/UCNQHebTzfRahptcsmuOVufg"
    "I am providing you with the resources which you may find useful."
    "For Mathematics, you can refer the following link : https://drive.google.com/drive/u/0/folders/0B6eUQ5fyKy1FclR1Uk9XR2lPNnc"
    "Anything else you want help with?"
    "No Thank you"
    "For Physics, you can check this out : https://drive.google.com/drive/u/0/folders/0B6eUQ5fyKy1FQno2N095aTRkWHM"
    "This link is for the common subjects : https://drive.google.com/drive/u/0/folders/0B6eUQ5fyKy1FbXJ5UVpDTHBoWlE"
    "I am Sorry, I couldn't get you!"
    "Ok! Bubye, Have a great day :)"
]

trainer = L_Train(bot)  # L_train object with reference to the bot
trainer.train(convo)    # invoking the trained data into text


# creating a new window for storing chats
main = Tk()
main.geometry("500x600")
main.title("BAYMAX")


# text screen where responses are shown
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msg.insert(END, "User : " + query)
    msg.insert(END, "Baymax : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msg.yview(END)


# creating scrollbar
frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)

msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

# creating text field
textF = Entry(main, font=("Verdana", 15))
textF.pack(fill=X, pady=20)

# creating input button
btn = Button(
    main,
    text="SEND",
    bg="lightblue",
    fg="black",
    activebackground="black",
    font=("Verdana", 15),
    command=ask_from_bot,
)
btn.pack()

# invoking enter key press


def enter_function(event):  
    btn.invoke()


# now you can press return key to send the message
main.bind("<Return>", enter_function)

# closing the separate chat window
main.mainloop()
