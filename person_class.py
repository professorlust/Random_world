from randomizer import *

class creature:
    '''Everything that breathes is one of these.'''
    def num_of_legs(self, num_of_legs):
        self.num_of_legs = num_of_legs
        num_of_legs = random.randint(1, 100)
        if num_of_legs <=35:
            return "2"
        elif num_of_legs > 35 and x <= 70:
            return "4"
        elif num_of_legs > 70 and x <= 95:
            return "8"
        else:
            return "6"


class person(creature):
    #default person class; to be a subclass of creature
    def __init__(self, person_name):
        self.person_name = person_name
    number_of_legs = 2 #class-level attribute
"""
Figured it out on my break here at Lowe's.
It would seem that in this case, the
person_name var takes in the x var from
main.py. I still have a lot to learn, but
I'm making a little progress.
"""
