import mysql.connector
class DAL:
    def __init__(self , dbname) -> None:

        self.conn = mysql.connector.connect(
        host='eagle-mysql',
        user='eagle_user',
        password='eaglepass',
        database=dbname,
        port=3306,
        auth_plugin='mysql_native_password'
    )
       

    def get_conn(self):
        return self.conn