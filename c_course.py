def b_course():
    def write20():
        import csv
        import os
        f=open("course11.csv","a",newline="")
        w=csv.writer(f)
        n=int(input("Enter the number of students : "))
        for x in range(n):
            Course_ID=input("Enter the Course ID : ")
            Course_Name=input("Enter the Course Name : ")
            Marks_obtained=input("Enter the Marks obtained : ")
            l=[Course_ID,Course_Name,Marks_obtained]
            w.writerow(l)
        f.close()

    #View performance of all students in the examination:
    def view60():
        import csv
        with open('course11.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    #creation of course data
    def write19():
        import csv
        import os
        f=open("course12.csv","a",newline="")
        w=csv.writer(f)
        n=int(input("Number of data want to store : "))
        for x in range(n):
            Course_Name=input("Enter the Course Name : ")
            Grade_obtained=input("Enter the Grade : ")
            Number_of_students=int(input("Enter the Number of students belong to this Grade : "))
            l=[Course_Name,Grade_obtained,Number_of_students]
            w.writerow(l)
        f.close()

    # #view statistics
    def stat2():
        import matplotlib.pyplot as plt
        import csv
        
        x = []
        y = []
        
        with open('course12.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            
            for row in plots:
                x.append(row[1])
                y.append(int(row[2]))
        
        plt.bar(x, y, color = 'pink', width = 0.72,edgecolor='black',label = "Course Performance")
        plt.xlabel('Grades')
        plt.ylabel('Number of students')
        plt.title('Course Performance')
        plt.legend()
        plt.show()


    while True:
        print("****************************")
        print("\n---------------------------")
        print("\nWelcome to the Course Module")
        print("\n---------------------------")
        print("\n****************************")
        print("MENU\n1>Create a new Course\n2>View Course Details\n3>create course grade\n4>View Grade statistics of the Course(Histogram)\n5>Exit and Go to Home page")
        ch=int(input("Enter your choice : "))
        if ch==1:
            write20()
        if ch==2:
            view60()
        if ch==3:
            write19()
        if ch==4:
            stat2()
        if ch==5:
            print("END")
            import a_Main       
            a_Main.main11()
            break;
b_course()