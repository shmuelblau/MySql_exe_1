import mysql.connector
class DAL:
    def __init__(self , dbname) -> None:

        self.conn = mysql.connector.connect(
        host='localhost',
        user='intel_user',
        password='intelpass',
        database=dbname,
        port=3306,
        auth_plugin='mysql_native_password'
    )
       

    def get_conn(self):
        return self.conn