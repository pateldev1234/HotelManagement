from tkinter import*
from PIL import Image,ImageTk
from Cutomer import Cust_win
from Room import Room_win
from Detail import DetailRoom
class HotelManagementSystem: 
    def __init__(self,root):
        self.root = root;
        self.root.title("Hotel Management System");
        self.root.geometry("1580x800+0+0");
         
        #first Image 
        img1 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel1.jpg")
        img1 = img1.resize((1580,150),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)                      #we convert the image using tool kit
        lbimg = Label(self.root,image=self.photoimage1 ,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1580,height=150) 
        # first logo
        img2 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel2.png")
        img2 = img2.resize((160,150),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage2 = ImageTk.PhotoImage(img2)                      #we convert the image using tool kit
        lbimg = Label(self.root,image=self.photoimage2 ,bd=4,relief=RIDGE) # relief is the style
        lbimg.place(x=0,y=0,width=160,height=150) 
        # Title we need to place
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief = RIDGE)
        lbl_title.place(x=0,y=150,width = 1580,height=50)
        # we make one frame in which all the things are to be placed
        main_frame = Frame(self.root,bd = 5,relief=RIDGE)
        main_frame.place(x=0,y=200,width=1580,height=700)
        # we need to set the frame in order window
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief = RIDGE)
        lbl_menu.place(x=0,y=0,width = 230)
        # we have button frame below the manu bar
        main_btn = Frame(main_frame,bd = 4,relief=RIDGE)
        main_btn.place(x=0,y=35,width=230,height=200)
        #we have to place some button in the button frame
        cust_btn = Button(main_btn,text="CUSTOMER",command=self.cust_details,width=18,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        cust_btn.grid(row=0,column=0,pady=1)
        room_btn = Button(main_btn,text="ROOM",command = self.room_details,width=18,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        room_btn.grid(row=1,column=0,pady=1)
        detail_btn = Button(main_btn,text="DETAIL",command = self.details,width=18,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        detail_btn.grid(row=2,column=0,pady=1)
        report_btn = Button(main_btn,text="REPORT",width=18,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        report_btn.grid(row=3,column=0,pady=1)
        logout_btn = Button(main_btn,text="LOGOUT",command=self.Logout,width=18,font=("times new roman",16,"bold"),bg="black",fg="gold",bd=0)
        logout_btn.grid(row=4,column=0,pady=1) # grid is basically used when you do not want to place anything else except the similar things in the frame
        # Right Side Image we Need to place 
        img3 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel3.jpg")
        img3 = img3.resize((1300,600),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage3 = ImageTk.PhotoImage(img3)                      #we convert the image using tool kit
        lbimg3 = Label(main_frame,image=self.photoimage3 ,bd=4,relief=RIDGE)
        lbimg3.place(x=225,y=0,width=1300,height=600) 
        #down image
        img4 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\Hotel4.jpg")
        img4 = img4.resize((230,210),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage4 = ImageTk.PhotoImage(img4)                      #we convert the image using tool kit
        lbimg4 = Label(main_frame,image=self.photoimage4 ,bd=4,relief=RIDGE)
        lbimg4.place(x=0,y=230,width=230,height=150) 
        img5 = Image.open(r"C:\Users\devesh patel\Desktop\Hotel ManagementSystem\food1.jpg")
        img5 = img5.resize((230,210),Image.ANTIALIAS) # Antilias convert high level image to low level image
        self.photoimage5 = ImageTk.PhotoImage(img5)                      #we convert the image using tool kit
        lbimg5 = Label(main_frame,image=self.photoimage5 ,bd=4,relief=RIDGE)
        lbimg5.place(x=0,y=380,width=230,height=150) 
        # now we are going to design that after clicking on to the the customer cbutton new window needs to be open .now we discuss about how to do that thing
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Cust_win(self.new_window)
    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_win(self.new_window)
    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailRoom(self.new_window)

    
    def Logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()      