"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""
import datetime


class WorkStartError(ValueError):
    """classdoc"""
    pass
class WorkEndError(ValueError):
    """classdoc"""
    pass
class FactoryItter():
    """classdoc"""
    def __init__(self,data:list):
        """methoddoc"""
        self.data=data


    def __iter__(self):
        """methoddoc"""
        return self

    def __next__(self):
        """methoddoc"""
        if not self.data:
            raise StopIteration
        return self.data.pop(0)

class Factory():
    """classdoc"""
    def __init__(self):
        """methoddoc"""

        self.all_workers = {}

    def __iter__(self):
        """methoddoc"""
        result=[]
        #for name,v in self.all_workers.items():
            #result.append((name,v[1]-v[0]))
        return FactoryItter(result)

    def addstarttime(self,name:str,hour:int , min:int,sec:int):
        """methoddoc"""
        timp=datetime.datetime()
        if name not in self.all_workers.keys():
            self.all_workers[name]=[0,0]
        else:
            if self.all_workers[name][0]:
                raise WorkStartError(name,self.all_workers[name][0])
            else:
                self.all_workers[name][0]=start_time
        if self.all_workers[name][0] and self.all_workers[name][1]:
            self.all_workers[name] = tuple(self.all_workers[name])


    def addendtime(self,name:str,end_time:datetime):
        """methoddoc"""
        if name not in self.all_workers.keys():
            self.all_workers[name]=[0,0]
        else:
            if self.all_workers[name][1]:
                raise WorkEndError(name,self.all_workers[name][1])
            else:
                self.all_workers[name][1]=end_time
        if self.all_workers[name][0] and self.all_workers[name][1]:
            self.all_workers[name] = tuple(self.all_workers[name])



day1=Factory()

try:
    day1.addstarttime("Joe",datetime.datetime(2021,6,12,9,1,20))
except ValueError:
    pass

try:
    day1.addstarttime("Ana",datetime.datetime(2021,6,12,9,3,15))
except ValueError:
    pass

try:
    day1.addstarttime("Tim",datetime.datetime(2021,6,12,9,4,25))
except ValueError:
    pass
try:
    day1.addstarttime("Tim",datetime.datetime(2021,6,12,9,4,30))
except ValueError:
    pass

try:
    day1.addendtime("Joe",datetime.datetime(2021,6,12,16,1,20))
except ValueError:
    pass

try:
    day1.addendtime("Ana",datetime.datetime(2021,6,12,18,4,15))
except ValueError:
    pass

try:
    day1.addendtime("Tim",datetime.datetime(2021,6,12,18,5,25))
except ValueError:
    pass
try:
    day1.addendtime("Tim",datetime.datetime(2021,6,12,18,5,30))
except ValueError:
    pass


with open("fisout.txt","w") as fis:
    for x in day1:
        fis.write(str(x)+ " ")


