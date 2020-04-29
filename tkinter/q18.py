
import datetime
from datetime import date
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#global app,review1,sentiment,polarity,subjectivity

def validate_date(day,month,year):
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False
    return isValidDate





def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def validate_2():
    #global app,review1,sentiment,polarity,subjectivity
    
    #print(app,review1,sentiment,polarity,subjectivity)
    #validation for app name
    
    
    if app.get()=='':
        Label(screen_18_2, text="Please enter app name", font=("Open Sans",13,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter app name")
        return False
    
    #validation for review
    if review1.get()=='':
        Label(screen_18_2, text="Please enter the review                    ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the review")
        return False
    
    #validation for sentiment
    if sentiment.get()=='--sentiment--':
        Label(screen_18_2, text="Please choose the sentiment                         ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please choose the sentiment")
        return False
    
    #validation for sentiment polarity
    if str(polarity.get())=='' or is_float(str(polarity.get()))==False :
        Label(screen_18_2, text="Please enter the valid sentiment polarity                       ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the valid sentient polarity")
        return False
    if float(str(polarity.get()))<-1 or float(str(polarity.get()))>1:
        Label(screen_18_2, text="Please enter the valid sentiment polarity                       ", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the valid sentient polarity")
        return False
    
    #validation for sentiment subjectivity
    if str(subjectivity.get())=='' or is_float(str(subjectivity.get()))==False :
        Label(screen_18_2, text="Please enter the valid sentient subjectivity", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
       # print("Please enter the valid sentient subjectivity")
        return False
    if float(str(subjectivity.get()))<0 or float(str(subjectivity.get()))>1:
        Label(screen_18_2, text="Please enter the valid sentient subjectivity", font=("Open Sans",11,"bold"),fg="red",bg='white').place(x=0,y=y1+6*space_y)
        #print("Please enter the valid sentient subjectivity")
        return False
    
    Label(screen_18_2, text="                                                                                                   ",fg="black",bg='white').place(x=0,y=y1+6*space_y)
    new_data2=[app.get(),review1.get(),sentiment.get(),polarity.get(),subjectivity.get()]
    with open('dataset_2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_data2)
    csvFile.close()
    
    messagebox.showinfo("","Data Entered Successfully!!")
    screen_18_2.destroy()
    

    
    
def gui_18_2():
    global app,review1,sentiment,polarity,subjectivity,screen_18_2,x1,x2,y1,y2,space_y
    screen_18_2=Tk()
    screen_18_2.configure(bg='white')
    z1=Label(screen_18_2, text=" GOOGLE PLAY STATS", width='35', height="4", font=("Times New Roman", 40,'bold'), fg='white', bg='#00FFAF',anchor=NW,justify=CENTER).place(x=0, y=0)
    app=StringVar()
    review1=StringVar()
    sentiment=StringVar()
    polarity=StringVar()
    subjectivity=StringVar()
    x1=130
    y1=190
    x2=x1+210
    y2=y1
    space_y=65
    box_color='#E0FFFF'
    label_fg='#002F2F'
    label_bg='#B9FFFF'
    Label(screen_18_2, text="",bg='#B9FFFF',width=76,height=30).place(x=0.25*x1,y=0.45*y1)
    Label(screen_18_2, text="  Please Enter Data",bg='#800080',fg='white',width=35,height=2, font=("Times New Roman", 19,'bold'),anchor=W).place(x=0.25*x1+3,y=0.45*y1)
    #screen_18_2.title("My first frame")
    screen_18_2.geometry("600x665+20+40")
    a=Label(screen_18_2, text="App Name : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1)
    b=Entry(screen_18_2, textvar=app,bg=box_color).place(x=x2, y=y2)
    c=Label(screen_18_2, text="Review : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+space_y)
    d=Entry(screen_18_2, textvar=review1,bg=box_color).place(x=x2, y=y2+space_y)
    e=Label(screen_18_2, text="Sentiment : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+2*space_y)
    sentiment_list=['Possitive','Neutral','Negative']
    f = OptionMenu(screen_18_2, sentiment, *sentiment_list)
    f.config(width=12)
    sentiment.set('--sentiment--')
    f.place(x=x2, y=y2+2*space_y)
    g=Label(screen_18_2, text="Sentiment Polarity : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+3*space_y)
    h=Entry(screen_18_2, textvar=polarity,bg=box_color).place(x=x2, y=y2+3*space_y)
    i=Label(screen_18_2, text="Sentiment Subjectivity : ",bg=label_bg,fg=label_fg).place(x=x1,y=y1+4*space_y)
    j=Entry(screen_18_2, textvar=subjectivity,bg=box_color).place(x=x2, y=y2+4*space_y)
    k=Button(screen_18_2, text="Submit", bg="#00CDCD", width=15, height=1, font=("Open Sans",13,"bold"),fg="white",command=validate_2)
    k.place(x=x2-x1,y=y1+5*space_y)
    
    screen_18_2.mainloop()
    

    
#gui_18_2()