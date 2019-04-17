import mysql.connector
print("SLAMBOOK")

mydatabase=mysql.connector.connect(
    host="localhost",
    user="your_username",
    passwd="user_password",
    database="database_name"
    )
mydb=mydatabase.cursor()
while True:
    print("1.Insert Data into Slambook\n2.Display All Records\n3.Display Specific Record\n4.Update Data of Specific One\n5.Delete Data of Specific One\n6.Stop")
    opt=int(input("Enter your choice\n"))
    if opt==1:
        fname=input("Enter your Full Name\n")
        gndr=input("Enter your Gender\n")
        bday=input("Enter your Birthdate in YYYY-MM-DD\n")
        email=input("Enter your Email ID\n")
        contact=int(input("Enter your Contact Number\n"))
        hobbie=input("Enter your Hobbies\n")
        color=input("Enter your Favourite Colour\n")
        food=input("Enter your Favourite Food\n")
        song=input("Enter your Favourite Song\n")
        game=input("Enter your Favourite game\n")
        movie=input("Enter your Favourite Movie\n")
        tvshow=input("Enter your Favourite TVshow\n")
        number=int(input("Enter your Favourite Number\n"))
        rolemodel=input("Enter your Role Model\n")
        ambi=input("Enter your Ambition\n")
        sql="insert into book(FullName,Gender,DateOfBirth,Email,ContactNo,Hobbies,FavColor,FavFood,FavSong,FavGame,FavMovie,FavTVshow,FavNumber,RoleModel,Ambition ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(fname,gndr,bday,email,contact,hobbie,color,food,song,game,movie,tvshow,number,rolemodel,ambi)
        mydb.execute(sql,val)
        mydatabase.commit()
        print("Record Inserted Successfully")
    elif opt==2:
        print("All Records are as follows")
        mydb.execute("select * from book")
        result=mydb.fetchall()
        for i in result:
            print(i)
    elif opt==3:
        try:
            num=int(input("Enter Id whose data you want to see\n"))
            sql="select * from book where Id=%s"
            val=(num,)
            mydb.execute(sql,val)
            result=mydb.fetchone()
            for i in result:
                print(i)
        except:
            print("Enter valid ID")
        finally:
            pass
    elif opt==4: #update data of specific
        try:
            num=int(input("Enter ID to update data\n"))
            print("What you want to update")
            print("1.Email\n2.Contact Number")
            choice=int(input("Enter your choice\n"))
            if choice==1:
                email=input("Enter new email ID\n")
                sql="update book set Email=%s where ID=%s"
                val=(email,num)
                mydb.execute(sql,val)
                mydatabase.commit()
                print("Record is updated sucessfully")
            elif choice==2:
                try:
                    number=input("Enter Contact Nummber\n")
                    sql="update book set ContactNo=%s where ID=%s"
                    val=(number,num)
                    mydb.execute(sql,val)
                    mydatabase.commit()
                    print("Record is updated sucessfully")
                except:
                    print("Enter valid Contact Number")
                finally:
                    pass
            else:
                print("Wrong choice")
        except:
            print("Enter valid ID")
       
    elif opt==5: # delete data
        try:
            num=int(input("Enter ID whose data you want to see\n"))
            sql="delete from book where Id=%s"
            val=(num,)
            mydb.execute(sql,val)
            mydatabase.commit()
            print("Data deleted successfully")
        except:
            print("Enter valid ID")
        finally:    
            pass
    elif opt==6:
        break
    else:
        print("Wrong Choice")
#End Of Program
