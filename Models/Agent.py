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
        """קונברט משורת טבלה (tuple) לאובייקט Agent"""
        return Agent(
            id=row[0],
            codeName=row[1],
            realName=row[2],
            location=row[3],
            status=row[4],
            missionsCompleted=row[5]
        )

    def __repr__(self):
        return (f"<Agent id={self.id}, codeName='{self.codeName}', realName='{self.realName}', "
                f"location='{self.location}', status='{self.status}', missionsCompleted={self.missionsCompleted}>")
