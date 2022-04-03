# Pool

class Pool:
    def __init__(self, name):
        self.name = name
        self.computers = []
    
    computers = []

    def addComputer(self, computer):
        self.computers.append(computer)