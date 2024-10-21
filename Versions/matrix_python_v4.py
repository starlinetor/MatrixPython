from concurrent.futures import thread
import curses
from tkinter import Frame
from matrix_utils import randint_exception, remove_excess, matrix_char, copy_color, join_list_list_str
import time
import random

def frame_renderer (
                    #lists
                    frame: list[str], 
                    frame_temp: list[str],
                    line: list[str],
                    colums_positions: list[int],
                    #numbers
                    width: int, height: int, colums_lenght: int , change_prob: float
                    ) -> list[str]:
    
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
    remove_excess(frame_temp, height)

    return frame

def draw_matrix(stdscr) -> None:

    #settings
    stdscr.nodelay(True)

    #constants
    height:int 
    width:int
    height, width = stdscr.getmaxyx()

    matrix_width : int = width - 1
    matrix_height: int = height - 1

    colums_lenght: int = 18
    fps: int = 48
    change_prob: float = 0.8

    colums_positions: list[int] = []
    frame: list[str] = [" "*matrix_width+"\n"]*matrix_height
    frame_temp: list[str] = [" "*matrix_width+"\n"]*matrix_height
    line : list[str] = [" "]*matrix_width + ["\n"]

    #clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    #variables
    key = 0

    #start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)

    frames = 0

    while key != ord('q'):

        frames += 1

        #initialization
        stdscr.clear()

        frame = frame_renderer(frame, frame_temp, line, colums_positions, matrix_width, matrix_height, colums_lenght, change_prob)    
        stdscr.addstr(0,0,"".join(reversed(frame)),curses.color_pair(1))

        statusbarstr = f"Press 'q' to exit | STATUS BAR | Matrix_Python | Frames : {frames}"

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        #wait for next input
        key = stdscr.getch()

        stdscr.refresh()

        time.sleep(1/fps)

def main():
    curses.wrapper(draw_matrix)

if __name__ == "__main__":
    main()