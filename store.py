from PIL import Image,ImageTk
from tkinter import *
import PIL.Image
from tkinter import ttk
import random,os
from tkinter import messagebox
import tempfile
#import time

class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing software")

        #=========================variable=================================================================================
        self.c_name=StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        a=random.randint(1000,9000)
        self.bill_no.set(a)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product= StringVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()
        self.price = IntVar()
        self.qty=IntVar()

        #product categories list
        self.category=["select option","cloths","lifestyle"]
        self.subcatcoths=['Pant','t-shirt','shirt']
        self.pant=["levis",'Mufti','spykar']
        self.price_levis=6000
        self.price_mufti = 500
        self.price_spykar = 9000

        self.t_shirt=['polo','Roadstar','Jack&Jones']
        self.price_polo=1500
        self.price_roadstar = 1000
        self.price_jackjones= 900

        self.shirt=['Peter England','Louies Philipes','Park Avenue']
        self.price_peter=2500
        self.price_louies = 1000
        self.price_park= 2000



        self.subcatlifestyle=['bath soap','face cream','Hair oil']

        self.bath_soap=['lifeboy','lux','santoor']
        self.price_lifboy=float(20)
        self.price_lux = 20
        self.price_santoor= 20

        self.face_creame=['fair&lovely','pons','olay','Garnier']
        self.price_fair=150
        self.price_pons = 100
        self.price_olay= 40
        self.price_ganiner=30

        self.hair_oil=['Parachute','Jashmin','amla']
        self.price_Parachute=200
        self.price_jashmin= 150
        self.price_amla= 250

        self.subcatmobiles=['iphone','samsung','xiome','one+']





        #img 1
        fp=open("image/img.jpg",'rb')
        img=PIL.Image.open(fp)
        img=img.resize((500,130),PIL.Image. LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img)
        ib1_img=Label(self.root,image=self.photoimg_1)
        ib1_img.place(x=2,y=0,width=500,height=130)
        # img 2
        fp = open("image/img2.jpg", 'rb')
        img = PIL.Image.open(fp)
        img = img.resize((500, 130), PIL.Image. LANCZOS)
        self.photoimg_2= ImageTk.PhotoImage(img)
        ib2_img = Label(self.root, image=self.photoimg_2)
        ib2_img.place(x=505, y=0, width=500, height=130)

        # img 3
        fp = open("image/img3.png", 'rb')
        img = PIL.Image.open(fp)
        img = img.resize((500, 130), PIL.Image. LANCZOS)
        self.photoimg_3= ImageTk.PhotoImage(img)
        ib3_img = Label(self.root, image=self.photoimg_3)
        ib3_img.place(x=1009, y=0, width=500, height=130)

        ib1_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=('times new roman',35,'bold'),bg='white',fg='red')
        ib1_title.place(x=0,y=130,width=1530,height=45)




        main_frame=Frame(self.root,border=5,relief=GROOVE,bg="white")
        main_frame.place(x=0,y=175,width=1530,height=620)

        #customer labelframe
        cust_frame=LabelFrame(main_frame,text='customer',font=("arial",12,"bold"),bg='white',fg='red')
        cust_frame.place(x=10,y=5,width=350,height=140)

        self.lb1_mob=Label(cust_frame,text='mobile No : ',font=("arial",10,"bold"),bg='white')
        self.lb1_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mod=ttk.Entry(cust_frame,font=("times new roman",10,"bold"),textvariable=self.c_phone,width=24)
        self.entry_mod.grid(row=0,column=1)

        self.lb1_cust = Label(cust_frame, text='Customer Name : ', font=("arial", 10, "bold"), bg='white',bd=4)
        self.lb1_cust.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entrycustname = ttk.Entry(cust_frame, font=("arial", 10, "bold"),textvariable=self.c_name, width=24)
        self.entrycustname.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lb1_custemail = Label(cust_frame, text='Email : ', font=("arial", 10, "bold"), bg='white', bd=4)
        self.lb1_custemail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entrycustname_email = ttk.Entry(cust_frame, font=("arial", 10, "bold"),textvariable=self.c_email, width=24)
        self.entrycustname_email.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # product labelframe
        product_frame = LabelFrame(main_frame, text='product', font=("arial", 12, "bold"), bg='white', fg='red')
        product_frame.place(x=370, y=5, width=620, height=140)
        #category
        self.lb1_category = Label(product_frame, text='Select Categories :', font=("arial", 10, "bold"), bg='white', bd=4)
        self.lb1_category.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.comb_category = ttk.Combobox(product_frame, font=("arial", 10, "bold"),value=self.category,width=24,state="readonly")
        self.comb_category.current(0)
        self.comb_category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.comb_category.bind("<<ComboboxSelected>>",self.categories)
        #subCaterory
        self.lb1_subcategory = Label(product_frame, text='SubCategories :', font=("arial", 10, "bold"), bg='white', bd=4)
        self.lb1_subcategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.comb_subcategory = ttk.Combobox(product_frame,value=[""], font=("arial", 10, "bold"),width=24,state="readonly")
        self.comb_subcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.comb_subcategory.bind("<<ComboboxSelected>>", self.products)

        #productname
        self.lb1_product = Label(product_frame, text='ProductName :', font=("arial", 10, "bold"), bg='white', bd=4)
        self.lb1_product.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.comb_product = ttk.Combobox(product_frame,textvariable=self.product, font=("arial", 10, "bold"),width=24,state="readonly")
        self.comb_product.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.comb_product.bind("<<ComboboxSelected>>", self.prices)

        # price
        self.lb1_price = Label(product_frame, text='Price :', font=("arial", 10, "bold"), bg='white', bd=4)
        self.lb1_price.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.comb_price = ttk.Combobox(product_frame, font=("arial", 10, "bold"),textvariable=self.price, width=24, state="readonly")
        self.comb_price.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # qty
        self.lb1_qty = Label(product_frame, text='Quality :', font=("arial", 10, "bold"), bg='white', bd=4)
        self.lb1_qty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.comb_qty = ttk.Entry(product_frame, font=("arial", 10, "bold"),textvariable=self.qty, width=26)
        self.comb_qty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #middleframe
        middleframe=Frame(self.root,bd=10,bg='white')
        middleframe.place(x=10,y=328,width=980,height=340)

        #img 4
        fp=open("image/img4.jpg",'rb')
        img=PIL.Image.open(fp)
        img=img.resize((480,340),PIL.Image. LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img)
        ib4_img=Label(middleframe,image=self.photoimg_4)
        ib4_img.place(x=0,y=-9,width=480,height=340)
        # img 5
        fp = open("image/img5.jpg", 'rb')
        img = PIL.Image.open(fp)
        img = img.resize((480, 340), PIL.Image. LANCZOS)
        self.photoimg_5= ImageTk.PhotoImage(img)
        ib5_img = Label(middleframe, image=self.photoimg_5)
        ib5_img.place(x=490, y=0, width=480, height=340)

        #search
        search_frame=Frame(main_frame,bd=2,bg='white')
        search_frame.place(x=1006,y=4,width=500,height=40)

        self.iblbill = Button(search_frame,  text='Bill Number', font=('arial', 10, 'bold'),
                                   bg="red", fg='white',  cursor='hand2')
        self.iblbill.grid(row=0, column=0,sticky=W, padx=1)

        self.entry_search = ttk.Entry(search_frame,textvariable=self.search_bill, font=("arial", 10, "bold"), width=24)
        self.entry_search.grid(row=0, column=1, sticky=W, padx=2)

        self.btnsearch= Button(search_frame, command=self.find_bill, text='search', font=('arial', 10, 'bold'),width=15,cursor='hand2',
                                   bg="orangered", fg='white',justify="center")
        self.btnsearch.grid(row=0, column=2)


        #rightframe bill area
        rightlabelframe=LabelFrame(main_frame,text='Bill Area',font=('times new roman',12,'bold'),bg='white',fg='red')
        rightlabelframe.place(x=1030,y=45 ,width=480,height=440)

        scrollbar=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=scrollbar.set,bg='white',fg='blue',font=('times new roman',12,'bold'))
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbar.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter
        Billcounter_frame = LabelFrame(main_frame, text='Bill Counter', font=("arial", 12, "bold"), bg='#F5F5F5', fg='red')
        Billcounter_frame.place(x=0, y=485, width=1520, height=125)

        self.lb1subtotal = Label(Billcounter_frame, text='Sub Total :', font=("arial", 10, "bold"), bg='#F5F5F5', bd=4)
        self.lb1subtotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entrysubtotal = ttk.Entry(Billcounter_frame,textvariable=self.sub_total, font=("arial", 10, "bold"), width=24)
        self.entrysubtotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lb1gov = Label(Billcounter_frame, text='Gov Tax :', font=("arial", 10, "bold"), bg='#F5F5F5', bd=4)
        self.lb1gov.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entrygov = ttk.Entry(Billcounter_frame,textvariable=self.tax_input, font=("arial", 10, "bold"), width=24)
        self.entrygov.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lb1total = Label(Billcounter_frame, text='Total : ', font=("arial", 10, "bold"),bg='#F5F5F5', bd=4)
        self.lb1total.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entrytotal = ttk.Entry(Billcounter_frame, textvariable=self.total,font=("arial", 10, "bold"), width=24)
        self.entrytotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        #button
        button_frame=Frame(Billcounter_frame,bd=2,bg='white')
        button_frame.place(x=320,y=0)

        self.btnaddtocart=Button(button_frame,command=self.Additem,height=2,text='Add To Cart',font=('arial',12,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnaddtocart.grid(row=0,column=0,padx=6)
        self.btngenerate= Button(button_frame,command=self.gen_bill, height=2, text='Generate Bill', font=('arial', 12, 'bold'),width=15,cursor='hand2',
                                   bg="orangered", fg='white')
        self.btngenerate.grid(row=0, column=1,padx=6)

        self.btnsave = Button(button_frame, height=2,command=self.save_bill, text='Save', font=('arial', 12, 'bold'),width=15,cursor='hand2',
                                   bg="orangered", fg='white')
        self.btnsave.grid(row=0, column=3,padx=6)

        self.btnprint = Button(button_frame, height=2, command=self.iprint,text='Print', font=('arial', 12, 'bold'),width=15,cursor='hand2',
                                   bg="orangered", fg='white')
        self.btnprint.grid(row=0, column=4,padx=6)

        self.btnclear= Button(button_frame, command=self.clear,height=2, text='Clear', font=('arial', 12, 'bold'),width=15,cursor='hand2',
                                   bg="orangered", fg='white')
        self.btnclear.grid(row=0, column=5)

        self.btnexit= Button(button_frame,command=self.root.destroy, height=2, text='Exit', font=('arial', 12, 'bold'),width=15,cursor='hand2',
                                   bg="orangered", fg='white')
        self.btnexit.grid(row=0, column=6,padx=6)
        self.welcome()
        self.l = []

    def welcome(self):
            self.textarea.delete(1.0, END)
            self.textarea.insert(END, "\t\t Welcome to smart Bazar\t\t")
            self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
            self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
            self.textarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
            self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")

            self.textarea.insert(END, "\n==================================================")
            self.textarea.insert(END, f"\n \tProducts\t\tQty\t\tPrice")
            self.textarea.insert(END, "\n==================================================")
        #==========================================


    def Additem(self):

        Tax=1
        self.n=self.price.get()
        self.m=self.n*self.qty.get()
        self.l.append(self.m)
        if self.product.get()=='':
            messagebox.showerror('Error','Please select the product Name')
        else:
            self.textarea.insert(END,f'\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}')
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.price.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f' % ((sum(self.l)) + ((((sum(self.l)) - (self.price.get())) * Tax) / 100))))


    def gen_bill(self):
        if self.product.get()=='':
            messagebox.showerror('Error', 'Please click Add TO Card')
        else:
            text=self.textarea.get(9.0,(10.0+int(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n==================================================")
            self.textarea.insert(END,f'\n Sub Amount:\t\t\t{self.sub_total.get()}')
            self.textarea.insert(END, f'\n Tax Amount:\t\t\t{self.tax_input.get()}')
            self.textarea.insert(END, f'\n Total Amount:\t\t\t{self.total.get()}')
            self.textarea.insert(END, "\n==================================================")

    def save_bill(self):
        op=messagebox.askyesno('Save Bill',"Do u want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bill/'+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            messagebox.showinfo('save bill',f'Bill NO: {self.bill_no.get()} is saved successfully')
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filname=tempfile.mktemp('.txt')
        open(filname,'w').write(q)
        os.startfile(filname,'print')
    def find_bill(self):
        found='no'
        for i in os.listdir('bill/'):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bill/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found='yes'

        if found=='no':
                messagebox.showerror('error','invaild bill number')

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set('')
        self.c_name.set('')
        self.c_phone.set('')
        self.bill_no.set('')
        a = random.randint(1000, 9000)
        self.bill_no.set(str(a))
        self.c_email.set('')
        self.search_bill.set('')
        self.product.set('')
        self.sub_total.set('')
        self.tax_input.set('')
        self.total.set('')
        self.price.set(0)
        self.qty.set(0)
        self.l=[0]
        self.welcome()









    def categories(self,event=''):
        if self.comb_category.get()=='cloths':
            self.comb_subcategory.config(value=self.subcatcoths)
            self.comb_subcategory.current(0)

        if self.comb_category.get() == 'lifestyle':
            self.comb_subcategory.config(value=self.subcatlifestyle)
            self.comb_subcategory.current(0)


    def products(self,event=''):
        if self.comb_subcategory.get() =='Pant':
            self.comb_product.config(value=self.pant)
            self.comb_product.current(0)

        if self.comb_subcategory.get() =='shirt':
            self.comb_product.config(value=self.shirt)
            self.comb_product.current(0)
        if self.comb_subcategory.get() =='t-shirt':
            self.comb_product.config(value=self.t_shirt)
            self.comb_product.current(0)

        if self.comb_subcategory.get() == 'bath soap':
            self.comb_product.config(value=self.bath_soap)
            self.comb_product.current(0)
        if self.comb_subcategory.get() == 'face cream':
            self.comb_product.config(value=self.face_creame)
            self.comb_product.current(0)
        if self.comb_subcategory.get() == 'bath soap':
            self.comb_product.config(value=self.bath_soap)
            self.comb_product.current(0)
        if self.comb_subcategory.get() == 'Hair oil':
            self.comb_product.config(value=self.hair_oil)
            self.comb_product.current(0)

    def prices(self,event=''):
        #pant
        if self.comb_product.get()=='levis':
            self.comb_price.config(value=self.price_levis)
            self.comb_price.current(0)
            self.qty.set(1)

        if self.comb_product.get()=='Mufti':
            self.comb_price.config(value=self.price_mufti)
            self.comb_price.current(0)
            self.qty.set(1)

        if self.comb_product.get()=='spykar':
            self.comb_price.config(value=self.price_spykar)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='polo':
            self.comb_price.config(value=self.price_polo)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Jack&Jones':
            self.comb_price.config(value=self.price_jackjones)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Roadstar':
            self.comb_price.config(value=self.price_roadstar)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Peter England':
            self.comb_price.config(value=self.price_peter)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Louies Philipes':
            self.comb_price.config(value=self.price_louies)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Park Avenue':
            self.comb_price.config(value=self.price_park)
            self.comb_price.current(0)
            self.qty.set(1)

        if self.comb_product.get()=='lifeboy':
            self.comb_price.config(value=self.price_lifboy)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='lux':
            self.comb_price.config(value=self.price_lux)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='santoor':
            self.comb_price.config(value=self.price_santoor)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='fair&lovely':
            self.comb_price.config(value=self.price_fair)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='pons':
            self.comb_price.config(value=self.price_pons)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='olay':
            self.comb_price.config(value=self.price_olay)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Ganier':
            self.comb_price.config(value=self.price_ganiner)
            self.comb_price.current(0)
            self.qty.set(1)
        if self.comb_product.get()=='Parachute':
            self.comb_price.config(value=self.price_Parachute)
            self.comb_price.current(0)
            self.qty.set(1)




root = Tk()
obj=Bill_app(root)
root.mainloop()