# Custom Exception Class
# Created by Xiangpu Chen
# Version 0.0.2
# 02/28/2020

class Error(Exception):
    pass

# given a assigned type/varibale, raise exception if the assigned type does not match with the required type
class WrongDataType(Error):
    def __init__(self, assigned_type, required_type):
        self.assigned_type = assigned_type
        self.required_type = required_type

    def __str__(self):
        return 'Error Code 100: Assigned data does not have the correct required data type.' + "\n" + \
            '{} is of type: '.format(self.assigned_type) + str(type(self.assigned_type)) + "\n" + \
                'But type ' + str(type(self.required_type)) + " is required"