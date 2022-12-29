def c_batch():
    import csv
    import os
    def write():
        f=open("batch.csv","a",newline="")
        w=csv.writer(f)
        w.writerow(["batch_id","Batch_name","Dept_Name","List_of_Cources","List_of_Students","No_of_Students"]) #(for header)
        n=int(input("Enter the number of students :"))
        for x in range(n):
            batch_id=input("Enter Batch the ID :")
            Batch_name=input("Enter the Name of the Batch :")
            Dept_Name=input("Enter the Name of the Dept. :")
            List_of_Cources=input("Enter List Of the courses :")
            List_of_Students=input("Enter List Of students :")
            No_of_Students=int(input("Enter Total Number of studnts :"))
            l=[batch_id,Batch_name,Dept_Name,List_of_Cources,List_of_Students,No_of_Students]
            w.writerow(l)
        f.close()
    #view list of all the students
    def view1():
        import csv
        with open('batch.csv', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            print("List of Students")
            print("----------------")
            for row in data:
                print(row["List_of_Students"])   
    #view list of all the Courses in the batch:
    def view2():
        import csv
        with open('batch.csv', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            print("List of Cources")
            print("---------------------------------")
            for row in data:
                print(row["List_of_Cources"])
    # #performance of all the students
    # import csv
    # import os
    # def write1():
    #     f=open("performance.csv","a",newline="")
    #     w=csv.writer(f)
    #     w.writerow(["roll","name","batch","marks"]) #(for header)
    #     n=int(input("Enter the number of students :"))
    #     for x in range(n):
    #         roll=int(input("Enter the roll number : "))
    #         name=input("Enter the name of the student : ")
    #         batch=input("enter the Batch name : ")
    #         marks=input("Enter percentage obtained(considering all subject) : ")
    #         l=[roll,name,batch,marks]
    #         w.writerow(l)
    #     f.close()

    #performance of all the students
    import csv
    import os
    def write1():
        f=open("performance.csv","a",newline="")
        w=csv.writer(f)
        #w.writerow(["batch_id","Batch_name","Dept_Name","List_of_Cources","List_of_Students","No_of_Students"]) #(for header)
        n=int(input("Enter the number of students :"))
        for x in range(n):
            roll=int(input("Enter the roll number : "))
            name=input("Enter the name of the student : ")
            batch=input("enter the Batch name : ")
            marks=input("Enter percentage obtained(considering all subject) : ")
            l=[roll,name,batch,marks]
            w.writerow(l)
        f.close()

    def pi2():
        import matplotlib.pyplot as plt
        import csv
    
        Subjects = []
        Scores = []
    
        with open('performance.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter = ',')
            for row in lines:
                Subjects.append(row[1])
                Scores.append(int(row[3])) 
    
        plt.pie(Scores,labels = Subjects,autopct = '%.2f%%')
        plt.title('Number of students', fontsize = 20)
        plt.show()



    while True:
        print("****************************")
        print("\n---------------------------")
        print("\nWelcome to the Batch Module")
        print("\n---------------------------")
        print("\n****************************")
        print("MENU\n1>WRITE\n2>view list of all the students\n3>view list of all the courses\n4>Store performance of all the students\n5>Pi chart to visualize the Number of students\n6>Exit and Go to Home page")
        ch=int(input("Enter your choice : "))
        if ch==1:
            write()
        if ch==2:
            view1()
        if ch==3:
            view2()
        if ch==4:
            write1()
        if ch==5:
            pi2()
        if ch==6:
            print("END")
            import a_Main       
            a_Main.main11()
            break;
c_batch()
