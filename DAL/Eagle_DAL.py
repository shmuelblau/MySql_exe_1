import mysql.connector
from DAL.DAL import DAL
from Models.Agent import Agent

class Eagle_DAL:
    
    def __init__(self):
        db= DAL("eagleEyeDB")
        self.conn = db.get_conn()
   

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
        cursor.execute(query, (agent.id ,))
        self.conn.commit()
        cursor.close()               

    def c(self):
        self.conn.close()