
import curses
import sys
from time import sleep



def main(stdscr):
    h, w = stdscr.getmaxyx()
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(0)
    selection = -1
    option = 0

    while selection < 0:
        graphics = [0]*5
        graphics[option] = curses.A_REVERSE

        stdscr.addstr(10,20, """

                                                  .-""''._
                                                 F   .-''
                                                F   J
                                               I    I
                                                L   `.
                                                 L    `-._,
                                                  `-.__.-'            ##
                                                                     ###
                                             #                      ####
                                    _____   ##                 .---#####-...__
                                .--'     `-###          .--..-'    ######     ""`---....
                       _____.----.        ###`.._____ .'          #######
                                          ###       /       -.    ####### _.---
                                          ###     .(              #######
                                           #      : `--...        ######
                                           #       `.     ``.     ######
                                                     :       :.    #####
                                                   .'          )    ###
                                                 .'            /    ##
                                              _.'              |   .##
                                            ,:'                |     '
                                          .'                  <
                                         '                   |
                                        /                    |
                                       '                     .

             sSSs   .S  S.       .S    S.    .S_sSSs      sSSs_sSSs     .S_SSSs     .S_sSSs
            d%%SP  .SS  SS.     .SS    SS.  .SS~YS%%b    d%%SP~YS%%b   .SS~SSSSS   .SS~YS%%b
           d%S'    S%S  S%S     S%S    S&S  S%S   `S%b  d%S'     `S%b  S%S   SSSS  S%S   `S%b
           S%|     S%S  S%S     S%S    d*S  S%S    S%S  S%S       S%S  S%S    S%S  S%S    S%S
           S&S     S&S  S&S     S&S   .S*S  S%S    d*S  S&S       S&S  S%S SSSS%S  S%S    S&S
           Y&Ss    S&S  S&S     S&S_sdSSS   S&S   .S*S  S&S       S&S  S&S  SSS%S  S&S    S&S
           `S&&S   S&S  S&S     S&S~YSSY%b  S&S_sdSSS   S&S       S&S  S&S    S&S  S&S    S&S
             `S*S  S&S  S&S     S&S    `S%  S&S~YSY%b   S&S       S&S  S&S    S&S  S&S    S&S
              l*S  S*S  S*b     S*S     S%  S*S   `S%b  S*b       d*S  S*S    S&S  S*S    d*S
             .S*P  S*S  S*S.    S*S     S&  S*S    S%S  S*S.     .S*S  S*S    S*S  S*S   .S*S
           sSS*S   S*S   SSSbs  S*S     S&  S*S    S&S   SSSbs_sdSSS   S*S    S*S  S*S_sdSSS
           YSS'    S*S    YSSP  S*S     SS  S*S    SSS    YSSP~YSSY    SSS    S*S  SSS~YSSY
                   SP           SP          SP                                SP
                   Y            Y           Y                                 Y





                                         made by kebab ind.
        """)

        stdscr.addstr(32,53, "PLAY", graphics[0])
        stdscr.addstr(33,50, "ABOUT GAME", graphics[1])
        stdscr.addstr(34, 50, "CREATOR", graphics[2])
        stdscr.addstr(35, 50,  "INFO", graphics[3])
        stdscr.addstr(36, 49, "EXIT", graphics[4])
#
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            option = (option-1)% 5

        elif key == curses.KEY_DOWN:
            option = (option+1)% 5

        elif key == ord("\n"):
            selection = option
    stdscr.clear()



    if selection == 0:
        curses.curs_set(0)
        stdscr.clear()
        stdscr.nodelay(0)
        selection2 = -1
        option2 = 0

#TYPING EFFECT
#words = "This is just a test :P"
#for char in words:
#    sleep(0.1)
#    sys.stdout.write(char)
#    sys.stdout.flush()

        try:
            while selection2 < 0:
                graphics = [0]*5
                graphics[option2] = curses.A_REVERSE

                stdscr.addstr(10,45, """





                """)

                stdscr.addstr(55,10, "press enter to continue...", graphics[0])



                stdscr.refresh()

                key = stdscr.getch()

                if key == curses.KEY_LEFT:
                    option2 = (option2-1)% 5

                elif key == curses.KEY_RIGHT:
                    option2 = (option2+1)% 5

                elif key == ord("\n"):
                    selection2 = option2
            stdscr.clear()


        except curses.error:
            pass

    elif selection == 1:
        stdscr.clear()

        try:

                stdscr.addstr(0,0, """
GAME INFO \n\n\n
this game is about the hitman scam with the owner of the silkroad(ross ulbricht) aka dread pirate roberts

The ultimate goal of the game is not to get caught being the owner of the silkroad aswell as not get scammed by

several users. \n\n

the game is mostly text based aswell as a choose your own adveture game.\n\n

use the left and right arrow key to navigate between options and the enter key to select an option\n\n


PRESS ANY KEY TO GO BACK...
                 """)
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                curses.wrapper(main)


        except curses.error:
            pass

    elif selection == 2:
        stdscr.clear()

        try:

                stdscr.addstr(5,5, """
CREATOR Information\n\n\n

Kebab industries is a small orginisation I started with 2 friends, mostly small little game projects will be made\n\n


Buy me a coffee(PayPal): legoytcreators@gmail.com\n\n

PRESS ANY KEY TO GO BACK...
                """)
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                curses.wrapper(main)

        except curses.error:
            pass

    elif selection == 3:
        stdscr.clear()

        try:

                stdscr.addstr(5,5, """
BACKGROUNF INFORMATION\n\n\n


MAIN CHARACTERS:

Dread pirate roberts (YOU): the owner of the silkroad, real name Ross ulbricht

Lucydrop : Silkroad vendor(seller), from canada

Tony76 : Silkroad vendor(seller), from canada

FriendlyChemist : Middle man between the hells angels and Lucydrop

redandwhite : 'the hells angels' a motorbike gang which is experienced in drug selling on the streets

\n\n\n

Ross ulbricht was caught


PRESS ANY KEY TO GO BACK...
                """)
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                curses.wrapper(main)

        except curses.error:
            pass



if (__name__ == "__main__"):
    curses.wrapper(main)
