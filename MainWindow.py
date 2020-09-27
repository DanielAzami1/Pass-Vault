from tkinter import *
from tkinter import messagebox
import time,random, sqlite3, os

def ReadFromUser():
    current_user = open("User","r")
    global active_user
    active_user = current_user.read()
    current_user.close

def main():
    ReadFromUser()

    SPECIALCHARACTERS ='!$%^&*@#¬'
    DIGITS = '0123456789'
    LOWERSET='abcdefghijklmnopqrstuvwxyz'
    UPPERSET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    global password 
    password = ""

    master = Tk()
    master.title("Vault")
    win_width = master.winfo_screenwidth()
    win_height = master.winfo_screenheight()
    
    master.geometry("%dx%d+0+0" % (win_width, win_height))

    LeftFrame = Frame(master, width=win_width/4, height=900, bg="light steel blue1", relief=GROOVE,borderwidth=5)
    LeftFrame.pack(side=LEFT,fill=Y,expand=False)

    RightFrame = Frame(master, width=win_width/2, height=900, bg="slate blue", relief=GROOVE,borderwidth=5)
    RightFrame.pack(side=RIGHT,fill=BOTH,expand=True)

    #================================LeftFrame===============================================
    lblTitle = Label(LeftFrame, font=('times',50,'bold','underline'),text="%s's Vault"%active_user,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
    lblTitle.grid(row=0,columnspan=2,padx=15,pady=15,sticky=W+E)

    lblGreeting = Label(LeftFrame, font=('courier new',11,'italic'),text="Any accounts you have stored in the Vault will be displayed here:\n [Click the icons to view account information]",
                        fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
    lblGreeting.grid(row=1,columnspan=2,padx=15,pady=15,sticky=W+E)

    def ManageAccount():
        master.withdraw()
        root = Tk()
        root.title("Manage Your Account")
        root.resizable(0,0)
        ManagerFrame = Frame(root, bg="alice blue",relief=GROOVE,borderwidth=5)
        ManagerFrame.pack(fill=BOTH, expand=True)

        lblTitleManager = Label(ManagerFrame, font=('system',35,'bold'),text="Welcome, %s"%active_user,fg="dark slate blue",bg="aquamarine",borderwidth=5,relief=SUNKEN)
        lblTitleManager.grid(row=0,columnspan=5,padx=15,pady=15,sticky=W+E)

        def OpenSecurityWindow():
                root.withdraw()
                master = Toplevel()
                master.geometry("1000x500")
                master.resizable(0,0)
                master.title("Choose Security Question")
                f1 = Frame(master, width=1000,height=100, relief=FLAT,borderwidth=3,bg="light slate blue")
                f1.pack(expand=True,fill=BOTH)
                f2 = Frame(master, width=1000,height=100, relief=SUNKEN,borderwidth=3,bg="dark slate blue")
                f2.pack(expand=True,fill=BOTH)
                f3 = Frame(master, width=1000,height=100, relief=FLAT,borderwidth=3,bg="light slate blue")
                f3.pack(expand=True,fill=BOTH)
                f4 = Frame(master, width=1000,height=200, relief=SUNKEN,borderwidth=3,bg="dark slate blue")
                f4.pack(expand=True,fill=BOTH)

                lblTitle = Label(f1, font=('system', 60,'underline'),text="Security Question",fg="ivory2",bg="light slate blue")
                lblTitle.grid(columnspan=3,padx=5,pady=5,sticky=W+E)
         
                lblInformation = Label(f1, font=('courier new', 12),text="Your privacy is important to us. Choose a security question to keep your data safe.",
                                       fg="ivory2",bg="dark slate blue")
                lblInformation.grid(row=1,columnspan=3,padx=5,pady=5,sticky=W+E)

                def QuestionOne():
                    master.withdraw()
                    root = Tk()
                    root.title("Answer")
                    root.resizable(0,0)
                    AnswerFrame = Frame(root, height=200,width=400, relief=FLAT,borderwidth=3,bg="light slate blue")
                    AnswerFrame.pack(expand=True,fill=BOTH)
                    lblQuestion = Label(AnswerFrame, font=('courier new',17,'bold'),text="In what city did your parents meet?",fg="ivory2",bg="dark slate blue",relief=FLAT)
                    lblQuestion.grid(row=0,columnspan=2, padx=10,pady=10,sticky=W)
                    EntryAnswer = Entry(AnswerFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
                    EntryAnswer.grid(row=1,columnspan=2,padx=10,pady=10,sticky=W+E)

                    def ReturnToQuestions():
                        root.withdraw()
                        master.deiconify()
                        
                    def SaveAnswerOne():
                        chosen_question = "In what city did your parents meet?"
                        security_answer = EntryAnswer.get()                    
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("SELECT chosen_security_question, security_answer FROM questions_table WHERE user_name = ?", (active_user,))
                        question_already_set = cursor.fetchone()
                        if security_answer == "":
                            messagebox.showerror("Ooops","Please enter an answer for the chosen security question")
                        elif question_already_set:
                            messagebox.showerror("Ooops","Sorry, it seems you have already set your security question")
                            ReturnToQuestions()
                        else:
                            conn.execute("INSERT INTO questions_table(user_name,chosen_security_question,security_answer) VALUES (?,?,?)", (active_user, chosen_question, security_answer))
                            conn.commit()
                            messagebox.showinfo("Success", "Security question successfully set")
                            ReturnToQuestions()                            

                        
                    
                    btnSave = Button(AnswerFrame,font=('courier new',15,'bold'),text="SAVE", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=SaveAnswerOne)
                    btnSave.grid(row=3,column=2,padx=15,pady=5)
                    
                    btnCancel = Button(AnswerFrame,font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=ReturnToQuestions)
                    btnCancel.grid(row=3,column=0,padx=15,pady=5,sticky=W)
                    

                def QuestionTwo():
                    master.withdraw()
                    root = Tk()
                    root.title("Answer")
                    root.resizable(0,0)
                    AnswerFrame = Frame(root, height=200,width=400, relief=FLAT,borderwidth=3,bg="light slate blue")
                    AnswerFrame.pack(expand=True,fill=BOTH)
                    lblQuestion = Label(AnswerFrame, font=('courier new',17,'bold'),text="What was the name of your first pet?",fg="ivory2",bg="dark slate blue",relief=FLAT)
                    lblQuestion.grid(row=0,columnspan=2, padx=10,pady=10,sticky=W)
                    EntryAnswer = Entry(AnswerFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
                    EntryAnswer.grid(row=1,columnspan=2,padx=10,pady=10,sticky=W+E)

                    def SaveAnswerTwo():
                        chosen_question = "What was the name of your first pet?"
                        security_answer = EntryAnswer.get()                    
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("SELECT chosen_security_question, security_answer FROM questions_table WHERE user_name = ?", (active_user,))
                        question_already_set = cursor.fetchone()
                        if security_answer == "":
                            messagebox.showerror("Ooops","Please enter an answer for the chosen security question")
                        elif question_already_set == None:
                            conn.execute("INSERT INTO questions_table(user_name,chosen_security_question,security_answer) VALUES (?,?,?)", (active_user, chosen_question, security_answer))
                            conn.commit()
                            messagebox.showinfo("Success", "Security question successfully set")
                            ReturnToQuestions()
                        else:
                            messagebox.showerror("Ooops","Sorry, it seems you have already set your security question")
                            ReturnToQuestions()
                            
                    btnSave = Button(AnswerFrame,font=('courier new',15,'bold'),text="SAVE", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=SaveAnswerTwo)
                    btnSave.grid(row=3,column=2,padx=15,pady=5)

                    def ReturnToQuestions():
                        root.withdraw()
                        master.deiconify()
                        
                    btnCancel = Button(AnswerFrame,font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=ReturnToQuestions)
                    btnCancel.grid(row=3,column=0,padx=15,pady=5,sticky=W)



                def QuestionThree():
                    master.withdraw()
                    root = Tk()
                    root.title("Answer")
                    root.resizable(0,0)
                    AnswerFrame = Frame(root, height=200,width=400, relief=FLAT,borderwidth=3,bg="light slate blue")
                    AnswerFrame.pack(expand=True,fill=BOTH)
                    lblQuestion = Label(AnswerFrame, font=('courier new',17,'bold'),text="What is your favourite TV show?",fg="ivory2",bg="dark slate blue",relief=FLAT)
                    lblQuestion.grid(row=0,columnspan=2, padx=10,pady=10,sticky=W)
                    EntryAnswer = Entry(AnswerFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
                    EntryAnswer.grid(row=1,columnspan=2,padx=10,pady=10,sticky=W+E)

                    def SaveAnswerThree():
                        chosen_question = "What is your favourite TV show?"
                        security_answer = EntryAnswer.get()                    
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("SELECT chosen_security_question, security_answer FROM questions_table WHERE user_name = ?", (active_user,))
                        question_already_set = cursor.fetchone()
                        if security_answer == "":
                            messagebox.showerror("Ooops","Please enter an answer for the chosen security question")
                        elif question_already_set == None:
                            conn.execute("INSERT INTO questions_table(user_name,chosen_security_question,security_answer) VALUES (?,?,?)", (active_user, chosen_question, security_answer))
                            conn.commit()
                            messagebox.showinfo("Success", "Security question successfully set")
                            ReturnToQuestions()
                        else:
                            messagebox.showerror("Ooops","Sorry, it seems you have already set your security question")
                            ReturnToQuestions()
                    btnSave = Button(AnswerFrame,font=('courier new',15,'bold'),text="SAVE", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=SaveAnswerThree)
                    btnSave.grid(row=3,column=2,padx=15,pady=5)

                    def ReturnToQuestions():
                        root.withdraw()
                        master.deiconify()
                        
                    btnCancel = Button(AnswerFrame,font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=ReturnToQuestions)
                    btnCancel.grid(row=3,column=0,padx=15,pady=5,sticky=W)

                def QuestionFour():
                    master.withdraw()
                    root = Tk()
                    root.title("Answer")
                    root.resizable(0,0)
                    AnswerFrame = Frame(root, height=200,width=400, relief=FLAT,borderwidth=3,bg="light slate blue")
                    AnswerFrame.pack(expand=True,fill=BOTH)
                    lblQuestion = Label(AnswerFrame, font=('courier new',17,'bold'),text="Name a memorable character or figure",fg="ivory2",bg="dark slate blue",relief=FLAT)
                    lblQuestion.grid(row=0,columnspan=2, padx=10,pady=10,sticky=W)
                    EntryAnswer = Entry(AnswerFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
                    EntryAnswer.grid(row=1,columnspan=2,padx=10,pady=10,sticky=W+E)

                    def SaveAnswerFour():
                        chosen_question = "Name a memorable character or figure"
                        security_answer = EntryAnswer.get()                    
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("SELECT chosen_security_question, security_answer FROM questions_table WHERE user_name = ?", (active_user,))
                        question_already_set = cursor.fetchone()
                        if security_answer == "":
                            messagebox.showerror("Ooops","Please enter an answer for the chosen security question")
                        elif question_already_set == None:
                            conn.execute("INSERT INTO questions_table(user_name,chosen_security_question,security_answer) VALUES (?,?,?)", (active_user, chosen_question, security_answer))
                            conn.commit()
                            messagebox.showinfo("Success", "Security question successfully set")
                            ReturnToQuestions()
                        else:
                            messagebox.showerror("Ooops","Sorry, it seems you have already set your security question")
                            ReturnToQuestions()
                    
                    btnSave = Button(AnswerFrame,font=('courier new',15,'bold'),text="SAVE", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=SaveAnswerFour)
                    btnSave.grid(row=3,column=2,padx=15,pady=5)

                    def ReturnToQuestions():
                        root.withdraw()
                        master.deiconify()
                        
                    btnCancel = Button(AnswerFrame,font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=ReturnToQuestions)
                    btnCancel.grid(row=3,column=0,padx=15,pady=5,sticky=W)

                btnQuestionOne = Button(f2, font=('courier new',15,'italic','bold'),text="In what city did your parents meet?",fg="ivory2",bg="light slate blue",relief=RAISED,borderwidth=3, command=QuestionOne)
                btnQuestionOne.pack(side=LEFT,padx=10,pady=10)

                btnQuestionThree = Button(f2, font=('courier new',15,'italic','bold'),text="What is your favourite TV show?",fg="ivory2",bg="light slate blue",relief=RAISED,borderwidth=3, command=QuestionThree)
                btnQuestionThree.pack(side=RIGHT,padx=10,pady=10)       

                btnQuestionTwo = Button(f4, font=('courier new',15,'italic','bold'),text="What was the name of your first pet?",fg="ivory2",bg="light slate blue",relief=RAISED,borderwidth=3, command=QuestionTwo)
                btnQuestionTwo.pack(side=LEFT,padx=10,pady=10)

                btnQuestionFour = Button(f4, font=('courier new',15,'italic','bold'),text="Name a memorable character or figure",fg="ivory2",bg="light slate blue",relief=RAISED,borderwidth=3, command=QuestionFour)
                btnQuestionFour.pack(side=RIGHT,padx=10,pady=10)   

                lblExtraInformation = Label(f3, font=('courier new',11,'italic'),text="Remember to keep your answers concise and memorable - \nThis is the only way to login if you forget your password",
                                            fg="ivory2",bg="dark slate blue")
                lblExtraInformation.pack()

                def ReturnToAccountManager():
                    root.deiconify()
                    master.destroy()

                btnReturnToAccountManager= Button(f3, font=('courier new',15,'bold'),text="RETURN TO ACCOUNT MANAGER",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ReturnToAccountManager)
                btnReturnToAccountManager.pack(pady=20,padx=10,side=LEFT)

                def ResetSecurityQuestion():
                    conn = sqlite3.connect('Password-Gen.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT chosen_security_question, security_answer FROM questions_table WHERE user_name = ?", (active_user,))
                    question_exists = cursor.fetchone()
                    if question_exists:
                        cursor.execute("DELETE FROM questions_table WHERE user_name = ?", (active_user,))
                        conn.commit()
                        messagebox.showinfo("Successful", "Security question successfully reset")
                        conn.close()
                    else:
                        messagebox.showwarning("Ooops","Security question has not been declared yet")

                btnResetSecurityQuestion = Button(f3, font=('courier new',15,'bold'),text="RESET SECURITY QUESTION",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ResetSecurityQuestion)
                btnResetSecurityQuestion.pack(pady=20,padx=10,side=RIGHT)

        def UpdateEmail():
            updateEmailWindow = Toplevel()
            updateEmailWindow.title("Add your email address for additional login options")
            updateEmailWindow.configure(background = "slate blue")
            lblEmailToAdd = Label(updateEmailWindow, font=('courier new',15,'bold'),text="Update/Enter your email",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailToAdd.grid(row=0,column=0,padx=15,pady=15,sticky=W)
            entryEmail = Entry(updateEmailWindow, font=('courier new',17),insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
            entryEmail.grid(row=0,column=1,sticky=W,padx=15,pady=15)

            def SaveEmail(entryEmail, active_user):
                email_update = entryEmail.get()
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE users_table SET email_address_main = ? WHERE user_name = ?", (email_update, active_user))
                conn.commit()
                messagebox.showinfo("Success", "Email added to DB")
                updateEmailWindow.destroy()
                
            btnSaveEmail = Button(updateEmailWindow, font=('courier new',15,'bold'),text="SAVE EMAIL",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=lambda:SaveEmail(entryEmail, active_user))
            btnSaveEmail.grid(row=1,column=2,padx=15,pady=15,sticky=E)  
            
            btnCancel = Button(updateEmailWindow,font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=updateEmailWindow.destroy)
            btnCancel.grid(row=1,column=0,padx=15,pady=5,sticky=W)

        btnOpenEmailWindow = Button(ManagerFrame,font=('courier new',15,'bold'),text="UPDATE EMAIL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=UpdateEmail)
        btnOpenEmailWindow.grid(row=4,columnspan=5,padx=15,pady=5,sticky=W+E)             

    #=============================================Security Questions=====================================   
        btnSecurityQuestion = Button(ManagerFrame, font=('courier new',15,'bold'),text="CHOOSE SECURITY QUESTION",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=OpenSecurityWindow)
        btnSecurityQuestion.grid(row=2,columnspan=5,padx=15,pady=15,sticky=W+E)

        def SeeAccountDetails():
            root.withdraw()
            master = Tk()
            master.title("Account Details")
            master.resizable(0,0)
            master.configure(bg="light slate blue")
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            cursor.execute("SELECT user_pass FROM users_table WHERE user_name = ?", (active_user,))
            master_pass = cursor.fetchone()
            cursor.execute("SELECT security_answer FROM questions_table WHERE user_name =?", (active_user,))
            given_answer = cursor.fetchone()
            lblUsername = Label(master, font=('system',25,'bold'),text="Username: %s"%active_user,fg="black",bg="aquamarine",borderwidth=3,relief=SUNKEN)
            lblUsername.grid(row=0,column=0,padx=15,pady=15,sticky=W)
            lblPassword = Label(master, font=('system',25,'bold'),text="Password: %s"%master_pass,fg="black",bg="aquamarine",borderwidth=3,relief=SUNKEN)
            lblPassword.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            lblSecurityQuestion = Label(master, font=('system',25,'bold'),text="Security Answer: %s"%given_answer,fg="black",bg="aquamarine",borderwidth=3,relief=SUNKEN)
            lblSecurityQuestion.grid(row=2,column=0,padx=15,pady=15,sticky=W)
        
            def ResetPassword():
                master.withdraw()
                root = Tk()
                root.title("Reset Password")
                root.resizable(0,0)
                root.configure(bg="dark slate blue")
                lblResetPass = Label(root, font=('system',20,'bold'),text="New Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
                lblResetPass.grid(row=0,column=0,padx=15,pady=15,sticky=W)
                entryPassReset = Entry(root,font=('courier new',17),insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
                entryPassReset.grid(row=0,column=1,sticky=W,padx=15,pady=15)


                def SaveReset():
                    reset_userpass = entryPassReset.get()
                    if reset_userpass == "":
                        messagebox.showwarning("Ooops", "Please enter a password")
                    else:
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("UPDATE users_table SET user_pass = ? WHERE user_name = ?", (reset_userpass, active_user))
                        conn.commit()
                        messagebox.showinfo("Success!", "Password updated - Re-open 'Account Details' to see changes")
                        root.destroy()
                        master.deiconify()


                btnFinishAndSave = Button(root, font=('courier new',15,'bold'),text="SUBMIT",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=SaveReset)
                btnFinishAndSave.grid(row=2,columnspan=5,padx=15,pady=15,sticky=E)
                
                def ReturnToSeeDetails():
                    root.destroy()
                    master.deiconify()

                btnCancel = Button(root, font=('courier new',15,'bold'),text="CANCEL",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ReturnToSeeDetails)
                btnCancel.grid(row=2,columnspan=5,padx=15,pady=15,sticky=W)

                        
            
            btnResetPassword = Button(master, font=('courier new',15,'bold'),text="RESET",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ResetPassword)
            btnResetPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)
            
            def ReturnToAccountManager():
                root.deiconify()
                master.destroy()
                
            btnReturnToAccountManager = Button(master, font=('courier new',15,'bold'),text="RETURN TO ACCOUNT MANAGER",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ReturnToAccountManager)
            btnReturnToAccountManager.grid(row=3,columnspan=3,padx=15,pady=15,sticky=W+E)
            

        btnSeeAccountDetails = Button(ManagerFrame, font=('courier new',15,'bold'),text="VIEW ACCOUNT DETAILS",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=SeeAccountDetails)
        btnSeeAccountDetails.grid(row=3,columnspan=5,padx=15,pady=15,sticky=W+E)

        def ReturnToMainWindow():
            root.destroy()
            master.deiconify()

        btnReturnToMainWindow = Button(ManagerFrame, font=('courier new',15,'bold'),text="RETURN TO MAIN WINDOW",fg="ivory",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ReturnToMainWindow)
        btnReturnToMainWindow.grid(row=5,column=0,padx=15,pady=15,sticky=W)
            
        

        

    btnManageAccount = Button(LeftFrame,font=('courier new', 15, 'bold'),text="MANAGE ACCOUNT",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ManageAccount,cursor="hand1")
    btnManageAccount.grid(row=9,column=1,sticky=E,padx=10,pady=10)
#===============================Button Functions==============================================
    def OpenButton1():
        current_application = btnAccount1["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount1["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()

    def OpenButton2():
        current_application = btnAccount2["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount2["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton3():
        current_application = btnAccount3["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount3["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton4():
        current_application = btnAccount4["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount4["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton5():
        current_application = btnAccount5["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount5["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()

    def OpenButton6():
        current_application = btnAccount6["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                root.destroy()
                conn.close()
                btnAccount6["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton7():
        current_application = btnAccount7["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount7["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton8():
        current_application = btnAccount8["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                root.destroy()
                conn.close()
                btnAccount8["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton9():
        current_application = btnAccount9["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount9["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()


    def OpenButton10():
        current_application = btnAccount10["text"]
        if current_application == "Available slot":
            messagebox.showinfo("Empty Slot", "Slot has not been allocated to an account yet")
        else:
            root = Toplevel()
            root.grab_set()
            root.title("More information")
            root.resizable(0,0)
            f1 = Frame(root, width=600, height=350, bg="light slate blue", relief=GROOVE,borderwidth=5)
            f1.pack(side=LEFT,fill=BOTH,expand=True)
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            lblAppDesc = Label(f1, font=('system',30,'bold'),text="Application",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblAppDesc.grid(row=0,column=0,padx=15,pady=15,sticky=W)        
            lblApp = Label(f1, font=('system',20,'bold'),text="%s"%current_application,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblApp.grid(row=0,column=1,padx=15,pady=15,sticky=W)

            lblPassDesc = Label(f1, font=('system',30,'bold'),text="Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblPassDesc.grid(row=1,column=0,padx=15,pady=15,sticky=W)
            cursor.execute("SELECT password FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_password = cursor.fetchone()
            
            def CopyToClip():
                root.clipboard_clear()
                root.clipboard_append(retrieved_password[0])
                root.update()
                btnPassword["text"] = "Copied To Clipboard"
                btnPassword.configure(fg="pale green",font="system")
                
            btnPassword = Button(f1, font=('system',15,'bold'),text="%s"%retrieved_password[0],fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RAISED, command=CopyToClip,cursor="bottom_right_corner")
            btnPassword.grid(row=1,column=1,padx=15,pady=15,sticky=W)

            lblEmailDesc = Label(f1, font=('system',30,'bold'),text="Email Address",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
            lblEmailDesc.grid(row=2,column=0,padx=15,pady=15,sticky=W)       
            cursor.execute("SELECT email_address FROM passwords_table WHERE application = ? AND user_name = ?", (current_application, active_user))
            retrieved_email = cursor.fetchone()
            lblEmail = Label(f1, font=('system',15,'bold'),text="%s"%retrieved_email,fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE)
            lblEmail.grid(row=2,column=1,padx=15,pady=15,sticky=W)
        
            btnCloseMoreInfo = Button(f1, font=('courier new',20,'bold'),text="CLOSE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE, command=root.destroy,cursor="X_cursor")
            btnCloseMoreInfo.grid(row=3,column=0, padx=15,pady=15,sticky=W)

            def DeleteAccount(current_application):
                conn = sqlite3.connect('Password-Gen.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, current_application))
                root.destroy()
                conn.commit()
                conn.close()
                btnAccount10["text"] = "Available slot"

            btnDelete = Button(f1, font=('courier new',20,'bold'),text="DELETE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=RIDGE,command=lambda:DeleteAccount(current_application),cursor="hand1")
            btnDelete.grid(row=3,column=1,padx=15,pady=15,sticky=E)
                        
            conn.close()

#===============================Button Functions==============================================        
    btnAccount1 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton1,cursor="iron_cross")
    btnAccount1.grid(row=2,columnspan=2,padx=15,pady=15,sticky=W)

    btnAccount2 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton2,cursor="iron_cross")
    btnAccount2.grid(row=3,columnspan=2,padx=15,pady=15,sticky=W)

    btnAccount3 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton3,cursor="iron_cross")
    btnAccount3.grid(row=4,columnspan=2,padx=15,pady=15,sticky=W)

    btnAccount4 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton4,cursor="iron_cross")
    btnAccount4.grid(row=5,columnspan=2,padx=15,pady=15,sticky=W)

    btnAccount5 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton5,cursor="iron_cross")
    btnAccount5.grid(row=6,columnspan=2,padx=15,pady=15,sticky=W)

    btnAccount6 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton6,cursor="iron_cross")
    btnAccount6.grid(row=2,columnspan=2,padx=15,pady=15,sticky=E)

    btnAccount7 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton7,cursor="iron_cross")
    btnAccount7.grid(row=3,columnspan=2,padx=15,pady=15,sticky=E)

    btnAccount8 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton8,cursor="iron_cross")
    btnAccount8.grid(row=4,columnspan=2,padx=15,pady=15,sticky=E)

    btnAccount9 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton9,cursor="iron_cross")
    btnAccount9.grid(row=5,columnspan=2,padx=15,pady=15,sticky=E)

    btnAccount10 = Button(LeftFrame, font=('courier new',18,'bold'),text="Available slot",fg="ivory2",bg="slate blue",borderwidth=3,relief=GROOVE, command=OpenButton10,cursor="iron_cross")
    btnAccount10.grid(row=6,columnspan=2,padx=15,pady=15,sticky=E)

    #Simple function to change the cursor when an account is added
    def ChangeCursors():
        if btnAccount1["text"] != "Available slot":
            btnAccount1.configure(cursor="rtl_logo")
        else:
            btnAccount1.configure(cursor="iron_cross")
        if btnAccount2["text"] != "Available slot":
            btnAccount2.configure(cursor="rtl_logo")
        else:
            btnAccount2.configure(cursor="iron_cross")
        if btnAccount3["text"] != "Available slot":
            btnAccount3.configure(cursor="rtl_logo")
        else:
            btnAccount3.configure(cursor="iron_cross")
        if btnAccount4["text"] != "Available slot":
            btnAccount4.configure(cursor="rtl_logo")
        else:
            btnAccount4.configure(cursor="iron_cross")
        if btnAccount5["text"] != "Available slot":
            btnAccount5.configure(cursor="rtl_logo")
        else:
            btnAccount5.configure(cursor="iron_cross")
        if btnAccount6["text"] != "Available slot":
            btnAccount6.configure(cursor="rtl_logo")
        else:
            btnAccount6.configure(cursor="iron_cross")
        if btnAccount7["text"] != "Available slot":
            btnAccount7.configure(cursor="rtl_logo")
        else:
            btnAccount7.configure(cursor="iron_cross")
        if btnAccount8["text"] != "Available slot":
            btnAccount8.configure(cursor="rtl_logo")
        else:
            btnAccount8.configure(cursor="iron_cross")
        if btnAccount9["text"] != "Available slot":
            btnAccount9.configure(cursor="rtl_logo")
        else:
            btnAccount9.configure(cursor="iron_cross")
        if btnAccount10["text"] != "Available slot":
            btnAccount10.configure(cursor="rtl_logo")
        else:
            btnAccount10.configure(cursor="iron_cross")

        master.after(1, ChangeCursors)

    ChangeCursors()

    def SignOut(event):
        master.destroy()
        try:
            os.remove("RememberUser.txt")
            print("\n{Credential save cancelled - User has signed out}\n")
        except:
            pass
        from LoginWindow import main
        main()

    btnSignOut = Button(LeftFrame, font=('courier new',15,'bold'),text="SIGN OUT",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=lambda:SignOut(event=None),cursor="hand1")
    btnSignOut.grid(row=8,column=0,padx=15,pady=15,sticky=W)

    master.bind("<Escape>", SignOut)

    def SubscriptionManager():
        master.destroy()
        from SubscriptionManager import main
        main()

    btnSubscriptionManager = Button(LeftFrame, font=('courier new',15,'bold'),text="SUBSCRIPTION MANAGER",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=SubscriptionManager,cursor="hand1")
    btnSubscriptionManager.grid(row=8,column=1,padx=15,pady=15,sticky=E)

    btnExit = Button(LeftFrame, font=('courier new',15,'bold'),text="EXIT",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=master.destroy,cursor="X_cursor")
    btnExit.grid(row=9,column=0,padx=15,pady=15,sticky=W)
    #=============================================Security Questions=====================================

    #================================LeftFrame============================================
    #================================RightFrame===========================================
    lblGeneratorTitle = Label(RightFrame, font=('system',80,'bold','underline'),text="Generator",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=FLAT)
    lblGeneratorTitle.grid(row=0,columnspan=2,sticky=W,padx=15,pady=15)

    input_Account = StringVar()

    input_Email = StringVar()

    input_Length = IntVar()

    input_Uppers = IntVar()

    input_Digits = IntVar()

    input_Specials = IntVar()

    def InfoPopup():
        messagebox.showinfo("Information","To add an account, you must simply fill out the fields below and press 'Generate'. Or, if you'd prefer, pick your own password using the button on the top.\n\nAccounts will only be stored if BOTH an email address and application are provided.")

    btnWhatIsThis = Button(RightFrame, font=('courier new',15,'bold'),text="Adding accounts",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=InfoPopup,cursor="hand1")
    btnWhatIsThis.grid(row=2,column=0,padx=15,pady=15,sticky=W)

    def ToolTip():
        messagebox.showinfo("Quick Tip", "Shortcuts:\nPress [Enter] key to generate passwords\nPress [Escape] key to sign out")

    btnToolTip = Button(RightFrame, font=('courier new',15,'bold'),text="Tool-Tip",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ToolTip,cursor="hand1")
    btnToolTip.grid(row=2,column=1,padx=15,pady=15,sticky=W)

    def UseOwnPassword():
        root = Toplevel()
        root.grab_set()
        root.title("Manually Add Account")
        root.resizable(0,0)
        MainFrame = Frame(root, width=600,height=400, relief=GROOVE,borderwidth=5,bg="slate blue")
        MainFrame.pack(fill=BOTH,expand=True)
        
        lblInformation = Label(MainFrame, font=('courier new',10), text="Using your own password is risky, but we understand if you want your password to be a bit more personal.",fg="ivory2",bg="dark slate blue")
        lblInformation.grid(row=0,columnspan=5,sticky=W,pady=10,padx=10)

        lblAccountOwn = Label(MainFrame, font=('courier new',17,'bold'),text="Account/Application",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
        lblAccountOwn.grid(row=1,column=0,sticky=E,padx=15,pady=15)
        entryAccountOwn = Entry(MainFrame,font=('courier new',17), insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
        entryAccountOwn.grid(row=1,column=1,sticky=W)

        lblEmailAddressOwn = Label(MainFrame, font=('courier new',17,'bold'),text="Account Email Address",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
        lblEmailAddressOwn.grid(row=2,column=0,sticky=E,padx=15,pady=15)
        entryEmailAddressOwn = Entry(MainFrame,font=('courier new',17),insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
        entryEmailAddressOwn.grid(row=2,column=1,sticky=W)

        lblPasswordOwn = Label(MainFrame, font=('courier new',17,'bold'),text="Your Password",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
        lblPasswordOwn.grid(row=3,column=0,sticky=E,padx=15,pady=15)
        entryPasswordOwn = Entry(MainFrame,font=('courier new',17),insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
        entryPasswordOwn.grid(row=3,column=1,sticky=W)

        def StoreAccountOwn(entryAccountOwn,entryEmailAddressOwn,entryPasswordOwn):
            
            application_own = entryAccountOwn.get()
            email_own = entryEmailAddressOwn.get()
            password_own = entryPasswordOwn.get()

            if application_own == "" or email_own == "" or password_own == "":
                messagebox.showerror("Ooops", "Please fill out all required fields")
            else:
                conn = sqlite3.connect('Password-Gen.db')
                conn.execute("INSERT INTO passwords_table VALUES (?,?,?,?)", (active_user,application_own,email_own,password_own))
                conn.commit()
                conn.close()
                root.destroy()
                messagebox.showinfo("Success", "You have manually added '"+application_own+"' under email address - ''"+email_own+"' - with password '"+password_own+"'")
                LoadAccounts()

        btnStoreAccountOwn = Button(MainFrame, font=('courier new',15,'bold'),text="FINISH AND SAVE",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,
                                    command=lambda:StoreAccountOwn(entryAccountOwn,entryEmailAddressOwn,entryPasswordOwn),cursor="hand1")
        btnStoreAccountOwn.grid(row=4,column=2,sticky=W,padx=15,pady=15)

        def ReturnToMainWindow():
            root.destroy()
            master.deiconify()

        btnReturnToMainWindow = Button(MainFrame, font=('courier new',15,'bold'),text="CANCEL",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=ReturnToMainWindow,cursor="hand1")
        btnReturnToMainWindow.grid(row=4,column=0,sticky=W,padx=15,pady=15)

    btnUseOwnPassword = Button(RightFrame, font=('courier new',15,'bold'),text="Use Own Password",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=UseOwnPassword,cursor="hand1")
    btnUseOwnPassword.grid(row=0,column=1,sticky=S,pady=45)

    def PassStrength():
        length = input_Length.get()
        upper_characters = input_Uppers.get()
        digit_characters = input_Digits.get()
        special_characters = input_Specials.get()
        if upper_characters == 0 and digit_characters == 0 and special_characters == 0:
            lblShowPassStrength["text"] = "Questionable"
            lblShowPassStrength.configure(fg="alice blue")
            lblShowPassStrength.configure(bg="powder blue")

        elif upper_characters == 1 and digit_characters == 0 and special_characters == 0:
            lblShowPassStrength["text"] = "Getting Better"
            lblShowPassStrength.configure(bg="light green")
            lblShowPassStrength.configure(fg="alice blue")

        elif upper_characters == 0 and digit_characters == 1 and special_characters == 0:
            lblShowPassStrength["text"] = "Getting Better"
            lblShowPassStrength.configure(fg="alice blue")
            lblShowPassStrength.configure(bg="light green")        

        elif upper_characters == 0 and digit_characters == 0 and special_characters == 1:
            lblShowPassStrength["text"] = "Getting Better"
            lblShowPassStrength.configure(fg="alice blue")
            lblShowPassStrength.configure(bg="light green")

        elif upper_characters == 1 and digit_characters == 1 and special_characters == 0:
            lblShowPassStrength["text"] = "Not Bad"
            lblShowPassStrength.configure(bg="orange")
            lblShowPassStrength.configure(fg="alice blue")

        elif upper_characters == 0 and digit_characters == 1 and special_characters == 1:
            lblShowPassStrength["text"] = "Not Bad"
            lblShowPassStrength.configure(bg="orange")
            lblShowPassStrength.configure(fg="alice blue")

        elif upper_characters == 1 and digit_characters == 0 and special_characters == 1:
            lblShowPassStrength["text"] = "Not Bad"
            lblShowPassStrength.configure(bg="orange")
            lblShowPassStrength.configure(fg="alice blue")

        elif upper_characters == 1 and digit_characters == 1 and special_characters == 1:
            lblShowPassStrength["text"] = "Impressive"
            lblShowPassStrength.configure(bg="red")
            lblShowPassStrength.configure(fg="alice blue")

        master.after(1,PassStrength)
        
    lblPassStrength = Label(RightFrame, font=('courier new',13,'bold'),text="How Strong Is My Password?",fg="ivory2",bg="dark slate blue",relief=SUNKEN,borderwidth=3)
    lblPassStrength.grid(row=10,column=1,sticky=W)

    lblShowPassStrength = Label(RightFrame, font=('times',18,'bold'),text="STRENGTH",fg="ivory2",bg="dark slate blue",relief=SUNKEN,borderwidth=5)
    lblShowPassStrength.grid(row=10,column=2,ipadx=5,ipady=5)
    PassStrength()

    def MasterReset():
        conn = sqlite3.connect('Password-Gen.db')
        cursor = conn.cursor()
        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ?", (active_user,))
        accounts_stored = cursor.fetchone()
        if accounts_stored == None:
            messagebox.showinfo("Ooops!", "No accounts stored on the system")
        else:
            cursor.execute("DELETE FROM passwords_table")
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "All stored accounts have been wiped from the system")
            btnAccount1["text"] = "Available slot"
            btnAccount2["text"] = "Available slot"
            btnAccount3["text"] = "Available slot"
            btnAccount4["text"] = "Available slot"
            btnAccount5["text"] = "Available slot"
            btnAccount6["text"] = "Available slot"
            btnAccount7["text"] = "Available slot"
            btnAccount8["text"] = "Available slot"
            btnAccount9["text"] = "Available slot"
            btnAccount10["text"] = "Available slot"


    btnMasterReset = Button (RightFrame, font=('courier new',15,'bold'),text="Reset All Accounts",fg="ivory2",bg="dark slate blue",borderwidth=3,relief=GROOVE,command=MasterReset,cursor="hand1")
    btnMasterReset.grid(row=0,column=1,sticky=N,padx=15,pady=15)

    lblAccount = Label(RightFrame, font=('courier new',17,'bold'),text="Account/Application",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblAccount.grid(row=3,column=0,sticky=E,padx=15,pady=15)
    entryAccount = Entry(RightFrame,font=('courier new',17),textvariable=input_Account, insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    entryAccount.grid(row=3,column=1,sticky=W)

    lblEmailAddress = Label(RightFrame, font=('courier new',17,'bold'),text="Account Email Address",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblEmailAddress.grid(row=4,column=0,sticky=E,padx=15,pady=15)
    entryEmailAddress = Entry(RightFrame,font=('courier new',17),textvariable=input_Email, insertwidth=4,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    entryEmailAddress.grid(row=4,column=1,sticky=W)
        
    lblPassLength = Label(RightFrame, font=('courier new',16,'bold'),text="Number of Characters",fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN)
    lblPassLength.grid(row=5,column=0,sticky=E,padx=15,pady=15)
    entryPassLength = Scale(RightFrame,from_=0, to =20,orient=HORIZONTAL,fg="azure2",bg="dark slate blue",borderwidth=3,relief=SUNKEN,variable=input_Length,cursor="hand2")
    entryPassLength.grid(row=5,column=1,sticky=W)

    lblParameters = Label(RightFrame, font=('courier new',16,'bold','underline'),text="Extra requirements",fg="azure2",bg="dark slate blue",borderwidth=3,relief=FLAT)
    lblParameters.grid(row=6,column=0,sticky=W,padx=15,pady=15)

    checkUpperCase = Checkbutton(RightFrame,font=('courier new',16,'bold'),text="Upper-Case Characters",fg="DeepSkyBlue2",bg="slate blue", variable=input_Uppers,cursor="hand2")
    checkUpperCase.grid(row=7,columnspan=2,sticky=W,padx=15,pady=15)

    checkDigits = Checkbutton(RightFrame,font=('courier new',16,'bold'),text="Digits",fg="DeepSkyBlue2",bg="slate blue", variable=input_Digits,cursor="hand2")
    checkDigits.grid(row=8,columnspan=2,sticky=W,padx=15,pady=15)

    checkSpecialCharacters = Checkbutton(RightFrame,font=('courier new',16,'bold'),text="Special Characters",fg="DeepSkyBlue2",bg="slate blue", variable=input_Specials,cursor="hand2")
    checkSpecialCharacters.grid(row=9,columnspan=2,sticky=W,padx=15,pady=15)

    def CheckAccountNumber():
        conn = sqlite3.connect('Password-Gen.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM passwords_table WHERE user_name = ?",(active_user,))
        result = cursor.fetchone()
        global num_of_accounts
        num_of_accounts = result[0]
        conn.close()

    def Generate(password, input_Uppers, input_Length, input_Digits, input_Specials,entryAccount, entryExpirationDate,event):
    
        pass_length = input_Length.get()
        upper_characters = input_Uppers.get()
        digit_characters = input_Digits.get()
        special_characters = input_Specials.get()
        account = entryAccount.get()
        email_address = entryEmailAddress.get()
        conn = sqlite3.connect('Password-Gen.db')
        
        if pass_length == 0:
            messagebox.showwarning("Oops!","Password length not set.")
        else:
            if upper_characters  == 0 and digit_characters  == 0 and special_characters  == 0:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0, len(LOWERSET))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful", password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")

            elif upper_characters  == 1 and digit_characters  == 0 and special_characters  == 0:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + UPPERSET[random.randrange(0,len(UPPERSET))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful",password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")
                    
            elif upper_characters == 1 and digit_characters  == 1 and special_characters  == 0:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + UPPERSET[random.randrange(0,len(UPPERSET))] + DIGITS[random.randrange(0,len(DIGITS))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful",password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")
                    
            elif upper_characters == 1 and digit_characters  == 1 and special_characters == 1:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + UPPERSET[random.randrange(0,len(UPPERSET))] + DIGITS[random.randrange(0,len(DIGITS))] + SPECIALCHARACTERS[random.randrange(0,len(SPECIALCHARACTERS))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful",password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")
                        
            elif upper_characters == 0 and digit_characters  == 1 and special_characters == 0:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + DIGITS[random.randrange(0,len(DIGITS))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful",password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")
                    
            elif upper_characters == 0 and digit_characters  == 1 and special_characters == 1:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + DIGITS[random.randrange(0,len(DIGITS))] + SPECIALCHARACTERS[random.randrange(0,len(SPECIALCHARACTERS))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful", password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")

            elif upper_characters == 0 and digit_characters  == 0 and special_characters == 1:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + SPECIALCHARACTERS[random.randrange(0,len(SPECIALCHARACTERS))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful", password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")

            elif upper_characters == 1 and digit_characters  == 0 and special_characters == 1:
                for i in range(0, pass_length):
                    password = password + LOWERSET[random.randrange(0,len(LOWERSET))] + UPPERSET[random.randrange(0,len(UPPERSET))] + SPECIALCHARACTERS[random.randrange(0,len(SPECIALCHARACTERS))]
                    password = password[:pass_length]
                if account == "" or email_address == "":
                    messagebox.showinfo("Generation successful",password)
                else:
                    CheckAccountNumber()
                    if num_of_accounts > 9:
                        messagebox.showwarning("Insufficient storage", "Sorry! you've used up all of your available slots. Delete some of your accounts if you want to add more.")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ? AND application = ?", (active_user, account))
                        existing_account = cursor.fetchone()
                        if existing_account == None:
                            messagebox.showinfo("Generation successful", "Your new Password for your '"+account+"' account is ["+password+"], and is linked to '"+email_address+"'")
                            conn.execute("INSERT INTO passwords_table(user_name, application, email_address, password) VALUES (?,?,?,?)",(active_user, account, email_address, password))
                            conn.commit()
                            conn.close()
                            LoadAccounts()
                        else:
                            messagebox.showerror("Ooops","Account already exists!")
                   
    btnGenerate = Button(RightFrame,font=('courier new',18,'bold'),text="GENERATE",fg="azure2",bg="dark slate blue",relief=GROOVE, command= lambda:Generate(password, input_Uppers,
                                                                                                                                                            input_Length, input_Digits, input_Specials, entryAccount, entryEmailAddress,event=None),cursor="hand1")
    btnGenerate.grid(row=10,column=0,sticky=W,padx=15,pady=15)

    master.bind("<Return>", lambda event: Generate(password, input_Uppers, input_Length, input_Digits, input_Specials, entryAccount, entryEmailAddress,event))
    
    def LoadAccounts():
        conn = sqlite3.connect('Password-Gen.db')
        cursor = conn.cursor()
        cursor.execute("SELECT application FROM passwords_table WHERE user_name = ?", (active_user,))
        btnAccount1["text"] = cursor.fetchone()
        btnAccount2["text"] = cursor.fetchone()
        btnAccount3["text"] = cursor.fetchone()
        btnAccount4["text"] = cursor.fetchone()
        btnAccount5["text"] = cursor.fetchone()
        btnAccount6["text"] = cursor.fetchone()
        btnAccount7["text"] = cursor.fetchone()
        btnAccount8["text"] = cursor.fetchone()
        btnAccount9["text"] = cursor.fetchone()
        btnAccount10["text"] = cursor.fetchone()
        

    LoadAccounts()
    #================================RightFrame===========================================
    master.mainloop()


if __name__ == '__main__':
    main()

