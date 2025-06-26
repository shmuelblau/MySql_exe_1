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
        query  = """INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, %s) """
        cursor.execute(query, (agent.codeName, agent.realName, agent.location, agent.status, agent.missionsCompleted))

        self.conn.commit()
        cursor.close()

    def edit(self, agent):
        cursor = self.conn.cursor()
        query = """UPDATE agents SET codeName = %s, realName = %s, location = %s, status = %s, missionsCompleted = %s WHERE id = %s """
        cursor.execute(query, (agent.codeName, agent.realName, agent.location, agent.status, agent.missionsCompleted , agent.id))
         
        self.conn.commit()
        cursor.close()



    def delete(self ,agent):
        cursor = self.conn.cursor()
        query ="""DELETE FROM agents WHERE id = %s"""
        cursor.execute(query, (agent.id))
        self.conn.commit()
        cursor.close()               

    def c(self):
        self.conn.close()