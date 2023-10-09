from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter.font import Font
class First:
#------------Connecting to database--------
global mydb
mydb=mysql.connector.connect(host="localhost", user="root",
passwd="",database=’canteen’)
global mycursor
mycursor=mydb.cursor()
#-----------Creating window-----------
global root
root=Tk()
global width
width=root.winfo_screenwidth()
global height
height=root.winfo_screenheight()
root.title("Welcome")
root.geometry("%dx%d" % (width, height))
root.resizable(False, False)
#----------Commonly used Fonts
global Helv50
Helv50=Font(family="Helvetica", size=50, weight="bold")
global Times20
Times20=Font(family="Times", size=20, slant="italic")
global Times26
Times26=Font(family="Times", size=26)
global Times16
Times16=Font(family="Times", size=16)
global Times23
Times23=Font(family="Times", size=23, weight="bold")
#--------Background Images-------------
#Opening the Main Window's Background Image
bg=ImageTk.PhotoImage(Image.open("cafe-bg1.jpg"))
#Creating a Label for the background image
bgimage=Label(root, image=bg).place(x=0,y=0, relwidth=1, relheight=1)
global sign_up_image
sign_up_image=ImageTk.PhotoImage(Image.open("cant.jpeg"))
global forgot_image
forgot_image=ImageTk.PhotoImage(Image.open("forgot.jpeg"))
global logged_in_image
logged_in_image=ImageTk.PhotoImage(Image.open("logged_in.jpg").resize((4325,5800),
Image.ANTIALIAS))
global cart_image
cart_image=ImageTk.PhotoImage(Image.open("coffee.png"))
#--------Menu Items-------------------
#---Creating Global Variables storing Image Information---
global aloo_sabji_pic
aloo_sabji_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\aloo
sabji.png").resize((125,125), Image.ANTIALIAS))
global butter_chicken_pic
butter_chicken_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\butter
chicken.png").resize((125,125), Image.ANTIALIAS))
global dal_fry_pic
dal_fry_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\dal
fry.png").resize((125,125), Image.ANTIALIAS))
global vada_pic
vada_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\vada.png").resize((125,125),
Image.ANTIALIAS))
global dosa_pic
dosa_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\dosa.png").resize((125,125), Image.ANTIALIAS))
global idli_pic
idli_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\idli.png").resize((125,125), Image.ANTIALIAS))
global mushroom_chilli_pic
mushroom_chilli_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\mushroom
chilli.png").resize((125,125), Image.ANTIALIAS))
global paneer_butter_masala_pic
paneer_butter_masala_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\paneer
butter masala.png").resize((125,125), Image.ANTIALIAS))
global pepper_chicken_pic
pepper_chicken_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\pepper
chicken.png").resize((125,125), Image.ANTIALIAS))
global roti_pic
roti_pic=ImageTk.PhotoImage(Image.open("Menu\\Breakfast\\roti.png").resize((125,125),Image.ANTIALIAS))
global chicken_biriyani_pic
chicken_biriyani_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\chicken
biriyani.png").resize((125,125), Image.ANTIALIAS))
global chicken_fry_pic
chicken_fry_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\chicken
fry.png").resize((125,125), Image.ANTIALIAS))
global coin_parotta_pic
coin_parotta_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\coin
parotta.png").resize((125,125), Image.ANTIALIAS))
global egg_fried_rice_pic
egg_fried_rice_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\egg fried
rice.png").resize((125,125), Image.ANTIALIAS))
global kichdi_pic
kichdi_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\kichdi.png").resize((125,125), Image.ANTIALIAS))
global meal_pic
meal_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\meal.png").resize((125,125),Image.ANTIALIAS))
global veg_fried_rice_pic
veg_fried_rice_pic=ImageTk.PhotoImage(Image.open("Menu\\Lunch\\veg fried
rice.png").resize((125,125), Image.ANTIALIAS))
global chicken_burger_pic
chicken_burger_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\chicken
burger.png").resize((125,125), Image.ANTIALIAS))
global chicken_puff_pic
chicken_puff_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\chicken
puff.jpg").resize((125,125), Image.ANTIALIAS))
global chocolate_donut_pic
chocolate_donut_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\chocolate
donut.jpg").resize((125,125), Image.ANTIALIAS))
global egg_puff_pic
egg_puff_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\egg
puff.jpg").resize((125,125), Image.ANTIALIAS))
global gulab_jamun_pic
gulab_jamun_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\gulab
jamun.png").resize((125,125), Image.ANTIALIAS))
global kulfi_pic
kulfi_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\kulfi.jpg").resize((125,125), Image.ANTIALIAS))
global paneer_puff_pic
paneer_puff_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\paneer
puff.png").resize((125,125), Image.ANTIALIAS))
global samosa_pic
samosa_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\samosa.jpg").resize((125,125), Image.ANTIALIAS))
global vada_pav_pic
vada_pav_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\vada
pav.png").resize((125,125), Image.ANTIALIAS))
global veg_burger_pic
veg_burger_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\veg
burger.jpg").resize((125,125), Image.ANTIALIAS))
global veg_puff_pic
veg_puff_pic=ImageTk.PhotoImage(Image.open("Menu\\Snacks\\veg
puff.png").resize((125,125), Image.ANTIALIAS))
global coco_cola_pic
coco_cola_pic=ImageTk.PhotoImage(Image.open("Menu\\Drinks\\coco
cola.jpg").resize((125,125), Image.ANTIALIAS))
global coffee_pic
coffee_pic=ImageTk.PhotoImage(Image.open("Menu\\Drinks\\coffee.jpg").resize((125,125), Image.ANTIALIAS))
global cold_coffee_pic
cold_coffee_pic=ImageTk.PhotoImage(Image.open("Menu\\Drinks\\cold
coffee.jpg").resize((125,125), Image.ANTIALIAS))
global mirinda_pic
mirinda_pic=ImageTk.PhotoImage(Image.open("Menu\\Drinks\\mirinda.png").resize((125,125), Image.ANTIALIAS))
global sprite_pic
sprite_pic=ImageTk.PhotoImage(Image.open("Menu\\Drinks\\sprite.jpg").resize((125,125), Image.ANTIALIAS))
global tea_pic
tea_pic=ImageTk.PhotoImage(Image.open("Menu\\Drinks\\tea.jpg").resize((125,125), Image.ANTIALIAS))
#----------Login Function------------
def Login():
#---------All errors------------
check=1 #Variable to check if entries are filled
exist=False #Variable to check if user exists
if Username_Login.get()=="" or Password_Login.get()=="": #If entries are empty
messagebox.showerror("Enter Details", "Enter both your username and password")
check=0
mycursor.execute("Select user from students")
for names in mycursor:
if names[0]==Username_Login.get(): #names is a tuple
exist=True #User exists
if exist==False and check==1:
messagebox.showerror("User does not exist", "Username does not exist. Check the
username again or sign up for a new account")
mycursor.execute("Select password from students where
user='"+Username_Login.get()+"'") #Obtaining the password of the respective
username
password_database= mycursor.fetchone()
if exist==True and password_database[0]!=Password_Login.get():
messagebox.showerror("Password entered is wrong", "The password that you
entered does not match the username")
elif exist==True and password_database[0]==Password_Login.get():
#Resetting the entries and hiding the main page for later use
global uname
uname=Username_Login.get()
Username_Login.delete(0,END)
Password_Login.delete(0,END)
login_frame.place_forget()
introimage.place_forget()
#---------Adding a Scroll Bar---------
main_frame=Frame(root)
main_frame.pack(fill=BOTH, expand=1)
mycanvas=Canvas(main_frame)
mycanvas.place(x=0, y=0, relwidth=1, relheight=1)
myscrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,
command=mycanvas.yview)
myscrollbar.place(x=width-15, y=0, relheight=1, width=15)
mycanvas.configure(yscrollcommand=myscrollbar.set)
mycanvas.bind('<Configure>', lambda e:
mycanvas.configure(scrollregion=mycanvas.bbox("all")))
second_frame=Frame(mycanvas, bd=0, bg="white")
mycanvas.create_window(((width/2)+425, 76), window=second_frame,
anchor="nw", height=5600)
#Allowing the use of mouse scroll for the scrollbar
def _on_mousewheel(event):
mycanvas.yview_scroll(int(-1*(event.delta/120)), "units")
mycanvas.bind_all('<MouseWheel>', _on_mousewheel)
global itemscost #List storing the cost of each individual item in the cart
itemscost=[]
global itemsname #List storing the name of each individual item in the cart
itemsname=[]
global itemsno #List storing the index position of each individual item in the cart
itemsno=[]
global piclist #List storing the image information of the items in the cart
piclist=[]
def Add_to_Cart(No_of_items, Item_Name, cost, pic):
i=len(itemsname)
exist=0 #Variable to check if item is already present in cart
if (No_of_items==""):
messagebox.showerror("No Items to Add", "Type in how many %ss you
would like to add to the cart above the Add to Cart Button" %Item_Name)
else: #Adding the items to cart
No_of_items=int(No_of_items)
for r in range(i):
if itemsname[r]==Item_Name and No_of_items!=0: #Checking if item
already exists in cart
incart=itemsno[r]
itemsno[r]=incart+No_of_items
exist=1
messagebox.showinfo("Item added to Cart", "%d %s was added to the
cart" % (No_of_items, Item_Name))
if exist==0 and i==3:
messagebox.showerror("Cannot add more than 3 dishes to cart in 1 order",
"In an initiative to reduce obesity in students, we do not allow users to order
more than 3 dishes at once. If you have are hosting a party, then please do
contact the canteen staff 2 days earlier at 9468237889")
elif exist==0 and i!=3:
itemsname.append(Item_Name)
itemsno.append(No_of_items)
itemscost.append(cost)
piclist.append(pic)
messagebox.showinfo("Item added to Cart", "%d %s was added to the cart"
% (No_of_items, Item_Name))
def Back_to_Menu():
Cart.place_forget() #Hiding the Cart Page for later use
main_frame.pack(fill=BOTH, expand=1)
def Logout():
main_frame.pack_forget() #Hiding the Menu Page for later use
Your_Cart_exists=True
#Checking if user created cart page
try:
Your_Cart
except NameError:
Your_Cart_exists=FALSE
if Your_Cart_exists:
Cart.place_forget() #Hiding the Cart Page for later use
#Going back to the main page
login_frame.place(x=200, y=225, height=350, width=400)
introimage.place(x=750, y=275)
def Confirm_Order():
Confirm=Toplevel(root, bg="white")
Confirm.geometry("+500+275")
def Confirm_final():
messagebox.showinfo("Thank you for placing the order", "Your order will be
ready at %s %s on %s" %(Time.get(), am_pm.get(), Date.get()))
for i in range(0, length):
mycursor.execute("Insert into orders values ('%s', '%s', '%s', '%s', '%s', '%s',
%d,%d, %d)" %(uname, Date.get(), Time.get(), piclist[i], "Accepted",
itemsname[i], itemscost[i], itemsno[i], itemscost[i]*itemsno[i]))
mydb.commit()
itemsno=[]
itemsname=[]
itemscost=[]
piclist=[]
Confirm.destroy()
Label(Confirm, text="Make sure the date is in DD/MM/YYYY format",
bg="white").grid(row=0, column=0, columnspan=3)
Label(Confirm, text="Once entered the date and time cannot be changed",
bg="white").grid(row=1, column=0, columnspan=3)
Label(Confirm, text="Timing: ", bg="white").grid(row=3, column=0)
Label(Confirm, text="Date: ", bg="white").grid(row=4, column=0)
Time=Entry(Confirm, width=15)
Time.grid(row=3, column=1)
am_pm=StringVar()
OptionMenu(Confirm, am_pm, "AM", "PM").grid(row=3, column=2)
am_pm.set("AM")
Date=Entry(Confirm, width=25)
Date.grid(row=4, column=1, columnspan=2)
Button(Confirm, text="Confirm", command=Confirm_final,
bg="white").grid(row=5, column=1)
def Go_to_Cart():
main_frame.pack_forget() #Hiding the Menu Page for later use
global Cart
Cart=Frame(root)
Cart.place(x=0,y=0, relheight=1, relwidth=1)
global First
def Delete_Dish(position):
itemsname.pop(position)
itemscost.pop(position)
itemsno.pop(position)
piclist.pop(position)
Cart.destroy()
Go_to_Cart()
Label(Cart, image=cart_image).place(x=0, y=0)
First=Frame(Cart, bg="white")
First.place(x=(width/2)-625, y=(height/2)-325, width=1250, height=650)
global Your_Cart #This has been made global for the login function to know if
the Go_to_Cart function has been called
Your_Cart=Label(First, text="Your Cart", font=Helv50,
bg="white").place(x=475, y=0)
Button(First, bg="orange", fg="purple", text="← Go Back to Menu",
font=Font(size=14), command=Back_to_Menu, anchor=W,
height=2).place(y=0, x=0)
Logout_Button=Button(First, text="Logout", command=Logout,
font=Font(size=14))
Logout_Button.place(x=1175, y=0)
global length
length=len(itemsname) #Variable storing the number of items in the cart
if length==0:
Label(First, text="There are no items in your cart, go back to the menu and
add some items", font=Times26, anchor=W, bg="white").place(x=(width/2)-
550, y=325)
else:
global total_amt #Variable storing the total amount
total_amt=0
amount=0
for item in range(0,length):
amount=itemsno[item]*itemscost[item]
image_cart=Label(First, image=piclist[item])
image_cart.place(x=75, y=(135*item)+100, anchor=NW)
name_cart=Label(First, text=itemsname[item], bg="white", font=Times23,
anchor=CENTER, width=150)
name_cart.place(x=350, y=135*(item+1))
quantity_cart=Label(First, text=str(itemsno[item]), bg="white",
font=Times23)
quantity_cart.place(x=550, y=135*(item+1))
cost_cart=Label(First, text="₹ " + str(itemscost[item]), bg="white",
font=Times23)
cost_cart.place(x=750, y=135*(item+1))
amount_cart=Label(First, text="₹ " + str(amount), bg="white",
font=Times23)
amount_cart.place(x=950, y=135*(item+1))
if item==0:
Button(First, text="Delete", command=lambda:
Delete_Dish(0)).place(x=1150, y=135)
elif item==1:
Button(First, text="Delete", command=lambda:
Delete_Dish(1)).place(x=1150, y=270)
elif item==2:
Button(First, text="Delete", command=lambda:
Delete_Dish(2)).place(x=1150, y=405)
total_amt+=amount
Subtotal_cart=Label(First, text="Total\t =\t₹" + str(total_amt), bg="white",
font=Times23).place(x=850, y=475)
Place_Order_Button=Button(First, command=Confirm_Order, text="Place
Order", bg='#E74C3C', fg="white", font=Times26).place(x=550, y=525)
Terms=Label(First, text="(Once placed, the order cannot be cancelled)",
font=Times20, bg="white",).place(x=475, y=600)
#---------------Displaying the menu----------------------
Logout_Button=Button(second_frame, text="Logout", command=Logout,
font=Font(size=14))
Logout_Button.pack(pady=50)
mycanvas.create_image(-1800,0, image=logged_in_image, anchor=NW)
mycanvas.create_rectangle((width/2)-625, 75, (width/2)+625, 5700, fill="white")
mycanvas.create_text((width/2)-50, 35, text="Menu", font=Font(family="Times
New Roman", size=50, weight="bold"), fill="white")
mycanvas.create_text((width/2)-550, 175, text="Breakfast", anchor=W,
font=Helv50)
mycanvas.create_image((width/2)-550, 230, image=idli_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 230, text="Idli - ₹30", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 275, text="A set of two soft and fluffy steamed
rice cakes with a mild spiced sambar and coconut chutney", anchor=NW,
font=Times20, width=700)
idliframe=Frame(second_frame, bg="white")
idliframe.pack(pady=33)
idlinos=Entry(idliframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
idlinos.grid(row=0, column=0)
Button(idliframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(idlinos.get(),"Idli", 30, idli_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 380, image=dosa_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 380, text="Masala Dosa - ₹60 ", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 425, text="A thin and crispy rice pancake with
potato fillings, a mild spiced sambar and coconut chutney", anchor=NW,
font=Times20, width=700)
dosaframe=Frame(second_frame, bg="white")
dosaframe.pack(pady=33)
dosanos=Entry(dosaframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
dosanos.grid(row=0, column=0)
Button(dosaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(dosanos.get(), "Masala Dosa", 60, dosa_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 530, image=vada_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 530, text="Vada - ₹20", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 575, text="A doughnut shaped fritter made of
black lentils", anchor=NW, font=Times20,
width=700)
vadaframe=Frame(second_frame, bg="white")
vadaframe.pack(pady=33)
vadanos=Entry(vadaframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
vadanos.grid(row=0, column=0)
Button(vadaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(vadanos.get(), "Vada", 20, vada_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 680, image=roti_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 680, text="Roti - ₹30", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 725, text="A set of two unleavened flat breads
made of wheat flour", anchor=NW, font=Times20, width=700)
rotiframe=Frame(second_frame, bg="white")
rotiframe.pack(pady=33)
rotinos=Entry(rotiframe, bg="white", fg="black", width=7, justify=CENTER, =
relief=GROOVE)
rotinos.grid(row=0, column=0)
Button(rotiframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(rotinos.get(), "Roti", 30, roti_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 830, image=aloo_sabji_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 830, text="Aloo sabji- ₹40", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 875, text="A traditional Indian dish of stir-
fried, seasoned potatoes", anchor=NW, font=Times20, width=700)
asabjiframe=Frame(second_frame, bg="white")
asabjiframe.pack(pady=33)
asabjinos=Entry(asabjiframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
asabjinos.grid(row=0, column=0)
Button(asabjiframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(asabjinos.get(), "Aloo sabji", 40, aloo_sabji_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 980, image=mushroom_chilli_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 980, text="Mushroom chilli - ₹50",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 1025, text="Crunchy deep fried mushrooms
sautéed with spicy green chillies, pungent onions and a medley of tongue-licking
sauces", anchor=NW, font=Times20, width=700)
mchilliframe=Frame(second_frame, bg="white")
mchilliframe.pack(pady=33)
mchillinos=Entry(mchilliframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
mchillinos.grid(row=0, column=0)
Button(mchilliframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(mchillinos.get(), "Mushroom Chilli", 50,
mushroom_chilli_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 1130, image=paneer_butter_masala_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 1130, text="Paneer Butter Masala - ₹60",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 1175, text="A rich & creamy curry made with
paneer, spices, onions, tomatoes, cashews and butter", anchor=NW, font=Times20,
width=700)
pbmasalaframe=Frame(second_frame, bg="white")
pbmasalaframe.pack(pady=33)
pbmasalanos=Entry(pbmasalaframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
idlinos.grid(row=0, column=0)
Button(pbmasalaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(pbmasalanos.get(), "Paneer Butter Masala", 60,
paneer_butter_masala_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 1280, image=pepper_chicken_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 1280, text="Pepper chicken - ₹80",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 1325, text="Lip-smacking peppery chicken in
a thick spicy gravy of onion, grated coconut and buttermilk", anchor=NW,
font=Times20, width=700)
pchickenframe=Frame(second_frame, bg="white")
pchickenframe.pack(pady=33)
pchickennos=Entry(pchickenframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
pchickennos.grid(row=0, column=0)
Button(pchickenframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(pchickennos.get(), "Pepper Chicken", 80,
pepper_chicken_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 1430, image=butter_chicken_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 1430, text="Butter chicken - ₹90",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 1475, text="Chunks of grilled
chicken(tandoori chicken) cooked in a smooth buttery & creamy tomato based
gravy", anchor=NW,
font=Times20, width=700)
bchickenframe=Frame(second_frame, bg="white")
bchickenframe.pack(pady=33)
bchickennos=Entry(bchickenframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
bchickennos.grid(row=0, column=0)
Button(bchickenframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(bchickennos.get(), "Butter Chicken", 90,
butter_chicken_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 1580, image=dal_fry_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 1580, text="Dal Fry - ₹70", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 1625, text="Delicious, creamy yellow lentils
which is mildly spiced and slightly tangy to taste cooked in a tomato-onion base",
anchor=NW, font=Times20, width=700)
dalframe=Frame(second_frame, bg="white")
dalframe.pack(pady=33)
dalnos=Entry(dalframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
dalnos.grid(row=0, column=0)
Button(dalframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(dalnos.get(), "Dal Fry", 70, dal_fry_pic)).grid(row=1, column=0)
mycanvas.create_text((width/2)-550, 1775, text="Lunch", anchor=W,
font=('Georgia', '50', 'bold'))
Frame(second_frame).pack(pady=50)
mycanvas.create_image((width/2)-550, 1830, image=meal_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 1830, text="Meal - ₹100", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 1875, text="A typical meal with 4 different
curries, a sweet kheer, some rice and a chapati", anchor=NW, font=Times20,
width=700)
mealframe=Frame(second_frame, bg="white")
mealframe.pack(pady=33)
mealnos=Entry(mealframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
mealnos.grid(row=0, column=0)
Button(mealframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(mealnos.get(), "Meal", 100, meal_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 1980, image=chicken_biriyani_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 1980, text="Chicken Biriyani - ₹120",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 2025, text="A savory chicken and rice dish
that includes layers of chicken, rice, and aromatics that are steamed together",
anchor=NW, font=Times20, width=700)
cbiriyaniframe=Frame(second_frame, bg="white")
cbiriyaniframe.pack(pady=33)
cbiriyaninos=Entry(cbiriyaniframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
cbiriyaninos.grid(row=0, column=0)
Button(cbiriyaniframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(cbiriyaninos.get(), "Chicken Biriyani", 120,
chicken_biriyani_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 2130, image=coin_parotta_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 2130, text="Coin Parotta - ₹40",
anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 2175, text="A set of 3 small, round, flaky,
layered breads made of refined wheat flour or maida", anchor=NW, font=Times20,
width=700)
cparottaframe=Frame(second_frame, bg="white")
cparottaframe.pack(pady=33)
cparottanos=Entry(cparottaframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
cparottanos.grid(row=0, column=0)
Button(cparottaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(cparottanos.get(), "Coin Parotta", 40, coin_parotta_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 2280, image=egg_fried_rice_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 2280, text="Egg Fried Rice - ₹110",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 2325, text="A dish of cooked rice stir-fried
mixed with scrambled eggs and vegetables,", anchor=NW, font=Times20,
width=700)
efriceframe=Frame(second_frame, bg="white")
efriceframe.pack(pady=33)
efricenos=Entry(efriceframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
efricenos.grid(row=0, column=0)
Button(efriceframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(efricenos.get(), "Egg Fried Rice", 110,
egg_fried_rice_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 2430, image=kichdi_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 2430, text="Kichdi - ₹40", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 2475, text="A mild spicy mixture of rice and
lentils served steamingly hot", anchor=NW, font=Times20, width=700)
kichdiframe=Frame(second_frame, bg="white")
kichdiframe.pack(pady=33)
kichdinos=Entry(kichdiframe, bg="white", fg="black", width=7,
justify=CENTER,
relief=GROOVE)
kichdinos.grid(row=0, column=0)
Button(kichdiframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(kichdinos.get(), "Kichdi", 40, kichdi_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 2580, image=veg_fried_rice_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 2580, text="Veg Fried Rice - ₹100",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 2625, text="A dish of cooked rice stir fried
mixed with vegetables", anchor=NW, font=Times20, width=700)
vfriceframe=Frame(second_frame, bg="white")
vfriceframe.pack(pady=33)
vfricenos=Entry(vfriceframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
vfricenos.grid(row=0, column=0)
Button(vfriceframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda: ‘
Add_to_Cart(vfricenos.get(), "Veg Fried Rice", 100,
veg_fried_rice_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 2730, image=chicken_fry_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 2730, text="Chicken Fry - ₹70",
anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 2775, text="Half plate of juicy chicken pieces
coated in seasoned batter and deep fried", anchor=NW, font=Times20, width=700)
cfryframe=Frame(second_frame, bg="white")
cfryframe.pack(pady=33)
cfrynos=Entry(cfryframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
cfrynos.grid(row=0, column=0)
Button(cfryframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(cfrynos.get(), "Chicken Fry", 70, chicken_fry_pic)).grid(row=1,
column=0)
mycanvas.create_text((width/2)-550, 2925, text="Snacks", anchor=W,
font=('Times', '50', 'bold'))
Frame(second_frame).pack(pady=50)
mycanvas.create_image((width/2)-550, 2980, image=chicken_burger_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 2980, text="Chicken burger - ₹60",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 3025, text="Tender and juicy chicken patty
cooked to perfection, with creamy mayonnaise and crunchy lettuce packed into
toasted sesame buns", anchor=NW, font=Times20, width=700)
cburgerframe=Frame(second_frame, bg="white")
cburgerframe.pack(pady=33)
cburgernos=Entry(cburgerframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
cburgernos.grid(row=0, column=0)
Button(cburgerframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(cburgernos.get(), "Chicken Burger", 60,
chicken_burger_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 3130, image=chicken_puff_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 3130, text="Chicken Puff - ₹25",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 3175, text="Crispy, flakey puffs filled with
curry-flavored chicken", anchor=NW, font=Times20, width=700)
cpuffframe=Frame(second_frame, bg="white")
cpuffframe.pack(pady=33)
cpuffnos=Entry(cpuffframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
cpuffnos.grid(row=0, column=0)
Button(cpuffframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(cpuffnos.get(), "Chicken Puff", 25, chicken_puff_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 3280, image=veg_puff_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 3280, text="Veg puff - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 3325, text="Vegetables cooked in a spicy
masala gravy, and wrapped in flaky puff pastry", anchor=NW, font=Times20,
width=700)
vpuffframe=Frame(second_frame, bg="white")
vpuffframe.pack(pady=33)
vpuffnos=Entry(vpuffframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
vpuffnos.grid(row=0, column=0)
Button(vpuffframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(vpuffnos.get(), "Veg Puff", 15, veg_puff_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 3430, image=egg_puff_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 3430, text="Egg Puff - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 3475, text="Crispy, flakey puffs filled with a
whole boiled egg and some sautéed onions and spices", anchor=NW,
font=Times20,
width=700)
eggframe=Frame(second_frame, bg="white")
eggframe.pack(pady=33)
eggnos=Entry(eggframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
eggnos.grid(row=0, column=0)
Button(eggframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(eggnos.get(), "Egg Puff", 15, egg_puff_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 3580, image=paneer_puff_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 3580, text="Paneer Puff - ₹25", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 3625, text="Paneer cooked in spicy masala
gravy, and wrapped in flaky puff pastry", anchor=NW, font=Times20, width=700)
ppuffframe=Frame(second_frame, bg="white")
ppuffframe.pack(pady=33)
ppuffnos=Entry(ppuffframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
ppuffnos.grid(row=0, column=0)
Button(ppuffframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(ppuffnos.get(), "Paneer Puff", 25, paneer_puff_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 3730, image=samosa_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 3730, text="Samosa - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 3775, text="A crispy and spicy deep fried
snack that has a crisp and flaky outer layer made of maida and rich fillings of mashed
potato, peas and spices", anchor=NW, font=Times20, width=700)
samosaframe=Frame(second_frame, bg="white")
samosaframe.pack(pady=33)
samosanos=Entry(samosaframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
samosanos.grid(row=0, column=0)
Button(samosaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(samosanos.get(), "Samosa", 15, samosa_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 3880, image=vada_pav_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 3880, text="Vada Pav - ₹30", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 3925, text="A deep fried potato dumpling
placed inside a bread bun(pav)", anchor=NW, font=Times20, width=700)
vpavframe=Frame(second_frame, bg="white")
vpavframe.pack(pady=33)
vpavnos=Entry(vpavframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
vpavnos.grid(row=0, column=0)
Button(vpavframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(vpavnos.get(), "Vada Pav", 30, vada_pav_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 4030, image=veg_burger_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 4030, text="Veg Burger - ₹50", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 4075, text="A patty filled with potatoes, peas,
carrots and tasty Indian spices. Topped with crispy lettuce, mayonnaise, and packed
into toasted sesame buns", anchor=NW, font=Times20, width=700)
vburgerframe=Frame(second_frame, bg="white")
vburgerframe.pack(pady=33)
vburgernos=Entry(vburgerframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
vburgernos.grid(row=0, column=0)
Button(vburgerframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(vburgernos.get(), "Veg Burger", 50, veg_burger_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 4180, image=chocolate_donut_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 4180, text="Chocolate Donut - ₹25",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 4225, text="Moist and fluffy donuts baked and
covered in thick chocolate glaze", anchor=NW, font=Times20, width=700)
donutframe=Frame(second_frame, bg="white")
donutframe.pack(pady=33)
donutnos=Entry(donutframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
idlinos.grid(row=0, column=0)
Button(donutframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(idlinos.get(), "Chocolate Donut", 25,
chocolate_donut_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 4330, image=gulab_jamun_pic,
anchor=NW)
mycanvas.create_text((width/2)-350, 4330, text="Gulab Jamun - ₹10",
anchor=NW, font=Times26)
mycanvas.create_text((width/2)-360, 4375, text="Soft delicious berry sized balls
made of milk solids, flour & a leavening agent soaked in sugar syrup", anchor=NW,
font=Times20, width=700)
jamunframe=Frame(second_frame, bg="white")
jamunframe.pack(pady=33)
jamunnos=Entry(jamunframe, bg="white", fg="black", width=7,justify=CENTER,
relief=GROOVE)
jamunnos.grid(row=0, column=0)
Button(jamunframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(jamunnos.get(), "Gulab Jamun", 10, gulab_jamun_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 4480, image=kulfi_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 4480, text="Kulfi - ₹20", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 4525, text="A dessert made by slow boiling
sweetned milk", anchor=NW, font=Times20, width=700)
kulfiframe=Frame(second_frame, bg="white")
kulfiframe.pack(pady=33)
kulfinos=Entry(kulfiframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
kulfinos.grid(row=0, column=0)
Button(kulfiframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(kulfinos.get(), "Kulfi", 20, kulfi_pic)).grid(row=1, column=0)
mycanvas.create_text((width/2)-550, 4675, text="Drinks", anchor=W,
font=('Times', '50', 'bold'))
Frame(second_frame).pack(pady=50)
mycanvas.create_image((width/2)-550, 4730, image=tea_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 4730, text="Tea - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 4775, text="A popular bevarage with milk for
all those tea lovers", anchor=NW, font=Times20, width=700)
teaframe=Frame(second_frame, bg="white")
teaframe.pack(pady=33)
teanos=Entry(teaframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
teanos.grid(row=0, column=0)
Button(teaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(teanos.get(), "Tea", 15, tea_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 4880, image=coffee_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 4880, text="Coffee - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 4925, text="A bevarage consisting of espresso,
steamed milk, and milk foam", anchor=NW, font=Times20, width=700)
coffeeframe=Frame(second_frame, bg="white")
coffeeframe.pack(pady=33)
coffeenos=Entry(coffeeframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
coffeenos.grid(row=0, column=0)
Button(coffeeframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(coffeenos.get(), "Coffee", 15, coffee_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 5030, image=cold_coffee_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 5030, text="Cold Coffee - ₹50",
anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 5075, text="Merge two amazing things, coffee
and cold drinks and what you get is this amazingly refreshing and tasty drink",
anchor=NW, font=Times20, width=700)
ccoffeeframe=Frame(second_frame, bg="white")
ccoffeeframe.pack(pady=33)
ccoffeenos=Entry(ccoffeeframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
ccoffeenos.grid(row=0, column=0)
Button(ccoffeeframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(ccoffeenos.get(), "Cold Coffee", 50, cold_coffee_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 5180, image=mirinda_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 5180, text="Mirinda - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 5225, text="A glass of cold and refreshing
Mirinda", anchor=NW, font=Times20, width=700)
mirindaframe=Frame(second_frame, bg="white")
mirindaframe.pack(pady=33)
mirindanos=Entry(mirindaframe, bg="white", fg="black", width=7,
justify=CENTER, relief=GROOVE)
mirindanos.grid(row=0, column=0)
Button(mirindaframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(mirindanos.get(), "Mirinda", 15, mirinda_pic)).grid(row=1,
column=0)
mycanvas.create_image((width/2)-550, 5330, image=sprite_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 5330, text="Sprite - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 5375, text="A glass of cold and refreshing
Sprite", anchor=NW, font=Times20, width=700)
spriteframe=Frame(second_frame, bg="white")
spriteframe.pack(pady=33)
spritenos=Entry(spriteframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
spritenos.grid(row=0, column=0)
Button(spriteframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(spritenos.get(), "Sprite", 15, sprite_pic)).grid(row=1, column=0)
mycanvas.create_image((width/2)-550, 5480, image=coco_cola_pic, anchor=NW)
mycanvas.create_text((width/2)-350, 5480, text="Coca Cola - ₹15", anchor=NW,
font=Times26)
mycanvas.create_text((width/2)-360, 5525, text="A glass of cold and refreshing
Coca Cola", anchor=NW, font=Times20, width=700)
cokeframe=Frame(second_frame, bg="white")
cokeframe.pack(pady=33)
cokenos=Entry(cokeframe, bg="white", fg="black", width=7, justify=CENTER,
relief=GROOVE)
cokenos.grid(row=0, column=0)
Button(cokeframe, text="Add to Cart", bg="orange", fg="purple",
font=Font(weight="bold"), height=2, width=10, command=lambda:
Add_to_Cart(cokenos.get(), "Coco Cola", 15, coco_cola_pic)).grid(row=1,
column=0)
Button(mycanvas, text="Go to Cart", fg="white", bg="#E74C3C",
font=Font(family="Times", size=20, slant="italic", weight="bold"),
command=Go_to_Cart).grid(row=0, column=0, padx=600, pady=700, ipadx=50,
ipady=10)
#----------Forgot Password Function-----------
def ForgotPassword():
Forgot=Toplevel(root)
Forgot.title("Forgot Password")
fwidth=(width/2)-450
Forgot.geometry("900x550+%d+100" % fwidth)
Forgot.resizable(False, False)
def Forgot_Password():
mycursor.execute("select student_id, user, phone_number from students")
check=0 #Variable to verify if all the details entered are matching
for rows in mycursor:
if rows[0]==int(School_ID.get()):
check=1
if rows[2]==Phone_Number.get():
check=2
if rows[1]==Username.get():
check=3
if Username.get()=="" or Phone_Number.get()=="" or Password.get()=="" or
Confirm_Password.get()=="" or School_ID.get()=="": #validating entries
messagebox.showerror("Enter all data", "You have not typed in the information
requested in 1 or more fields", parent=Forgot)
elif check==0:
messagebox.showerror("School ID not registered","Please do consider signing up
because your school ID is not registered with us", parent=Forgot)
elif check==1:
messagebox.showerror("Phone Number not registered","Please do enter your
registered phone number. If you have changed your number, consult with your
Cyber safety leader", parent=Forgot)
elif check==2:
messagebox.showerror("Username entered is wrong", "The username that you
entered is wrong. If you have forgotten your username, consult your Cyber safety
leader", parent=Forgot)
elif Password.get()!=Confirm_Password.get() and check==3:
messagebox.showerror("The Passwords do not match", "The passwords that you
entered in confirm password and password fields do not match", parent=Forgot)
elif check==3: #Updating the password of the corresponding user
mycursor.execute("update students set password='" + Password.get() +"'" +
"where user='"+Username.get()+"'")
success=Label(Forgot_frame, text="Password Resetted successfully").place(x=50,
y=450)
mydb.commit()
Label(Forgot, image=forgot_image).place(x=0,y=0, relwidth=1, relheight=1)
Forgot_frame=Frame(Forgot, bg="white")
Forgot_frame.place(x=50, y=50, height=475, width=400)
Label(Forgot_frame,text="Forgot Password", font=("Times New Roman",32, "bold"),
bg="white").place(x=25, y=10) #Sign up Label
Label(Forgot_frame, text="Registered Username:", bg="white").place(x=25, y=90)
#Username Label
Username=Entry(Forgot_frame, bg="lightgrey")
Username.place(x=25, y=110, width=300, height=30) #Username Entry Box
Label(Forgot_frame, text="Registered Phone Number:", bg="white").place(x=25,
y=145) #Phone Number Label
Phone_Number=Entry(Forgot_frame, bg="lightgrey")
Phone_Number.place(x=25, y=165, width=300, height=30) #Phone Number Entry
Label(Forgot_frame, text="School ID:", bg="white").place(x=25, y=200) #School ID
School_ID=Entry(Forgot_frame, bg="lightgrey")
School_ID.place(x=25, y=220, width=300, height=30) #School ID Entry Box
Label(Forgot_frame, text="New Password:", bg="white").place(x=25, y=255)
#Password Label
Password=Entry(Forgot_frame, bg="lightgrey")
Password.place(x=25, y=275, width=300, height=30) #Password Entry Box
Label(Forgot_frame, text="Confirm Password:", bg="white").place(x=25, y=310)
#Confirm Password Label
Confirm_Password=Entry(Forgot_frame, bg="lightgrey")
Confirm_Password.place(x=25, y=330, height=30, width=300)
Button(Forgot_frame, text="Reset Password", font=("Times New Roman", 18),
bg="white", command=Forgot_Password).place(x=50, y=390, width=250, height=40)
#Sign Up Button
#----------Sign Up Window function------------
def SignUpWin():
Sign=Toplevel(root)
Sign.title("SignUp")
swidth=(width/2)-625
sheight=(height/2)-350
Sign.geometry("1250x700+%d+%d" %(swidth,sheight))
Sign.resizable(False, False)
#-----------Sign Up Function-----------------
def SignUp():
# ----All possible errors that could arise------
try:
check=0
if Username.get()=="" or Phone_Number.get()=="" or First_Name.get()==""
or Last_Name.get()=="" or Confirm_Password.get()=="" or
School_ID.get()=="":
#Checking if all entries are filled
messagebox.showerror("Enter all data", "You have not typed in the
information requested in 1 or more fields", parent=Sign)
check=1
#Checking if any details are a duplicate of another user
mycursor.execute("Select user, phone_number, student_id from students")
for rows in mycursor:
if rows[0]==Username.get():
check=1
messagebox.showerror("Username already exists", "The username that
you have entered already exists, enter another username", parent=Sign)
elif rows[1]==Phone_Number.get():
check=1
messagebox.showerror("Phone Number already exists", "The Phone
number that you provided already exists. Try logging in",
parent=Sign)
elif rows[2]==School_ID.get():
check=1
messagebox.showerror("School ID already exists", "The School ID that
you provided already exists. Try logging in", parent=Sign)
if Password.get()!=Confirm_Password.get() and check==0:
check=1
messagebox.showerror("The Passwords do not match", "The passwords that
you entered in confirm password and password fields do not match",
parent=Sign)
elif len(Phone_Number.get())!=10 and check==0:
check=1
messagebox.showerror("Phone Number incorrect", "Please do enter your
correct 10-digit Phone Number", parent=Sign)
elif len(School_ID.get())!=5 and check==0:
check=1
messagebox.showerror("School ID incorrect", "Please do enter your correct 5-
digit School ID", parent=Sign)
except ValueError:
messagebox.showerror("Enter proper data", "You have not entered the proper
datatype", parent=Sign)
try:
int(Phone_Number.get())
except ValueError:
messagebox.showerror("Phone number can only contain digits", "Phone Number
cannot contain any alphabets or special characters", parent=Sign)
check=1
try:
int(School_ID.get())
except ValueError:
messagebox.showerror("School ID can only contain digits", "School ID cannot
contain any alphabets or special characters", parent=Sign)
check=1
#--------Adding data to the database----------
if check==0:
mycursor.execute("insert into students values(%s, %s, %s, %s, %d, %s)"
%("'" + Username.get() + "'",
"'" + Password.get() + "'",
"'" + First_Name.get() + "'",
"'" + Last_Name.get() + "'",
int(School_ID.get()),
"'" + Phone_Number.get() + "'"))
mydb.commit()
success=Label(SignUp_frame, text="Account created successfully").place(x=50,
y=560)
#Resetting the entries
Username.delete(0,END)
Password.delete(0,END)
Confirm_Password.delete(0,END)
Phone_Number.delete(0,END)
School_ID.delete(0,END)
First_Name.delete(0, END)
Last_Name.delete(0, END)
Sign.destroy()
Label(Sign, image=sign_up_image).place(x=0,y=0, relwidth=1, relheight=1)
SignUp_frame=Frame(Sign, bg="white")
SignUp_frame.place(x=200, y=50, height=600, width=400)
Label(SignUp_frame,text="Sign Up", font=("Times New Roman",32, "bold"),
bg="white").place(x=50, y=10) #Sign up Label
#First Name Label
Label(SignUp_frame, text="First Name:", bg="white").place(x=25, y=90)
First_Name=Entry(SignUp_frame, bg="lightgrey")
First_Name.place(x=25, y=110, width=300, height=30) # First Name Entry box
Label(SignUp_frame, text="Last Name:", bg="white").place(x=25, y=145)
#Last Name Label
Last_Name=Entry(SignUp_frame, bg="lightgrey")
Last_Name.place(x=25, y=165, width=300, height=30) #Last Name Entry box
#Username Label
Label(SignUp_frame, text="Username:", bg="white").place(x=25, y=200)
Username=Entry(SignUp_frame, bg="lightgrey")
Username.place(x=25, y=220, width=300, height=30) #Username Entry Box
#Password Label
Label(SignUp_frame, text="Password:", bg="white").place(x=25, y=255)
Password=Entry(SignUp_frame, bg="lightgrey")
Password.place(x=25, y=275, width=300, height=30) #Password Entry Box
Label(SignUp_frame, text="Confirm Password:", bg="white").place(x=25, y=310)
#Confirm Password Label
Confirm_Password=Entry(SignUp_frame, bg="lightgrey")
Confirm_Password.place(x=25, y=330, width=300, height=30) #Confirm Password
Label(SignUp_frame, text="Phone Number:", bg="white").place(x=25, y=365)
#Phone Number Label
Phone_Number=Entry(SignUp_frame, bg="lightgrey")
Phone_Number.place(x=25, y=385, width=300, height=30) #Phone Number Entry
#School ID Label
Label(SignUp_frame, text="School ID:", bg="white").place(x=25, y=420)
School_ID=Entry(SignUp_frame, bg="lightgrey")
School_ID.place(x=25, y=440, width=300, height=30) #School ID Entry Box
Button(SignUp_frame, text="Sign Up", font=("Times New Roman", 20),
bg="white",
command=SignUp).place(x=100, y=500, width=150, height=50) #Sign Up Button
#----------"How we operate" pic---------
global introimage
intro=ImageTk.PhotoImage(Image.open("intro.png"))
introimage=Label(root, image=intro)
introimage.place(x=750, y=275)
#------Login Frame-------------------
global login_frame
login_frame=Frame(root, bg="white")
login_frame.place(x=200, y=225, height=350, width=400)
Label(login_frame,text="Student Login", font=("Times New Roman",32, "bold"),
bg="white").place(x=50, y=10)
Label(login_frame, text="Username:", bg="white").place(x=25, y=90)
global Username_Login
Username_Login=Entry(login_frame, bg="lightgrey")
Username_Login.place(x=25, y=110, width=300, height=30)
Label(login_frame, text="Password:", bg="white").place(x=25, y=150)
global Password_Login
Password_Login=Entry(login_frame, bg="lightgrey", show='*')
Password_Login.place(x=25, y=170, width=300, height=30)
Button(login_frame, text="Not registered? Sign Up here", font=("Times New Roman",
14), fg="blue", bg="white", bd=0, command=SignUpWin).place(x=25, y=200)
Button(login_frame, text="Forgot Password?", font=("Times New Roman", 14),
fg="blue", bd=0, bg="white", command=ForgotPassword).place(x=25, y=230)
Button(login_frame, text="Login", font=("Times New Roman", 20), fg="blue",
bg="white", command=Login).place(x=165, y=275)
root.mainloop()