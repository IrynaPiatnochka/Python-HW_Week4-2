
class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
            
            
        def info(self):
            print(f"The vehicle with registration number '{self.registration_number}', type {self.type} belongs to {self.owner}. ")   
            
        def update_owner(self, new_owner):
            print(f'The vehicle was sold by {self.owner} to {new_owner}.')
            self.owner = new_owner
            
lexus = Vehicle('1339MN', 'SUV', 'Billy Bob')
            
lexus.info()
lexus.update_owner('Peter Johnson')

        
        