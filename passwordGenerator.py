#PassWord Generator
import random
#classic tkinter
import tkinter as tk


#Function: Generates a random password with the amount characters chosen from input
#Returns the random generated password with X number of characters
def generatePassword():
    characterAmountGiven = int(characterAmountEntry.get())
    password = ''
    randomCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
    for characters in range(characterAmountGiven):
        password += random.choice(randomCharacters)
    aRandomGeneratedPasswordLabel["text"] = password

window = tk.Tk()
window.title("PassWord Generator")
window.resizable(width = False, height = False)


#Frames are used as containers to separate the different sections in your GUI
frame1 = tk.Frame(bg = "black")
intro = tk.Label(master = frame1 , text = "PassWord Generator",fg = "white", bg = "black")
#This is important if you ever want to minimize the GUI the intro text won't be affected
intro.pack(pady = 20)
frame1.pack(fill = tk.BOTH, expand = True)

#frame 2 is the section where you enter the amount of characters you want in the password generated
frame2 = tk.Frame(bg = "black")
characterAmountEnter = tk.Label(master = frame2, text = "Enter Character Amount:",fg = "white",bg = "black")
characterAmountEntry = tk.Entry(master = frame2 , fg = "black", bg= "white", width = 25)
characterAmountEnter.pack()
characterAmountEntry.pack(pady = 20)
frame2.pack(fill = tk.BOTH, expand = True)

#frame 3 is the section in the GUI where the Button is for the function of generating the random password
frame3 = tk.Frame(bg = "black")
generatePasswordButton = tk.Button(master = frame3 , text = "Generate Password",relief=tk.RAISED ,width = 15,height = 5,fg = "black",bg = "white",command = generatePassword)
generatePasswordButton.pack()
frame3.pack(fill = tk.BOTH, expand = True)

frame4 = tk.Frame(bg = "black")
aRandomGeneratedPasswordLabel = tk.Label(master = frame4, text = "Generated Password:", bg = "black")
aRandomGeneratedPasswordLabel.pack()
frame4.pack(fill = tk.BOTH, expand = True)

window.mainloop()


    



    

