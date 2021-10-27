import pymysql

class database:
    def __init__(self) -> None:
        global mycursor
        global conn
        conn = pymysql.connect(
        host='discordbot.cxqpkfk4tqmw.ap-south-1.rds.amazonaws.com',
        user="admin",
        passwd='helloThisismysqlpassword12345',
    )
        mycursor = conn.cursor()
        mycursor.execute("use Discordbot;")

    def addUser(self, name, role, email, username):
        mycursor.execute("INSERT INTO Userbase(Name, Role, Email, Username) VALUES('%s','%s','%s','%s')"%(name, role, email, username))
        conn.commit()

    def show(self):
        mycursor.execute("Select * from Userbase")
        print(mycursor.fetchall())
        


        














