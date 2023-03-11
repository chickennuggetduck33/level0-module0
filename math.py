from tkinter import messagebox, simpledialog, Tk
import random

window = Tk()
window.withdraw()
while True:
    play = messagebox.askyesno(title='play',message="would you like to play")
    if play == True:
        for i in range(5):
            outlaw = random.randint(0, 10)
            sheriff = random.randint(3, 10)
            print(outlaw)
            print(sheriff)
            messagebox.showinfo(None, message="The outlaw's score is score is "+str(outlaw)+" and the sheriff's score is "+str(sheriff))
    else:
        messagebox.showinfo(None, message="too bad so sad")
        
