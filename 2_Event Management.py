#Extend an existing Event class by adding an attribute to keep track of the number of participants. 
#Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.people = []
            self.counter = 0
             
        def add_participant(self):
            self.counter += 1
            print(self.people)
        
        def get_participant_count(self):
            return self.counter
     
        








            