from tkinter import *
import speech_recognition as speech

authorized = False
c = 1
def success():
    suc_screen = Tk()
    suc_screen.geometry("250x70")
    suc_screen.title("Logged In :)")
    Label(suc_screen, text='Successfully logged in', fg='green').pack()
    suc_screen.mainloop()

def failed():
    fail_screen = Tk()
    fail_screen.geometry("260x100")
    fail_screen.title("Failed to Login :(")
    Label(fail_screen, text='Your credentials are not correct', fg='red').pack()
    Label(fail_screen, text='You have been locked out', fg='red').pack()
    fail_screen.mainloop()

def login():
    global c
    if authorized == True:
        login_screen.destroy()
        success()
    elif(c==3):
        login_screen.destroy()
        failed()
    else:
        message.set("Credentials not Authorized")
        c+=1

def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("200x95")
    global message
    message = StringVar()
    Label(login_screen, text="", textvariable=message).place(x=25, y=10)
    Button(login_screen, text="Authenticate", width=20, height=1, bg="orange", command=COMMAND).place(x=25, y=40)
    login_screen.mainloop()

def COMMAND():
  
    global authorized
    command=""
    voice = speech.Recognizer()
    with speech.Microphone() as source:
        voice_command = voice.listen(source)
    try:
        command = voice.recognize_google(voice_command)
    except speech.UnknownValueError:
        print("Google Speech Recognition system could not understand your instructions please give instructions carefully")
    except speech.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if command == "hello":
        authorized = True
    elif command == "Archit password boom":
        authorized = True
    elif command == "Ashish password hello":
        authorized = True
    else:
        authorized = False
    authorized = True
    login()

Loginform()