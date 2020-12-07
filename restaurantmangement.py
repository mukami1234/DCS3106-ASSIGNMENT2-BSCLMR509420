from tkinter import*
import random
import time
import os
root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,bg="black",width = 1600,height=50,relief=SUNKEN )
Tops.pack(side=TOP)

f1 = Frame(root,bg='floral white',width = 900,height=700,relief=SUNKEN)
f1.pack()


#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Rose Wood hotel",fg="red",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="green",anchor=W)
lblinfo.grid(row=1,column=0)
#------------------------------------------------------------------------------------------------------------
rand = StringVar()
cname=StringVar()
PILAU = StringVar()
BRIYANI = StringVar()
UGALI = StringVar()
MANAGU = StringVar()
Subtotal = StringVar()
Total=StringVar()
Service_Charge = StringVar()
DRINKS = StringVar()
Tax = StringVar()
cost = StringVar()
BEEF = StringVar()
Billtot="0"
Billtot1=StringVar()


def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    #global Total
    x=random.randint(100, 999)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(PILAU.get())
    colPILAU= float(BRIYANI.get())
    cob= float(UGALI.get())
    cofi= float(MANAGU.get())
    cochee= float(BEEF.get())
    codr= float(DRINKS.get())

    costofPILAU = cof*25
    costofBRIYANI = colPILAU*40
    costofUGALI = cob*35
    costofMANAGU = cofi*50
    costofcheeseUGALI = cochee*50
    costofdrinks = codr*35

    costofmeal = "KSH.",str('%.2f'% (costofPILAU +  costofBRIYANI + costofUGALI + costofMANAGU + costofcheeseUGALI + costofdrinks))
    PayTax=((costofPILAU +  costofBRIYANI + costofUGALI + costofMANAGU +  costofcheeseUGALI + costofdrinks)*0.09)
    Totalcost=(costofPILAU +  costofBRIYANI + costofUGALI + costofMANAGU  + costofcheeseUGALI + costofdrinks)
    Ser_Charge=((costofPILAU +  costofBRIYANI + costofUGALI + costofMANAGU + costofcheeseUGALI + costofdrinks)/99)
    Service="KSH.",str('%.2f'% Ser_Charge)
    OverAllCost="KSH.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="KSH.",str('%.2f'% PayTax)
    Billtot= str(PayTax + Totalcost + Ser_Charge)
    Billtot1.set(Billtot)
    

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    qexit=messagebox.askyesno('Thank you','Do you wish to exit')
    if qexit>0:
        root.destroy()

def reset():
    rand.set(0)
    PILAU.set(0)
    BRIYANI.set(0)
    UGALI.set(0)
    MANAGU.set(0)
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    DRINKS.set(0)
    Tax.set("")
    cost.set("")
    BEEF.set(0)
  
def bill():
    global Total
    roo = Tk()
    
    Total1=0
    roo.geometry("600x220+0+0")
    roo.title("BILL")
    billlabel1=Label(roo, font=('aria',16,'bold'), text="Enter coustomer name", bg='floral white',fg="black",bd=10)
    billlabel1.grid(row=0,column=0)
    billentry1=Entry(roo,font=('ariel',16, 'bold'),textvariable=cname,bd=6,bg="powder blue")
    billentry1.grid(row=0,column=1)
    billlabel2=Label(roo,font=('ariel',16,'bold'),text="Bill of the coustomer is    KSH.",bg='floral white',fg="black",bd=10)
    billlabel2.grid(row=1,column=0)
    billentry2=Label(roo,font=('ariel',16,'bold'),text=Billtot,bd=6,bg="red",relief='sunken')
    billentry2.grid(row=1,column=1)
    def bill1():
        Total1= Billtot1.get()
        billentry2.configure(text=Total1)
    def bill2():
        file=open("bill.txt","w")
        file.write('*********Rose Wood Hotel**********\n')
        file.write('Order Id: %d\n'%int(rand.get()))
        file.write("Customer's Name: "+billentry1.get())
        file.write('\nTotal Bill: %.2f\n'%float(Billtot1.get()))
        file.write('*****Thank You for Your Visit*****')
        file.close()
        os.system('notepad.exe bill.txt')
        
        
        
        
    btnbill1=Button(roo,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="GENERATE BILL", bg="powder blue",command=bill1)
    btnbill1.grid(row=2, column=0)
    btnbill1=Button(roo,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRINT BILL", bg="powder blue",command=bill2)
    btnbill1.grid(row=2, column=1)

    

#---------------------------------------------------------------------------------------



lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",bg='floral white',fg="black",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblPILAU = Label(f1, font=( 'aria' ,16, 'bold' ),text="PILAU",bg='floral white',fg="black",bd=10,anchor='w')
lblPILAU.grid(row=1,column=0)
txtPILAU = Spinbox(f1,font=('ariel' ,16,'bold'), textvariable=PILAU , from_=0, to=20, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtPILAU.grid(row=1,column=1)

lblBRIYANI = Label(f1, font=( 'aria' ,16, 'bold' ),text="BRIYANI",bg='floral white',fg="black",bd=10,anchor='w')
lblBRIYANI.grid(row=2,column=0)
txtBRIYANI = Spinbox(f1,font=('ariel' ,16,'bold'), textvariable=BRIYANI ,from_=0, to=20, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBRIYANI.grid(row=2,column=1)


lblUGALI = Label(f1, font=( 'aria' ,16, 'bold' ),text="UGALI",bg='floral white',fg="black",bd=10,anchor='w')
lblUGALI.grid(row=3,column=0)
txtUGALI = Spinbox(f1,font=('ariel' ,16,'bold'), textvariable=UGALI ,from_=0, to=20, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtUGALI.grid(row=3,column=1)

lblMANAGU = Label(f1, font=( 'aria' ,16, 'bold' ),text="MANAGU",bg='floral white',fg="black",bd=10,anchor='w')
lblMANAGU.grid(row=4,column=0)
txtMANAGU = Spinbox(f1,font=('ariel' ,16,'bold'), textvariable=MANAGU ,from_=0, to=20, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtMANAGU.grid(row=4,column=1)

lblBEEF = Label(f1, font=( 'aria' ,16, 'bold' ),text="BEEF",bg='floral white',fg="black",bd=10,anchor='w')
lblBEEF.grid(row=5,column=0)
txtBEEF = Spinbox(f1,font=('ariel' ,16,'bold'), textvariable=BEEF ,from_=0, to=20, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBEEF.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="DRINKS",bg='floral white',fg="black",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Spinbox(f1,font=('ariel' ,16,'bold'), textvariable=DRINKS ,from_=0, to=20, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",bg='floral white',fg="black",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",bg='floral white',fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bg='floral white',bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",bg='floral white',fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",bg='floral white',fg="black",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)




#-----------------------------------------buttons------------------------------------------


btnbill=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="BILL", bg="powder blue",command=bill)
btnbill.grid(row=7, column=1)


btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=2)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=3)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=4)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PILAU", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BRIYANI", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="UGALI", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="MANAGU", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BEEF", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="DRINKS", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()

