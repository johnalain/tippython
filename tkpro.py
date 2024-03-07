import tkinter as tk
from PIL import ImageTk
bg_color = "28392a"
def load_frame1():
    frame1.pack_propagate(False)
# logo widget
    logo_img=ImageTk.PhotoImage(file="//Users//michelkadi//Desktop//download (2).ico")
    logo_widget=tk.Label(frame1,image=logo_img,bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()
#https://youtu.be/5qOnzF7RsNA?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81&t=576
#instruction widget
    tk.Label(frame1, text = 'ready for your random recipes',
         bg=bg_color,fg='white',
         font=('TkMenuFont',14)).pack(pady=30)
#button widget
    tk.Button(frame1,text='SHUFFLE',
          font = ('TkHeadingFont',20),bg='white',
          fg='white',cursor='hand2',
          activebackground='#badee2',
          activeforeground='black',
          command=lambda:load_frame2()).pack(pady=20)
    
def load_frame2():
    print('hello Mariya')
bg_color = '#3f6436'
#initialize application
root = tk.Tk()
root.title("recipe picker")
# root.eval("tk::PlaceWindow . center")
##place application in the center of the screen
x = root.winfo_screenwidth()//2
y = int(root.winfo_screenheight()*0.1)
root.geometry('500x600+'+ str(x)+ '+' + str(y))
#create a frame widget
frame1 = tk.Frame(root,width=500,height=600,bg=bg_color)
frame2 = tk.Frame(root,bg=bg_color)
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=0)
for frame in (frame1,frame2):
    frame.grid(row=0,column=0)

load_frame1()
#https://youtu.be/5qOnzF7RsNA?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81&t=1198 


#run application
root.mainloop()
