#https://www.loom.com/share/42b8944871534f08845adebd8edf4975



from tkinter import *
import random 
root = Tk()
root.title("Colour Changer")
root.geometry("500x500")



dictionary1 = {"colour":["light blue","blue","aqua","orange","dark orange","navajowhite","coral","lime","yellow","tan","firebrick","red","peach"]}


def randomColor():
    ran = random.randint(0,11)
    print(ran)  
    root.configure(background = dictionary1["colour"][ran])

btn = Button(root,text = "click me",command = randomColor)
btn.place(relx = 0.5,rely = 0.5,anchor = CENTER)

root.mainloop()