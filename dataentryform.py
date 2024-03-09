#https://youtu.be/vusUfPBsggw
import tkinter

window = tkinter.Tk()
window.title('data entry form')

#placing widget on screen
frame = tkinter.Frame(window)
frame.pack()
user_info_frame = tkinter.LabelFrame(frame,text=('user information'))
user_info_frame.grid(row=0,column=0)

first_name_label=tkinter.Label(user_info_frame,text=('first name'))
first_name_label.grid(row=0,column=0)
#https://youtu.be/vusUfPBsggw?t=789

window.mainloop()