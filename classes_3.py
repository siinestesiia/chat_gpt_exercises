# Chat GPT exercises about Classes.


class Person:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height =  height
        self.weight = weight

    # Body Max Index (BMI) 
    def bmi(self):
        result = self.weight / (self.height**2)
        return f'The Body Max Index is: {result}.'
    
    def can_vote(self):
        if self.age >= 18:
            return 'This person can vote.'
        elif self.age < 18:
            return 'This person can\'t vote.'


npc_1 = Person('Mike', 19, 180, 80)
print(npc_1.bmi())        
print(npc_1.can_vote())        
