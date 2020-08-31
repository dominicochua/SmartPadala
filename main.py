from tkinter import *
from time import time, ctime
import sqlite3
from sqlite3 import Error

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
# create add_transanction function
def add_transaction():
    transact = Toplevel()
    transact.title("ADD TRANSACTION")
    transact.iconbitmap(".\\assets\\icon.ico")
    transact.geometry("400x400")

    return
    

def main():

    database = r"SmartPadala.db" 
    # define customer table
    customer_table = """CREATE TABLE IF NOT EXISTS customer_info(
                        customer_id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number INTEGER,
                        UNIQUE (first_name, last_name)
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
                            REFERENCES customer_Info(customer_id)
                    )"""
    # define claim table
    claim_table = """CREATE TABLE IF NOT EXISTS claim_info(
                    claim_id INTEGER PRIMARY KEY,
                    date_and_time TEXT NOT NULL,
                    customer_id INTEGER NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    phone_number INTEGER NOT NULL,
                    amount_of_claim REAL NOT NULL,
                    reference_number TEXT NOT NULL,
                    FOREIGN KEY (customer_id)
                        REFERENCES customer_Info(customer_id) 
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
                                REFERENCES padala_Info(padala_id),
                            FOREIGN KEY (claim_id)
                                REFERENCES padala_Info(claim_id)
                        )"""
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
    root.geometry("400x400")

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
    add_button = Button(frameAR, text = "ADD TRANSACTION ", command = add_transaction)
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

if __name__ == '__main__':
    main()









