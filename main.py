from tkinter import *
from time import time, ctime

root= Tk()
root.title("SMART PADALA")
root.iconbitmap(".\\assets\\icon.ico")
root.geometry("400x400")

# Buttons

# Root Labels
time_label = Label(root, text=ctime())
time_label.grid(row = 0, column = 0, columnspan=2)

# Frame 1
frame1 = LabelFrame(root, borderwidth = 0)
frame1.grid(row = 1, column = 0, pady =(10,10), padx=(0,10))
# frame1 labels
cash_on_hand = Label(frame1, text="Cash on hand:")
cash_on_hand.grid(row=0, column= 0, sticky = W)
cash_in_padala = Label(frame1, text="Cash in Padala:")
cash_in_padala.grid(row=1, column = 0, sticky = W)

# frame2
frame2 = LabelFrame(root, borderwidth = 0)
frame2.grid(row = 1, column = 1,pady =(10,10), padx=(0,10))
# frame2 labels
today = Label(frame2, text = "Today's")
today.grid(row=0, column=0)
earnings = Label(frame2, text = "Earnings:")
earnings.grid(row=1, column=0, sticky = W)
no_of_padala = Label(frame2, text = "No. of Padala:")
no_of_padala.grid(row=2, column=0, sticky = W)
no_of_claims = Label(frame2, text = "No. of Claims:")
no_of_claims.grid(row=3, column=0, sticky = W)
total_padala = Label(frame2, text = "Total Padala:")
total_padala.grid(row=4, column=0, sticky = W)
total_claims = Label(frame2, text = "Total Claims:")
total_claims.grid(row=5, column=0, sticky = W)

# Frame Add and refresh
frameAR = LabelFrame(root, borderwidth = 0)
frameAR.grid(row = 2, column = 0, columnspan=2, padx = 10)
add_button = Button(frameAR, text = "ADD + ")
add_button.grid(row=0, column=0, ipadx=100)
refresh_button = Button(frameAR, text = "Refresh")
refresh_button.grid(row=0, column=1)

# frame3
frame3 = LabelFrame(root, text= "Unclaimed")
frame3.grid(row = 3, column = 0, padx = 10)
# frame3 labels
date_f3 = Label(frame3, text="Date&Time")
date_f3.grid(row = 0, column = 0)
amount_f3 = Label(frame3, text = "Amount")
amount_f3.grid(row = 0, column= 1)

# frame4
frame4 = LabelFrame(root, text = "Padala History")
frame4.grid(row = 3, column = 1)
# frame4 labels
date_f4 = Label(frame4, text="Date&Time")
date_f4.grid(row = 0, column = 0)
amount_f4 = Label(frame4, text = "Amount")
amount_f4.grid(row = 0, column= 1)
name_f4 = Label(frame4, text = "Name")
name_f4.grid(row=0, column=2)



root.mainloop()