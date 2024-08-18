
import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
       


       

       





if __name__ == "__main__":
     root = Tk()
     app = hospital(root)
     root.mainloop()
    
