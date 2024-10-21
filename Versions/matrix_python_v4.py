import curses 

def draw_matrix(stdscr) -> None:

    #clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    


def main():
    curses.wrapper(draw_matrix)

if __name__ == "__main__":
    main()