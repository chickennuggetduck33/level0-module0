from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__== "__main__":
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    q=''
    q = simpledialog.askstring(None,prompt="do you know how to code?")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
if q == "yes":
        messagebox.showinfo(message="you will rule the world")
else:
        messagebox.showinfo(message="then sign up for classes at The League")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
pass
