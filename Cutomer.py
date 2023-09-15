from tkinter import*
from PIL import Image ,ImageTk
from tkinter import ttk 
import random
import mysql.connector
from tkinter import messagebox
class Cust_win:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+233+230")

        #We will make variables so that we can place the data in the database
        self.var_ref = StringVar() # string var is the data type as we donot want to perform the calculation so we take stringvar
        x = random.randint(1000,9999)
        self.var_ref.set(str(x)) 


        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()

        
        #we have to make the title 
        lbl1_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("time new roman",40,"bold"),bg="black",fg="gold")
        lbl1_title.place(x=0,y=0,width=1295,height=50)
        # logo paste here
        img2 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel2.png")
        img2 = img2.resize((160,50),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage2 = ImageTk.PhotoImage(img2)                      #we convert the image using tool kit
        lbimg = Label(self.root,image=self.photoimage2 ,bd=4,relief=RIDGE) # relief is the style
        lbimg.place(x=0,y=0,width=160,height=50)

        # we now will make the lable frame
        labelframeleft = LabelFrame(self.root,bd = 2,relief=RIDGE,text="Customer Details",font=("time new roman",14,"bold"),padx=2,pady=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        #we have to put the labels in the frame and button # Customer Ref
        lbl_cus_ref = Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=2)
        lbl_cus_ref.grid(row=0,column=0,sticky=W)
        #we will make the entry fill like a search box type
        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width=30,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        #Customer name
        lbl_cus_name = Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_cus_name.grid(row=1,column=0,sticky=W)
        entry_name = ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=30,font=("arial",13,"bold"))
        entry_name.grid(row=1,column=1)
        # Mother Name
        lbl_Mother_name = Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Mother_name.grid(row=2,column=0,sticky=W)
        entry_Mname = ttk.Entry(labelframeleft,textvariable=self.var_mother,width=30,font=("arial",13,"bold"))
        entry_Mname.grid(row=2,column=1)
        # Gender
        lbl_Gender_name = Label(labelframeleft,text="Gender Name",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Gender_name.grid(row=3,column=0,sticky=W)
        Combo_Gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width = 28,state="readonly")
        Combo_Gender["value"] = ("Male","Female","other")
        Combo_Gender.current(0)
        Combo_Gender.grid(row=3,column=1)
        #postcode
        lbl_Post_code = Label(labelframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Post_code.grid(row=4,column=0,sticky=W)
        entry_Pc = ttk.Entry(labelframeleft,textvariable=self.var_post,width=30,font=("arial",13,"bold"))
        entry_Pc.grid(row=4,column=1)
        #Mobile Number
        lbl_Mobile_num = Label(labelframeleft,text="Mobile Number",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Mobile_num.grid(row=5,column=0,sticky=W)
        entry_Mnum = ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=30,font=("arial",13,"bold"))
        entry_Mnum.grid(row=5,column=1)
        #Email
        lbl_Email = Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Email.grid(row=6,column=0,sticky=W)
        entry_Email = ttk.Entry(labelframeleft,textvariable=self.var_email,width=30,font=("arial",13,"bold"))
        entry_Email.grid(row=6,column=1)
        #Nationality
        lbl_Nationality = Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Nationality.grid(row=7,column=0,sticky=W)
        Combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width = 28,state="readonly")
        Combo_Nationality["value"] = ("Indian","Australia","New zealand","England")
        Combo_Nationality.current(0)
        Combo_Nationality.grid(row=7,column=1)
        #Id Proof
        lbl_IdProof = Label(labelframeleft,text="Id Proof",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_IdProof.grid(row=8,column=0,sticky=W)
        Combo_IdProof = ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width = 28,state="readonly")
        Combo_IdProof["value"] = ("Adhar Card","Pan Card","Passport","Other")
        Combo_IdProof.current(0)
        Combo_IdProof.grid(row=8,column=1)
        #Id Number
        lbl_IdNumber = Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_IdNumber.grid(row=9,column=0,sticky=W)
        entry_IdNumber = ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=30,font=("arial",13,"bold"))
        entry_IdNumber.grid(row=9,column=1)
        #Address
        lbl_Address = Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Address.grid(row=10,column=0,sticky=W)
        entry_Address = ttk.Entry(labelframeleft,textvariable=self.var_address ,width=30,font=("arial",13,"bold"))
        entry_Address.grid(row=10,column=1)
        # Now We to make one frame in which all the button to update the data is placed
        btn_frame = Frame(labelframeleft,bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=40)
        ADD_btn = Button(btn_frame,text="ADD",command=self.add_data,width=8,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        ADD_btn.grid(row=0,column=0,padx=1)
        UPDATE_btn = Button(btn_frame,text="UPDATE",command = self.update,width=8,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        UPDATE_btn.grid(row=0,column=1,padx=1)
        DELETE_btn = Button(btn_frame,text="DELETE",width=8,command=self.mdelete,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0,padx=2)
        DELETE_btn.grid(row=0,column=3,padx=1)
        RESET_btn = Button(btn_frame,text="RESET",width=8,command = self.reset,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        RESET_btn.grid(row=0,column=4,padx=1)
        # tableFrame
        Tableframe = LabelFrame(self.root,bd = 2,relief=RIDGE,text="View Details && Search System",font=("time new roman",14,"bold"),padx=2,pady=2)
        Tableframe.place(x=430,y=50,width=700,height=450)
        # Search System
        self.search_var = StringVar() # This is Made to Store the Values with the help of which we can search the values 
        Search_Sys = Label(Tableframe,text="Search By",font=("arial",10,"bold"),bg="black",fg="Red")
        Search_Sys.grid(row=1 ,column=0,sticky=W)
        Combo_Search = ttk.Combobox(Tableframe,textvariable=self.search_var,font=("arial",10,"bold"),width = 20,state="readonly")
        Combo_Search["value"] = ("Mobile Number","Ref")
        Combo_Search.current(0) 
        Combo_Search.grid(row=1,column=1,padx=4)
        self.text_var = StringVar()
        Search_Entry = ttk.Entry(Tableframe,textvariable = self.text_var,width=20,font=("arial",10,"bold"))
        Search_Entry.grid(row=1,column=2,padx=4)
        Search_btn = Button(Tableframe,text="Search",command = self.search,width=6,font=("times new roman",13,"bold"),bg="black",fg="gold",bd=0)
        Search_btn.grid(row=1,column=3,padx=4)
        ShowAll_btn = Button(Tableframe,text="Show",command = self.fetch_data,width=6,font=("times new roman",13,"bold"),bg="black",fg="gold",bd=0)
        ShowAll_btn.grid(row=1,column=4,padx=4)
        #Show Data Table Means all the search data is to be shown here in the Data Table
        
        Table_frame = Frame(Tableframe,bd=2, relief=RIDGE)
        Table_frame.place(x=0,y=50,width=680,height=330)
        # we have to Make one table with the scroll bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Customer_Details_Table = ttk.Treeview(Table_frame,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Customer_Details_Table.xview)
        scroll_y.config(command=self.Customer_Details_Table.yview)

        self.Customer_Details_Table.heading("ref",text="Ref Num")
        self.Customer_Details_Table.heading("name",text="Name")
        self.Customer_Details_Table.heading("mother",text="Mother")
        self.Customer_Details_Table.heading("gender",text="Gender")
        self.Customer_Details_Table.heading("post",text="Post")
        self.Customer_Details_Table.heading("mobile",text="Mobile")
        self.Customer_Details_Table.heading("email",text="Email")
        self.Customer_Details_Table.heading("nationality",text="Nationality")
        self.Customer_Details_Table.heading("idproof",text="Idproof")
        self.Customer_Details_Table.heading("idnumber",text="Idnumber")
        self.Customer_Details_Table.heading("address",text="Address")
        self.Customer_Details_Table["show"] ="headings"
        self.Customer_Details_Table.column("ref",width=100)
        self.Customer_Details_Table.column("name",width=100)
        self.Customer_Details_Table.column("mother",width=100)
        self.Customer_Details_Table.column("gender",width=100)
        self.Customer_Details_Table.column("post",width=100)
        self.Customer_Details_Table.column("mobile",width=100)
        self.Customer_Details_Table.column("email",width=100)
        self.Customer_Details_Table.column("nationality",width=100)
        self.Customer_Details_Table.column("idproof",width=100)
        self.Customer_Details_Table.column("idnumber",width=100)
        self.Customer_Details_Table.column("address",width=100)

        self.Customer_Details_Table.pack(fill=BOTH,expand=1)
        self.Customer_Details_Table.bind("<ButtonRelease-1>",self.get_currsor) 
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":                                         # get is used for getting  the entry fill data
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_idproof.get(),
                                                                                                self.var_idnumber.get(),
                                                                                                self.var_address.get()
                                                                                                ))  

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer hase added the data",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
        

    # to show the data in the customer details RHS we need to fetch the data from the database for tha we have to make one function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor() # with the help of the cursor we try to run our mysql query;
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall() #we need to storw all the data in some variable
        if len(rows)!=0:
            self.Customer_Details_Table.delete(*self.Customer_Details_Table.get_children())
            for i in rows:
                self.Customer_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # now we want to add data back to the corresponding variables in the LHS so that we can update the data for that we have to write one function
    def get_currsor(self,event=""): # event is used because we need to Bind

        cursor_row = self.Customer_Details_Table.focus()
        content = self.Customer_Details_Table.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",
            
                                                                                                                                        (
                                                                                                                                            self.var_cust_name.get(),
                                                                                                                                            self.var_mother.get(),
                                                                                                                                            self.var_gender.get(),
                                                                                                                                            self.var_post.get(),
                                                                                                                                            self.var_mobile.get(),
                                                                                                                                            self.var_email.get(),
                                                                                                                                            self.var_nationality.get(),
                                                                                                                                            self.var_idproof.get(),
                                                                                                                                            self.var_idnumber.get(),
                                                                                                                                            self.var_address.get(),
                                                                                                                                            self.var_ref.get()                                                            


            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Has Been Updates Successfully",parent=self.root)
    def mdelete(self):
        mDelete = messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent = self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")
        x = random.randint(1000,9999)
        self.var_ref.set(str(x)) 
    
    def search(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor()
        my_cursor.execute("select* from customer where "+str( self.search_var.get())+ " LIKE '%"+str(self.text_var.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Customer_Details_Table.delete(*self.Customer_Details_Table.get_children())
            for i in rows:
                self.Customer_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()




if __name__ == "__main__":
    root = Tk()
    obj1 = Cust_win(root)
    root.mainloop()