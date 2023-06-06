from tkinter import *
import tkinter as tk
from tkinter import messagebox,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import mysql.connector 
import winsound
from tkinter import filedialog
window = tk.Tk()
window.title("Face_Recogniser")


 
#window.geometry("1280*720")
window.configure(background='lightblue')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)





lbl0 = tk.Label(window, text="Face-Recognition-Based-Attendance-System" ,bg='lightblue'  ,fg="white"  ,width=45  ,height=2,font=('times', 20, 'italic bold underline')) 
lbl0.place(x=1, y=1)

lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="black"  ,bg="lightblue" ,font=('times', 15, ' bold ') ) 
lbl.place(x=50, y=110)

txt = tk.Entry(window,width=20  ,bg="aliceblue" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=250, y=125)

lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="black"  ,bg="lightblue"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=50, y=180)

txt2 = tk.Entry(window,width=20  ,bg="aliceblue"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=250, y=200)

lbl3 = tk.Label(window, text="Contact No",width=20  ,height=2  ,fg="black"  ,bg="lightblue" ,font=('times', 15, ' bold ') ) 
lbl3.place(x=50, y=250)

txt3 = tk.Entry(window,width=20  ,bg="aliceblue" ,fg="black",font=('times', 15, ' bold '))
txt3.place(x=250, y=260)

lbl4 = tk.Label(window, text="Class",width=20  ,fg="black"  ,bg="lightblue"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl4.place(x=50, y=320)

txt4 = tk.Entry(window,width=20  ,bg="aliceblue"  ,fg="black",font=('times', 15, ' bold ')  )
txt4.place(x=250, y=330)

lbl5 = tk.Label(window, text="Message: ",width=20  ,fg="black"  ,bg="lightblue"  ,height=2 ,font=('times', 15, ' bold  ')) 
lbl5.place(x=50, y=450)

message = tk.Label(window, text="" ,bg="aliceblue"  ,fg="black"  ,width=40  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=280, y=450)


def terminate():
    dialog_title = 'QUIT'
    dialog_text = 'Are you sure?'
    if tk.messagebox.askyesno(dialog_title,dialog_text,icon='question'):
        window.withdraw()
        
        

def attendence():
    at=tk.Tk()
    at.title("Attendance Viewer")
    #at.attributes('-fullscreen', True)
    at.configure(background='lightblue')
    at.grid_rowconfigure(0, weight=1)
    at.grid_columnconfigure(0, weight=1)
    lbx=Listbox(at,width=90,height=30,bg="aliceblue" ,font=('times','15'))
    lbx.place(x=1,y=40)
    def attendenced():
        filename=filedialog.askopenfilename(initialdir="F:\Project_Bsc.CS\Attendance",title="select a file",filetype=(("CSV File","*.csv"),("All files","*")))
        lbl=Label(at,text=filename)
        lbl.place(x=400,y=20)
        #row=['Id','Name','Date','Time']
        with open(filename) as csvfile:
            reader=csv.DictReader(csvfile,delimiter=" ")
            for row in reader:
                lbx.insert(200,row)
    btn1=Button(at,text="view attend",command=attendenced,bg="skyblue")
    btn1.place(x=250,y=15)
    quitWindow = tk.Button(at, text="Quit", command=at.destroy,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
    quitWindow.place(x=1000, y=540)       
    at.mainloop()
    
    
def create_studentw():
    student=tk.Tk()
    student.attributes('-fullscreen', True)
    student.title("Student Details")
    student.configure(background="lightblue")

    lbx=Listbox(student,width=30,height=18, font=('times','15'))
    lbx.place(x=2,y=240)
    def fetch():
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",db="facerecognize",auth_plugin="mysql_native_password")
        mycursor=mydb.cursor()
        mycursor.execute("select id,name,contact,class from tycs order by id desc")
        ss=mycursor.fetchall()
        for s in ss:
            lbx.insert(0,s)
    btn4 = tk.Button(student, text="fetch", command=fetch  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1 ,activebackground = "red" ,font=('times', 15, ' bold '))
    btn4.place(x=2, y=200)
    def clr():
        lbx.delete('0','end')
    
    btn5 = tk.Button(student, text="clear", command=clr  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1 ,activebackground = "red" ,font=('times', 15, ' bold '))
    btn5.place(x=2, y=660)



    def delete():
        mydb=mysql.connector.connect(host="localhost",user="root",password="2901",db="facerecognize")
        mycursor=mydb.cursor()
        sql_stmt="delete from tycs where id=%s"
        data=txt1.get()
        mycursor.execute(sql_stmt,(data,))
        mydb.commit()
    lbl = tk.Label(student, text="Enter ID",width=15  ,height=2  ,fg="black"  ,bg="lightblue" ,font=('times', 15, ' bold ') )
    lbl.place(x=10, y=10)
    txt1 = tk.Entry(student,width=20  ,bg="aliceblue" ,fg="black",font=('times', 15, ' bold '))
    txt1.place(x=225, y=15)
    btn1 = tk.Button(student, text="Delete", command=delete  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1 ,activebackground = "red" ,font=('times', 15, ' bold '))
    btn1.place(x=450, y=18)



    def update():
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",db="facerecognize")
        mycursor=mydb.cursor()
        sqldelete="update tycs set contact=%s where id=%s"
        data=txt3.get()
        data2=txt2.get()
        mycursor.execute(sqldelete,(data,data2))
        mydb.commit()
    
    lbl2 = tk.Label(student, text="Enter ID",width=15 ,fg="black"  ,bg="lightblue"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=10, y=80)
    txt2 = tk.Entry(student,width=20  ,bg="aliceblue"  ,fg="black",font=('times', 15, ' bold ')  )
    txt2.place(x=225, y=80)
    lbl2 = tk.Label(student, text="Enter New Contact",width=15 ,fg="black"  ,bg="lightblue"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=10, y=120)
    txt3 = tk.Entry(student,width=20  ,bg="aliceblue"  ,fg="black",font=('times', 15, ' bold ')  )
    txt3.place(x=225, y=120)
    btn2 = tk.Button(student, text="Update contact", command=update  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=2 ,activebackground = "red" ,font=('times', 15, ' bold '))
    btn2.place(x=450, y=80)


  

    quitWindow = tk.Button(student, text="Quit", command=student.destroy,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
    quitWindow.place(x=1000, y=540)       
    student.mainloop()
        


    
def opn3():
    label=Label(window,text='Image removed',width=45,bg="lightblue")
    label.place(x=650,y=10)
    imagelbl=Label(width=40,height=15,bg="powderblue")
    imagelbl.place(x=650,y=35)
    
    
def opn():
    global myimg
    filename=filedialog.askopenfilename(initialdir="F:\Project_Bsc.CS\TrainingImage",title="Select A File",filetypes=(("Jpg files","*.jpg"),("all files","*.*")))
    label=Label(window,text=filename)
    label.place(x=650,y=10)
    myimg=ImageTk.PhotoImage(Image.open(filename))
    imagelbl=Label(image=myimg,bg="lightblue")
    imagelbl.place(x=730,y=40)
lbli1=Label(window,text="",width=40,height=15,bg="powderblue")
lbli1.place(x=650,y=35)    
btni1=Button(window,text="View Images",command=opn,fg="black",bg="skyblue",width=20,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
btni1.place(x=680,y=270)
btni3=Button(window,text="clear",command=opn3,fg="black",bg="skyblue",width=10,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
btni3.place(x=740,y=310)    


def opn4():
    label=Label(window,text="Image removed",width=45,bg="lightblue")
    label.place(x=1050,y=10)
    imagelbl=Label(width=40,height=15,bg="powderblue")
    imagelbl.place(x=1050,y=35)
    
def opn2():
    global unimg
    filename=filedialog.askopenfilename(initialdir="F:\Project_Bsc.CS\ImagesUnknown",title="Select A File",filetypes=(("Jpg files","*.jpg"),("all files","*.*")))
    label=Label(window,text=filename)
    label.place(x=1050,y=10)
    unimg=ImageTk.PhotoImage(Image.open(filename))
    imagelbl=Label(image=unimg,bg="lightblue")
    imagelbl.place(x=1060,y=35)
lbli2=Label(window,text="",width=40,height=15,bg="powderblue",)
lbli2.place(x=1050,y=35)    
btni2=Button(window,text="View Unknown Images",command=opn2,fg="black",bg="skyblue",width=20,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
btni2.place(x=1070,y=270)
btni4=Button(window,text="clear",command=opn4,fg="black",bg="skyblue",width=10,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
btni4.place(x=1140,y=310) 

    
    
def clear():
        txt.delete(0, 'end')    
        res = "Enter New Id"
        message.configure(text= res)

def clear2():
        txt2.delete(0, 'end')    
        res = "Enter New Name"
        message.configure(text= res)

def clear3():
        txt3.delete(0,'end')
        res="Enter New Contact"
        message.configure(text=res)
    
def clear4():
        txt4.delete(0,'end')
        res="Enter Proper Class"
        message.configure(text=res)
    
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


 
def TakeImages():        
    Id=(txt.get())
    Name=(txt2.get())
    Contact=(txt3.get())
    Class=(txt4.get())
    row=[Id,Name,Contact,Class]
    if(is_number(Id) and Name.isalpha()):
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",db="facerecognize")
            mycursor=mydb.cursor()
            mycursor.execute("create table if not exists `tycs`(id int,name varchar(25),contact varchar(10), class varchar(10),primary key(id))")
            sql_stmt="insert into tycs(Id,Name,Contact,Class) values(%s,%s,%s,%s)"
            data=txt.get()
            data2=txt2.get()
            data3=txt3.get()
            data4=txt4.get()
            mycursor.execute(sql_stmt,(data,data2,data3,data4))
            mydb.commit()
        except mysql.connector.errors.IntegrityError:
            res="Id already Exist"
            message.configure(text=res)
        except mysql.connector.errors.DataError:
            res="please enter 10 digit contact number"
            message.configure(text=res)
        else:
            with open("StudentDetails\StudentDetails.csv","a",newline="") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
                csvFile.close()
                cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            row=[Id,Name,Contact,Class]
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+Name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(50) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>99:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID:" + Id +" Name: "+ Name
            message.configure(text=res)
            row = [Id,Name,Contact,Class]
  
     
    else:
        if(is_number(Id)):
            res="Enter Alphabetical Name"
            message.configure(text=res)
        if(Name.isalpha()):
            res="Enter Numeric Id"
            message.configure(text=res)
                             
       
    
def TrainImages():
    Name=(txt2.get())
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id= getImagesAndLabels(path)
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trained\Trainner.yml")
    res = "Image Trained For "+Name#.join(str(f) for f in Id)
    message.configure(text= res)
path='TrainingImage'
def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample 
        faces.append(imageNp)
        Ids.append(Id)
    return faces,Ids

def TrackImages():
    recognizer =cv2.face.LBPHFaceRecognizer_create() #cv2.createLBPHFaceRecognizer()
    recognizer.read("Trained\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX    
    col_names =  ['Id','Name','Date','Time','Subject']
    attendance = pd.DataFrame(columns = col_names)
    subject=""
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.3,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                tm=datetime.datetime.now()
                if tm.hour==7 and tm.minute>=00:
                    subject='Python'
                elif tm.hour==8 and tm.minute>=00:
                    subject='Android'
                elif tm.hour==9 and tm.minute>=00:
                    subject='Ethical hacking'
                elif tm.hour==10 and tm.minute>=00:
                    subject='Data Science'
                elif tm.hour==11 and tm.minute>=00:
                    subject='c programming'
                elif tm.hour==12 and tm.minute>=00:
                    subject='Advance DBMS'
                elif tm.hour==13 and tm.minute>=00:
                    subject='Cloud Computing'
                elif tm.hour==14 and tm.minute>=00:
                    subject='Ethical hacking'
                elif tm.hour==15 and tm.minute>=00:
                    subject='Data Structure'
                else:
                    subject='Free_Period'
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp,subject]
                
            else:
                Id='Unknown'                
                tt=str(Id)
                fr=2500
                dur=750
                winsound.Beep(fr,dur)
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 0.8,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    #fileName="Attendance\Attendance.csv"
    fileName="Attendance\Attendance_"+subject+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res="Successfully Attendance Taken "
    message.configure(text= res)
 
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1 ,activebackground = "cyan" ,font=('times', 15, ' bold '))
clearButton.place(x=500, y=120)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
clearButton2.place(x=500, y=190)
clearButton3 = tk.Button(window, text="Clear", command=clear3  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1 ,activebackground = "red" ,font=('times', 15, ' bold '))
clearButton3.place(x=500, y=260)
clearButton4 = tk.Button(window, text="Clear", command=clear4  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
clearButton4.place(x=500, y=330)



takeImg = tk.Button(window, text="Register", command=TakeImages  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=540)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=540)
trackImg = tk.Button(window, text="Take Attendence", command=TrackImages  ,fg="black"  ,bg="skyblue"  ,width=15  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
trackImg.place(x=800,y=540)
quitWindow = tk.Button(window, text="Quit", command=terminate ,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "lightskyblue" ,font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=540)

StudentsDetails= tk.Button(window, text="Students", command=create_studentw ,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
StudentsDetails.place(x=600, y=640)

AttendenceDetails= tk.Button(window, text="Attendence", command=attendence  ,fg="black"  ,bg="skyblue"  ,width=10  ,height=2, activebackground = "red" ,font=('times', 15, ' bold '))
AttendenceDetails.place(x=800, y=640)




window.mainloop()

  

