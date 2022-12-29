def d_dept():
    #DEPERTMENT( Create a new department,Department ID,Department Name,List of batches)
    import csv
    import os
    def write2():
        print("*************************************************************************************************************************************************************")
        print("Department ID should be in the form of :")
        print('\n','Computer Sience and Engineering : CSE','\n',
            'Computer Sience and Engineering and Artificial Intelligence : CSEAI','\n',
            'Computer Sience and Engineering and Artificial Intelligence and Machine Learning : CSEAIML','\n',
            'Computer Sience and Engineering and Internet of Things and Business Studies : CSEIOTCSBS','\n',
            'Information Technology : IT','\n',
            'Electronics and Communication Engineering : ECE','\n',
            'Mechanical Engineering : ME','\n',
            'Electrical Engineering : EE','\n',
            'Electrical & Electronics Engineering : EEE','\n')
        print("Please write all Department IDs as mentioned above and in CAPITAL LETTERS only!")
        print("   ")
        print("*************************************************************************************************************************************************************")
        print("Department Name should be in the form of :")
        print('\n','Computer Sience and Engineering','\n',
            'Computer Sience and Engineering and Artificial Intelligence','\n',
            'Computer Sience and Engineering and Artificial Intelligence and Machine Learning','\n',
            'Computer Sience and Engineering and Internet of Things and Business Studies','\n',
            'Information Technology','\n',
            'Electronics and Communication Engineering','\n',
            'Mechanical Engineering','\n',
            'Electrical Engineering','\n',
            'Electrical & Electronics Engineering','\n')
        print("    ")
        print("*************************************************************************************************************************************************************")
        print("List of the Batches should be in the form of :")
        print("If only one batch is there,e.g - a student is from Electronics and Communication Engineering background and 2021 batch then -")
        print("ECE21")
        print("")
        print("If more than one batches are there,e.g - ")
        print("a student is from Electronics and Communication Engineering background and 2021 batch and ")
        print("another student is from Electronics and Communication Engineering background but 2022 batch,then")
        print("Write in the form of list i.e - ECE21:ECE22")
        print("    ")
        print("*************************************************************************************************************************************************************")

        f=open("dept1.csv","a",newline="")
        w=csv.writer(f)
        w.writerow(["dept_id","dept_name","list_of_batches"])
        n=int(input("Enter the number of students :"))
        for x in range(n):
            dept_id=input("Enter the Department ID : ")
            dept_name=input("Enter the Name of the Department : ")
            list_of_batches=input("Enter the list of the Batches : ")
            l=[dept_id,dept_name,list_of_batches]
            w.writerow(l)
        f.close()
    #view all the batches
    def view3():
        import csv   #read a column of csv file
        with open('dept1.csv', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            print("list of batches")
            print("---------------")
            for row in data:
                print(row["list_of_batches"])
    # #View average performance of all batches in the department
    # def view4():
    #     import csv
    #     filename = open('performance.csv', 'r')
    #     file = csv.DictReader(filename)
    #     students = []
    #     for col in file:
    #         students.append(col['marks'])
    #         print('marks : ')
 #View average performance of all batches in the department
    def view4():
        import csv   #read a column of csv file
        with open('performance.csv', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            print("Average Performance")
            print("-------------------")
            for row in data:
                print(row["marks"])

    #Department statistics:
    def bar1():
        import matplotlib.pyplot as plt
        import csv
        
        x = []
        y = []
        
        with open('performance.csv','r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[2])
                y.append(int(row[3]))
        
        plt.plot(x, y, color = 'g', linestyle = 'dashed',
                marker = 'o',label = "Performance")
        
        plt.xticks(rotation = 25)
        plt.xlabel('Batch Name')
        plt.ylabel('Average Percentage')
        plt.title('Line plot:Average percentage of all students for each batch.', fontsize = 20)
        plt.grid()
        plt.legend()
        plt.show()

    while True:
        print("****************************")
        print("\n---------------------------")
        print("\nWelcome to the Depertment Module")
        print("\n---------------------------")
        print("\n****************************")
        print("MENU FOR DEPERTMENT MODULE :\n1>Create a new Dept.\n2>View all batches in a department\n3>View average performance of all batches in the department\n4>Department statistics(line plot)\n5>Exit and Go to Home page")
        ch=int(input("Enter your choice : "))
        if ch==1:
            write2()
        if ch==2:
            view3()
        if ch==3:
            view4()
        if ch==4:
            bar1()
        if ch==5:
            print("END")
            import a_Main       
            a_Main.main11()
            break;
d_dept()

