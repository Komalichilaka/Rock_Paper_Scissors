from tkinter import *
import random

def rock():
    gamelist=["rock","paper","scissors"]
    comp_choice=random.choice(gamelist)
    if(comp_choice=="rock"):
        t.config(text="oh! It's a Tie")
    elif(comp_choice=="paper"):
        t.config(text="Sorry, computer won")
    else:
        t.config(text="Congrats, you won")


def paper():
    gamelist=["rock","paper","scissors"]
    comp_choice=random.choice(gamelist)
    if(comp_choice=="paper"):
        t.config(text="oh! It's a Tie")
    elif(comp_choice=="scissors"):
        t.config(text="Sorry, computer won")
    else:
        t.config(text="Congrats, you won")



def scissors():
    gamelist=["rock","paper","scissors"]
    comp_choice=random.choice(gamelist)
    if(comp_choice=="scissors"):
        t.config(text="oh! It's a Tie")
    elif(comp_choice=="rock"):
        t.config(text="Sorry, computer won")
    else:
        t.config(text="Congrats, you won")


def reset():
    t.config(text="")


window=Tk()
window.geometry("600x600")
window.title("rockpaperscissors")

#rock button
rock_btn=Button(window,font=("Ink free",35),text="Rock",command=rock)
rock_btn.grid(row=1,column=1)

#paper button
paper_btn=Button(window,font=("ink free",35),text="Paper",command=paper)
paper_btn.grid(row=1,column=2)


#scissors button
scissors_btn=Button(window,font=("Ink free",35),text="Scissors",command=scissors)
scissors_btn.grid(row=1,column=3)

#A heading
label=Label(window,font=("Ink free",45),text="choose one")
label.grid(row=0,column=2)

#created labels to make spaces between
space=Label(window,text="",font=("Ink free",35))
space.grid(row=1,column=0)
space2=Label(window,font=("Ink free",35),text="")
space2.grid(row=2,column=1)

#label for the result
t=Label(window,text="",font=("ink free",20))
t.grid(row=3,column=2)

#exit button
exit_btn=Button(window,text="quit",font=("Ink free",20),command=quit)
exit_btn.grid(row=4,column=3)

#reset button 
reset_btn=Button(window,font=("Ink free",20),text="reset",command=reset)
reset_btn.grid(row=4,column=1)



window.mainloop()