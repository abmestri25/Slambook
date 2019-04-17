import mysql.connector
mydatabase=mysql.connector.connect(
    host="localhost",
    user="your_username",
    passwd="user_password",
    database="slambook"
)
print(mydatabase) #to_Check_the_connection
mydb=mydatabase.cursor()
mydb.execute("create database slambook")
mydb.execute("show databases")
for i in mydb:
    print(i)
mydb.execute("CREATE TABLE book(ID INT AUTO_INCREMENT PRIMARY KEY,FullName varchar(100),Gender varchar(10),DateOfBirth DATE ,Email varchar(50),ContactNo BIGINT(20),Hobbies varchar(100),FavColor varchar(30),FavFood varchar(30),FavSong varchar(50),FavGame varchar(40),FavMovie varchar(50),FavTVshow varchar(100),FavNumber INT(20),RoleModel varchar(100),Ambition varchar(200))")
data="INSERT INTO book(FullName,Gender,DateOfBirth,Email,ContactNo,Hobbies,FavColor,FavFood,FavSong,FavGame,FavMovie,FavTVshow,FavNumber,RoleModel,Ambition) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
value=[
('Sanjay Shankar Mestri','Male','1971-11-01','sanjaymestri343@gmail.com','9860343348','Carpentery','Black','Non-Vage','Jay bhavani,Jay shivaray','Cards','Banavabanvi','Chala Hawa Yeudya','26','Shivaji Maharaj','Its time to relax')]
mydb.executemany(data,value)
mydatabase.commit()
mydb.execute("select * from book")
result=mydb.fetchall()
for i in result:
    print(i)
print("All Records Displayed")
