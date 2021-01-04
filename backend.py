import sqlite3
from Expense_tracker import Expense

class Expense2:

    # Connect Database
    conn = sqlite3.connect('expenses.db')

    # create cursor
    c = conn.cursor()

    # Create Table
    # c.execute('''
    #         CREATE TABLE expenses(
    #         number INTEGER PRIMARY KEY,
    #         date text,
    #         spent_on text,
    #         amount int,
    #         notes text)
    #         ''')


    # Create Submit Function For Databases
    def submit():
        txt_expID.delete(0, END)
        txt_DoE.delete(0, END)
        txt_SpE.delete(0, END)
        txt_AmT.delete(0, END)






    conn.commit()
    conn.close()


lbl_notes=Label(Manage_Frame,text="Notes",bg="cadet blue",font=("arial",20,"bold"))
lbl_notes.grid(row=5,column=0,pady=10,padx=20,sticky="w")

txt_notes=Text(Manage_Frame,width=31,height=4,font=("",10),fg="Ghost White",bg="cadet blue",bd=5,relief=RIDGE)
txt_notes.grid(row=5,column=1,pady=10,padx=20,sticky="w")


records = c.fetchall()
print(records)
print_records = ''
for record in records[0]:
    print_records += str(record)
query_label = Label(Table_Frame, text=print_records)
query_label.grid(row=0, column=0, columnspan=5)




