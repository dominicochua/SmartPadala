from tkinter import *
from time import time, ctime
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

# create db connection function
def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return conn

# create table function
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
# create add_activity function
# new window to fill up
def add_activity():
    global transact
    transact = Toplevel()
    transact.iconbitmap(".\\assets\\icon.ico")
    transact.geometry("400x400")
    if choice.get()=="PADALA":
        transact.title("PADALA")
        global first_name_entry
        global last_name_entry
        global phone_number_entry
        global amount_entry
        global smart_padala_no_entry
        global receiver_no_entry
        global reference_number_entry
        first_name_label = Label(transact, text= "FIRST NAME:").grid(row=1, column=0, ipadx=10, pady=(20,10), sticky=W)
        first_name_entry = Entry(transact, width=35)
        first_name_entry.grid(row=1, column=1, pady=(20,10))
        last_name_label = Label(transact, text= "LAST NAME:").grid(row=2, column=0, ipadx=10, pady=(0,10), sticky=W)
        last_name_entry = Entry(transact, width=35)
        last_name_entry.grid(row=2, column=1, pady=(0,10))
        phone_number_label = Label(transact, text= "PHONE NUMBER:").grid(row=3, column=0, ipadx=10, pady=(0,10), sticky=W)
        phone_number_entry = Entry(transact, width=35)
        phone_number_entry.grid(row=3, column=1, pady=(0,10))
        amount_label = Label(transact, text= "AMOUNT:").grid(row=4, column=0, ipadx=10, pady=(0,10), sticky=W)
        amount_entry = Entry(transact, width=35)
        amount_entry.grid(row=4, column=1, pady=(0,10))
        smart_padala_no_label = Label(transact, text= "SMART PADALA NUMBER:").grid(row=5, column=0, ipadx=10, pady=(0,10), sticky=W)
        smart_padala_no_entry = Entry(transact, width=35)
        smart_padala_no_entry.grid(row=5, column=1, pady=(0,10))
        receiver_no_label = Label(transact, text= "RECEIVER NUMBER:").grid(row=6, column=0, ipadx=10, pady=(0,10), sticky=W)
        receiver_no_entry = Entry(transact, width=35)
        receiver_no_entry.grid(row=6, column=1, pady=(0,10))
        confirm_button = Button(transact, text="CONFIRM", command=add_transaction).grid(row=7,column=1,ipadx=10, pady=(15,0))
    elif choice.get()=="CLAIM":
        transact.title("CLAIM")
        reference_number_label = Label(transact, text= "REFERENCE NUMBER:").grid(row=1, column=0, ipadx=10, pady=(20,10), sticky=W)
        reference_number_entry = Entry(transact, width=35)
        reference_number_entry.grid(row=1, column=1, pady=(20,10))
        amount_label = Label(transact, text= "AMOUNT:").grid(row=2, column=0, ipadx=10, pady=(0,10), sticky=W)
        amount_entry = Entry(transact, width=35)
        amount_entry.grid(row=2, column=1, pady=(0,10))
        confirm_button = Button(transact, text="CONFIRM", command=add_transaction).grid(row=3,column=1,ipadx=10, pady=(15,0))
    elif choice.get()=="TOP UP":
        transact.title("TOP UP")
        amount_label = Label(transact, text= "AMOUNT:").grid(row=1, column=0, ipadx=10, pady=(20,10), sticky=W)
        amount_entry = Entry(transact, width=35)
        amount_entry.grid(row=1, column=1,pady=(20,10))
        confirm_button = Button(transact, text="CONFIRM", command=add_transaction).grid(row=2,column=1,ipadx=10, pady=(15,0))
    elif choice.get()=="WITHDRAW":
        transact.title("WITHDRAW")
        amount_label = Label(transact, text= "AMOUNT:").grid(row=1, column=0, ipadx=10, pady=(20,10), sticky=W)
        amount_entry = Entry(transact, width=35)
        amount_entry.grid(row=1, column=1, pady=(20,10))
        confirm_button = Button(transact, text="CONFIRM", command=add_transaction).grid(row=2,column=1,ipadx=10, pady=(15,0))
    elif choice.get()=="DEPOSIT":
        transact.title("DEPOSIT")
        amount_label = Label(transact, text= "AMOUNT:").grid(row=1, column=0, ipadx=10, pady=(20,10), sticky=W)
        amount_entry = Entry(transact, width=35)
        amount_entry.grid(row=1, column=1, pady=(20,10))
        confirm_button = Button(transact, text="CONFIRM", command=add_transaction).grid(row=2,column=1,ipadx=10, pady=(15,0))
    else:
        transact.destroy()
        messagebox.showerror("TRANSACTION ERROR", "CHOOSE A VALID TYPE OF TRANSACTION")
    return
# refresh the root window
def refresh():
    return
# add customer in customer_info table
def add_customer():
    conn = create_connection(database)
    c = conn.cursor()
    value = (str(first_name_entry.get()),str(last_name_entry.get()), int(phone_number_entry.get()))
    sql = '''INSERT INTO customer_info (first_name, last_name, phone_number)
                VALUES(?,?,?)'''
    c.execute(sql,value)
    conn.commit()
    return c.lastrowid
# check if customer exist in customer_info table
def customer_checker():
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT * FROM customer_info")
    rows = c.fetchall()
    for name in rows:
        if name[1]==str(first_name_entry.get()) and name[2]==str(last_name_entry.get()) and name[3]==int(phone_number_entry.get()):
            return name[0]
            break
    return add_customer()

# function to get the charge fee in transactions
def charge(amount):
    if amount < 1000:
        fee=30
    else:
        amount_to_charge = amount - 1000
        fee = 30
        while(amount_to_charge > 0):
            fee += 15
            amount_to_charge -= 500
    return fee
def claim_charge(amount):
    if amount < 1000:
        fee=11.50
    else:
        amount_to_charge = amount - 1000
        fee = 11.50
        while(amount_to_charge > 0):
            fee += 5.75
            amount_to_charge -= 500
    return fee
def padala_charge(amount):
    if amount < 1000:
        fee=18.50
    else:
        amount_to_charge = amount - 1000
        fee = 18.50
        while(amount_to_charge > 0):
            fee += 9.25
            amount_to_charge -= 500
    return fee
# adding to padala_info table
def add_padala():
    conn = create_connection(database)
    c = conn.cursor()
    customer_id = customer_checker()
    value = (str(ctime()), customer_id, str(first_name_entry.get()),str(last_name_entry.get()), int(phone_number_entry.get()),float(amount_entry.get()),int(smart_padala_no_entry.get()),int(receiver_no_entry.get()))
    sql = '''INSERT INTO padala_info (date_and_time, customer_id, first_name, last_name, phone_number, amount_of_padala, padala_to, receiver_number)
                VALUES(?,?,?,?,?,?,?,?)'''
    c.execute(sql,value)
    conn.commit()
    return c.lastrowid
# adding to claim_info table   
def add_claim():
    conn = create_connection(database)
    c = conn.cursor()
    value = (str(ctime()),str(amount_entry.get()), str(reference_number_entry.get()))
    sql = '''INSERT INTO claim_info (date_and_time, amount_of_claim, reference_number)
                VALUES(?,?,?)'''
    c.execute(sql,value)
    conn.commit()
    return c.lastrowid
# get the cash onhand and cash on padala before transaction
def get_cash():
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT cash_on_hand_after, cash_on_padala_after FROM transactions_info ORDER BY transaction_id DESC LIMIT 1")
    cash = c.fetchall()
    try:
        list_cash = cash[0]
        return list_cash
    except:
        if not bool(cash):
            cash.append(0)
            cash.append(0)
            return cash
# adding to transaction_info table
def add_transaction():
    conn = create_connection(database)
    c = conn.cursor()
    if choice.get()=="PADALA":
        padala_id = add_padala()
        current_cash = get_cash()
        coh_after = current_cash[0] + float(amount_entry.get()) + charge(float(amount_entry.get()))
        cop_after = current_cash[1] - float(amount_entry.get()) - padala_charge(float(amount_entry.get()))
        value = (str(ctime()), "PADALA", padala_id, float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
        sql = '''INSERT INTO transactions_info (date_and_time, type, padala_id, amount, cash_on_hand_before,
                    cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                VALUES(?,?,?,?,?,?,?,?)'''

    elif choice.get()=="CLAIM":
        claim_id = add_claim()
        current_cash = get_cash()
        coh_after = current_cash[0] - float(amount_entry.get())
        cop_after = current_cash[1] + float(amount_entry.get()) + claim_charge(float(amount_entry.get()))
        value = (str(ctime()), "CLAIM", claim_id, float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
        sql = '''INSERT INTO transactions_info (date_and_time, type, claim_id, amount, cash_on_hand_before,
                    cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                VALUES(?,?,?,?,?,?,?,?)'''
    elif choice.get()=="TOPUP":
        current_cash = get_cash()
        coh_after = current_cash[0] - float(amount_entry.get())
        cop_after = current_cash[1] + float(amount_entry.get())
        value = (str(ctime()), "TOPUP", float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
        sql = '''INSERT INTO transactions_info (date_and_time, type, amount, cash_on_hand_before,
                    cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                VALUES(?,?,?,?,?,?,?)'''
    elif choice.get()=="WITHDRAW":
        current_cash = get_cash()
        coh_after = current_cash[0] + float(amount_entry.get())
        cop_after = current_cash[1]
        value = (str(ctime()), "WITHDRAW", float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
        sql = '''INSERT INTO transactions_info (date_and_time, type, amount, cash_on_hand_before,
                    cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                VALUES(?,?,?,?,?,?,?)'''
    elif choice.get()=="DEPOSIT":
        current_cash = get_cash()
        coh_after = current_cash[0] - float(amount_entry.get())
        cop_after = current_cash[1]
        value = (str(ctime()), "DEPOSIT", float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
        sql = '''INSERT INTO transactions_info (date_and_time, type, amount, cash_on_hand_before,
                    cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                VALUES(?,?,?,?,?,?,?)'''

    c.execute(sql,value)
    conn.commit()
    transact.destroy()
    return
class table_columns:
    def __init__(self, date, amount,name,num):
        self.date = date
        self.amount = amount
        self.name = name
        self.num = num 
def display_padala_history():
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT * FROM padala_info ORDER BY padala_id DESC LIMIT 10")
    padala_list = c.fetchall()
    padala_date_history = ''
    padala_amount_history = ''
    padala_name_history = ''
    padala_num_history = ''
    for padala in padala_list:
        padala_date_history += str(padala[1]) + '\n'
        padala_amount_history += str(padala[6]) + '\n' 
        padala_name_history += str(padala[3]) +" "+str(padala[4])+'\n'  
        padala_num_history += str(padala[5]) + '\n' 
    padala_history = table_columns(padala_date_history, padala_amount_history, padala_name_history, padala_num_history)
    return padala_history


def main():
    global database
    database = r"SmartPadala.db" 
    # define customer table
    customer_table = """CREATE TABLE IF NOT EXISTS customer_info(
                        customer_id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number INTEGER,
                        UNIQUE (first_name, last_name, phone_number)
                    )"""
    # define padala table
    padala_table ="""CREATE TABLE IF NOT EXISTS padala_info(
                        padala_id INTEGER PRIMARY KEY,
                        date_and_time TEXT NOT NULL,
                        customer_id INTEGER NOT  NULL,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number INTEGER NOT NULL,
                        amount_of_padala REAL NOT NULL,
                        padala_to TEXT NOT NULL,
                        receiver_number INTEGER NOT NULL,
                        FOREIGN KEY (customer_id)
                            REFERENCES customer_info(customer_id)
                    )"""
    # define claim table
    claim_table = """CREATE TABLE IF NOT EXISTS claim_info(
                    claim_id INTEGER PRIMARY KEY,
                    date_and_time TEXT NOT NULL,
                    customer_id INTEGER,
                    first_name TEXT,
                    last_name TEXT,
                    phone_number INTEGER,
                    amount_of_claim REAL NOT NULL,
                    reference_number TEXT NOT NULL,
                    FOREIGN KEY (customer_id)
                        REFERENCES customer_info(customer_id) 
                )"""
    # define transaction table
    transaction_table = """CREATE TABLE IF NOT EXISTS transactions_info(
                            transaction_id INTEGER PRIMARY KEY,
                            date_and_time TEXT NOT NULL,
                            type TEXT NOT NULL,
                            padala_id INTEGER,
                            claim_id INTEGER,
                            amount REAL NOT NULL,
                            cash_on_hand_before REAL NOT NULL,
                            cash_on_hand_after REAL NOT NULL,
                            cash_on_padala_before REAL NOT NULL,
                            cash_on_padala_after REAL NOT NULL,
                            FOREIGN KEY (padala_id)
                                REFERENCES padala_info(padala_id),
                            FOREIGN KEY (claim_id)
                                REFERENCES padala_info(claim_id)
                        )"""
    global conn
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, customer_table)
        create_table(conn, padala_table)
        create_table(conn, claim_table)
        create_table(conn, transaction_table)
    else:
        print("no database connection")
    
    root= Tk()
    root.title("SMART PADALA TRACKER")
    root.iconbitmap(".\\assets\\icon.ico")
    root.geometry("600x400")

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
    types = ["PADALA", "CLAIM", "TOP UP", "WITHDRAW", "DEPOSIT"]
    global choice
    choice = StringVar()
    choice.set("CHOOSE A TRANSACTION")
    add_drop = OptionMenu(frameAR, choice, *types)
    add_drop.grid(row=0, column=0, ipadx=10, sticky=W)
    add_button = Button(frameAR, text="ADD", command=add_activity)
    add_button.grid(row=0, column=1, padx=(0,5))
    refresh_button = Button(frameAR, text = "REFRESH", anchor=CENTER, command=display_padala_history)
    refresh_button.grid(row=0, column=2)

    # frame3
    frame3 = LabelFrame(root, text= "Unclaimed")
    frame3.grid(row = 3, column = 0, padx = 10)
    # frame3 labels
    date_f3 = Label(frame3, text="Date&Time")
    date_f3.grid(row = 0, column = 0)
    amount_f3 = Label(frame3, text = "Amount")
    amount_f3.grid(row = 0, column= 1)

    # frame4
    frame4 = LabelFrame(root, text = "Padala History", labelanchor=N,bg="#c0c0c2",font = ("Nexa", 12))
    frame4.grid(row = 3, column = 1)
    # frame4 labels
    date_f4 = Label(frame4, text="Date&Time",bg = 'blue',font = ("Roboto", 12))
    date_f4.grid(row = 0, column = 0, ipadx=40)
    amount_f4 = Label(frame4, text = "Amount", bg='red',font = ("Roboto", 12))
    amount_f4.grid(row = 0, column= 1, ipadx=30)
    name_f4 = Label(frame4, text = "Name", bg='green',font = ("Roboto", 12))
    name_f4.grid(row=0, column=2, ipadx=30)
    number_f4 = Label(frame4, text = "Number", bg='yellow',font = ("Roboto", 12))
    number_f4.grid(row=0, column=3, ipadx=35)
    padala_history = display_padala_history()
    padala_history_date_label = Label(frame4, text = padala_history.date,font = ("Sans-serif", 10),bg="#c0c0c2")
    padala_history_date_label.grid(row=1, column = 0)
    padala_history_amount_label = Label(frame4, text = padala_history.amount,font = ("Sans-serif", 10),bg="#c0c0c2")
    padala_history_amount_label.grid(row=1, column = 1)
    padala_history_name_label = Label(frame4, text = padala_history.name,font = ("Sans-serif", 10),bg="#c0c0c2")
    padala_history_name_label.grid(row=1, column = 2)
    padala_history_num_label = Label(frame4, text = padala_history.num,font = ("Sans-serif", 10),bg="#c0c0c2")
    padala_history_num_label.grid(row=1, column = 3)

    root.mainloop()

if __name__ == '__main__':
    main()









