from tkinter import *
from tkinter import messagebox
import sqlite3, time, random, os, webbrowser,smtplib

def WriteToUser(user_name):
    new =  user_name.get()
    current_user = open("User","w")
    current_user.write(new)
    current_user.close()

def WriteToUserUsingSecurity(requesting_user):
    current_user = open("User","w")
    current_user.write(requesting_user)
    current_user.close()
    

def main():    
    #==============Window/Frame creation=====================
    global submit_pressed
    submit_pressed = 0 
    root = Tk()
    root.title("Login page")
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()
    
    root.geometry("%dx%d+0+0" % (win_width, win_height))

    topFrame = Frame(root, width=1280, height=200, bg="slate blue", relief=GROOVE,borderwidth=6)
    topFrame.pack(side=TOP, fill=BOTH, expand=False)

    bottomLeft = Frame(root, width=600, height=824, bg="azure2", relief=GROOVE,borderwidth=6)
    bottomLeft.pack(side=LEFT, fill=BOTH, expand=False)

    bottomRight = Frame(root, width=680, height=824, bg="azure3", relief=GROOVE,borderwidth=6)
    bottomRight.pack(side=RIGHT, fill=BOTH, expand=True)
    #========================================================
    def ResetAfterSignOut(name_Input, password_Input):
        name_Input.set("")
        password_Input.set("")

    #=============================Top Frame stuff======================================
    lblTitle = Label(topFrame, font=('times',100,'bold'),text="Pass-Vault",fg="DeepSkyBlue2",bg="honeydew2",borderwidth=3,relief=FLAT)
    lblTitle.grid(row=0,columnspan=3,sticky=W,pady=15,padx=15)

    lblInfo = Label(topFrame, font=('courier new', 15,'bold'),text="Convient Password Storage Solutions",fg="SteelBlue2",bg="honeydew2",borderwidth=2,relief=FLAT)
    lblInfo.grid(row=1,columnspan=3,sticky=W,padx=15,pady=15)

    image = PhotoImage(file="giphy.gif")
    lblImage = Label(topFrame,image=image, width=700,height=150,borderwidth=3,relief=SUNKEN)
    lblImage.grid(row=0,column=5,padx=50,pady=15,sticky=N+S+E)
    lblImage.image = image
    #=====================================================================================


    #===========================Bottom Left Stuff=========================================
    def RememberFromLast(name_Input, password_Input):
        try:
            remember_user = open("RememberUser.txt","r")
            saved_user = remember_user.readline()
            saved_password = remember_user.readline()
            name_Input.set(saved_user.strip())
            password_Input.set(saved_password)
            Switch()
            remember_Me.set(1)
            messagebox.showinfo("Hello!", "Welcome back, "+saved_user)
            remember_user.close()
        except:
            pass
            
        
    name_Input = StringVar()
    password_Input = StringVar()

    lblLoginTitle = Label(bottomLeft, font=('courier new',15,'bold'),text="Log in to access your Vault.",fg="ivory2",bg="DeepSkyBlue2",borderwidth=3,relief=FLAT)
    lblLoginTitle.grid(row=0,columnspan=3,sticky=W,padx=10,pady=20)

    lblName = Label(bottomLeft, font=('courier new',20,'bold'),text="Username",fg="ivory2",bg="DeepSkyBlue2",borderwidth=3,relief=RAISED)
    lblName.grid(row=1,column=0,sticky=E,padx=10,pady=15)
    user_name = Entry(bottomLeft,font=('courier new',20),textvariable=name_Input,insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
    user_name.grid(row=1,column=1,sticky=W+E)

    lblPassword = Label(bottomLeft, font=('courier new',20,'bold'),text="Password",fg="ivory2",bg="DeepSkyBlue2",borderwidth=3,relief=RAISED)
    lblPassword.grid(row=2,column=0,sticky=E,padx=10,pady=15)
    user_password = Entry(bottomLeft,font=('courier new',20),textvariable=password_Input,insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
    user_password.grid(row=2,column=1,sticky=W+E)
    
    captcha1 = PhotoImage(file="Captcha1.gif")
    captcha2 = PhotoImage(file="Captcha2.gif")
    captcha3 = PhotoImage(file="Captcha3.gif")
    captcha4 = PhotoImage(file="Captcha4.gif")

    global captchaAnswers
    captchaAnswers = ["DJ290AQ", "QWERTY", "Jjko3+", "bdjOW_S"]

    captchaImages = [captcha1, captcha2, captcha3, captcha4]

    def DisplayCaptcha(captchaAnswers, captchaImages):
        if submit_pressed >= 3:
            captchaWindow = Toplevel()
            captchaWindow.grab_set()
            captchaWindow.title("Trouble logging in?")
            captchaWindow.resizable(0,0) 
            captchaFrame = Frame(captchaWindow, bg="slate blue", relief=RAISED, borderwidth=3)
            captchaFrame.grid()
            lblProveHuman = Label(captchaFrame, font=('times',15,'bold'),text="Type in the characters shown to prove you are not a robot",fg="ivory2",bg="light slate blue",borderwidth=3,relief=SUNKEN)
            lblProveHuman.grid(row=0,columnspan=6,sticky=W+E,padx=10,pady=20)
            lblCaptcha = Label(captchaFrame,image=random.choice(captchaImages),relief=RIDGE,borderwidth=5)
            lblCaptcha.grid(row=3, columnspan=2,sticky=W,padx=10,pady=10)
            answerCaptcha = Entry(captchaFrame,font=('courier new',20),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
            answerCaptcha.grid(row=3,column=3,sticky=W,padx=10,pady=10)

            def SubmitCaptcha(answerCaptcha):
                input_captcha = answerCaptcha.get()
                if input_captcha in captchaAnswers:
                    messagebox.showinfo("Verification Successful", "Checkpoint Passed")
                    captchaWindow.quit()
                    captchaWindow.destroy()
                else:
                    messagebox.showerror("Access Denied", "Remember, the Captcha is case-sensitive, and may include both numbers and 'special characters'")

            def StopQuit():
                messagebox.showwarning("Access Denied", "You must answer the Captcha before proceeding")

            captchaWindow.protocol('WM_DELETE_WINDOW', StopQuit) 
                    
            btnSubmitCaptcha = Button(captchaFrame,font=('courier new', 15, 'bold'),text="SUBMIT",fg="ivory2",bg="slate blue",relief=GROOVE,command=lambda:SubmitCaptcha(answerCaptcha),borderwidth=3,cursor="hand1")
            btnSubmitCaptcha.grid(row=4,column=3,sticky=E,padx=10,pady=10)
        else:
            pass
        root.after(9999999999999999, lambda:DisplayCaptcha(captchaAnswers, captchaImages))
        


    def ClearFields():
        name_Input.set("")
        password_Input.set("")

    def Switch():
        if root.counter ==1:
            user_password.config(show="\u2022")
            root.counter = root.counter + 1
        else:
            user_password.config(show="")
            root.counter = root.counter - 1

    btnReset = Button(bottomLeft,font=('courier new', 15, 'bold'),text="CLEAR FIELDS",fg="ivory2",bg="DeepSkyBlue2",relief=RIDGE,command=ClearFields,cursor="hand1")
    btnReset.grid(row=4,column=0,padx=10,pady=10,sticky=W)

    root.counter = 1
    btnHideShow = Button(bottomLeft,font=('courier new',15,'bold'),text="HIDE/SHOW PASSWORD",fg="ivory2",bg="DeepSkyBlue2",relief=RIDGE,command=Switch,cursor="hand1")
    btnHideShow.grid(row=4,column=1,padx=10,pady=10)
    
    #================================Authentication=====================================
    def Submit(event=None):
        global submit_pressed
        submit_pressed += 1
        DisplayCaptcha(captchaAnswers, captchaImages)
        conn = sqlite3.connect('Password-Gen.db')
        global username_input
        global password_input
        username_input = user_name.get()
        password_input = user_password.get()
        try:
            if username_input == "":
                messagebox.showerror("Error", "Enter a valid username to continue")
            else:
                cursor = conn.cursor()
                cursor.execute("SELECT user_name FROM users_table WHERE user_name = ?", (username_input,))
                username_exists = cursor.fetchone()
                if username_exists == None:
                    messagebox.showwarning("Error", "No account under the name: %s" %username_input)
                else:
                    if password_input == "":
                        messagebox.showerror("Error", "Enter a password to continue")
                    else:
                        cursor.execute("SELECT user_pass FROM users_table WHERE user_name = ? AND user_pass = ?", (username_input,password_input,))
                        password_exists = cursor.fetchone()
                        if password_exists == None:
                            messagebox.showwarning("Access denied", "Incorrect password")
                        else:
                            WriteToUser(user_name)
                            root.destroy()
                            from MainWindow import main
                            main()
        except:
                messagebox.showerror("Database Missing", "Account cannot exist if there is no DB inside the current directory!")
                            
        
    btnSubmit = Button(bottomLeft,font=('courier new', 15, 'bold'),text="SUBMIT",fg="ivory2",bg="DeepSkyBlue2",relief=RIDGE,command=lambda:Submit(event=None),cursor="hand1")
    btnSubmit.grid(row=4,column=2,sticky=E,padx=10,pady=10)

    root.bind("<Return>", Submit)

    def CreateNewAccount():
        root.withdraw()
        master = Toplevel()
        master.resizable(0,0)
        master.title("Pass-Vault")
        
        f1 = Frame(master, width=500, height=200, bg="slate blue", relief=RIDGE,borderwidth=7)
        f1.pack(side=TOP,fill=BOTH, expand=False)

        lblTitle = Label(f1, font=('times',30,'bold','underline'),text="\u2022     \u2022  Make a new account:  \u2022     \u2022",fg="ivory2",bg="dark slate blue",relief=FLAT)
        lblTitle.grid(row=0,columnspan=5,padx=10,pady=15,sticky=W+E)
        
        lblNameNew = Label(f1, font=('courier new',20,'bold'),text="Username",fg="ivory2",bg="light slate blue",borderwidth=2,relief=RAISED)
        lblNameNew.grid(row=1,column=0,sticky=W,padx=10,pady=15)
        
        lblPasswordNew = Label(f1, font=('courier new',20,'bold'),text="Password",fg="ivory2",bg="light slate blue",borderwidth=2,relief=RAISED)
        lblPasswordNew.grid(row=2,column=0,sticky=W,padx=10,pady=15)
        
        EntryNameNew = Entry(f1,font=('courier new',15),insertwidth=4,width=45,bg="light steel blue",borderwidth=3,relief=SUNKEN)
        EntryNameNew.grid(row=1,column=1,sticky=W)
        
        EntryPassNew = Entry(f1,font=('courier new',15),insertwidth=4,width=45,bg="light steel blue",borderwidth=3,relief=SUNKEN)
        EntryPassNew.grid(row=2,column=1,sticky=W)

        lblEmailNew = Label(f1, font=('courier new',20,'bold'),text="Email",fg="ivory2",bg="light slate blue",borderwidth=2,relief=RAISED)
        lblEmailNew.grid(row=3,column=0,sticky=W,padx=10,pady=15)

        EntryEmailNew = Entry(f1,font=('courier new',15),insertwidth=4,width=45,bg="light steel blue",borderwidth=3,relief=SUNKEN)
        EntryEmailNew.grid(row=3,column=1,sticky=W)

        lblRequiredOne = Label(f1, font=('times',15,'bold', 'italic'),text="* Required",fg="red",bg="slate blue")
        lblRequiredOne.grid(row=1,column=2,sticky=W,padx=10,pady=15)

        lblRequiredTwo = Label(f1, font=('times',15,'bold', 'italic'),text="* Required",fg="red",bg="slate blue")
        lblRequiredTwo.grid(row=2,column=2,sticky=W,padx=10,pady=15)

        lblTermsAndConditions = Label(f1,font=('courier new',20,'bold'),text="[Terms And Conditions]",fg="ivory2",bg="light slate blue",borderwidth=5,relief=SUNKEN)
        lblTermsAndConditions.grid(row=4,columnspan=5,sticky=W+E,padx=10,pady=15)

        lblTermsTitle = Label(f1, font=('courier new',12,'bold'),text="By signing up to Pass-Vault (Tm), you agree to the following:",fg="ivory2",bg="light slate blue",borderwidth=3,relief=FLAT)
        lblTermsTitle.grid(row=5,columnspan=2,sticky=W,padx=10,pady=15)

        lblTerms = Label(f1, font=('courier new',10,'bold'),text="[1] You use this service at your own risk - We cannot be held accountable for any loss, corruption or theft of personal data.\n[2] You will not share your login information with anyone.\n[3] You will not attempt to modify, redistribute or re-sell the software in any manner.",fg="ivory2",bg="light slate blue",borderwidth=3,relief=FLAT)
        lblTerms.grid(row=6,columnspan=5,sticky=W+E+S,padx=10,pady=15)

        global user_agree
        user_agree = IntVar()
        
        checkAgree = Checkbutton(f1, font=('courier new',15,'italic','bold'),text="I fully agree with the terms and conditions listed above",fg="LightBlue1",bg="slate blue",variable=user_agree,cursor="hand2")
        checkAgree.grid(row=7,columnspan=5,padx=10,pady=10)  


        def QuitAndDestroy(event=None):
            master.quit()
            master.destroy()
            root.deiconify()
        
        btnCancel = Button(f1, font=('courier new',15,'bold'),text="CANCEL",fg="ivory2",bg="dark slate blue",relief=RIDGE,command=lambda:QuitAndDestroy(event=None),cursor="X_cursor")
        btnCancel.grid(row=8,column=0,sticky=W,padx=15,pady=15)

        master.bind("<Escape>", QuitAndDestroy)

        def SaveAccount():
            prerequisite_filled = user_agree.get()
            if prerequisite_filled == 1:
                username = EntryNameNew.get()
                password = EntryPassNew.get()
                email_address = EntryEmailNew.get()
                try:
                    if username == "":
                        messagebox.showerror("Invalid","Please enter a username")
                    elif password == "":
                        messagebox.showerror("Invalid","Please enter a password")
                    else:
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("SELECT user_name FROM users_table WHERE user_name = ?", (username,))
                        existing_usernames = cursor.fetchone()
                        if existing_usernames == None:
                            if email_address == "":
                                conn.execute("INSERT INTO users_table(user_ID, user_name, user_pass, email_address_main) VALUES (NULL, ?, ?, 'Temp')", (username,password))
                            else:
                                conn.execute("INSERT INTO users_table(user_ID, user_name, user_pass, email_address_main) VALUES (NULL, ?, ?, ?)", (username,password,email_address))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Welcome to Pass-Vault", "Account Successfully Created")
                            QuitAndDestroy()                               
                        else:
                            messagebox.showwarning("Oops","Account under this username already exists")
                except:
                    messagebox.showerror("Database Missing", "To create an account, first set up the database using the button on the right-hand side of the previous page.")
            else:
                messagebox.showwarning("Invalid", "You must accept the terms and conditions before creating an account")
                                                                                                                       
        btnCreateAccount = Button(f1, font=('courier new',15,'bold'),text="CREATE ACCOUNT",fg="ivory2",bg="dark slate blue",relief=RIDGE,command=SaveAccount,cursor="hand1")
        btnCreateAccount.grid(row=8,column=2,sticky=W,padx=15,pady=15)

        master.mainloop()                             

    lblNewAccount = Label(bottomLeft, font=('courier new',14,'bold','italic'),text="First time user? Create an account:",fg="DeepSkyBlue2",bg="azure2")
    lblNewAccount.grid(row=5,columnspan=2,padx=5,pady=5,sticky=E)

    btnNewAccount = Button(bottomLeft, font=('courier new',15,'bold'),text="I'M NEW!",fg="ivory2",bg="DeepSkyBlue2",relief=RIDGE,command=CreateNewAccount,cursor="hand1")
    btnNewAccount.grid(row=5,column=2,pady=50,padx=10, sticky=W)
    #=====================================End of Authentication==============================================================
    def SaveForNextTime(user_name, user_password):
        user_wants_rememberance = remember_Me.get()
        if user_wants_rememberance == 1:
                user_name_save = user_name.get()
                if user_name_save == "":
                    messagebox.showinfo("Ooops!", "Please re-select this option once you have inputted your full credentials")
                    remember_Me.set(0)
                else:
                    user_pass_save = user_password.get()
                    if user_pass_save == "":
                        messagebox.showinfo("Ooops!", "Please re-select this option once you have inputted your full credentials")
                        remember_Me.set(0)
                    else:
                        remember_user = open("RememberUser.txt","w")
                        remember_user.write(user_name_save + "\n")
                        remember_user.write(user_pass_save)
                        remember_user.close()
        else:
            os.remove("RememberUser.txt")
            print("{RememberUser removed from working directory}")
                

    global remember_Me
    remember_Me = IntVar()
    
    checkSaveDetails = Checkbutton(bottomLeft, font=('courier new',15,'bold'),text="Remember my details",fg="DeepSkyBlue2",bg="azure2",variable=remember_Me, command=lambda:SaveForNextTime(user_name, user_password),cursor="hand2")
    checkSaveDetails.grid(row=3,columnspan=2,padx=10,pady=10,sticky=W)  
    
    btnQuit = Button(bottomLeft, font=('courier new',15,'bold'),text="QUIT",fg="ivory2",bg="DeepSkyBlue2",relief=RIDGE,command=root.destroy,cursor="X_cursor")
    btnQuit.grid(row=7,column=0,sticky=W,padx=10)

    def AlternativeOptions():
        root.withdraw()
        master = Toplevel()
        master.title("Alternative sign-in options")
        master.resizable(0,0)
        UseQuestionFrame = Frame(master, height=300,width=600, relief=GROOVE,borderwidth=3,bg="slate blue")
        UseQuestionFrame.pack(fill=BOTH,expand=True,side=LEFT)
        resetPassFrame = Frame(master,height=300,width=600,relief=GROOVE,borderwidth=3,bg="medium slate blue")
        resetPassFrame.pack(fill=BOTH,expand=True,side=RIGHT)

        lblUseSecurityQuestion = Label(UseQuestionFrame, font=('times',30,'bold','underline'),text="Answer Your Security Question",fg="ivory2",bg="dark slate blue",borderwidth=1,relief=RIDGE)
        lblUseSecurityQuestion.grid(row=0,columnspan=5,sticky=W+E,padx=10,pady=10)
        
        lblUsername = Label(UseQuestionFrame, font=('courier new',20,'bold'),text="Username",fg="ivory2",bg="dark slate blue",borderwidth=1,relief=SUNKEN)
        lblUsername.grid(row=1,column=0,sticky=W+E,padx=10,pady=10)
        entryUserName = Entry(UseQuestionFrame,font=('courier new',15),insertwidth=4,width=30,bg="light steel blue",borderwidth=3,relief=SUNKEN)
        entryUserName.grid(row=1,column=1,sticky=W,padx=10,pady=10)

        lblDisplayQuestion = Label(UseQuestionFrame, font=('times',15,'italic'),text="{Your Security Question Will Be Displayed Here}",fg="ivory2",bg="dark slate blue",relief=RAISED)
        lblDisplayQuestion.grid(row=3,columnspan=3,sticky=W+E,padx=10)

        def RetrieveSecurityQuestion():
            global requesting_user
            requesting_user = entryUserName.get()
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT user_name FROM users_table WHERE user_name = ?", (requesting_user,))
                user_exists = cursor.fetchone()
                if requesting_user == "":
                    messagebox.showerror("Ooops", "Please enter an account name")
                elif user_exists:
                    cursor.execute("SELECT chosen_security_question FROM questions_table WHERE user_name = ?", (requesting_user,))
                    question_set = cursor.fetchone()
                    if question_set:
                        lblDisplayQuestion["text"] = question_set[0]
                    else:
                        messagebox.showinfo("Ooops","Sorry, it seems you have not set a security question")
                    conn.close()
                else:
                    messagebox.showerror("Ooops","No account found under the name %s" %requesting_user)
            except:
                messagebox.showerror("Database Missing", "No account can exist if the DB doesn't exist")
        
            

        btnUseSecurityQuestion = Button(UseQuestionFrame, font=('courier new',15,'bold'),text="DISPLAY SECURITY QUESTION",fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=RetrieveSecurityQuestion,cursor="hand1")
        btnUseSecurityQuestion.grid(row=2,columnspan=2,sticky=E,padx=10,pady=15)

        entryAnswer = Entry(UseQuestionFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
        entryAnswer.grid(row=4,columnspan=3,sticky=W+E,padx=10,pady=15)

        def SubmitAnswer():
            if lblDisplayQuestion["text"] == "Your Security Question Will Be Displayed Here":
                messagebox.showwarning("Ooops", "Please fill out previous fields before submitting your answer")
            else:
                input_answer = entryAnswer.get()
                if input_answer == "":
                    messagebox.showwarning("Ooops", "Security question must be answered in order to log in")
                else:
                    conn = sqlite3.connect('Password-Gen.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT security_answer FROM questions_table WHERE user_name = ?", (requesting_user,))
                    retrieved_answer = cursor.fetchone()
                    if retrieved_answer[0] == input_answer:
                        cursor.execute("SELECT user_pass FROM users_table WHERE user_name = ?", (requesting_user,))
                        user_pass = cursor.fetchone()
                        messagebox.showinfo("Data Match", "Success! Welcome to your Vault, " +requesting_user+ ".\nYour password for this account is '" +user_pass[0] +"', consider making a note of it.")
                        conn.close()
                        WriteToUserUsingSecurity(requesting_user)
                        master.destroy()
                        root.destroy()
                        from MainWindowTest11 import main
                        main()
                    else:
                        messagebox.showwarning("Incorrect", "The answer you have give does not match our records.\nPlease try again..")

        btnSubmitAnswer= Button(UseQuestionFrame, font=('courier new',15,'bold'),text="SUBMIT ANSWER",fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=SubmitAnswer,cursor="hand1")
        btnSubmitAnswer.grid(row=5,column=1,sticky=E,padx=10,pady=15)

        lblResetPassword = Label(resetPassFrame, font=('times',30,'bold','underline'),text="Reset Your Password",fg="ivory2",bg="dark slate blue",borderwidth=1,relief=RIDGE)
        lblResetPassword.grid(row=0,columnspan=5,sticky=W+E,padx=10,pady=10)
        
        lblUsernameForReset = Label(resetPassFrame, font=('courier new',20,'bold'),text="Username",fg="ivory2",bg="dark slate blue",borderwidth=1,relief=SUNKEN)
        lblUsernameForReset.grid(row=1,column=0,sticky=W+E,padx=10,pady=10)
        
        entryNameForReset = Entry(resetPassFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
        entryNameForReset.grid(row=1,column=1,sticky=W,padx=10,pady=15)

        def ReturnToLogin(event=None):
            master.destroy()
            root.deiconify()

        btnReturnToLogin = Button(UseQuestionFrame, font=('courier new',15,'bold'),text="RETURN TO LOGIN", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=lambda:ReturnToLogin(event=None),cursor="X_cursor")
        btnReturnToLogin.grid(row=5,column=0,sticky=W,padx=10,pady=15)

        master.bind("<Escape>", ReturnToLogin)


        def FindMyEmail(entryNameForReset):

            def OpenResetWindow():                
                global resetWindow
                resetWindow = Toplevel()
                resetWindow.title("Reset Your Password")
                resetWindow.grab_set()
                resetFrame = Frame(resetWindow, relief=GROOVE, borderwidth=3, bg="medium slate blue")
                resetFrame.pack()
                lblPassReset = Label(resetFrame, font=('courier new',20,'bold'),text="New Password",fg="ivory2",bg="dark slate blue",borderwidth=1,relief=SUNKEN)
                lblPassReset.grid(row=1,column=0,sticky=E,padx=10,pady=10)
                entryPassReset = Entry(resetFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
                entryPassReset.grid(row=1,column=1,sticky=W,padx=10,pady=15)
                lblPassResetConfirm = Label(resetFrame, font=('courier new',20,'bold'),text="Confirm Password",fg="ivory2",bg="dark slate blue",borderwidth=1,relief=SUNKEN)
                lblPassResetConfirm.grid(row=2,column=0,sticky=E,padx=10,pady=10)
                entryPassResetConfirm = Entry(resetFrame,font=('courier new',15),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN)
                entryPassResetConfirm.grid(row=2,column=1,sticky=W,padx=10,pady=15)

                def PasswordReset(entryPassReset, entryPassResetConfirm, name):
                    pass_reset = entryPassReset.get()
                    pass_reset_confirmation = entryPassResetConfirm.get()
                    if pass_reset == "" or pass_reset_confirmation == "":
                        messagebox.showwarning("Ooops!", "Required fields have been left bank")
                    elif pass_reset != pass_reset_confirmation:
                        messagebox.showwarning("Ooops!", "Passwords do not match")
                    else:
                        conn = sqlite3.connect('Password-Gen.db')
                        cursor = conn.cursor()
                        cursor.execute("UPDATE users_table SET user_pass = ? WHERE user_name = ?", (pass_reset, name))
                        conn.commit()
                        messagebox.showinfo("Success", "Password has been reset")
                        conn.close()
                        Cancel()
                
                                
                btnFinishReset= Button(resetFrame, font=('courier new',15,'bold'),text="FINISH AND SAVE",fg="ivory2",
                                       bg="dark slate blue",relief=GROOVE,borderwidth=3,command=lambda:PasswordReset(entryPassReset, entryPassResetConfirm,name),cursor="hand1")
                btnFinishReset.grid(row=3,column=1,sticky=E,padx=10,pady=15)

                def Cancel():
                    resetWindow.destroy()
                    master.destroy()
                    root.deiconify()

                btnCancel = Button(resetFrame, font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=Cancel,cursor="X_cursor")
                btnCancel.grid(row=3,column=0,sticky=W,padx=10,pady=15)
                
            conn = sqlite3.connect('Password-Gen.db')
            cursor = conn.cursor()    
            name = entryNameForReset.get()
#==========================#=======================================
            global verification_code
            
            def EmailVerificationMain(name, user_has_assigned_email):
                numbers = []
                for i in range(0,10):
                    numbers.append(random.randint(0,9))
                verification_code =''.join(map(str, numbers))
                TO = user_has_assigned_email[0]                    
                CONTENT = "Mr. / Ms. "+name+",\n\nEnter this 10-digit verification code into the Pass-Vault client to reset your password.\n\n"+verification_code
                BODY = '\r\n' .join([
                    'To: %s' % TO,
                    'From: passvault.inc@gmail.com',
                    'Subject: Pass-Vault Password Reset'
                    '',
                    CONTENT
                    ])                    
                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('passvault.inc@gmail.com','mosenco9')
                try:
                    mail.sendmail('passvault.inc@gmail.com',[TO],BODY)
                    messagebox.showinfo("Verification", "An Email has been sent to '"+TO+"' with a 10-Digit verification code to reset your password")
                    OpenVerificationWindow(name, verification_code)
                except:
                    messagebox.showinfo("Something Went Wrong", "Sorry, it seems we couldn't form a connection, try again later - if the problem persists, contact us via the email provided on the main page")
                mail.close()


            def EmailVerificationSecondary(name, email_in_system):
                numbers = []
                for i in range(0,10):
                    numbers.append(random.randint(0,9))
                verification_code =''.join(map(str, numbers))
                TO = email_in_system[0]
                CONTENT = "Mr. / Ms. "+name+",\n\nEnter this 10-digit verification code into the Pass-Vault client to reset your password.\n\n"+verification_code
                BODY = '\r\n' .join([
                    'To: %s' % TO,
                    'From: passvault.inc@gmail.com',
                    'Subject: Pass-Vault Password Reset'
                    '',
                    CONTENT
                    ])                    
                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('passvault.inc@gmail.com','mosenco9')
                try:
                    mail.sendmail('passvault.inc@gmail.com',[TO],BODY)
                    messagebox.showinfo("Verification", "An Email has been sent to '"+TO+"' with a 10-Digit verification code to reset your password")
                    OpenVerificationWindow(name, verification_code)
                except:
                    messagebox.showinfo("Something Went Wrong", "Sorry, it seems we couldn't form a connection, try again later - if the problem persists, contact us via the email provided on the main page")
                mail.close()

            def EmailVerificationTertiary(name, email_in_system):
                numbers = []
                for i in range(0,10):
                    numbers.append(random.randint(0,9))
                verification_code =''.join(map(str, numbers))
                TO = email_in_system[1]
                CONTENT = "Mr. / Ms. "+name+",\n\nEnter this 10-digit verification code into the Pass-Vault client to reset your password.\n\n"+verification_code
                BODY = '\r\n' .join([
                    'To: %s' % TO,
                    'From: passvault.inc@gmail.com',
                    'Subject: Pass-Vault Password Reset'
                    '',
                    CONTENT
                    ])                    
                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('passvault.inc@gmail.com','mosenco9')
                try:
                    mail.sendmail('passvault.inc@gmail.com',[TO],BODY)
                    messagebox.showinfo("Verification", "An Email has been sent to '"+TO+"' with a 10-Digit verification code to reset your password")
                    OpenVerificationWindow(name, verification_code)
                except:
                    messagebox.showinfo("Something Went Wrong", "Sorry, it seems we couldn't form a connection, try again later - if the problem persists, contact us via the email provided on the main page")
                mail.close()
                return(verification_code)

            def OpenVerificationWindow(name, verification_code):
                verificationWindow = Toplevel()
                verificationWindow.grab_set()
                verificationWindow.title("Enter Your Code Here")
                verificationWindow.configure(background="slate blue")
                
                VerCode = StringVar()

                def SubmitCode(verfication_code, entryCode, VerCode):
                    code_submitted = entryCode.get()
                    if code_submitted == verification_code:
                        messagebox.showinfo("Code Match", "Success! you may now reset your password")
                        verificationWindow.destroy()
                        master.destroy()
                        OpenResetWindow()
                    elif code_submitted == "":
                        messagebox.showwarning("Ooops!", "Please enter your code")
                    else:
                        messagebox.showwarning("Invalid Entry", "The code you have entered is incorrect")
                        VerCode.set("")


                entryCode = Entry(verificationWindow ,font=('system',30),insertwidth=4,bg="light steel blue",borderwidth=3,relief=SUNKEN, justify='center',textvariable=VerCode)
                entryCode.grid(row=0,columnspan=3,sticky=W+E,padx=10,pady=15)
                                        
                btnSubmitCode = Button(verificationWindow, font=('courier new',15,'bold'),text="SUBMIT", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=lambda:SubmitCode(verification_code, entryCode, VerCode),cursor="hand1")
                btnSubmitCode.grid(row=1,column=2,sticky=E,padx=10,pady=15)

                def CancelTwo():
                    verificationWindow.destroy()
                    master.deiconify()

                btnCancel = Button(verificationWindow, font=('courier new',15,'bold'),text="CANCEL", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=CancelTwo,cursor="X_cursor")
                btnCancel.grid(row=1,column=0,sticky=W,padx=10,pady=15)
                
#====================#============================
            if name == "":
                messagebox.showwarning("Ooops!", "Please enter your username to continue")
            else:
                cursor.execute("SELECT user_name FROM users_table WHERE user_name = ?", (name,))
                name_found = cursor.fetchone()
                if name_found == None:
                    messagebox.showwarning("Ooops!", "No account found under this name")
                else:
                    cursor.execute("SELECT email_address_main FROM users_table WHERE user_name = ?", (name,))
                    user_has_assigned_email = cursor.fetchone()
                    if user_has_assigned_email[0] == "Temp":
                        cursor.execute("SELECT email_address FROM passwords_table WHERE user_name = ?", (name,))
                        email_in_system = [row[0] for row in cursor.fetchmany()]
                        if email_in_system == None:
                            messagebox.showwarning("Query Unsuccessful", "No email addresses found with respect to the username provided")
                        else:
                            access_two = messagebox.askyesno("Email Located", "Email Address: '"+str(email_in_system[0])+"' is stored in the system with respect to username '"+name+"'.\nDo you have access to this email?")
                            if access_two == True:
                                EmailVerificationSecondary(name, email_in_system)
                            else:
                                try:
                                    access_three = messagebox.askyesno("Email Located", "Another Email Address: '"+str(email_in_system[1])+"' is stored in the system with respect to username '"+name+"'.\nDo you have access to this email?")
                                    if access_three == True:
                                        EmailVerificationTertiary(name, email_in_system)

                                except:
                                    messagebox.showinfo("Sorry", "Unfortunately, we were unable to retrieve any more stored email addresses")
                    else:
                        access_one = messagebox.askyesno("Items Located", "Email Address: '"+str(user_has_assigned_email[0])+"' is stored in the system with respect to username "+name+".\nDo you have access to this email?")
                        if access_one == True:
                            EmailVerificationMain(name, user_has_assigned_email)

                conn.close()

        btnFindMyEmail = Button(resetPassFrame, font=('courier new',15,'bold'),text="RESET PASSWORD", fg="ivory2",bg="dark slate blue",relief=GROOVE,borderwidth=3,command=lambda:FindMyEmail(entryNameForReset),cursor="hand1")
        btnFindMyEmail.grid(row=5,column=2,sticky=E,padx=10,pady=15)

        lblInfo = Label(resetPassFrame, font=('courier new',12,'bold'),text="You can only reset your password if there's an email associated\n with your account",fg="ivory2",bg="dark slate blue")
        lblInfo.grid(row=6,columnspan=3,padx=5,pady=5,sticky=W+E)
        
    lblCantLogIn = Label(bottomLeft, font=('courier new',15,'italic','bold'),text="Can't sign in?",fg="DeepSkyBlue2",bg="azure2")
    lblCantLogIn.grid(row=7,column=1,padx=5,pady=5,sticky=E)
    
    btnForgottenPassword = Button(bottomLeft, font=('courier new',15,'bold'),text="HELP",fg="ivory2",bg="DeepSkyBlue2",relief=RIDGE,command=AlternativeOptions,cursor="hand1")
    btnForgottenPassword.grid(row=7,column=2,sticky=W,padx=10)
    #======================================End of Bottom Left Stuff==========================================================

    #=====================================Bottom Right Stuff=================================================================
    def CreateDatabase():
        def CreateAccountsTable():
            conn = sqlite3.connect('Password-Gen.db')
            conn.execute('''CREATE TABLE users_table
                        (user_ID                            INTEGER PRIMARY KEY,
                        user_name                        TEXT,
                        user_pass                         TEXT,
                        email_address_main          TEXT);''')
            conn.close()

    

        def CreateSecurityQuestionsTable():
            conn = sqlite3.connect('Password-Gen.db')
            conn.execute('''CREATE TABLE questions_table
                        (user_name                        TEXT,
                        chosen_security_question    TEXT,
                        security_answer                  TEXT);''')
            conn.close()

        def CreateSubscriptionsTable():
            conn = sqlite3.connect('Password-Gen.db')
            conn.execute('''CREATE TABLE subscriptions_table
                         (user_name                 TEXT,
                         subscription                TEXT,
                         payment_frequency      TEXT,
                         payment_amount         REAL,
                         activity                        TEXT);''')
            conn.close()

        def CreatePasswordsTable():
            conn = sqlite3.connect('Password-Gen.db')
            conn.execute('''CREATE TABLE passwords_table
                        (user_name             TEXT,
                        application             TEXT,
                        email_address         TEXT,
                        password               TEXT);''')
            conn.close()
            
        try:
            CreateAccountsTable()
            CreateSecurityQuestionsTable()
            CreatePasswordsTable()
            CreateSubscriptionsTable()
            messagebox.showinfo("Application Runtime", "Password-Gen.db added to current directory")
        except:
            pass

    def update_UTC():
        current = time.strftime("%H:%M:%S --- %d/%m/%Y")
        UTC.configure(text="[Local Time] \u2022 \u2022 \u2022 \u2022 "+ current)
        root.after(1000,update_UTC)

    UTC = Label(bottomRight,font=('times', 20,'bold'),text="", fg="ivory2",bg="SlateBlue3",relief=GROOVE,borderwidth=4)
    UTC.grid(row=0,columnspan=2,padx=15,pady=15,sticky=W+E)
    update_UTC()

    lblStatement = Label(bottomRight, font=('courier new', 10,'bold'),text="All of your apps, all in one place.", fg="ivory2",bg="SlateBlue3",relief=FLAT)
    lblStatement.grid(row=1,columnspan=3,padx=15,pady=15,sticky=W)

    lblFeedback = Label(bottomRight, font=('times',35,'bold','underline'),text="Developer Feedback", fg="ivory2",bg="SlateBlue3",relief=FLAT)
    lblFeedback.grid(row=2,columnspan=5,padx=15,pady=15,sticky=W+E)

    lblSurveyTitle = Label(bottomRight, font=('courier new',15,'bold','underline'),text="Have some spare time? Fill out a short customer feedback survey:", fg="ivory2",bg="SlateBlue3",relief=FLAT)
    lblSurveyTitle.grid(row=3,columnspan=5,padx=15,pady=15,sticky=W)

    def OpenForm():
        webbrowser.open_new("https://goo.gl/forms/dXoTV0vyWJqLr54I3")

    btnSurvey = Button(bottomRight, font=('system',15,'bold'),text="https://goo.gl/forms/dXoTV0vyWJqLr54I3", fg="cyan",bg="SlateBlue3",relief=RAISED, borderwidth=5, command=OpenForm,cursor="left_side")
    btnSurvey.grid(row=4,columnspan=5,padx=15,pady=15)

    lblInfo = Label(bottomRight, font=('courier new',15,'bold','underline'),text="Or, alternatively, send us an email:",fg="ivory2",bg="SlateBlue3",relief=FLAT)
    lblInfo.grid(row=5,columnspan=2,padx=15,pady=15,sticky=W)

    lblEmailAddress = Label(bottomRight, font=('courier new',20),text="passvault.inc@gmail.com",fg="ivory2",bg="SlateBlue3",relief=SUNKEN,borderwidth=3)
    lblEmailAddress.grid(row=6,column=0,padx=15,pady=15,sticky=W)

    CreateDatabase()
    RememberFromLast(name_Input, password_Input)
    root.focus_set()
    user_name.focus_set()
    user_password.focus_set()
    root.focus_force()
    #===================================End of Bottom Right=============================
    root.mainloop()

    

if __name__ == '__main__':
    main()
