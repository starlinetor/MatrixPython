import os, time, random, sys

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

def matrix_char() -> str:
    '''
    Returns a random char for a matrix like effect\n
    Missing functionality : random char -> default X
    '''

    return chr(random.randint(33,126))

height: int = 25
width: int = 100 
colums_lenght: int = 12
change_prob: float = 0.8

colums_positions: list[int] = []
frame: list[str] = [" "*width+"\n"]*height
frame_temp: list[str] = [" "*width+"\n"]*height

#setting the last charcter of the line to \n
line : list[str] = [" "]*width + ["\n"]

while True:
    #clear the canvas
    os.system('cls')

    #add a new line
    colums_positions.append(randint_exception(width, colums_positions))
    remove_excess(colums_positions, colums_lenght)

    for i in range(width):
        if i in colums_positions:
            line[i] = matrix_char()
        else:
            line[i] = " "

    #add the line to the frame
    frame.append("".join(line))

    for line_frame in frame:
        for i in range(len(line_frame)-1):
            if(line_frame[i] == " "):
                line[i] = " "
            elif(random.random() < change_prob):
                line[i] = matrix_char()
            else:
                line[i] = line_frame[i]
        frame_temp.append("".join(line)) 
    
    for line_frame in frame_temp:
        frame.append(line_frame)

    #crop the frame
    remove_excess(frame, height)
    
    #print the frame
    print("".join(reversed(frame)))
    #delay
    time.sleep(0.02)
