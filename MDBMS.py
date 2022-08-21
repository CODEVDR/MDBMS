from sqlmodule import  *
from datetime import datetime as dt

#Connection From Sql Server
pw=input("Enter Server Password : ")
cs=connect_server(pw)
try:
    q1="create database if not exists Medical_Store_DB;"
    execute_query(cs[0],q1)
except:
    pass
cd=connect_database(cs[1])
#Date And Time
x=str(dt.now())
date=x.split()

if cs[2]==1:
    print("Login Sucess")
    print("\t\t\t\t\tWelcome To VDR Pharma")
    while True:
        print("------------")
        print("Medicienes info")
        print("------------")
        print("1. Medicines records")
        print("2. Medicines Details")
        print("------------")
        print("Patient info")
        print("------------")
        print("3. Patients records")
        print("4. Veiw Patient Detail")
        print("5. Delete patient detail")
        print("------------")
        print("Employees info")
        print("------------")
        print("6. Employee records")
        print("7. Employee details")
        print("----------------------------")
        print("8. EXIT")
        s=input("Enter Your Choice : ")
        if s=="1":
            print()
            print("=====================================================")
            #Medicines records
            q0="use Medical_Store_DB"
            q1="""create table if not exists mediciene_records(mediciene_name varchar(20),mediciene_group varchar(20),Date_of_Manufacture varchar(30),Date_of_Expiry varchar(30),qty int(20),date_and_time varchar(50));"""
            #Entries
            md_nm=input("Enter Mediciene Name : ").capitalize()
            md_gp=input("Enter Mediciene Group : ").capitalize()
            ct=int(input("Enter Mediciene Quantity : "))
            mfg=input("Enter Date of Manufacture[YYYY-MM-DD] : ")
            exp=input("Enter Date of Expiry[YYYY-MM-DD] : ")
            q2=f"""insert into mediciene_records values("{md_nm}","{md_gp}","{mfg}","{exp}",{ct},"{x}");"""
            execute_query(cd,q0)#A function That Executes Above query
            execute_query(cd,q1)#A function That Executes Above query
            execute_query(cd,q2)#A function That Executes Above query
            print("-------------------")
            print("Sucessfully Stored")
            print("-------------------")
            print("=====================================================")
            print()
        elif s=="2":
            print()
            print("Medicines Details")
            print("=====================================================")
            #Medicines Details
            q0="use Medical_Store_DB"
            q1="select * from mediciene_records;"
            data=read_query(cd,q1)
            all=[]
            expire=[]
            not_expire=[]
            for i in data:
                dat=i[-3].split()
                if str(dat[0])==date[0]:
                    expire.append(i)
                elif i!=date:
                    not_expire.append(i)
                all.append(i)
            while True:
                s=input("1.Do You Want to See Expired Mediciene\n2.Do You Want To see Non-Expired Mediciene\n3.Do You Want to See All Mediciene Data\n4.EXIT\nEnter Your Choice : ")     
                if s=="1":
                    print("Expired Medicienes")
                    print("===========================================================")
                    for i in expire:
                        print(i)
                    print("===========================================================")
                elif s=="2":
                    print("Non-Expired Medicienes")
                    print("===========================================================")
                    for i in not_expire:
                        print(i)
                    print("===========================================================")
                elif s=="3":
                    print("All Medicienes")
                    print("===========================================================")
                    for i in all:
                        print(i)
                    print("===========================================================")
                elif s=="4":
                    break
                else:
                    print("Invalid Syntax")
            print("=====================================================")
            print()
        elif s=="3":
            print()
            print("==================================================")
            #Patients records
            #Entries
            name=input("Enter Patient' Name : ").capitalize()
            age=input("Enter Patient's age : ")
            addr=input("Enter Patient's Address : ").capitalize()            
            ph_no=input("Enter Patient's Phone Number : ")
            md_nm=input("Enter Mediciene Purchased By Patient : ").capitalize()
            #For Reading Count Of Mediciene
            q3=f"""select * from mediciene_records where mediciene_name="{md_nm}";"""
            rd=read_query(cd,q3)
            if rd!=[]:#If User Enter A invalid mediciene name then it throws an error
                if int(rd[0][-2])>0 and int(rd[0][-2])<=100:#I took The Max Mediciene count as 100
                    #Sql Code for Creating Table
                    q0="use Medical_Store_DB"
                    q1="""create table if not exists patient_records(name varchar(20),age varchar(8),address varchar(30),ph_no varchar(20),mediciene_name varchar(20),date_time varchar(30));"""
                    #Sql Code For Storing Data in Database
                    q2=f"""insert into patient_records values("{name}","{age}","{addr}","{ph_no}","{md_nm}","{x}");"""
                    #For updating Mediciene Count im mediciene_record
                    val=int(rd[0][-2])-1
                    q3=f"""update mediciene_records set qty={val} where mediciene_name="{md_nm}";"""
                    execute_query(cd,q0)#A function That Executes Above query
                    execute_query(cd,q1)#A function That Executes Above query
                    execute_query(cd,q2)#A function That Executes Above query
                    execute_query(cd,q3)#A function That Executes Above query
                    print("-------------------")
                    print("Sucessfully Stored")
                    print("-------------------")
                    print("==================================================")
                    print()
                else:
                    print("Mediciene Not Avaiable")
            else:
                print("Invalid Mediciene Name")
        elif s=="4":
            #Veiw Patient Detail
            print()
            print("===========================================================")
            q0="use Medical_Store_DB"
            q1="""select * from patient_records;"""
            rd=read_query(cd,q1)
            print("NAME\t  AGE  ADDRESS\t\t  PHONE NUMBER  MEDICIENE NAME\t AT DATE AND TIME")
            for i in rd:
                print("----------------------------------------------------")
                print(i[0]+"\t"+i[1]+" "+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5])
            print("----------------------------------------------------")
            print("===========================================================")
            print()
        elif s=="5":
            #Delete patient detail
            print()
            print("===========================================================")
            nm=input("Enter Patient's Name : ")
            ph_no=input("Enter Phone Number : ")
            try:
                q0="use Medical_Store_DB"
                q1=f"""delete from patient_records where name="{nm}"&& ph_no="{ph_no}";"""
                execute_query(cd,q0)
                execute_query(cd,q1)
                print("-------------------")
                print("Sucessfully Stored")
                print("-------------------")
            except:
                print("Error Occured")
            print("===========================================================")
            print()
    
        elif s=="6":
            #Employee records
            print()
            print("===========================================================")
            q0="use Medical_Store_DB"
            q1="""create table if not exists employees_records(name varchar(20),age varchar(8),profession varchar(30),ph_no varchar(10),address varchar(20),joined_at_date_time varchar(30));"""
            name=input("Enter Employee's Name : ")
            age=input("Enter Employee's age : ")
            pro=input("Enter Employee's Profession : ")
            ph_no=input("Enter Employee's Phone Number : ")
            addr=input("Enter Employee's Address  :")
            q2=f"""insert into employees_records values("{name}","{age}","{pro}","{ph_no}","{addr}","{x}");"""
            execute_query(cd,q0)#A function That Executes Above query
            execute_query(cd,q1)#A function That Executes Above query
            execute_query(cd,q2)#A function That Executes Above query
            print("-------------------")
            print("Sucessfully Stored")
            print("-------------------")
            print("===========================================================")
            print()
        elif s=="7":
            print()
            print("===========================================================")
            q0="use Medical_Store_DB"
            q1="""select * from employees_records;"""
            rd=read_query(cd,q1)
            print("NAME\t  AGE  PROFESSION\t  PHONE NUMBER  ADDRESS\t\t AT DATE AND TIME")
            for i in rd:
                print("----------------------------------------------------")
                print(i[0]+"\t"+i[1]+" "+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5])
            print("----------------------------------------------------")
            print("===========================================================")
            print()
        elif s=="8":
            break
        else:
            print("Enter A Valid Option")
else:
    print("Try Again")


