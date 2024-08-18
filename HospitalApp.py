from gc import disable
import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
    root = Tk()
    app = Windows1(root)
    root.mainloop()

class Windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0') # x-axis, y-axis, z-axis dimension of application
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="Pharmacy Management System", font=("Arial", 40, "bold"), bd=10, relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(self.frame,width=1000,height = 300,bd=10,relief = "groove")
        self.Loginframe1.grid(row=1,column=0)
        
        self.Loginframe2 = Frame(self.frame,width=1000,height = 100,bd=10,relief = "groove")
        self.Loginframe2.grid(row=2,column=0,pady=15)
        
        self.Loginframe3 = Frame(self.frame,width=1000,height = 200,bd=10,relief = "groove")
        self.Loginframe3.grid(row=6,column=0,pady=5)
      
        self.button_reg = Button(self.Loginframe3,text="Patient Registration Window",font = ("arial",15,"bold"),state = DISABLED,command= self.Registration_window)
        self.button_reg.grid(row= 0,column = 0, padx = 10,pady = 10)
        
        self.button_Hosp = Button(self.Loginframe3,text="Hospital Window",font = ("arial",15,"bold"),state = DISABLED,command= self.Hospital_window)
        self.button_Hosp.grid(row= 0,column = 1, padx = 10,pady = 10)
        
        self.button_Dr_Appt = Button(self.Loginframe3,text="Dr Appointement Window",font = ("arial",15,"bold"),state = DISABLED,command= self.Dr_Apoint_window)
        self.button_Dr_Appt.grid(row= 1,column = 0, padx = 10,pady = 10)
        
        self.button_med_stock = Button(self.Loginframe3,text="Medicine Stock Window",font = ("arial",15,"bold"),state = DISABLED,command= self.Medicine_stock)
        self.button_med_stock.grid(row= 1,column = 1, padx = 10,pady = 10)

        # login form
        
        self.LabelUsername = Label(self.Loginframe1, text = "Username", font = ("arial",20,"bold"), bd=3)
        self.LabelUsername.grid(row = 0, column = 0)
        
        self.textUsername = Entry(self.Loginframe1,font =("arial",20,"bold"), bd=3, textvariable= self.Username)
        self.textUsername.grid(row = 0, column =1, padx = 40, pady =15)
        
        self.LabelPassword = Label(self.Loginframe1, text = "Password", font = ("arial",20,"bold"), bd=3)
        self.LabelPassword.grid(row = 1, column = 0)
        self.textPassword = Entry(self.Loginframe1,font =("arial",20,"bold"), show = '*',bd=3, textvariable= self.Password)
        self.textPassword.grid(row = 1, column =1, padx = 40, pady =15)
        
        self.button_login = Button(self.Loginframe2, text = "Login", width = 20, font = ("arial",18,"bold"),command=self.login_system)
        self.button_login.grid(row=0, column=0, padx=10,pady=10)
        
        self.button_reset = Button(self.Loginframe2, text = "Reset", width = 20, font = ("arial",18,"bold"),command=self.reset_btn)
        self.button_reset.grid(row=0, column=3, padx=10,pady=10)
        
        self.button_exit = Button(self.Loginframe2, text = "Exit", width = 20, font = ("arial",18,"bold"), command=self.exit_btn)
        self.button_exit.grid(row=0, column=6, padx=10,pady=10)
        

    def login_system(self):
        user = self.Username.get()
        pwd = self.Password.get()

        if(user == str("admin") and (pwd == str("admin"))): #str("admin") is the text in the textbox
         self.button_Hosp.config(state=NORMAL)
         self.button_reg.config(state=NORMAL)
         self.button_Dr_Appt.config(state=NORMAL)
         self.button_med_stock.config(state=NORMAL)
         
        else:
          tkinter.messagebox.askyesno("Pharmacy Management System", "Invalid username or password")
          self.button_Hosp.config(state=DISABLED)
          self.button_reg.config(state=DISABLED)
          self.button_Dr_Appt.config(state=DISABLED)
          self.button_med_stock.config(state=DISABLED)

          self.Username.set("")
          self.Password.set("")
          self.textUsername.focus()

    def reset_btn(self):
        self.button_Hosp.config(state=DISABLED)
        self.button_reg.config(state=DISABLED)
        self.button_Dr_Appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()
        
    def exit_btn(self):
        self.exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure you want to exit?");
        if self.exit_btn > 0:
           self.master.destroy() # close application
           return

    def Registration_window(self):
      self.newWindow = Toplevel(self.master)
      self.app = Registration(self.newWindow)

    def Hospital_window(self):
      self.newWindow = Toplevel(self.master)
      self.app = hospital(self.newWindow)

    def Dr_Apoint_window(self):
      self.newWindow = Toplevel(self.master)
      self.app = doctormg(self.newWindow)
      
    def Medicine_stock(self):
      self.newWindow = Toplevel(self.master)
      self.app = Windows5(self.newWindow)


class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry('1350x750+0+0')
        self.root.configure(background = "black")
        
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref =   StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address  = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        
        var1 =StringVar()
        var2 =StringVar()
        var3 =StringVar()
        var4 =StringVar()
        var5 =IntVar()
        
        Membership = StringVar()
        Membership.set("0")
        
        
        def exitbtnf():
            exitbtt = tkinter.messagebox.askyesno("Member Registration Form", "Are you sure you want to exit?")
            if exitbtt > 0:
                root.destroy()
            else:
               
               self.newWindow = Toplevel(self.Master)
               self.app = Windows1(self.newWindow)
               return
        
        def resetbtt():
               
               Firstname.set("")
               Lastname.set("")
               Ref.set("")
               Mobile_no.set("")
               Pincode.set("")
               Address.set("")
               Firstname.set("")
               var1.set("")
               var2.set("")
               var3.set("")
               var4.set("")
               var5.set("")
               Membership.set("")
               member_gendercmb.current(0)
               member_IDproofcmb.current(0)
               member_memtypecmb.current(0)
               member_paymentcmb.current(0)
               #member_membershiptxt(state =DISABLED)  

        def resetbtnf():
            resetbtt2 = tkinter.messagebox.askokcancel("Member Registration Form", "Are you sure you want to reset everything?")
            if resetbtt2 > 0:
               resetbtt()
            elif resetbtt2<=0:
                resetbtt()
                detail_labeltxt.delete("1.0",END)
                return
                

        def Reference_number():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)
            
        def membership_fees():
            if(var5.get()==1): #when checkbox is clicked
                member_membershiptxt.configure(state=NORMAL)
                item = float(25)
                Membership.set("$"+str(item))
            elif(var5.get()==0):
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")
        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t"+Date_of_Registration.get()+"    \t"+Ref.get()+"     \t"+Firstname.get()+"   \t"+
                                   Lastname.get()+"    \t"+Mobile_no.get()+"    \t"+Address.get()+"     \t"+Pincode.get()+"    \t"+member_gendercmb.get()+ "   \t"+Membership.get()+"\n")
         
        title = Label(self.root,text = "Member Registration Form", font = ("monotype corsiva",30,"bold"),bd=5,relief = GROOVE,
        bg = "#E6005C",fg = "#000000")
        title.pack(side=TOP,fill = X)
                      
        Manage_Frame = Frame(self.root, bd=4,relief = RIDGE, bg = "#001a66")
        Manage_Frame.place(x=20,y=100,width=450,height=630)
        Cus_title = Label(Manage_Frame,text="Customer Details",font=("arial",20,"bold"),bg ="#001a66",fg = "white")
        Cus_title.grid(row=0,columnspan=2,pady=5)
        
        member_data1b1= Label(Manage_Frame,text="Date",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_data1b1.grid(row=1,column=0,pady=5,padx=10,sticky="w")    

        member_datetext = Entry(Manage_Frame,font = ("arial",15,"bold"),textvariable=Date_of_Registration)
        member_datetext.grid(row = 1,column=1,pady=5,padx=10,sticky="w")

        member_ref1b1 = Label(Manage_Frame,text="Reference ID",font=("arial",15,"bold"),bg = "#001a66",fg = "white")
        member_ref1b1.grid(row = 2,column=0,padx =10,pady=5,sticky="w")
        
        member_reftxt = Entry(Manage_Frame,font=("arial",15,"bold"),state = DISABLED,text=Ref)
        member_reftxt.grid(row=2,column=1,padx=10,pady=5,sticky="w")
        
        member_fname1b1= Label(Manage_Frame,text="First Name",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_fname1b1.grid(row=3,column=0,pady=5,padx=10,sticky="w")    

        member_fnametext = Entry(Manage_Frame,font = ("arial",15,"bold"),textvariable=Firstname)
        member_fnametext.grid(row = 3,column=1,pady=5,padx=10,sticky="w")

        member_lname1b1= Label(Manage_Frame,text="Last Name",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_lname1b1.grid(row=4,column=0,pady=5,padx=10,sticky="w")    

        member_lnametext = Entry(Manage_Frame,font = ("arial",15,"bold"),textvariable=Lastname)
        member_lnametext.grid(row = 4,column=1,pady=5,padx=10,sticky="w")

        member_mobile1b1= Label(Manage_Frame,text="Mobile Number",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_mobile1b1.grid(row=5,column=0,pady=5,padx=10,sticky="w")    

        member_mobiletext = Entry(Manage_Frame,font = ("arial",15,"bold"),textvariable=Mobile_no)
        member_mobiletext.grid(row = 5,column=1,pady=5,padx=10,sticky="w")
        
        member_address1b1= Label(Manage_Frame,text="Address",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_address1b1.grid(row=6,column=0,pady=5,padx=10,sticky="w")    

        member_addresstext = Entry(Manage_Frame,font = ("arial",15,"bold"),textvariable=Address)
        member_addresstext.grid(row = 6,column=1,pady=5,padx=10,sticky="w")
        
        member_pincode1b1= Label(Manage_Frame,text="Pin Code",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_pincode1b1.grid(row=7,column=0,pady=5,padx=10,sticky="w")    

        member_pincodetext = Entry(Manage_Frame,font = ("arial",15,"bold"),textvariable=Pincode)
        member_pincodetext.grid(row = 7,column=1,pady=5,padx=10,sticky="w")
        
        member_gender1b1= Label(Manage_Frame,text="Gender",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_gender1b1.grid(row=8,column=0,pady=5,padx=10,sticky="w")    

        member_gendercmb = ttk.Combobox(Manage_Frame,text=var4,state="readonly",font=("arial",15,"bold"),width=19)

        member_gendercmb['values'] = ("","Male","Female")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8,column=1,padx=10,pady=5,sticky="w")
        
        member_IDproof1b1= Label(Manage_Frame,text="ID Proof",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_IDproof1b1.grid(row=9,column=0,pady=5,padx=10,sticky="w")    

        member_IDproofcmb = ttk.Combobox(Manage_Frame,text=var3,state="readonly",font=("arial",15,"bold"),width=19)

        member_IDproofcmb['values'] = ("","Driver License","Passport","Student ID","Insurance ID")
        member_IDproofcmb.current(0)
        member_IDproofcmb.grid(row=9,column=1,padx=10,pady=5,sticky="w")
        
        member_memtype1b1= Label(Manage_Frame,text="Member Type",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_memtype1b1.grid(row=10,column=0,pady=5,padx=10,sticky="w")    

        member_memtypecmb = ttk.Combobox(Manage_Frame,text=var2,state="readonly",font=("arial",15,"bold"),width=19)

        member_memtypecmb['values'] = ("","Insurance","Pay Immediately","Pay when leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10,column=1,padx=10,pady=5,sticky="w")
        
        member_payment1b1= Label(Manage_Frame,text="Payment Method",font = ("arial",15,"bold"),bg="#001a66",fg = "white")
        member_payment1b1.grid(row=11,column=0,pady=5,padx=10,sticky="w")    

        member_paymentcmb = ttk.Combobox(Manage_Frame,text=var1,state="readonly",font=("arial",15,"bold"),width=19)

        member_paymentcmb['values'] = ("","Cash","Debit Card","Credit Card","GooglePay")
        member_paymentcmb.current(0)
        member_paymentcmb.grid(row=11,column=1,padx=10,pady=5,sticky="w")

        member_membership = Checkbutton(Manage_Frame,text="Membership Fees",variable=var5,onvalue=1,offvalue=0,font=("arial",15,"bold"),bg="#001a66",fg="white",command=membership_fees)
        member_membership.grid(row=12,column=0,sticky="w")
        member_membershiptxt = Entry(Manage_Frame,font=("arial",15,"bold"),state=DISABLED,justify =RIGHT,textvariable=Membership)
        member_membershiptxt.grid(row=12,column=1,padx=10,pady=5,sticky="w")

        detail_frame = Frame(self.root,relief =RIDGE,bg="#001a66")
        detail_frame.place(x=500,y=100,width=820,height=630)

        detail_label = Label(detail_frame,font=("arial",11,"bold"),padx=0,pady=10,width=95,text="Date\t Ref ID\t  Firstname    Lastname    Mobile No   Address   Pincode   Gender    Membership")
        detail_label.grid(row = 0,column=0,columnspan=4,sticky="w")
        detail_labeltxt = Text(detail_frame,width=123,height=25,font=("arial",12))
        detail_labeltxt.grid(row=1,column=0,columnspan=4,sticky="w")
        
        receiptbtn = Button(detail_frame,padx=15,bd=5,font = ("arial",12,"bold"),bg = "#ff9966",width=15,text="Receipt",command=Receipt)
        receiptbtn.grid(row=2,column=0,sticky="w")

        resetbtn = Button(detail_frame,padx=15,bd=5,font = ("arial",12,"bold"),bg = "#ff9966",width=15,text="Reset",command=resetbtnf)
        resetbtn.grid(row=2,column=1,sticky="w")
        
        exitbtn = Button(detail_frame,padx=15,bd=5,font = ("arial",12,"bold"),bg = "#ff9966",width=15,text="Exit",command=exitbtnf)
        exitbtn.grid(row=2,column=2,sticky="w")
        


class hospital():
    def __init__(self,root):
       self.root = root
       self.root.title("Hospital Management System")
       self.root.geometry('1550x900+0+0')
       self.root.configure(background = "black")
       
       Date_of_Registration = StringVar()
       Date_of_Registration.set(time.strftime("%d/%m/%y"))
       
       Ref=StringVar()
       cmbTabletNames=StringVar()
       HospitalCode = StringVar()
       Number_of_Tablets = StringVar()
       Lot = StringVar()
       IssuedDate = StringVar()
       ExpiryDate = StringVar()
       DailyDose = StringVar()
       SideEffects = StringVar()
       MoreInformation = StringVar()
       StorageAdvice = StringVar()
       Medication = StringVar()
       PatientID = StringVar()
       PatientNHnumber = StringVar()
       Patientname = StringVar()
       Dateofbirth=StringVar()
       PatientAddress=StringVar()
       Prescription=StringVar()
       NHSnumber=StringVar()
       
       def Reference_numfunc():
           ranumber = random.randint(10000,99999999);
           randomnumber = str(ranumber)
           Ref.set(randomnumber)
           
       def prescriptiondatafunc():
           Reference_numfunc()
           TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"
            +Patientname.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"
            +Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+
            StorageAdvice.get()+"\t\t"+PatientID.get()+"\n")
           return
       
       def prescriptionfunc():
           Reference_numfunc()
           TextPrescription.insert(END,"Patient ID: \t\t"+PatientID.get()+"\n")
           TextPrescription.insert(END,"Patient Name: \t\t"+Patientname.get()+"\n")
           TextPrescription.insert(END,"Tablet: \t\t"+cmbTabletNames.get()+"\n")
           TextPrescription.insert(END,"Number of tablet: \t\t"+Number_of_Tablets.get()+"\n")
           TextPrescription.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n")
           TextPrescription.insert(END,"Issued Date: \t\t"+IssuedDate.get()+"\n")
           TextPrescription.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
           TextPrescription.insert(END,"Storage: \t\t"+StorageAdvice.get()+"\n")
           TextPrescription.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")
           
       def exitbtnf():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System","Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy();
                return;
    
       def deletefunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
       
       def resetfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            
            return

       title = Label(self.root,text="Hospital Management System",font=("monotype corsiva",42,"bold"),bd=5,relief=GROOVE,bg="#2eb8b8",fg="black")
       title.pack(side=TOP,fill=X)
       
       Manage_Frame = Frame(self.root,width=2840,height=380,bd=6,relief=RIDGE,bg="#0099cc")
       Manage_Frame.place(x=0,y=80)
       
       Button_Frame = Frame(self.root,width=1585,height=55,bd=4,relief=RIDGE,bg="#328695")
       Button_Frame.place(x=0,y=460)
       
       Data_Frame = LabelFrame(self.root,width=1510,height=270,bd=4,relief=RIDGE,bg="#266e73")
       Data_Frame.place(x=0,y=510)
       
       Data_Frameleft = LabelFrame(Manage_Frame,width=1510,text="General Information",font = ("arial",15,"italic bold"),height=400,bd=7,relief=RIDGE,bg="#0099cc")
       #Data_Frameleft.place(x=10,y=10)
       Data_Frameleft.pack(side =LEFT)
       Data_FrameRight = LabelFrame(Manage_Frame,width=1510,text="Prescription",font = ("arial",15,"italic bold"),height=400,bd=7,relief=RIDGE,bg="#0099cc")
       #Data_FrameRight.place(x=700,y=10)
       Data_FrameRight.pack(side =RIGHT)
       Data_Framedata = LabelFrame(Data_Frame,width=1050,text="Prescription Data",font=("arial",12,"italic bold"),
                                   height=390,bd=4,relief=RIDGE,bg="#3eb7bb")
       Data_Framedata.pack(side =LEFT)
       
       Date1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Date",padx=2,bg="#0099cc")
       Date1b1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
       Datetxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=Date_of_Registration)
       Datetxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)
       
       Ref1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Reference Number",padx=2,bg="#0099cc")
       Ref1b1.grid(row=1,column=0,padx=10,pady=5,sticky=W)
       Reftxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,state=DISABLED,textvariable=Ref)
       Reftxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)
       
       PatientID1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Patient ID",padx=2,bg="#0099cc")
       PatientID1b1.grid(row=2,column=0,padx=10,pady=5,sticky=W)
       PatientIDtxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=PatientID)
       PatientIDtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)
       
       PatientName1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Patient Name",padx=2,bg="#0099cc")
       PatientName1b1.grid(row=3,column=0,padx=10,pady=5,sticky=W)
       PatientNametxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=Patientname)
       PatientNametxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)
       
       Dateofbirth1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Date of Birth",padx=2,bg="#0099cc")
       Dateofbirth1b1.grid(row=4,column=0,padx=10,pady=5,sticky=W)
       Dateofbirthtxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=Dateofbirth)
       Dateofbirthtxt.grid(row=4,column=1,padx=10,pady=5,sticky=E)
       
       Address1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Address",padx=2,bg="#0099cc")
       Address1b1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
       Addresstxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=PatientAddress)
       Addresstxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

       NHSnumber1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="NHSnumber",padx=2,bg="#0099cc")
       NHSnumber1b1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
       NHSnumbertxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=NHSnumber)
       NHSnumbertxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

       Tablet1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Tablet",padx=2,bg="#0099cc")
       Tablet1b1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
       
       Tabletcmb = ttk.Combobox(Data_Frameleft,textvariable=cmbTabletNames,width=25,state="readonly",font=("arial",12,"bold"))
       Tabletcmb['values'] = ("","Paracetmol","Dan-p","Dio-1","Calpol","Amlodipine Besylate","Nexium","Singulair","Plavix","Amoxicillian","Limcin-900")
       Tabletcmb.current(0)
       Tabletcmb.grid(row=7,column=1,padx=10,pady=5)
       
       No_of_Tablets1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="No of Tablets",padx=2,bg="#0099cc")
       No_of_Tablets1b1.grid(row=8,column=0,padx=10,pady=5,sticky=W)
       No_of_Tabletstxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=Number_of_Tablets)
       No_of_Tabletstxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)
       

       HospitalCode1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Hospital Code",padx=2,bg="#0099cc")
       HospitalCode1b1.grid(row=0,column=2,padx=10,pady=5,sticky=W)
       HospitalCodetxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=HospitalCode)
       HospitalCodetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)
       
       StorageAdvice1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Storage Advice",padx=2,bg="#0099cc")
       StorageAdvice1b1.grid(row=1,column=2,padx=10,pady=5,sticky=W)
       
       StorageAdvicecmb = ttk.Combobox(Data_Frameleft,textvariable=StorageAdvice,width=23,state="readonly",font=("arial",12,"bold"))
       StorageAdvicecmb['values']=("","Under room temp","below 5^C","below 0^C","Refrigeration")
       StorageAdvicecmb.current(0)
       StorageAdvicecmb.grid(row=1,column=3,padx=10,pady=5,sticky=E)
       
       Lot_no1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Lot Number",padx=2,bg="#0099cc")
       Lot_no1b1.grid(row=2,column=2,padx=10,pady=5,sticky=W)
       Lot_notxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=Lot)
       Lot_notxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

       IssuedDate1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Issued Date",padx=2,bg="#0099cc")
       IssuedDate1b1.grid(row=3,column=2,padx=10,pady=5,sticky=W)
       IssuedDatetxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=IssuedDate)
       IssuedDatetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)
       
      
       ExpiryDate1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Expiry Date",padx=2,bg="#0099cc")
       ExpiryDate1b1.grid(row=4,column=2,padx=10,pady=5,sticky=W)
       ExpiryDatetxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=ExpiryDate)
       ExpiryDatetxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

       DailyDose1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Daily Dose",padx=2,bg="#0099cc")
       DailyDose1b1.grid(row=5,column=2,padx=10,pady=5,sticky=W)
       DailyDosetxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=DailyDose)
       DailyDosetxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

       SideEffects1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Side Effects",padx=2,bg="#0099cc")
       SideEffects1b1.grid(row=6,column=2,padx=10,pady=5,sticky=W)
       SideEffectstxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=SideEffects)
       SideEffectstxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

       MoreInfo1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="More Information",padx=2,bg="#0099cc")
       MoreInfo1b1.grid(row=7,column=2,padx=10,pady=5,sticky=W)
       MoreInfotxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=MoreInformation)
       MoreInfotxt.grid(row=7,column=3,padx=10,pady=5,sticky=E)
       
       Medication1b1 = Label(Data_Frameleft,font=("arial",12,"bold"),width=20,text="Medication",padx=2,bg="#0099cc")
       Medication1b1.grid(row=8,column=2,padx=10,pady=5,sticky=W)
       Medicationtxt = Entry(Data_Frameleft,font=("arial",12,"bold"),width=27,textvariable=Medication)
       Medicationtxt.grid(row=8,column=3,padx=10,pady=5,sticky=E)

       TextPrescription = Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17,padx=3,pady=5)
       TextPrescription.grid(row=0,column=0)
       
       TextPrescriptionData = Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=13,padx=3,pady=5)
       TextPrescriptionData.grid(row=1,column=0)
       


       Prescriptionbtn = Button(Button_Frame,text="Prescription",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=prescriptionfunc)
       Prescriptionbtn.grid(row=0,column=0,padx=15)
       
       Receiptbtn = Button(Button_Frame,text="Prescription Data",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=prescriptiondatafunc)
       Receiptbtn.grid(row=0,column=1,padx=15)
       
       Resetbtn = Button(Button_Frame,text="Reset",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=resetfunc)
       Resetbtn.grid(row=0,column=2,padx=15)
       
       Deletebtn = Button(Button_Frame,text="Delete",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=deletefunc)
       Deletebtn.grid(row=0,column=3,padx=15)
       
       Exitbtn = Button(Button_Frame,text="Exit",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=exitbtnf)
       Exitbtn.grid(row=0,column=4,padx=15)
       
       prescriptiondatarow = Label(Data_Framedata,bg="white",font=("arial",12,"bold"),
                             text="Date\tReference ID\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNumber of Tablets\t     Issued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatient ID")
       prescriptiondatarow.grid(row=0,column=0,sticky=W);

class doctormg():
     def __init__(self,root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure( background="black")
        
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrID = StringVar()
        Drname= StringVar()
        Spes= StringVar()
        GovtPri= StringVar()
        Surgeries= StringVar()
        Experiences= StringVar()
        Nurses= StringVar()
        Dateofbirth = StringVar()
        DrMobile= StringVar()
        PtName= StringVar()
        Apptime= StringVar()
        PtAge= StringVar()
        PatientAddress= StringVar()
        PtMobile= StringVar()
        Disease= StringVar()
        Case = StringVar()
        BenefitCard= StringVar()
        
        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Doctor Managenement","Are you sure you want to exit?")
            if exitbtn > 0:
               self.newWindow = Toplevel(self.root)
               self.app = Windows1(self.newWindow)
               return
        def resetfunc():
            
            DrID.set("")
            Drname.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            Dateofbirth.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return
        
        def deletefunc():
            DrID.set("")
            Drname.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            Dateofbirth.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return


        def Patient_idFunc():
            ranumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            DrID.set(randomnumber)
            return
        def prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrID.get()+"\t\t"
            +Drname.get()+"\t\t"+Dateofbirth.get()+"\t\t"+Spes.get()+"\t\t"+GovtPri.get()+"\t"
            +Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t\t"+DrMobile.get()+"\t\t"+
            PtName.get()+"\t\t"+Case.get()+"\t"+PtAge.get()+"\n")
            return
        def prescriptionfunc():
           Patient_idFunc()
           TextPrescription.insert(END,"Date: \t\t"+Date_of_Registration.get()+"\n")
           TextPrescription.insert(END,"Patient Name: \t\t"+PtName.get()+"\n")
           TextPrescription.insert(END,"Appointment Time: \t\t"+Apptime.get()+"\n")
           TextPrescription.insert(END,"Age: \t\t"+PtAge.get()+"\n")
           TextPrescription.insert(END,"Address: \t\t"+PatientAddress.get()+"\n")
           TextPrescription.insert(END,"Disease: \t\t"+Disease.get()+"\n")
           TextPrescription.insert(END,"Case: \t\t"+Case.get()+"\n")
           TextPrescription.insert(END,"Storage: \t\t"+BenefitCard.get()+"\n")
           TextPrescription.insert(END,"Dr. Mobile: \t\t"+DrMobile.get()+"\n")
           return

        title = Label(self.root,text="Doctor Management System",font=("monotype corsiva",42,"bold"),bd=5,relief=GROOVE,bg="#b7d8d6",fg="black")
        title.pack(side=TOP,fill=X)
        
        Manage_Frame = Frame(self.root,width =1510,height=400,bd=5,relief=RIDGE,bg="#789e9e")
        Manage_Frame.place(x=10,y=80)
        
        Buttons_Frame = Frame(self.root,width =1510,height=55,bd=4,relief=RIDGE,bg="#eef3db")
        Buttons_Frame.place(x=10,y=460)
        
        Data_Frame = Frame(self.root,width =1510,height=270,bd=4,relief=RIDGE,bg="#eef3db")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame,width=1050,text="General Information",font=("arial",20,"italic bold"),height=390,bd=7,pady=1,relief=RIDGE,bg="#789e9e")
        Data_FrameLeft.pack(side =LEFT)
        
        Data_Framedata = LabelFrame(Data_Frame,width=1050,text="Doctor's Details",font=("arial",12,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#b7d8d6")
        Data_Framedata.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width=1050,text="Patient's Information",font=("arial",20,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#789e9e")
        Data_FrameRight.pack(side =RIGHT)
        
        DrID1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor ID",bg="#789e9e")
        DrID1b1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        DrIDtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,state=DISABLED,textvariable=DrID)
        DrIDtxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)
        
        DrNameID1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor Name",bg="#789e9e")
        DrNameID1b1.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        DrNameIDtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Drname)
        DrNameIDtxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)
        
        DateofbirthID1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date of Birth",bg="#789e9e")
        DateofbirthID1b1.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        DateofbirthIDtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Dateofbirth)
        DateofbirthIDtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)
        
        SpesID1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Specialization",bg="#789e9e")
        SpesID1b1.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        SpesIDtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Spes)
        SpesIDtxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)
        
        GovtPriID1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Govt/Private",bg="#789e9e")
        GovtPriID1b1.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft,textvariable=GovtPri,width=25,state="readonly",font=("arial",12,"bold"))
        GovtPricmb['values'] = ("","Government","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row=4,column=1,padx=10,pady=5,sticky=E)
        
        Surgeries1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Surgeries",bg="#789e9e")
        Surgeries1b1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        Surgeriestxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Surgeries)
        Surgeriestxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)
        
        ExperienceID1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Experience",bg="#789e9e")
        ExperienceID1b1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        Experiencetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Experiences)
        Experiencetxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)
        
        Nurses1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Nurses",bg="#789e9e")
        Nurses1b1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        Nursestxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Nurses)
        Nursestxt.grid(row=7,column=1,padx=10,pady=5,sticky=E)
        
        DrMobile1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor Mobile No",bg="#789e9e")
        DrMobile1b1.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        DrMobiletxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=DrMobile)
        DrMobiletxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)
        
        Date1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date",padx=2,bg="#789e9e")
        Date1b1.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Datetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)
        
        
        PtName1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Name",padx=2,bg="#789e9e")
        PtName1b1.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        PtNametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtName)
        PtNametxt.grid(row=1,column=3,padx=10,pady=5,sticky=E)
        
        Apptime1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Appointement Time",padx=2,bg="#789e9e")
        Apptime1b1.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Apptimetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Apptime)
        Apptimetxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

        PtAge1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Age",padx=2,bg="#789e9e")
        PtAge1b1.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        PtAgetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtAge)
        PtAgetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

        PtAddress1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Address",padx=2,bg="#789e9e")
        PtAddress1b1.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        PtAddresstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PatientAddress)
        PtAddresstxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

        PtMobile1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Mobile",padx=2,bg="#789e9e")
        PtMobile1b1.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        PtMobiletxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtMobile)
        PtMobiletxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

        Disease1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Disease",padx=2,bg="#789e9e")
        Disease1b1.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        Diseasetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Disease)
        Diseasetxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

        Case1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Case",padx=2,bg="#789e9e")
        Case1b1.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        Casecmb = ttk.Combobox(Data_FrameLeft,textvariable=Case,width=25,state="readonly",font=("arial",12,"bold"))
        Casecmb['values'] = ("","New Case","Old Case")
        Casecmb.current(0)
        Casecmb.grid(row=7,column=3,padx=10,pady=5,sticky=E)


        BenefitCard1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Benefit Card",padx=10,bg="#789e9e")
        BenefitCard1b1.grid(row=8,column=2,sticky=W)
        
       
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft,textvariable=BenefitCard,width=25,state="readonly",font=("arial",12,"bold"))
        BenefitCardcmb['values'] = ("","Health Insurance","Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8,column=3,padx=10,sticky=E)

        TextPrescription = Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17,padx=3,pady=5)
        TextPrescription.grid(row=0,column=0)
        TextPrescriptionData = Text(Data_Framedata,font=("awirial",12,"bold"),width=203,height=12)
        TextPrescriptionData.grid(row=1,column=0)
        
        TextPrescriptionbtn = Button(Buttons_Frame,text="Patient Information",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=prescriptionfunc)
        TextPrescriptionbtn.grid(row=0,column=0,padx=15)
        
        DoctorDetailbtn = Button(Buttons_Frame,text="Doctor's Details",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=prescriptiondatafunc)
        DoctorDetailbtn.grid(row=0,column=1,padx=15)
        
        Resetbtn = Button(Buttons_Frame,text="Reset",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=resetfunc)
        Resetbtn.grid(row=0,column=2,padx=15)
        
        Deletebtn = Button(Buttons_Frame,text="Delete",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=deletefunc)
        Deletebtn.grid(row=0,column=3,padx=15)
        
        Exitbtn = Button(Buttons_Frame,text="Exit",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)
        
        Prescriptiondatarow = Label(Data_Framedata,bg="white",font=("arial",12,"bold"),
        text="Date\tDoctor ID\tDoctor Name\tDate of Birth\tSpecialization\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name\tCase\tPt.Age")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)


class Windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine Management System")
        self.master.geometry('1350x750+0+0') # x-axis, y-axis, z-axis dimension of application
        self.frame = Frame(self.master)
        self.frame.pack()
if __name__ == "__main__":
    main()



