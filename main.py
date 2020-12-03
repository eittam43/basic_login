from tkinter import *
import pyodbc
from tkinter import messagebox

''' This program is a simple login which stores the login data. If the correct credentials 
    are entered, the user will be prompted that the user name and password are correct. If
    the credentials entered are not correct, the user will be prompted that the user name and 
     password are incorrect'''

m_Gui = Tk()
m_Gui.geometry('250x350+500+300')
m_Gui.title("Login to your account")
u_name_input_str = StringVar("")
pw_input_str = StringVar("")


def check_cred():
    ''' def check_cred(): connect to database and gather user name and password from cred
        table stored in database. return results in two strings
         parse into format_creds(): '''
    conn_str = ()  # *** Add database path and auth. *** #
    conn = pyodbc.connect(conn_str)  # *** Create database connection *** #
    cur = conn.cursor()  # *** Create cursor object *** #
    cur.execute(
        "select user_name from cred where id=?")  # *** sql statement for username, NOTE: database structure (ERD) provided at *** #
    user_name = cur.fetchone()  # *** get username from database *** #
    cur.execute("select password from cred where id=?")  # *** sql statement for password *** #
    password = cur.fetchone()  # *** get password from database *** #
    cur.close()  # *** close cursor *** #
    conn.close()  # *** close connection *** #
    print("STEP ONE SUCCESSFUL")  # *** console output (debug), remove at will *** #
    format_creds(user_name, password)  # *** call format_creds and pass database data *** #


def format_creds(user_name, password):
    ''' format_creds(): store user name and password in new strings
        and pass in *user_name* and *password* as lists respectively.
        return new strings into check_all(): '''
    user_name2 = str(user_name[0])  # *** convert user_name list object into a string *** #
    passwd = str(password[0])  # *** convert password list object into a string *** #
    print("STEP TWO SUCCESSFUL")  # *** console output (debug) *** #
    check_all(user_name2, passwd)  # *** call check_all and pass new strings *** #


def check_all(user_name2, passwd):
    ''' check_all(): store entry text and pass the values into condition
        statement and try it against the data pulled from the database. User
        will be prompted whether the login was good or bad.'''
    username = u_name_input_str.get()  # *** get user name input *** #
    pword = pw_input_str.get()  # *** get password input *** #
    if user_name2 == username and passwd == pword:  # *** try user input against saved credentials in database *** #
        print("STEP THREE SUCCESSFUL")  # *** console output (debug) *** #
        messagebox.showinfo("LOGIN GRANTED", "You have entered the correct login!")
    else:
        messagebox.showinfo("LOGIN FAILED", "You have not entered correct login, Try again!")

    return


# *** login form *** #
u_name_lab = Label(m_Gui, text="Username :")
u_name_lab.grid(row=0, column=1)
pw_lab = Label(m_Gui, text="Password :")
pw_lab.grid(row=1, column=1)

u_name_input = Entry(m_Gui, textvariable=u_name_input_str)
u_name_input.grid(row=0, column=2)
pw_input = Entry(m_Gui, textvariable=pw_input_str)
pw_input.grid(row=1, column=2)

login_butt = Button(m_Gui, text="LOGIN", command=check_cred)
login_butt.grid(row=3, columnspan=2, column=1)
u_name_input.focus()

m_Gui.mainloop()
