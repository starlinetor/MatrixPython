import curses
import matrix_utils

def draw_matrix(stdscr) -> None:

    #settings
    stdscr.nodelay(True)

    #constants
    height = 50
    width = 100
    colums_lenght: int = 18
    change_prob: float = 0.8
    fps : int = 24

    #fixing terminal size
    curses.resize_term(height, width)

    #runtime varable
    colums_positions: list[int] = []
    frame: list[list[str]] = [[" "]*width + ["\n"]]*height
    frame_moving: list[list[str]] = [[" "]*width + ["\n"]]*height

    #setting the last charcter of the line to \n
    line : list[str] = [" "]*width + ["\n"]

    #clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    #variables
    key = 0

    #start colors in curses
    curses.start_color()

    while key != ord('q'):
        #initialization
        stdscr.clear()






        stdscr.refresh()

        #wait for next input
        key = stdscr.getch()

def main():
    curses.wrapper(draw_matrix)

if __name__ == "__main__":
    main()