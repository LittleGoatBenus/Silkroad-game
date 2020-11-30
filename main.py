import curses
import sys
import time
from options import *

from pygame import mixer

mixer.init()
mixer.music.load("menumusic2.mp3")
mixer.music.play(True)

def main(stdscr):
    h, w = stdscr.getmaxyx()
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(0)
    selection = -1
    option = 0
    #playsound('menumusic.mp3')


    while selection < 0:



        graphics = [0]*5
        graphics[option] = curses.A_REVERSE



        stdscr.refresh()

        stdscr.addstr(10,50, """                                                                                                                                    *
                                                                                                                                   +
                                                .                                                                     .-""''._                                        O                                 *
                                                                                                   +                 F   .-''           .                                                                               .
                                                                                                                    F   J                                -
        .                                               *                                                          I    I
                                                                                                                    L   `.                                                      +                           .
                                                                                                                     L    `-._,        .
                    .                                    - 0 -                              +                          `-.__.-'                                                                                       *

                                                                                                                #                                     .
                                                                                                        _____   ##                 .----------...__                         *                0            *
                                    *                                                               .--'     `-###          .--..-'                ""`---...........__                                                +
                                                                            ______________ _____.----.        ###`.._____ .'                                         '''''''''''___                                  .
                                                                                                              ###        /       -.             .---      \/ /                       ''''''....___
                                                                                                              ###      .(                                  \/      |/\                          '''..__
                                                                                                                #      : `--...                       _\_\__\    | /______/_
                                                                                                               #       `.     ``.                            \ / |/
                                                                                                                          :       :.             .   __ _-----'  |{,--------~
                                                                                        ,,_                              .'          )                         \ }{
                                                                                        (=-'                           .'            /                          }{{
                                                                                  /\/\  ))                           .'              |   .                      }}{
                                                                                ~/    \/ |                        ,:'                |     '                    {{}
                                                                                | )___(  |                      .'                  <                       -=-~{ .-^- _
                                                                                |/      ||                     '                   |                            '}
                                                                                |'      |'                    /                    |
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





                                                                                                  [*]PLAY WITH SOUND FOR FULL EXPERIENCE[*]
                                                                                              [*]ADVISED READ THE INFO AND ABOUT GAME SECTION                                                                            made by kebab ind.""")

        stdscr.addstr(32,122, "PLAY", graphics[0])
        stdscr.addstr(33,119, "ABOUT GAME", graphics[1])
        stdscr.addstr(34, 120, "CREATOR", graphics[2])
        stdscr.addstr(35,121,  "SKIP", graphics[3])
        stdscr.addstr(36, 121, "EXIT", graphics[4])
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



#BRANCH 1

    if selection == 0:
        mixer.music.stop()
        mixer.music.load("scary.mp3")
        mixer.music.play()
        curses.wrapper(animation)


#other menu selections
    elif selection == 1:
        stdscr.clear()

        try:

                stdscr.addstr(0,0, """
GAME INFO \n\n\n

[*] the messages arent exact 1:1 as the real ones\n
[*] do not spam the enter button or you will select options which are loading, click it once and have patience\n

this game is about the hitman scam with the owner of the silkroad(ross ulbricht) aka dread pirate roberts

The ultimate goal of the game is not to get caught being the owner of the silkroad aswell as not get scammed by

several users. \n\n

MAIN CHARACTERS:

Dread pirate roberts (YOU): the owner of the silkroad, real name Ross ulbricht\n\n

Lucydrop : Silkroad vendor(seller), from canada\n\n

Tony76 : Silkroad vendor(seller), from canada\n\n

FriendlyChemist : Middle man between the hells angels and Lucydrop\n\n

redandwhite : 'the hells angels' a motorbike gang which is experienced in drug selling on the streets\n\n

Nob : a buyer and seller\n\n

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
            curses.curs_set(0)
            stdscr.clear()
            stdscr.nodelay(0)
            selectionskip = -1
            optionskip = 0

            while selectionskip < 0:
                graphics = [0]*5
                graphics[optionskip] = curses.A_REVERSE

                stdscr.addstr(0,0, """
If you want to skip to certain parts
                                """)

                stdscr.addstr(1,0, "message1: FriendlyChemist : Requesting to speek with Dread pirate roberts(YOU)", graphics[0])
                stdscr.addstr(2,0, "message3: FriendlyChemist : When are you paying lucydrop?", graphics[1])
                stdscr.addstr(3,0, "message4: FriendlyChemist : i placed a keylogger on his computer!", graphics[2])
                stdscr.addstr(4,0,  "SKIP", graphics[3])
                stdscr.addstr(5,0, "EXIT", graphics[4])
        #
                stdscr.refresh()

                key = stdscr.getch()

                if key == curses.KEY_UP:
                    optionskip = (optionskip-1)% 5

                elif key == curses.KEY_DOWN:
                    optionskip = (optionskip+1)% 5

                elif key == ord("\n"):
                    selectionskip = optionskip
            stdscr.clear()

            if optionskip == 0:
                curses.wrapper(opt2)

            if optionskip == 1:
                curses.wrapper(opt3)

            if optionskip == 2:
                curses.wrapper(opt4)

        except curses.error:
            pass



if (__name__ == "__main__"):
    curses.wrapper(main)
