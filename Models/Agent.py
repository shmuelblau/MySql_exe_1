class Agent:
    def __init__(self, id=None, codeName='', realName='', location='', status='', missionsCompleted=0):
        self.id = id
        self.codeName = codeName
        self.realName = realName
        self.location = location
        self.status = status
        self.missionsCompleted = missionsCompleted



    @staticmethod
    def from_db_row(row):
       
        return Agent(
           
            codeName=row[1],
            realName=row[2],
            location=row[3],
            status=row[4],
            missionsCompleted=row[5]
        )
    
    @staticmethod
    def from_post_request(data):
        return Agent(
            id= data["id"] if "id" in data else None ,
            codeName=data["codeName"],
            realName=data["realName"],
            location=data["location"],
            status=data["status"],
            missionsCompleted=data["missionsCompleted"]

        )

    


    def __repr__(self):
        return (f"<Agent id={self.id}, codeName='{self.codeName}', realName='{self.realName}', "
                f"location='{self.location}', status='{self.status}', missionsCompleted={self.missionsCompleted}>")
