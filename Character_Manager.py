from Character import Character
from __init__ import debugging, testing, path
import json

class CharacterManager:
    character_list = []
    file_list = []
    current_character = None

    @staticmethod
    def generate_character_list():
        with open('character_list.json', 'r') as f:
            character_dict = json.load(f)
        for character in character_dict:
            CharacterManager.character_list.append(Character(character['Name'],character['Index']))
        if(len(CharacterManager.character_list) == 0 or CharacterManager.character_list == []):
            raise Exception("Failed to generater character list")
        CharacterManager.current_character = CharacterManager.character_list[0]
        CharacterManager.generate_file_list()

    @staticmethod
    def generate_file_list():
        new_list = []
        if CharacterManager.current_character == None:
            raise Exception("Character not found!")
        for i in range(24):
            new_list.append(path+CharacterManager.current_character.name+"/-"+("{:02d}".format(i))+".mp3")
        new_list.append(path+CharacterManager.current_character.name+"/-short_intro.mp3")
        new_list.append(path+CharacterManager.current_character.name+"/-long_intro.mp3")
        CharacterManager.file_list = new_list


    @staticmethod
    def search_character_by_name(name):
        for character in CharacterManager.character_list:
            if(character.name == name):
                return character.index
        return -1

    @staticmethod
    def set_current_character(name):
        index_of_character = CharacterManager.search_character_by_name(name)
        if(index_of_character != -1):
            CharacterManager.current_character = CharacterManager.character_list[index_of_character]
            CharacterManager.generate_file_list()
        else:
            raise Exception("Character not found!")

