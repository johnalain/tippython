import tkinter as tk
from PIL import ImageTk
root = tk.Tk()
root.title("recipe picker")
# root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth()//2
y = int(root.winfo_screenheight()*0.1)
root.geometry('500x600+'+ str(x)+ '+' + str(y))

frame1 = tk.Frame(root,width=500,height=600,bg='#3d6466')
frame1.grid(row=0,column=0)

logo_img=ImageTk.PhotoImage(file="//Users//michelkadi//Desktop//download (2).ico")
logo_widget=tk.Label(frame1,image=logo_img)
logo_widget.image = logo_img
logo_widget.pack()


root.mainloop()
