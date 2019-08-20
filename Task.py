class Task:
 
   priority = -1
 
   def __init__(self, name, priority):
       self.name = name
       self.priority = priority
 
   def getName(self):
       return self.name
   def getPriority(self):
       return self.priority
