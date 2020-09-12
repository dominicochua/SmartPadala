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
# function to claim an unclaimed padala

def claim_now(date):
    if date == "None":
        messagebox.showerror("CLAIM ERROR", "CHOOSE AN UNCLAIMED PADALA")
    else:
        conn = create_connection(database)
        c = conn.cursor()
        c.execute("SELECT * FROM claim_info WHERE date_and_time = ?",(date,))
        record = c.fetchall()
        global claim_window
        global fn_entry
        global ln_entry
        global pn_entry
        claim_window = Toplevel()
        claim_window.iconbitmap(".\\assets\\icon.ico")
        claim_window.geometry("400x400")
        claim_window.title("CLAIM INFO")
        Label(claim_window, text= "FIRST NAME:").grid(row=1, column=0, ipadx=10, pady=(20,10), sticky=W)
        fn_entry = Entry(claim_window, width=35)
        fn_entry.grid(row=1, column=1, pady=(20,10))
        Label(claim_window, text= "LAST NAME:").grid(row=2, column=0, ipadx=10, pady=(0,10), sticky=W)
        ln_entry = Entry(claim_window, width=35)
        ln_entry.grid(row=2, column=1, pady=(0,10))
        Label(claim_window, text= "PHONE NUMBER:").grid(row=3, column=0, ipadx=10, pady=(0,10), sticky=W)
        pn_entry = Entry(claim_window, width=35)
        pn_entry.grid(row=3, column=1, pady=(0,10))
        Label(claim_window, text= "AMOUNT:").grid(row=4, column=0, ipadx=10, pady=(0,10), sticky=W)
        Label(claim_window, text= record[0][6]).grid(row=4, column=1, pady=(0,10))
        Label(claim_window, text= "REFERENCE NUMBER").grid(row=5, column=0, ipadx=10, pady=(0,10), sticky=W)
        Label(claim_window, text= record[0][7]).grid(row=5, column=1, pady=(0,10))
        confirm_button = Button(claim_window, text="CONFIRM", command=lambda: edit_claim(date)).grid(row=7,column=1,ipadx=10, pady=(15,0))
        return 
def edit_claim(date):
    try: 
        conn = create_connection(database)
        c = conn.cursor()
        customer_id = customer_checker()
        value = (customer_id,fn_entry.get(), ln_entry.get(), pn_entry.get(), date)
        sql = ''' UPDATE claim_info 
                    SET customer_id = ? ,
                    first_name = ? , 
                    last_name = ? ,
                    phone_number = ?
                WHERE date_and_time = ?'''
        c.execute(sql,value)
        conn.commit()
        claim_window.destroy()
        refresh()
    except:
        messagebox.showerror("TRANSACTION ERROR", "INPUT CORRECT INFORMATION")
    return
# refresh the root window
def refresh():
    frame1.destroy()
    frame2.destroy()
    frameAR.destroy()
    frame3.destroy()
    frame4.destroy()
    time_label.destroy()
    display_frame1()
    display_frame2()
    display_frameAR()
    display_frame3()
    display_frame4()
    return
def display_frame1():
    global frame1
    global time_label
    # Root Labels
    time_label = Label(root, text=ctime(),font = ("Roboto", 14), bg="#71afe5")
    time_label.grid(row = 0, column = 0, columnspan=2)
    # Frame 1
    frame1 = LabelFrame(root, borderwidth = 0, bg="#71afe5")
    frame1.grid(row = 1, column = 0, sticky=W)
    # frame1 labels
    current_cash = get_cash()
    cash_on_hand = current_cash[0]
    cash_on_padala = current_cash[1]
    Label(frame1, text="Cash on hand:",font = ("Roboto", 14), bg="#71afe5").grid(row=0, column= 0,sticky=W,padx=(20,0))
    Label(frame1, text = cash_on_hand,font = ("Roboto", 14), bg="#71afe5").grid(row=0, column= 1,sticky=W)
    Label(frame1, text="Cash in Padala:",font = ("Roboto", 14), bg="#71afe5").grid(row=1, column = 0,sticky=W,padx=(20,0))
    Label(frame1, text=cash_on_padala,font = ("Roboto", 14), bg="#71afe5").grid(row=1, column = 1,sticky=W)
    return
def display_frame2():
    global frame2
    # frame2
    frame2 = LabelFrame(root, borderwidth = 0, bg="#71afe5")
    frame2.grid(row = 1, column = 1, sticky=W, padx=(60,0))
    # frame2 labels
    today_display = get_earnings()
    total_earning = today_display.date
    no_of_padala = today_display.amount 
    no_of_claim = today_display.name
    total_padala = today_display.num
    total_claim = today_display.unknown
    Label(frame2, text = "TODAY",font = ("Baufra", 15), bg="#71afe5").grid(row=0, column=0,pady=(0,5))
    Label(frame2, text = "Earnings:",font = ("Roboto", 14), bg="#71afe5").grid(row=1, column=0, sticky = W)
    Label(frame2, text = total_earning,font = ("Roboto", 14), bg="#71afe5").grid(row=1, column=1, sticky = W)
    Label(frame2, text = "No. of Padala:",font = ("Roboto", 14), bg="#71afe5").grid(row=2, column=0, sticky = W)
    Label(frame2, text = no_of_padala,font = ("Roboto", 14), bg="#71afe5").grid(row=2, column=1, sticky = W)
    Label(frame2, text = "No. of Claims:",font = ("Roboto", 14), bg="#71afe5").grid(row=3, column=0, sticky = W)
    Label(frame2, text = no_of_claim,font = ("Roboto", 14), bg="#71afe5").grid(row=3, column=1, sticky = W)
    Label(frame2, text = "Total Padala:",font = ("Roboto", 14), bg="#71afe5").grid(row=4, column=0, sticky = W)
    Label(frame2, text = total_padala,font = ("Roboto", 14), bg="#71afe5").grid(row=4, column=1, sticky = W)
    Label(frame2, text = "Total Claims:",font = ("Roboto", 14), bg="#71afe5").grid(row=5, column=0, sticky = W)
    Label(frame2, text = total_claim,font = ("Roboto", 14), bg="#71afe5").grid(row=5, column=1, sticky = W)
    return
def display_frameAR():
    global frameAR
    # Frame Add and refresh
    frameAR = LabelFrame(root, borderwidth = 0, bg="#71afe5")
    frameAR.grid(row = 2, column = 0, columnspan=2,pady=(10,2))
    types = ["PADALA", "CLAIM", "TOP UP", "WITHDRAW", "DEPOSIT"]
    global choice
    choice = StringVar()
    choice.set("CHOOSE A TRANSACTION")
    add_drop = OptionMenu(frameAR, choice, *types)
    add_drop.config(bg="white", font =("Roboto", 10), borderwidth = 2, relief = FLAT)
    add_drop.grid(row=0, column=0, ipadx=10, sticky=W)
    add_button = Button(frameAR, text="ADD", command=add_activity)
    add_button.config(bg="white", font =("Roboto", 10), borderwidth = 2, relief = RAISED)
    add_button.grid(row=0, column=1, padx=(2,5))
    refresh_button = Button(frameAR, text = "REFRESH", anchor=CENTER, command=refresh)
    refresh_button.config(bg="white", font =("Roboto", 10), borderwidth = 2, relief = RAISED)
    refresh_button.grid(row=0, column=2)
    return
def display_frame3():
    global frame3
    # frame3
    frame3 = LabelFrame(root, text= "Unclaimed Padalas", labelanchor=N,bg="white",font = ("Nexa", 13))
    frame3.grid(row = 3, columnspan = 2, pady=(0,5))
    to_claim_list = display_unclaimed()
    # frame3 labels
    Label(frame3, text="Date&Time",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5).grid(row = 0, column = 0, ipadx=40,padx=(5,0))
    Label(frame3, text = "Amount",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5).grid(row = 0, column= 1,padx=(5,5))
    Label(frame3, text = "Reference Number",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5).grid(row = 0, column= 2,padx=(0,5))
    date = StringVar()
    date.set('None')
    row = 0
    for record in to_claim_list:
        Radiobutton(frame3, text=to_claim_list[row][1], variable=date, value=record[1],font = ("Sans-serif", 11),bg="white").grid(row = row+1, column= 0)
        Label(frame3, text = to_claim_list[row][6],font = ("Sans-serif", 11),bg="white").grid(row = row+1, column= 1)
        Label(frame3, text = to_claim_list[row][7],font = ("Sans-serif", 11),bg="white").grid(row = row+1, column= 2)
        row +=1
    claim_button = Button(frame3, text="CLAIM", command=lambda: claim_now(date.get()), font =("Roboto", 10), borderwidth = 2, relief = RAISED)
    claim_button.grid(row=row+1, columnspan= 3, ipadx=15)
    return
def display_frame4():
    global frame4
    # frame4
    frame4 = LabelFrame(root, text = "Padala History", labelanchor=N,bg="white",font = ("Nexa", 13))
    frame4.grid(row = 4, columnspan = 2,padx=10)
    # frame4 labels
    date_f4 = Label(frame4, text="Date&Time",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5)
    date_f4.grid(row = 0, column = 0, ipadx=35,padx=(5,5))
    amount_f4 = Label(frame4, text = "Amount",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5)
    amount_f4.grid(row = 0, column= 1, ipadx=30,padx=(0,5))
    name_f4 = Label(frame4, text = "Name",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5)
    name_f4.grid(row=0, column=2, ipadx=30,padx=(0,5))
    number_f4 = Label(frame4, text = "Number",bg = '#c7e0f4',font = ("Roboto", 13),borderwidth=5)
    number_f4.grid(row=0, column=3, ipadx=35,padx=(0,5))
    padala_history = display_padala_history()
    padala_history_date_label = Label(frame4, text = padala_history.date,font = ("Sans-serif", 11),bg="white")
    padala_history_date_label.grid(row=1, column = 0)
    padala_history_amount_label = Label(frame4, text = padala_history.amount,font = ("Sans-serif", 11),bg="white")
    padala_history_amount_label.grid(row=1, column = 1)
    padala_history_name_label = Label(frame4, text = padala_history.name,font = ("Sans-serif", 11),bg="white")
    padala_history_name_label.grid(row=1, column = 2)
    padala_history_num_label = Label(frame4, text = padala_history.num,font = ("Sans-serif", 11),bg="white")
    padala_history_num_label.grid(row=1, column = 3)
    return
# add customer in customer_info table
def add_customer():
    conn = create_connection(database)
    c = conn.cursor()
    try:
        value = (str(first_name_entry.get()),str(last_name_entry.get()), int(phone_number_entry.get()))
        sql = '''INSERT INTO customer_info (first_name, last_name, phone_number)
                VALUES(?,?,?)'''
        c.execute(sql,value)
        conn.commit()
        return c.lastrowid
    except:
        value = (str(fn_entry.get()),str(ln_entry.get()), int(pn_entry.get()))
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
    try:
        for name in rows:
            if name[1]==str(first_name_entry.get()) and name[2]==str(last_name_entry.get()) and name[3]==int(phone_number_entry.get()):
                return name[0]
                break
        return add_customer()
    except:
        for name in rows:
            if name[1]==str(fn_entry.get()) and name[2]==str(ln_entry.get()) and name[3]==int(pn_entry.get()):
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
    value = (customer_id, str(first_name_entry.get()),str(last_name_entry.get()), int(phone_number_entry.get()),float(amount_entry.get()),int(smart_padala_no_entry.get()),int(receiver_no_entry.get()))
    sql = '''INSERT INTO padala_info (date_and_time, customer_id, first_name, last_name, phone_number, amount_of_padala, padala_to, receiver_number)
                VALUES(datetime('now', 'localtime'),?,?,?,?,?,?,?)'''
    c.execute(sql,value)
    conn.commit()
    return c.lastrowid
# adding to claim_info table   
def add_claim():
    conn = create_connection(database)
    c = conn.cursor()
    value = (str(amount_entry.get()), str(reference_number_entry.get()).upper())
    sql = '''INSERT INTO claim_info (date_and_time, amount_of_claim, reference_number)
                VALUES(datetime('now', 'localtime'),?,?)'''
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
    try:
        conn = create_connection(database)
        c = conn.cursor()
        if choice.get()=="PADALA":
            padala_id = add_padala()
            current_cash = get_cash()
            coh_after = current_cash[0] + float(amount_entry.get()) + charge(float(amount_entry.get()))
            cop_after = current_cash[1] - float(amount_entry.get()) - padala_charge(float(amount_entry.get()))
            value = ("PADALA", padala_id, float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
            sql = '''INSERT INTO transactions_info (date_and_time, type, padala_id, amount, cash_on_hand_before,
                        cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                    VALUES(datetime('now', 'localtime'),?,?,?,?,?,?,?)'''
        elif choice.get()=="CLAIM":
            if amount_entry.get() != "" and reference_number_entry.get() != "":
                claim_id = add_claim()
                current_cash = get_cash()
                coh_after = current_cash[0] - float(amount_entry.get())
                cop_after = current_cash[1] + float(amount_entry.get()) + claim_charge(float(amount_entry.get()))
                value = ("CLAIM", claim_id, float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
                sql = '''INSERT INTO transactions_info (date_and_time, type, claim_id, amount, cash_on_hand_before,
                            cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                        VALUES(datetime('now', 'localtime'),?,?,?,?,?,?,?)'''
            else:
                raise
        elif choice.get()=="TOP UP":
            current_cash = get_cash()
            coh_after = current_cash[0] - float(amount_entry.get())
            cop_after = current_cash[1] + float(amount_entry.get())
            value = ("TOPUP", float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
            sql = '''INSERT INTO transactions_info (date_and_time, type, amount, cash_on_hand_before,
                        cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                    VALUES(datetime('now', 'localtime'),?,?,?,?,?,?)'''
        elif choice.get()=="WITHDRAW":
            current_cash = get_cash()
            coh_after = current_cash[0] + float(amount_entry.get())
            cop_after = current_cash[1]
            value = ("WITHDRAW", float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
            sql = '''INSERT INTO transactions_info (date_and_time, type, amount, cash_on_hand_before,
                        cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                    VALUES(datetime('now', 'localtime'),?,?,?,?,?,?)'''
        elif choice.get()=="DEPOSIT":
            current_cash = get_cash()
            coh_after = current_cash[0] - float(amount_entry.get())
            cop_after = current_cash[1]
            value = ("DEPOSIT", float(amount_entry.get()), current_cash[0], coh_after, current_cash[1],cop_after)
            sql = '''INSERT INTO transactions_info (date_and_time, type, amount, cash_on_hand_before,
                        cash_on_hand_after, cash_on_padala_before, cash_on_padala_after)
                    VALUES(datetime('now', 'localtime'),?,?,?,?,?,?)'''

        c.execute(sql,value)
        conn.commit()
        transact.destroy()
        refresh()
    except:
        messagebox.showerror("TRANSACTION ERROR", "INPUT CORRECT INFORMATION")
    return
class table_columns:
    def __init__(self, date, amount,name,num, unknown):
        self.date = date
        self.amount = amount
        self.name = name
        self.num = num 
        self.unknown = unknown
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
    padala_history = table_columns(padala_date_history, padala_amount_history, padala_name_history, padala_num_history, "none")
    return padala_history
# function to display unclaimed incoming padala
def display_unclaimed():
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT * FROM claim_info  WHERE customer_id IS NULL ORDER BY date_and_time DESC")
    unclaimed_list = c.fetchall()
    return unclaimed_list
# function to get earnings for the day
def get_earnings():
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT * FROM transactions_info WHERE (type IN (?,?)) AND (date(date_and_time) = date(datetime('now', 'localtime')))",("PADALA","CLAIM"))
    earnings = c.fetchall()
    total_earning=0
    no_of_padala=0
    no_of_claim=0
    total_padala=0
    total_claim=0
    for record in earnings:
        # get total earnings 
        total_earning += claim_charge(record[5])

        if record[2] == "PADALA":
            # no of padala
            no_of_padala += 1 
            # total padala
            total_padala += record[5]
        else:
            # no of claims
            no_of_claim += 1
            # total padala
            total_claim += record[5]
    today_display = table_columns(total_earning, no_of_padala,no_of_claim,total_padala,total_claim)
    """
    today_display.date = total_earning
    today_display.amount = no_of_padala
    today_display.name = no_of_claim
    today_display.num = total_padala
    today_display.unknown = total_claim
    """
    return today_display
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
    global root
    root= Tk()
    root.title("SMART PADALA TRACKER")
    root.iconbitmap(".\\assets\\icon.ico")
    root.geometry("590x700")
    root.configure(bg="#71afe5")
    display_frame1()
    display_frame2()
    display_frameAR()
    display_frame3()
    display_frame4()
    
    root.mainloop()

if __name__ == '__main__':
    main()









