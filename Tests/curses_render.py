import curses
from lib2to3.main import StdoutRefactoringTool 

def draw_matrix(stdscr) -> None:

    #settings
    stdscr.nodelay(True)

    #clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    #variables
    key = 0
    i = 0

    #start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    string_to_render_0:str = (  "db   db d88888b db      db       .d88b.       db   d8b   db  .d88b.  d8888b. db      d8888b.\n" 
                                "88   88 88'     88      88      .8P  Y8.      88   I8I   88 .8P  Y8. 88  `8D 88      88  `8D\n" 
                                "88ooo88 88ooooo 88      88      88    88      88   I8I   88 88    88 88oobY' 88      88   88\n" 
                                "88~~~88 88~~~~~ 88      88      88    88      Y8   I8I   88 88    88 88`8b   88      88   88\n" 
                                "88   88 88.     88booo. 88booo. `8b  d8'      `8b d8'8b d8' `8b  d8' 88 `88. 88booo. 88  .8D\n" 
                                "YP   YP Y88888P Y88888P Y88888P  `Y88P'        `8b8' `8d8'   `Y88P'  88   YD Y88888P Y8888D'")    

    string_to_render_1:str= "Hello World"

    while key != ord('q'):
        i = i+1
        #initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        stdscr.addstr(0,0,string_to_render_0,curses.color_pair(1))
        stdscr.addstr(7,0,"Frames done : " + str(i),curses.color_pair(1))


        stdscr.refresh()


        #wait for next input
        key = stdscr.getch()

def main():
    curses.wrapper(draw_matrix)

if __name__ == "__main__":
    main()