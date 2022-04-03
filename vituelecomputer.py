class VirtuelComputer:
    def __init__(self, name, on, os):
        self.name = name
        self.on = on
        self.os = os
    
    def Toggle(self):
        self.on = not self.on
    
