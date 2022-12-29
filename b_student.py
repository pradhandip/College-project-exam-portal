def a_student():
    #STUDENT(Create a student,Update student details,Remove a student from the database):
    import csv
    import os
    def write():
        import csv
        f=open("stud1.csv","a",newline="")
        w=csv.writer(f)
        w.writerow(['student_id',"name","class_roll_no","batch_name"])
        n=int(input("Enter the number of students :"))
        for x in range(n):
            student_id=input("Enter the Student's ID :")
            name=input("Enter the Name of the student :")
            class_roll_no=input("Enter the class Roll No. :")
            batch_name=input("Enter the batch name :")
            l=[student_id,name,class_roll_no,batch_name]
            w.writerow(l)
        f.close()
        
        
    def display():
        import csv
        f=open("stud1.csv","r",newline="")
        stud=csv.reader(f)
        for i in stud:
            print(i)
        f.close()

        
    def update():
        import csv
        f=open("stud1.csv","r")
        f1=open("temp.csv","a",newline="")
        stud=csv.reader(f)
        r=input("Enter class Roll No. to update :")
        for i in stud:
            if i[2]==r:
                print("Enter new data")
                student_id=input("Enter the Student's ID :")
                name=input("Enter the Name of the student :")
                class_roll_no=input("Enter the class Roll No. :")
                batch_name=input("Enter the batch name :")
                l=[student_id,name,class_roll_no,batch_name]
                w.writerow(l)
            else:
                w=csv.writer(f1)
                w.writerow(i)
        f.close()
        f1.close()
        os.remove("stud1.csv")
        os.rename("temp.csv","stud1.csv")
        f=open("stud1.csv","r")
        stud=csv.reader(f)
        for i in stud:
            print(i)
        f.close()
        

    def remove():
        import csv
        f=open("stud1.csv","r")
        f1=open("temp.csv","a",newline="")
        stud=csv.reader(f)
        r=input("Enter class Roll No. to remove :")
        for i in stud:
            if i[2]==r:
                pass
            else:
                w=csv.writer(f1)
                w.writerow(i)
        f.close()
        f1.close()
        os.remove("stud1.csv")
        os.rename("temp.csv","stud1.csv")
        f=open("stud1.csv","r")
        stud=csv.reader(f)
        for i in stud:
            print(i)
        f.close()

    #STUDENT(report card (Text File) generation)
    def rpt():
        def grade(num):
            if num>=90:
                    print("congratulations!You have passed the exam with grade - 'A'.")
            elif num<90 and num>=80:
                    print("congratulations!You have passed the exam with grade - 'B'.")
            elif num<80 and num>=70:
                    print("congratulations!You have passed the exam with grade - 'C'.")
            elif num<70 and num>=60:
                    print("congratulations!You have passed the exam with grade - 'D'.")
            elif num<60 and num>=50:
                    print("congratulations!You have passed the exam with grade - 'E'.")
            else:
                    print("oh!You have not qualified the Exam and got - 'F'.")
        f=open("demo34.txt","w")
        x=input("Name of the student : ")
        y=input("Batch Name : ")
        z=int(input("Emter Roll Number : "))
        Chemistry=int(input("Enter marks in 'Chemistry' : "))
        Mathematics_I=int(input("Enter marks in 'Mathematics I' : "))
        Biology=int(input("Enter marks in 'Biology' : "))
        Electrical=int(input("Enter marks in 'Electrical' : "))
        Mechanics=int(input("Enter marks in 'Mechanics' : "))
        Programming=int(input("Enter marks in 'Programming for Problem Solving Using Python' : "))
        dth=int(input("Enter marks in 'Design Thinking & Innovation(Basic)'  : "))
        eco=int(input("Enter marks in 'Economics,Finance & Entrepreneurship Skills(Foundation)' : "))
        esp=int(input("Enter marks in 'Essential Studies for Professionals I'  : "))
        sdp=int(input("Enter marks in 'Skill Development for Professionals I' : "))
        total=Chemistry+Mathematics_I+Biology+Electrical+Mechanics+Programming+dth+eco+esp+sdp
        num=(total/10)
        f.write("*******************************************************************************")
        f.write("\n*******************************************************************************")
        f.write("\n                                  REPORT CARD                                  "+"\n")
        f.write("\n...............................................................................")
        f.write("\n...............................................................................")
        f.write("\nName : "+str(x)+"\n")
        f.write("\nBatch : "+str(y)+"\n")
        f.write("\nRoll Number : "+str(z))
        f.write("\n-------------------------------------------------------------------------------")
        f.write("\n")
        f.write("\n")
        f.write("\nMarks in 'Chemistry(BSC102-Th)' : "+str(Chemistry))
        f.write("\nMarks in 'Mathematics-I(BSC103)' : "+str(Mathematics_I))
        f.write("\nMarks in 'Biology(BSC109)' : "+str(Biology))
        f.write("\nMarks in 'Electrical(ESC101-Th)' : "+str(Electrical))
        f.write("\nMarks in 'Mechanics(ESC202A)' : "+str(Mechanics))
        f.write("\nMarks in 'Programming for Problem Solving Using Python(IVC101)' : "+str(Programming))
        f.write("\nMarks in 'Design Thinking & Innovation(Basic)(IVC102)' : "+str(dth))
        f.write("\nMarks in 'Economics,Finance & Entrepreneurship Skills(Foundation)(IVC103)' : "+str(eco))
        f.write("\nMarks in 'Essential Studies for Professionals I(HSMC102)' : "+str(esp))
        f.write("\nMarks in 'Skill Development for Professionals I(HSMC182)' : "+str(sdp))
        f.write("\n")
        f.write("\n")
        f.write("\nTotal Percentage = "+str(num)+"\n")
        f.write(str(grade(num)))
        f.write("\n")
        f.write("\n-------------------------------------------------------------------------------")
        f.write("\n                                  VIEW GRADE                                  "+"\n")
        f.write("\n-------------------------------------------------------------------------------")
        f.write("\n")
        if num>=90:    #editimg from this line
            f.write("congratulations!You have passed the exam with grade - 'A'.")
        elif num<90 and num>=80:
            f.write("congratulations!You have passed the exam with grade - 'B'.")
        elif num<80 and num>=70:
            f.write("congratulations!You have passed the exam with grade - 'C'.")
        elif num<70 and num>=60:
            f.write("congratulations!You have passed the exam with grade - 'D'.")
        elif num<60 and num>=50:
            f.write("congratulations!You have passed the exam with grade - 'E'.")
        else:
            f.write("oh!You have not qualified the Exam and got - 'F'.")
        f.write("\n")
        f.write("\n")
        f.write("\n-------------------------------------------------------------------------------")
        f.write("\n")
        f.write("*******************************************************************************")
        f.write("\n*******************************************************************************")


        f.close()



    while True:
        print("****************************")
        print("\n---------------------------")
        print("\nWelcome to the Student Module")
        print("\n---------------------------")
        print("\n****************************")
        print("MENU FOR STUDENT MODULE :\n1>WRITE\n2>DISPLAY\n3>UPDATE\n4>REMOVE\n5>GENERATE REPORT CARD\n6>Exit and Go to Home page")
        ch=int(input("Enter your choice : "))
        if ch==1:
            write()
        if ch==2:
            display()
        if ch==3:
            update()
        if ch==4:
            remove()
        if ch==5:
            rpt()
        if ch==6:
            print("END")
            import a_Main       
            a_Main.main11()     
            break;

a_student()







