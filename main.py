from math import *
 
from Task import Task
 
 
class main:
   file1 = open("tasks.txt", "r+")
 
   boole = True
   sel = -1
   Mlists = []
   Slists = []
   priority = -1
   save = 1
   in_mainTasks = False
   in_sideTasks = False
   tasklist = []
   tasklist = file1.readlines()
  # Mlists.append(""+ tasklist[2])
   for task in tasklist:
       task = task.strip()
       if task == "Main Tasks":
           in_mainTasks = True
           in_sideTasks = False
       elif task.strip() == "":
           continue
       elif task == "Side Tasks":
           in_mainTasks = False
           in_sideTasks = True
 
       if in_mainTasks:
           if task != "Main Tasks":
            Mlists.append(task)
       elif in_sideTasks:
           if task != "Side Tasks":
            Slists.append(task)
 
       # and (tasklist[1] in ("ABCDEFGHIJKLMNOPQRSTUVWYXYZabsdefghijklmnopqrstuvwxyz") or tasklist[1] in ("123456789!@#$%^&*()<>?\\"))
   #print(Mlists[0])
 
   while boole:
       print("\n1. Add a task to end of a list")
       print("2. Print tasks")
       print("3. Remove a task")
       print("4. Clear lists")
       print("5. exit")
       sel = int(input("Select an option"))
 
       if sel == 1:
           print(" Task properties")
           name = input("what is the name of the task?")
           while priority < 0 or priority > 2:
               try:
                   priority = int(input("Press 1 for main task and 2 for side task."))
               except ValueError:
                   print("give an integer")
 
           a = Task(name, priority)
           if a.getPriority() == 1:
               Mlists.append(a.name)
               # file1.write("\n  "+a.name)
 
           elif a.getPriority() == 2:
               Slists.append(a.name)
               # file1.write("\n  "+a.name)
           if save == 1:
              file1.close()
              file1 = open("tasks.txt", "w")
              file1.write("-------")
              file1.write("\nMain Tasks\n")
              for task in range (len(Mlists)):
                  a = ""+Mlists[task]
                  file1.write(a)
                  file1.write("\n")
              file1.write("\nSide Tasks\n")
              for task in range (len(Slists)):
                a= ""+Slists[task]
                file1.write(a)
                file1.write("\n")
 
           file1.close()
           priority = -1
       elif sel == 2:
        file1 = open("tasks.txt", "r")
        z = file1.readlines()
        for index in z:
           print(index)
        file1.close()
       
       elif sel == 3:
            name = input("what is the name of the task you want to remove?")
            for i in range(len(Mlists)):
                if (name == Mlists[i]):
                   Mlists.remove(name)
                   if(i == (len(Mlists)-1)):
                     break
            for i in range(len(Slists)):         
                if (name == Slists[i]):
                   Slists.remove(name)
                   if(i == (len(Slists)-1)):
                     break
            file1.close()
            file1 = open("tasks.txt", "w")
            file1.write("-------")
            file1.write("\nMain Tasks\n")
            for task in range (len(Mlists)):
                file1.write(Mlists[task])
                file1.write("\n")
            file1.write("\nSide Tasks\n")
            for task in range (len(Slists)):
                file1.write(Slists[task])
                file1.write("\n")
            file1.close()
       elif sel == 4:
           clearing = int(input("Press 1 to clear Main Tasks, 2 to clear Side Tasks, and 3 to clear both."))

           if clearing == 1:
              Mlists.clear()
           elif clearing == 2:
              Slists.clear()
           elif clearing == 3:
              Mlists.clear()
              Slists.clear()

           file1.close()
           file1 = open("tasks.txt", "w")
           file1.write("-------")
           file1.write("\nMain Tasks\n")
           for task in range (len(Mlists)):
                file1.write(Mlists[task])
                file1.write("\n")
           file1.write("\nSide Tasks\n")
           for task in range (len(Slists)):
                file1.write(Slists[task])
                file1.write("\n")
           file1.close()

       elif sel == 5:
        boole = False
 
   file1.close()