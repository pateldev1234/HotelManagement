from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
class DetailRoom:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management Project")
        self.root.geometry("1295x550+230+230")
        

        lbl_Room = Label(self.root,text = "ADD ROOM DETAILS",font = ("time new roman",40,"bold"),bg = "black",fg="gold")
        lbl_Room.place(x=0,y=0,width=1295,height = 50)
        #Now we need to add one image on the mleft side of the txt we written upward
        img_Room = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel2.png")
        img_Room = img_Room.resize((160,50),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img_Room)
        img1_Room = Label(self.root,image=self.img2,bd=4,relief=RIDGE)
        img1_Room.place(x=0,y=0,width=160,height=50)
        # we will make one table frame
        lbl_frame = LabelFrame(self.root,text = "New Room Add ",font=("time new roman",12,"bold"),bd=4,relief=RIDGE )
        lbl_frame.place(x=5,y=50,width = 500,height = 350)
        # we will set one image at the top of the lable frame 
        #img1 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\bedroom.JPG")
        #img1 = img1.resize((530,75),Image.ANTIALIAS)
        #self.img3 = ImageTk.PhotoImage(img1)
        #Lbl_Detail = Label(lbl_frame,image=self.img3,bd=4,relief=RIDGE)
        #Lbl_Detail.place(x=0,y=0,width=530,height=75)
        # now we need to add the text and the search bar in the lable frame
        self.var_floor = StringVar()
        lbl_floor = Label(lbl_frame,text = "Floor",font = ("time new roman",12,"bold"),padx = 4,pady = 4)
        lbl_floor.grid(row=0,column=0,sticky=W)
        Ent_floor = ttk.Entry(lbl_frame,width=20 ,textvariable=self.var_floor,font = ("time new roman",12,"bold"))
        Ent_floor.grid(row = 0,column=1,sticky=W)
        
        self.var_roomno = StringVar()
        lbl_RoomNo = Label(lbl_frame,text = "Room No",font = ("time new roman",12,"bold"),padx = 4,pady = 4)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        Ent_RoomNo = ttk.Entry(lbl_frame,width=20 ,textvariable=self.var_roomno,font = ("time new roman",12,"bold"))
        Ent_RoomNo.grid(row = 1,column=1,sticky=W)
        
        self.var_roomtype = StringVar()
        lbl_RoomType = Label(lbl_frame,text = "Room Type",font = ("time new roman",12,"bold"),padx = 4,pady = 4)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        Ent_RoomType = ttk.Entry(lbl_frame,width=20 ,textvariable=self.var_roomtype ,font = ("time new roman",12,"bold"))
        Ent_RoomType.grid(row = 2,column=1,sticky=W)

        #Now we have to make some button to display the data from the database
        Add_button = Button(lbl_frame,text = "ADD",command=self.add_data,width=10,font=("time new roman",10,"bold"),fg="gold",bg="black",padx=4,pady=4)
        Add_button.grid(row = 5,column=8)
        Update_button = Button(lbl_frame,text = "UPDATE",command=self.update,width=10,font=("time new roman",10,"bold"),fg="gold",bg="black",padx=4,pady=4)
        Update_button.grid(row = 6,column=7)
        Delete_button = Button(lbl_frame,text = "DELETE",command=self.mdelete,width=10,font=("time new roman",10,"bold"),fg="gold",bg="black",padx=4,pady=4)
        Delete_button.grid(row = 7,column=8)
        Clear_button = Button(lbl_frame,text = "CLEAR",command = self.clear,width=10,font=("time new roman",10,"bold"),fg="gold",bg="black",padx=4,pady=4)
        Clear_button.grid(row = 8,column=7)

        Table_frame = LabelFrame(self.root,text = "Show Room ",font=("time new roman",12,"bold"),bd=4,relief=RIDGE)
        Table_frame.place(x=550,y=50,width = 500,height = 350)
        
        # we need to have the scroll bar at right side and on the Bottom of the table

        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.details_table = ttk.Treeview(Table_frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("floor",text="Floor")
        self.details_table.heading("roomno",text="RoomNo")
        self.details_table.heading("roomtype",text="RoomType")
        self.details_table["show"] ="headings"
        self.details_table.column("floor",width=100)
        self.details_table.column("roomno",width=100)
        self.details_table.column("roomtype",width=100)
        self.details_table.pack(fill=BOTH,expand=1)
        self.details_table.bind("<ButtonRelease-1>",self.get_currsor) 
        self.fetch_data()
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomno.get()=="":                                         # get is used for getting  the entry fill data
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),
                                                                                                self.var_roomno.get(),
                                                                                               
                                                                                                self.var_roomtype.get(),
                                                                                                
                                                                                                
                                                                                                ))  

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","rooms has been added ",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
        
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
        my_cursor = conn.cursor() # with the help of the cursor we try to run our mysql query;
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall() #we need to storw all the data in some variable
        if len(rows)!=0:
            self.details_table.delete(*self.details_table.get_children())
            for i in rows:
                self.details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def get_currsor(self,event=""): # event is used because we need to Bind

        cursor_row = self.details_table.focus()
        content = self.details_table.item(cursor_row)
        row = content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
    
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",
            
                                                                                                                                        (
                                                                                                                                            self.var_floor.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                    
                                                                                                                                   self.var_roomno.get()                                                            


            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update"," Details Has Been Updates Successfully",parent=self.root)
    
    def mdelete(self):
        mDelete = messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent = self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost",user="root",password="Devesh@123",database="customer", auth_plugin = 'mysql_native_password') 
            my_cursor = conn.cursor()
            query = "delete from details where floor=%s"
            value = (self.var_floor.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def clear(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("") 

        


    

if __name__ =="__main__":
    root = Tk()
    obj2 =DetailRoom(root)
    root.mainloop()