def e_exam():
    #EXAMINATION(Enter marks of all students for a specific examination,Course Name, Student Roll Number):
    import csv
    import os
    def write22():
        f=open("ex1.csv","a",newline="")
        w=csv.writer(f)
        # w.writerow(["student_name","roll","batch","course_name","marks"])
        n=int(input("Enter the number of students :"))
        for x in range(n):
            student_name=input("Enter the Student's Name :")
            roll=input("Enter the class Roll No. :")
            batch=input("Enter the batch name :")
            course_name=input("Enter the course name :")
            marks=input("Total Marks in this Examination :")
            l=[student_name,roll,batch,course_name,marks]
            w.writerow(l)
        f.close()

    #View performance of all students in the examination:
    def view6():
        import csv
        with open('ex1.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    #Show examination statistics:
    def sc():
        import matplotlib.pyplot as plt
        import csv
        
        marks = []
        batch = []
        
        with open('ex1.csv','r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                marks.append(int(row[4]))
                batch.append(row[2])
        
        plt.scatter(marks, batch, color = 'g',s = 100)
        plt.xticks(rotation = 25)
        plt.xlabel('Marks')
        plt.ylabel('Batch')
        plt.title('Examination Statistics', fontsize = 20)
        
        plt.show()
    while True:
        print("****************************")
        print("\n---------------------------")
        print("\nWelcome to the Examination Module")
        print("\n---------------------------")
        print("\n****************************")
        print("MENU\n1>Fill the Details of Examination\n2>View performances\n3>Show examination statistics\n4>Exit and Go to Home page")
        ch=int(input("Enter your choice : "))
        if ch==1:
            write22()
        if ch==2:
            view6()
        if ch==3:
            sc()
        if ch==4:
            print("END")
            import a_Main       
            a_Main.main11()
            break;

e_exam()