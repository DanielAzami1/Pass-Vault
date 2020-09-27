from tkinter import *
from tkinter import messagebox
import sqlite3

def ReadFromUser():
    current_user = open("User","r")
    global active_user
    active_user = current_user.read()
    current_user.close

def main():
    ReadFromUser()
    root = Tk()
    root.title("Subscription Manager")
    root.geometry("1400x900")
    root.resizable()

    f1 = Frame(root,width = 900, height = 900, bg="slate blue",relief=GROOVE,borderwidth=5)
    f1.pack(side=LEFT,fill=BOTH,expand=False)

    f2 = Frame(root,width=500,height = 900,bg="light steel blue1",relief=GROOVE,borderwidth=5)
    f2.pack(side=RIGHT,fill=BOTH,expand=True)

    #=====================f1===========================================================
    lblTitle = Label(f1, font=('system',40,'bold','underline'),text="%s's Subscriptions"%active_user,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
    lblTitle.grid(row=0,columnspan=3,padx=15,pady=15,sticky=W+E)

    #===============================Button Functions========================================
    def OpenButton1():
        master = Toplevel()
        master.title("More information")
        master.geometry("600x425")
        master.resizable(0,0)
        WindowFrame = Frame(master, width=600, height=350, bg="light slate blue", relief=GROOVE)
        WindowFrame.pack(fill=BOTH,expand=True)
        current_subscription = btnSub1["text"]
        conn = sqlite3.connect('Password-Gen.db')
        cursor = conn.cursor()
        lblSubDesc = Label(WindowFrame, font=('system',20,'bold'),text="Subscription",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
        lblSubDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
        lblSubscription = Label(WindowFrame, font=('system',20,'bold'),text="%s"%current_subscription,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
        lblSubscription.grid(row=0,column=2,padx=15,pady=15,sticky=W)

        lblFreqDesc = Label(WindowFrame, font=('system',20,'bold'),text="Payment Frequency",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
        lblFreqDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
        cursor.execute("SELECT payment_frequency FROM subscriptions_table WHERE subscription = ? AND user_name = ?", (current_subscription, active_user))
        retrieved_frequency = cursor.fetchone()
            
        lblFrequency = Label(WindowFrame, font=('system',15,'bold'),text="%s"%retrieved_frequency,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
        lblFrequency.grid(row=1,column=2,padx=15,pady=15,sticky=W)

        lblPaymentDesc = Label(WindowFrame, font=('system',20,'bold'),text="Payment Amount (£)",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
        lblPaymentDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
        cursor.execute("SELECT payment_amount FROM subscriptions_table WHERE subscription = ? AND user_name = ?", (current_subscription, active_user))
        retrieved_payment = cursor.fetchone()
        
        lblPayment = Label(WindowFrame, font=('system',15,'bold'),text="%s"%retrieved_payment,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
        lblPayment.grid(row=2,column=2,padx=15,pady=15,sticky=W)

        lblActivityDesc = Label(WindowFrame, font=('system',20,'bold'),text="Status",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
        lblActivityDesc.grid(row=3,column=0,padx=15,pady=15,sticky=W)       
        cursor.execute("SELECT activity FROM subscriptions_table WHERE subscription = ? AND user_name = ?", (current_subscription, active_user))
        retrieved_status = cursor.fetchone()
        
        lblActivity = Label(WindowFrame, font=('system',15,'bold'),text="%s"%retrieved_status,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
        lblActivity.grid(row=3,column=2,padx=15,pady=15,sticky=W)
    
        btnCloseMoreInfo = Button(WindowFrame, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=master.destroy)
        btnCloseMoreInfo.grid(row=4,column=0, padx=15,pady=15,sticky=W)

        def DeleteAccount(current_subscription):
            if btnSub1["text"] == "Available slot":
                messagebox.showinfo("Oops!","No subscription has been set.")
                master.destroy()
            else:
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM subscriptions_table WHERE user_name = ? AND subscription = ?", (active_user, current_subscription))
                messagebox.showinfo("Success", current_subscription + " Successfully Deleted")
                conn.commit()
                master.destroy()
                conn.close()
                btnSub1["text"] = "Available slot"

        btnDelete = Button(WindowFrame, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_subscription))
        btnDelete.grid(row=4,column=2,padx=15,pady=15,sticky=W)
        
    def InfoPopup():
        messagebox.showinfo("More Information", "The Subscription Manager is a handy way to manage all of your currently active subscriptions")
        
    btnInfo = Button(f1, font=('courier new',15),text="What is this?",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=InfoPopup)
    btnInfo.grid(row=1,column=0,padx=15,pady=15,sticky=W)

    btnSub1 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=OpenButton1)
    btnSub1.grid(row=2,columnspan=3,padx=15,pady=15,sticky=W)

    btnSub2 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub2.grid(row=3,columnspan=3,padx=15,pady=15,sticky=W)

    btnSub3 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub3.grid(row=4,columnspan=3,padx=15,pady=15,sticky=W)

    btnSub4 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub4.grid(row=5,columnspan=3,padx=15,pady=15,sticky=W)

    btnSub5 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub5.grid(row=6,columnspan=3,padx=15,pady=15,sticky=W)

    btnSub6 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub6.grid(row=2,columnspan=3,padx=15,pady=15,sticky=E)

    btnSub7 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub7.grid(row=3,columnspan=3,padx=15,pady=15,sticky=E)

    btnSub8 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub8.grid(row=4,columnspan=3,padx=15,pady=15,sticky=E)

    btnSub9 = Button(f1, font=('courier new',18,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub9.grid(row=5,columnspan=3,padx=15,pady=15,sticky=E)

    btnSub10 = Button(f1, font=('courier new',17,'bold'),text="Available Slot",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
    btnSub10.grid(row=6,columnspan=3,padx=15,pady=15,sticky=E)


    def TotalWeekly():
        pass
    
    def TotalMonthly():
        pass

    def TotalAnnually():
        pass

    btnTotalWeekly = Button(f1, font=('courier new',18,'bold'),text="WEEKLY TOTAL", fg="ivory2",bg="dark slate blue",borderwidth=3,relief=SUNKEN,command=TotalWeekly)
    btnTotalWeekly.grid(row=7,column=0,padx=15,pady=15,sticky=W)

    btnTotalMonthly = Button(f1, font=('courier new',18,'bold'),text="MONTHLY TOTAL", fg="ivory2",bg="dark slate blue",borderwidth=3,relief=SUNKEN,command=TotalMonthly)
    btnTotalMonthly.grid(row=7,column=1,padx=15,pady=15,sticky=W)

    btnTotalAnnually = Button(f1, font=('courier new',18,'bold'),text="ANNUAL TOTAL", fg="ivory2",bg="dark slate blue",borderwidth=3,relief=SUNKEN,command=TotalAnnually)
    btnTotalAnnually.grid(row=7,column=2,padx=15,pady=15,sticky=E)

    def ReturnToMainWindow():
        root.destroy()
        from MainWindow import main
        main()

    btnReturnToMainWindow = Button(f1, font=('courier new',15,'bold'),text="RETURN TO MAIN WINDOW", fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ReturnToMainWindow)
    btnReturnToMainWindow.grid(row=8,columnspan=2,padx=15,pady=15,sticky=W)

    btnExit = Button(f1, font=('courier new',15,'bold'),text="EXIT", fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=root.destroy)
    btnExit.grid(row=9,columnspan=2,padx=15,pady=15,sticky=W)
    #================================================f1========================================

    #===============================================f2==========================================
    input_Frequency = IntVar()    
    input_Weekly=IntVar()
    input_Monthly = IntVar()
    input_Annually = IntVar()

    input_Activity = IntVar()    
    input_Active = IntVar()
    input_Inactive = IntVar()

    lblTitle2 = Label(f2, font=('ms serif',50,'bold'),text="Add A Subscription",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
    lblTitle2.grid(row=0,columnspan=3,padx=15,pady=15,sticky=W+E)

    lblName = Label(f2, font=('courier new',17,'bold'),text="Name of subscription",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblName.grid(row=1,column=0,sticky=W,padx=15,pady=15)
    entrySubscriptionName = Entry(f2,font=('courier new',17), insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    entrySubscriptionName.grid(row=1,column=1,sticky=W)

    lblFrequency= Label(f2, font=('courier new',17,'bold'),text="How often are you billed?",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblFrequency.grid(row=2,columnspan=2,sticky=W,padx=15,pady=15)

    radioWeekly = Radiobutton(f2,font=('arial',17,'bold'),text="WEEKLY",
                              fg="dark slate blue",bg="light steel blue1",variable=input_Frequency,value=input_Weekly)
    radioWeekly.grid(row=3,column=0,sticky=W,padx=15,pady=10)

    radioMonthly = Radiobutton(f2,font=('arial',17,'bold'),text="MONTHLY",
                               fg="dark slate blue",bg="light steel blue1",variable=input_Frequency,value=input_Monthly)
    radioMonthly.grid(row=4,column=0,sticky=W,padx=15,pady=10)

    radioAnnually = Radiobutton(f2,font=('arial',17,'bold'),text="ANUALLY",
                                fg="dark slate blue",bg="light steel blue1",variable=input_Frequency,value=input_Annually)
    radioAnnually.grid(row=5,column=0,sticky=W,padx=15,pady=10)

    lblPayment = Label(f2, font=('courier new',17,'bold'),text="Payment Amount (£)",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblPayment.grid(row=6,column=0,sticky=E,padx=15,pady=15)
    entryPayment = Entry(f2,font=('courier new',17), insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    entryPayment.grid(row=6,column=1,sticky=W)

    lblStatus= Label(f2, font=('courier new',17,'bold'),text="Is this subscription currently active?",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblStatus.grid(row=7,columnspan=2,sticky=W,padx=15,pady=15)

    radioActive = Radiobutton(f2,font=('arial',17,'bold'),text="ACTIVE",
                              fg="dark slate blue",bg="light steel blue1",variable=input_Activity,value=input_Active)
    radioActive.grid(row=8,column=0,sticky=W,padx=15,pady=10)

    radioInactive = Radiobutton(f2,font=('arial',17,'bold'),text="INACTIVE",
                              fg="dark slate blue",bg="light steel blue1",variable=input_Activity,value=input_Inactive)
    radioInactive.grid(row=9,column=0,sticky=W,padx=15,pady=10)

    if input_Frequency == input_Weekly:
        bill_recurrence = "Weekly"
    elif input_Frequency == input_Monthly:
        bill_recurrence = "Monthly"
    else:
        bill_recurrence = "Annually"
        
    if input_Activity == input_Active:
        active_or_inactive = "Active"
    else:
        active_or_inactive = "Inactive"



    def AddSub(entrySubscriptionName, entryPayment, bill_recurrence, active_or_inactive):
        name_of_subscription = entrySubscriptionName.get()
        payment_amount = entryPayment.get()            
        if input_Frequency == "" or input_Activity =="" or name_of_subscription =="" or payment_amount =="":
            messagebox.showerror("Missing information", "Please fill out all fields before adding your subscription.")
        else:                
            conn = sqlite3.connect('Password-Gen.db')
            conn.execute("INSERT INTO subscriptions_table(user_name,subscription,payment_frequency,payment_amount,activity) VALUES (?,?,?,?,?)",
                         (active_user, name_of_subscription, bill_recurrence, payment_amount, active_or_inactive))
            messagebox.showinfo("Success!", "Subscription to "+name_of_subscription+" has been added")
            conn.commit()
            conn.close()



    btnAddSub = Button(f2, font=('courier new',15,'bold'),text="ADD SUBSCRIPTION", fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,
                       command=lambda:AddSub(entrySubscriptionName, entryPayment, bill_recurrence, active_or_inactive))
    btnAddSub.grid(row=10,column=0,padx=15,pady=15,sticky=W)

    def LoadSubscriptions():
        conn = sqlite3.connect('Password-Gen.db')
        cursor = conn.cursor()
        cursor.execute("SELECT subscription FROM subscriptions_table WHERE user_name = ?", (active_user,))
        btnSub1["text"] = cursor.fetchone()
        btnSub2["text"] = cursor.fetchone()
        btnSub3["text"] = cursor.fetchone()
        btnSub4["text"] = cursor.fetchone()
        btnSub5["text"] = cursor.fetchone()
        btnSub6["text"] = cursor.fetchone()
        btnSub7["text"] = cursor.fetchone()
        btnSub8["text"] = cursor.fetchone()
        btnSub9["text"] = cursor.fetchone()
        btnSub10["text"] = cursor.fetchone()
        

    LoadSubscriptions()

    root.mainloop()


if __name__ == '__main__':
    main()

