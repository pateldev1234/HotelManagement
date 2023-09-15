from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
class Room_win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management Project")
        self.root.geometry("1295x550+230+230")
        
        #we have to make the variable to store the data
        self.var_contact  = StringVar()
        self.var_checkin  = StringVar()
        self.var_checkout  = StringVar()
        self.var_roomtype  = StringVar()
        self.var_roomavailable  = StringVar()
        self.var_meal  = StringVar()
        self.var_noofdays  = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal  = StringVar()
        self.var_total  = StringVar()

        # we are first need to write the title of the page
        lbl_Room = Label(self.root,text = "ADD ROOM DETAILS",font = ("time new roman",40,"bold"),bg = "black",fg="gold")
        lbl_Room.place(x=0,y=0,width=1295,height = 50)
        #Now we need to add one image on the mleft side of the txt we written upward
        img_Room = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel2.png")
        img_Room = img_Room.resize((160,50),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img_Room)
        img1_Room = Label(self.root,image=self.img2,bd=4,relief=RIDGE)
        img1_Room.place(x=0,y=0,width=160,height=50)
        # we will make one table frame
        lbl_frame = LabelFrame(self.root,text = "ROOM BOOKING DETAILS",font=("time new roman",12,"bold"),bd=4,relief=RIDGE )
        lbl_frame.place(x=5,y=50,width = 425,height = 490)
        # Now We need to add some of the fields in the label frame
        lbl_Cust_con = Label(lbl_frame,text = "Customer Contact",font = ("time new roman",12,"bold"),padx = 2,pady = 2)
        lbl_Cust_con.grid(row=0,column=0,sticky=W)
        Ent_Cust_con = ttk.Entry(lbl_frame,textvariable = self.var_contact,width=20 ,font = ("time new roman",12,"bold"))
        Ent_Cust_con.grid(row = 0,column=1,sticky=W)
        # we need to have one button fetch data
        fetch_btn = Button(lbl_frame,text = "Fetch Data",command=self.Fetch_data,width=10,font = ("time new roman",9,"bold"),bg = "black",fg="gold")
        fetch_btn.place(x=335,y=2)
        # Check in Date
        check_in_date = Label(lbl_frame,text="Check_in_date:",font=("arial",12,"bold"),padx=2,pady=4)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date = ttk.Entry(lbl_frame,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)
        #checkout date
        check_out_date = Label(lbl_frame,text="Check_out_date:",font=("arial",12,"bold"),padx=2,pady=4)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date = ttk.Entry(lbl_frame,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2 ,column=1)
        #Room Type
        lbl_Room_type = Label(lbl_frame,text="Room Type",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Room_type.grid(row=3,column=0,sticky=W)
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor() # with the help of the cursor we try to run our mysql query;
        my_cursor.execute("select RoomType from details")
        row = my_cursor.fetchall() #we need to storw all the data in some variable
        Combo_Room_type = ttk.Combobox(lbl_frame,textvariable=self.var_roomtype,font=("arial",13,"bold"),width = 27,state="readonly")
        Combo_Room_type["value"] = row
        Combo_Room_type.current(0)
        Combo_Room_type.grid(row=3,column=1)
        #Available Room
        lbl_Room_Avai= Label(lbl_frame,text="Available Room",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_Room_Avai.grid(row=4,column=0,sticky=W)
        #txt_Room_Avai = ttk.Entry(lbl_frame,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        #txt_Room_Avai.grid(row=4 ,column=1)
        # we have to make it such that it will automaticaly suggest all the available room in the database
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor() # with the help of the cursor we try to run our mysql query;
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall() #we need to storw all the data in some variable
        Combo_Room_type = ttk.Combobox(lbl_frame,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width = 27,state="readonly")
        Combo_Room_type["value"] = rows
        Combo_Room_type.current(0)
        Combo_Room_type.grid(row=4,column=1)
        # Meal
        lblmeal = Label(lbl_frame,text="Meal",font=("arial",12,"bold"),padx=2,pady=4)
        lblmeal.grid(row=5,column=0,sticky=W)
        txtmeal = ttk.Entry(lbl_frame,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtmeal.grid(row=5 ,column=1)
        #Number of Days
        lbl_ND = Label(lbl_frame,text="Number of Days",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_ND.grid(row=6,column=0,sticky=W)
        txt_ND= ttk.Entry(lbl_frame,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txt_ND.grid(row=6 ,column=1)
        # Paid Tax
        lbl_PT = Label(lbl_frame,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_PT.grid(row=7,column=0,sticky=W)
        txt_PT= ttk.Entry(lbl_frame,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txt_PT.grid(row=7 ,column=1)
        #Sub Total
        lbl_ST = Label(lbl_frame,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_ST.grid(row=8,column=0,sticky=W)
        txt_ST= ttk.Entry(lbl_frame,textvariable=self.var_subtotal,width=29,font=("arial",13,"bold"))
        txt_ST.grid(row=8 ,column=1)
        #Total cost
        lbl_TC = Label(lbl_frame,text="Total cost",font=("arial",12,"bold"),padx=2,pady=4)
        lbl_TC.grid(row=9,column=0,sticky=W)
        txt_TC= ttk.Entry(lbl_frame,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txt_TC.grid(row=9 ,column=1)
        # Bill Button
        Bill_btn = Button(lbl_frame,text = "Bill",command=self.total,width=10,font = ("time new roman",12 ,"bold"),bg = "black",fg="gold")
        Bill_btn.grid(row =10,column=0,padx=1,sticky=W)
        # now we have to  make some of the button
        btn_frame = Frame(lbl_frame,bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=40)
        ADD_btn = Button(btn_frame,text="ADD",command=self.add_data,width=8,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        ADD_btn.grid(row=0,column=0,padx=1)
        #UPDATE_btn = Button(btn_frame,text="UPDATE",command=self.update,width=8,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        #UPDATE_btn.grid(row=0,column=1,padx=1)
        DELETE_btn = Button(btn_frame,text="DELETE",command = self.mdelete,width=8,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0,padx=2)
        DELETE_btn.grid(row=0,column=3,padx=1)
        RESET_btn = Button(btn_frame,text="RESET",command = self.reset,width=8,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        RESET_btn.grid(row=0,column=4,padx=1)
        # right side image
        img1_Room = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\bedroom.JPG")
        img1_Room = img1_Room.resize((400,210),Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img1_Room)
        img2_Room = Label(self.root,image=self.img3,bd=4,relief=RIDGE)
        img2_Room.place(x=720,y=50,width=400,height=210)
         # tableFrame
        Tableframe = LabelFrame(self.root,bd = 2,relief=RIDGE,text="View Details && Search System",font=("time new roman",14,"bold"),padx=2,pady=2)
        Tableframe.place(x=430,y=260,width=690,height=205)
        # Search System
        self.search_var = StringVar() # This is Made to Store the Values with the help of which we can search the values 
        Search_Sys = Label(Tableframe,text="Search By",font=("arial",10,"bold"),bg="black",fg="Red")
        Search_Sys.grid(row=1 ,column=0,sticky=W)
        Combo_Search = ttk.Combobox(Tableframe,textvariable=self.search_var,font=("arial",10,"bold"),width = 20,state="readonly")
        Combo_Search["value"] = ("Contact","RoomNo")
        Combo_Search.current(0) 
        Combo_Search.grid(row=1,column=1,padx=4)
        self.text_var = StringVar()
        Search_Entry = ttk.Entry(Tableframe,textvariable = self.text_var,width=20,font=("arial",10,"bold"))
        Search_Entry.grid(row=1,column=2,padx=4)
        Search_btn = Button(Tableframe,text="Search",command = self.search,width=6,font=("times new roman",13,"bold"),bg="black",fg="gold",bd=0)
        Search_btn.grid(row=1,column=3,padx=4)
        ShowAll_btn = Button(Tableframe,text="Show",command = self.fetch_data ,width=6,font=("times new roman",13,"bold"),bg="black",fg="gold",bd=0)
        ShowAll_btn.grid(row=1,column=4,padx=4)

        # we need to show the data for which we will make one frame
        Table_frame = Frame(Tableframe,bd=4,relief=RIDGE)
        Table_frame.place(x=0,y=25,width=680,heigh=150)
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.cust_details_table = ttk.Treeview(Table_frame,column=("contact","checkin","checkout","roomtype","roomavailable","meal","numberofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("contact",text="Contact")
        self.cust_details_table.heading("checkin",text="CheckIn")
        self.cust_details_table.heading("checkout",text="CheckOut")
        self.cust_details_table.heading("roomtype",text="Roomtype")
        self.cust_details_table.heading("roomavailable",text="RoomAvailable")
        self.cust_details_table.heading("meal",text="Meal")
        self.cust_details_table.heading("numberofdays",text="NumberofDays")
        self.cust_details_table["show"] ="headings"
        self.cust_details_table.column("contact",width=100)
        self.cust_details_table.column("checkin",width=100)
        self.cust_details_table.column("checkout",width=100)
        self.cust_details_table.column("roomtype",width=100)
        self.cust_details_table.column("roomavailable",width=100)
        self.cust_details_table.column("meal",width=100)
        self.cust_details_table.column("numberofdays",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_currsor) 
        self.fetch_data()

   # fetch the whole infomation about the person with the contact number
    def Fetch_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Some fields are Empty",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This item is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe = Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=430,y=60,width=300,height=200)

                lblframe = Label(showdataframe,text = "Name :",font = ("arial",12,"bold"))
                lblframe.grid(row=0,column=0)

                lbl1 = Label(showdataframe,text = row,font=("arial",12,"bold"))
                lbl1.grid(row=0,column=1)
                

                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblframe1 = Label(showdataframe,text = "Gender :",font = ("arial",12,"bold"))
                lblframe1.grid(row=1,column=0)

                lbl2 = Label(showdataframe,text = row,font=("arial",12,"bold"))
                lbl2.grid(row=1,column=1)

                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblframe2 = Label(showdataframe,text = "Email:",font = ("arial",12,"bold"))
                lblframe2.grid(row=2,column=0)

                lbl3 = Label(showdataframe,text = row,font=("arial",12,"bold"))
                lbl3.place(x=65,y=50)

                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblframe3 = Label(showdataframe,text = "Nationality :",font = ("arial",12,"bold"))
                lblframe3.grid(row=3,column=0)

                lbl4 = Label(showdataframe,text = row,font=("arial",12,"bold"))
                lbl4.grid(row=3,column=1)

                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblframe4 = Label(showdataframe,text = "Address :",font = ("arial",12,"bold"))
                lblframe4.grid(row=4,column=0)

                lbl5 = Label(showdataframe,text = row,font=("arial",12,"bold"))
                lbl5.grid(row=4,column=1)


    # we are now in a position to work on the functionality of the button we have made
    def add_data(self):
        if self.var_contact.get()=="" or self.var_roomavailable.get()=="":                                         # get is used for getting  the entry fill data
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofdays.get()
                                                                                                
                                                                                                ))  

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","rooms has added the data",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
        
                
    # to show the data in the customer details RHS we need to fetch the data from the database for tha we have to make one function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor() # with the help of the cursor we try to run our mysql query;
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall() #we need to storw all the data in some variable
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # now we want to add data back to the corresponding variables in the LHS so that we can update the data for that we have to write one function
   # now we want to add data back to the corresponding variables in the LHS so that we can update the data for that we have to write one function
    def get_currsor(self,event=""): # event is used because we need to Bind

        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        
        
    def mdelete(self):
        mDelete = messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent = self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()


    #def update(self):
     #   if self.var_contact.get()=="":
      #      messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
       # else:
        #    conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
         #   my_cursor = conn.cursor()
          #  my_cursor.execute("Update room set check_in=%s,check-out=%s,roomtype=%s,Roomno=%s,meal=%s,noofdays=%s where Contact=%s",
           # 
           #
           # 
           # 
           # 
           # 
           # 
           # 
           # 
           # 
           # 
           #                                                                                                                              (
            #                                                                                                                                self.var_checkin.get(),
             #                                                                                                                               self.var_checkout.get(),
              #                                                                                                                              self.var_roomtype.get(),
               #                                                                                                                             self.var_roomavailable.get(),
               #                                                                                                                             self.var_meal.get(),
                #                                                                                                                            self.var_noofdays.get(),
              #                                                                                                                              
               #                                                                                                                             self.var_contact.get()                                                            
  

         #   ))
          #  conn.commit()
           
           # self.fetch_data()
            #conn.close()
           #messagebox.showinfo("Update","Room Details Has Been Updates Successfully",parent=self.root)    
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        #self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("") 
        self.var_subtotal.set("")
        self.var_total.set("")
    
    
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3*q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST  = "Rs."+str("%.2f"%((q5)))
            TT  = "Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3*q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST  = "Rs."+str("%.2f"%((q5)))
            TT  = "Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3*q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST  = "Rs."+str("%.2f"%((q5)))
            TT  = "Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

    #search System we have to make
    def search(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor()
        my_cursor.execute("select* from room where "+str( self.search_var.get())+ " LIKE '%"+str(self.text_var.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ =="__main__":
    root = Tk()
    obj2 = Room_win(root)
    root.mainloop()
