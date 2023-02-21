import mysql.connector

class DBhelper:

    try:
        def __init__(self):
            self.conn = mysql.connector.connect(host='localhost',user='root',password='',database='user_login')
            self.mycursor = self.conn.cursor()
            print(self.conn)
    except:
        print("some error occured")

    else:
        print("connected successfully")
        

    # registration
    def register(self,name,email,password):
       try:
         self.mycursor.execute("""INSERT INTO `login` (`id`, `name`, `email`, `password`)
         VALUES (NULL, '{}', '{}', '{}'); """.format(name,email,password))
         self.conn.commit()
       except:
            return -1
       else:
            return 1

    # searching..
    def search(self,email,password):
        self.mycursor.execute("""
        select * from login where email like '{}' and password like '{}'""".format(email,password))
        data = self.mycursor.fetchall()
        return data
# obj = DBhelper()
 