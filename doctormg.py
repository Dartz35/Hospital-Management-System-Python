import random
from sqlite3 import Date
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from unittest import case


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
               root.destroy()
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

        


if __name__ == "__main__":
    root = Tk()
    app = doctormg(root)
    root.mainloop()
        