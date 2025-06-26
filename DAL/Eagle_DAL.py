import mysql.connector
from Models.Agent import Agent

class Eagle_DAL:
   

    conn = mysql.connector.connect(
        host='localhost',
        user='intel_user',
        password='intelpass',
        database='eagleEyeDB',
        port=3306,
        auth_plugin='mysql_native_password'
    )
    
    
   

    def Select(self):
        cursor =self.conn.cursor()
        cursor.execute("SELECT * FROM agents")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def add(self , agent):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
            VALUES (%s, %s, %s, %s, %s)
        """, (agent.codeName, agent.realName, agent.location, agent.status, agent.missionsCompleted))

        self.conn.commit()
        cursor.close()

    def edit(self):
        

    def c(self):
        self.conn.close()