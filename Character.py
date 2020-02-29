# Character Class
# Created by Xiangpu Chen
# Version 0.0.3
# 02/28/2020

# import
from Custom_Exception import WrongDataType
from __init__ import debugging, testing
#

'''
Character class object, should be use to create all character memebers
'''

class Character:
    def __init__(self, name, character_index):
        self.set_character_name(name)
        self.set_character_index(character_index)

    # setter
    def set_character_name(self, name):
        if isinstance(name,str):
            self.name = name
            return name
        else:
            raise WrongDataType(name, str())
    
    #setter
    def set_character_index(self, index):
        if isinstance(index, int):
            self.index = index
            return index
        else:
            raise WrongDataType(index, int())

if debugging and testing:
    print("---From Character.py---")
    print("Creating Character...")
    try:
        hi = Character("Conrad",1)
        print("Character name: " + str(hi.name))
        print("Character index: " + str(hi.index))
        print("Character creation sucessful!")
    except WrongDataType as e:
        print("Character creation failed...")
        print(str(e))
    print("---End of Character.py---")