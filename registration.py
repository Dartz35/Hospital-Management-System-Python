import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
                return
        
        def resetbtnf():
            resetbtt = tkinter.messagebox.askyesno("Member Registration Form", "Are you sure you want to reset everything?")
            if resetbtt > 0:
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
               member_membershiptxt(state =DISABLED)
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
            detail_labeltxt.insert(END,"\t"+Date_of_Registration.get()+"    \t"+Ref.get()+"\t\t"+Firstname.get()+"   \t"+
                                   Lastname.get()+"\t\t"+Mobile_no.get()+"   \t\t"+Address.get()+" \t"+Pincode.get()+"    \t"+member_gendercmb.get()+ "\t\t"+Membership.get()+"\n")
         
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
        

        
        

                              


if __name__ == "__main__":
     root = Tk()
     app = Registration(root)
     root.mainloop()



