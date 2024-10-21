import os, time, random, curses

#initializing stdcr
stdscr = curses.initscr()
#removes key imputs
curses.noecho()
#no enter required for keys
curses.cbreak()
#keypad mode
stdscr.keypad(True)




#terminate curses terminal
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
