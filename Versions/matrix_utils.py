import random

def randint_exception(max: int, exceptions: list[int]) -> int:
    '''
    Given a max value returns an int from 1 to the max value\n
    Does not return the values in the expetion list
    '''

    valid_values: list[int] = []

    #generating list of valid values
    #first we generate all possible values
    for i in range(1,max+1,):
        valid_values.append(i)
        
    #we remove not valid values
    for exception in exceptions:
        if exception in valid_values :
            valid_values.remove(exception) 

    if(len(valid_values) == 0):
        raise ValueError ("No valid values left")
    
    #chose a random valid value
    return valid_values[random.randint(0,len(valid_values)-1)]

def remove_excess(generic_list: list, max: int) -> None:
    '''
    Given a list it removes the first element untill the list shorter or equal to the max value
    '''
    while len(generic_list)>max:
        generic_list.pop(0)

def matrix_char(char_number: int = -1, max_number: int = -1) -> str:
    '''
    Returns a random char for a matrix like effect\n
    The char is colored following a green gradient\n
    Smaller char_number result in a more faded color
    '''
    if(char_number == -1 or max_number ==-1):
        return chr(random.randint(33,126))
    else:
        red = 0
        green = int(float((char_number+1)/(max_number+1))*255)
        blue = 0
        return f"\033[38;2;{red};{green};{blue}m{chr(random.randint(33,126))}\033[0m"
    
def copy_color(string_to_copy: str, new_str) -> str:
    '''
    Given a string with a Ansi escape color and a clean string the function returns\n
    the clean string with the color of the old one
    '''

    string_to_copy = string_to_copy.encode('unicode_escape').decode('ascii')
    return string_to_copy[:string_to_copy.find("m")+1].encode('ascii').decode('unicode_escape')+new_str+'\033[0m'

def join_list_list_str(list_list_str: list[list[str]]) -> str:
    '''
    Given a list of lists of strings it returns the string from joining all strings
    '''

    list_str: list[str] = []

    for element in list_list_str: 
        list_str.append("".join(element))
    
    return "".join(list_str)