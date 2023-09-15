from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
class Register_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_cnfpassword = StringVar()

        img1 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\flower.JPG")
        img1 = img1.resize((1580,800),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)                      #we convert the image using tool kit
        lbimg = Label(self.root,image=self.photoimage1 ,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1580,height=800) 

        img2 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\motivational.JPG")
        img2 = img2.resize((350,600),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage2 = ImageTk.PhotoImage(img2)                      #we convert the image using tool kit
        lbimg1 = Label(self.root,image=self.photoimage2 ,bd=4,relief=RIDGE)
        lbimg1.place(x=80,y=60,width=350,height=600) 


        frame = Frame(self.root,bd = 4,relief=RIDGE,bg="white")
        frame.place(x=430,y=60,width=800,height=600 )

        register_lbl = Label(frame,text='REGISTER HERE',font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        fname = Label(frame , text = "First Name" ,font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=70)
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"),width=25)
        fname_entry.place(x=55,y=110)

        lname = Label(frame , text = "Last Name" ,font=("times new roman",15,"bold"),bg="white")
        lname.place(x=350,y=70)
        lname_entry = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"),width=25)
        lname_entry.place(x=355,y=110)
        
        ContactNo = Label(frame , text = "Contact Num" ,font=("times new roman",15,"bold"),bg="white")
        ContactNo.place(x=50,y=160)
        ContactNo_entry = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"),width=25)
        ContactNo_entry.place(x=55,y=200)

        Email = Label(frame , text = "Email" ,font=("times new roman",15,"bold"),bg="white")
        Email.place(x=350,y=160)
        Email_entry = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"),width=25)
        Email_entry.place(x=355,y=200)

        Security = Label(frame , text = "Security" ,font=("times new roman",15,"bold"),bg="white")
        Security.place(x=50,y=250)
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),width=24,state="readonly")
        self.combo_security["values"] = ("Select","Your Birth Day","Your Father Name","Your Mother Name")
        self.combo_security.place(x=50,y=290)
        self.combo_security.current(0)
        
        
        Security_Ans = Label(frame , text = "Security Ans" ,font=("times new roman",15,"bold"),bg="white")
        Security_Ans.place(x=350,y=250)
        Security_Ans_entry = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"),width=25)
        Security_Ans_entry.place(x=355,y=290)

        Password = Label(frame , text = "Password" ,font=("times new roman",15,"bold"),bg="white")
        Password.place(x=50,y=340)
        Password_entry = ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"),width=25)
        Password_entry.place(x=55,y=380)

        ConfirmPassword = Label(frame , text = "Confirm Password" ,font=("times new roman",15,"bold"),bg="white")
        ConfirmPassword.place(x=350,y=340)
        ConfirmPassword_entry = ttk.Entry(frame,textvariable=self.var_cnfpassword,font=("times new roman",15,"bold"),width=25)
        ConfirmPassword_entry.place(x=355,y=380)
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",bg="white",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=420)
        

        img4 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\register.jpg")
        img4 = img4.resize((120,60),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage4 = ImageTk.PhotoImage(img4)                      #we convert the image using tool kit
        lbimg4 = Button(frame,command=self.register_data,image=self.photoimage4 ,bd=4,relief=RIDGE)
        lbimg4.place(x=50,y=470,width=120,height=60) 


        img3 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\login.JPG")
        img3 = img3.resize((120,60),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage3 = ImageTk.PhotoImage(img3)                      #we convert the image using tool kit
        lbimg3 = Button(frame,image=self.photoimage3 ,bd=4,relief=RIDGE)
        lbimg3.place(x=355,y=470,width=120,height=60) 

    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","Some fields are Empty")
        elif self.var_password.get()!=self.var_cnfpassword.get():
            messagebox.showerror("Error","Password and Confirm Password Must be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms and Conditions")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","This item is not found",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_password.get() 
                ))   

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","You Successfully Registered")

        

 
        



if __name__ == "__main__":
    root = Tk()
    register = Register_window(root)
    root.mainloop()