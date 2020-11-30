import curses
import sys
import time
from pygame import mixer

def animation(stdscr):
    curses.wrapper(opt1)


def opt1(stdscr):
    #type = mixer.Sound('typing.mp3')
    h, w = stdscr.getmaxyx()
    x = w//2 - 18//2
    y = h//2
    stdscr.clear()
    stdscr.nodelay(0)
    selection2 = -1
    option2 = 0
    ani = 0

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

            effect = mixer.Sound('key.wav')

            stdscr.addstr("""













                                                                                                                ,--._,--.
                                                                                                               ,'  ,'   ,-`.
                                                                                                    (`-.__    /  ,'   /
                                                                                                     `.   `--'        \__,--'-.
                                                                                                       `--/       ,-.  ______/
                                                                                                         (o-.     ,o- /
                                                                                                          `. ;        -
                                                                                                           |:          -
                                                                                        KEBAB INDUSTRIES  ,'`       ,   -
                                                                                                         (o o ,  --'     :
                                                                                                          \--','.        ;
                                                                                                           `;;  :       /
                                                                                                             ;'  ;  ,' ,'
                                                                                                            ,','  :  '
                                                                                                            \ \   :

                                                                                        █ ▄▄  █▄▄▄▄ ▄███▄     ▄▄▄▄▄   ▄███▄      ▄     ▄▄▄▄▀ ▄▄▄▄▄
                                                                                        █   █ █  ▄▀ █▀   ▀   █     ▀▄ █▀   ▀      █ ▀▀▀ █   █     ▀▄
                                                                                        █▀▀▀  █▀▀▌  ██▄▄   ▄  ▀▀▀▀▄   ██▄▄    ██   █    █ ▄  ▀▀▀▀▄
                                                                                        █     █  █  █▄   ▄▀ ▀▄▄▄▄▀    █▄   ▄▀ █ █  █   █   ▀▄▄▄▄▀
                                                                                         █      █   ▀███▀             ▀███▀   █  █ █  ▀
                                                                                          ▀    ▀                              █   ██




            """)
            stdscr.refresh()
            time.sleep(3)
            stdscr.clear()
            stdscr.addstr("""




7468657265206973206e6f20657363617065



                                                                                                                                                            7468657265206973206e6f20657363617065



                                                                                                    7468657265206973206e6f20657363617065

                                                                                 sSSs   .S  S.       .S    S.    .S_sSSs      sSSs_sSSs     .S_SSSs     .S_sSSs
                                                                7468657265206973206e6f20657363617065                d%%SP  .SS  SS.     .SS    SS.  .SS~YS%%b    d%%SP~YS%%b   .SS~SSSSS   .SS~YS%%b
                                                                               d%S'    S%S  S%S     S%S    S&S  S%S   `S%b  d%S'     `S%b  S%S   SSSS  S%S   `S%b
                                                                               S%|     S%S  S%S     S%S    d*S  S%S    S%S  S%S       S%S  S%S    S%S  S%S    S%S
                                                                               S&S     S&S  S&S     S&S   .S*S  S%S    d*S  S&S       S&S  S%S SSSS%S  S%S    S&S
                                                                               Y&Ss    S&S  S&S     S&S_sdSSS   S&S   .S*S  S&S       S&S  S&S  SSS%S  S&S    S&S
                                                                               `S&&S   S&S  S&S     S&S~YSSY%b  S&S_sdSSS   S&S       S&S  S&S    S&S  S&S    S&S7468657265206973206e6f20657363617065
                                                                                 `S*S  S&S  S&S     S&S    `S%  S&S~YSY%b   S&S       S&S  S&S    S&S  S&S    S&S
                    7468657265206973206e6f20657363617065                                                              l*S  S*S  S*b     S*S     S%  S*S   `S%b  S*b       d*S  S*S    S&S  S*S    d*S
                                                                                 .S*P  S*S  S*S.    S*S     S&  S*S    S%S  S*S.     .S*S  S*S    S*S  S*S   .S*S
                                                                               sSS*S   S*S   SSSbs  S*S     S&  S*S    S&S   SSSbs_sdSSS   S*S    S*S  S*S_sdSSS
                                                                               YSS'    S*S    YSSP  S*S     SS  S*S    SSS    YSSP~YSSY    SSS    S*S  SSS~YSSY
                                                                                       SP           SP          SP                                SP
                                                                                       Y            Y           Y                                 Y

                                                                                                                                                THE HITMAN SCAM



                                                                                                                                                                7468657265206973206e6f20657363617065



7468657265206973206e6f20657363617065



                                                                                        7468657265206973206e6f20657363617065

                                                                                                                        7468657265206973206e6f20657363617065



                                                                                                                                                            7468657265206973206e6f20657363617065
            """)
            stdscr.refresh()
            time.sleep(3)


            stdscr.clear()
            stdscr.addstr(0,0,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t")
            curses.curs_set(1)
            words = "Based on true events."
            curses.curs_set(0)
            for char in words:
                curses.curs_set(1)
                time.sleep(0.3)

                stdscr.addch(char)
                effect.play()
                #type.play()
                stdscr.refresh()

            time.sleep(4)
            stdscr.clear()



            curses.curs_set(0)
            stdscr.refresh()



            stdscr.clear()
            stdscr.addstr(y,x-3,"January 28th 2011,", curses.A_BOLD)
            stdscr.refresh()
            stdscr.refresh()
            time.sleep(5)




            stdscr.clear()

            stdscr.addstr(0,0,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")

            words = """
                                                                    The slik road is put online with the following onion link http://tydgccykixpbu6uz.onion.

"""
            for char in words:

                time.sleep(0.03)
                stdscr.addch(char)
                stdscr.refresh()

            curses.curs_set(0)

            stdscr.addstr(55,99, "press enter to continue...", graphics[0])



            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                option2 = (option2-1)% 5

            elif key == curses.KEY_RIGHT:
                option2 = (option2+1)% 5

            elif key == ord("\n"):
                selection2 = option2
        stdscr.clear()
#BRANCH 2
        if selection2 == 0:
            curses.wrapper(opt2)

    except curses.error:
        pass

def opt2(stdscr):
        curses.curs_set(0)
        stdscr.clear()
        stdscr.nodelay(0)
        selection3 = -1
        option3 = 0

        try:

            stdscr.addstr("""
FriendlyChemist
 ,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.
 |can u please get dread pirate roberts to message me RIGHT away ?   |
 |its very serious... a matter of life and death. also has to do     |
 | with the identities of a dozen top vendors and thousands of silk  |
 |road customers                                                     |
_;.................................................................'
                                                        3/13/2013




            """)

#import sys
#from time import sleep
#
#words = "This is just a test :P"
#for char in words:
#    sleep(0.1)
#    sys.stdout.write(char)
#    sys.stdout.flush()



            while selection3 < 0:


                graphics = [0]*5
                graphics[option3] = curses.A_REVERSE



    #            #stdscr.addstr(2,0, """
    #From : FriendlyChemist
    #To : Dread Pirate Roberts, 3/13/2013

    #can u please get dread pirate roberts to message me RIGHT away ?
    #its very serious... a matter of life and death. also has to do with the identities of a dozen
    #top vendors and thousands of silk road customers
#    its very important so please get him me right away. i will not talk to anyone but dread
    #pirate roberts so please do not ask me what it is conserning



            #    """)

                stdscr.addstr(55,4, """What can I do for you?""", graphics[0])
                stdscr.addstr(55,90, "Ignore him", graphics[1])


                stdscr.refresh()

                key = stdscr.getch()

                if key == curses.KEY_LEFT:
                    option3 = (option3-1)% 5

                elif key == curses.KEY_RIGHT:
                    option3 = (option3+1)% 5

                elif key == ord("\n"):
                    selection3 = option3




            if selection3 == 0:
                curses.wrapper(opt3)

            if selection3 == 1:
                stdscr.clear()
                curses.wrapper(opt3s)

        except curses.error:
            pass


#this is if you choose ignore him
def opt3s(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(0)
    selection3s = -1
    option3s = 0

    try:
        words = "[*] FriendlyChemist spams you over and over again, it seems pretty important"
        for char in words:
            time.sleep(0.03)
            stdscr.addch(char)
            stdscr.refresh()

        while selection3s < 0:

            graphics = [0]*5
            graphics[option3s] = curses.A_REVERSE



            stdscr.addstr(55,4, "Read the message again", graphics[0])
            stdscr.addstr(55,90, "Respond with: What can i do for you?", graphics[1])

    #
            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                option3s = (option3s-1)% 5

            elif key == curses.KEY_RIGHT:
                option3s = (option3s+1)% 5

            elif key == ord("\n"):
                selection3s = option3s

        stdscr.clear()

        if option3s == 0:
            curses.wrapper(opt2)

        if option3s == 1:
            curses.wrapper(opt3)

    except curses.error:
        pass


def opt3(stdscr):
    curses.curs_set(0)

    stdscr.nodelay(0)
    selection4 = -1
    option4 = 0

    try:

        stdscr.addstr(8, 60,"""
                                                                                                             YOU
                                                                                    .''''''''''''''''''''''''',
                                                                                    |What can i do for you?   |
                                                                                    '.........................;_
                                                                                    3/14/2013

        """)
        stdscr.refresh()
        time.sleep(2)


        stdscr.addstr(15,0, """
  FriendlyChemist
,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.
|When are you paying lucydrop? ive been waitin and he keeps sayin |
|hes waitin for you to pay him, u don know me but im his supplier |
|The only reason i lent him 900k of product is cuz he showed me   |
|chat logs of how you made him #1 seller on silkroad.             |
_;................................................................'
                                                        3/14/2013


        """)

        while selection4 < 0:
            graphics = [0]*5
            graphics[option4] = curses.A_REVERSE

            stdscr.addstr(55,4, "I dont know what your talking about", graphics[0])
            stdscr.addstr(55,90, "Lucydrop made it up", graphics[1])

    #
            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                option4 = (option4-1)% 5

            elif key == curses.KEY_RIGHT:
                option4 = (option4+1)% 5

            elif key == ord("\n"):
                selection4 = option4



        if selection4 == 0:
            curses.wrapper(opt4)

        if selection4 == 1:
            curses.wrapper(opt4s)

    except curses.error:
        pass

#selection i dont know what your talking about
def opt4(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(0)
    selection5 = -1
    option5 = 0

    try:


        stdscr.addstr(26,0, """

  FriendlyChemist
,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.
|When are you paying lucydrop? ive been waitin and he keeps sayin |
|hes waitin for you to pay him, u don know me but im his supplier |
|The only reason i lent him 900k of product is cuz he showed me   |
|chat logs of how you made him #1 seller on silkroad.             |
_;................................................................'
                                                        3/14/2013


        """)


        stdscr.addstr(15,0, "[NOTE]apparently FriendlyChemist has placed a keylogger this could be a lie", curses.A_BLINK)
        time.sleep(2)

        while selection5 < 0:
            graphics = [0]*5
            graphics[option5] = curses.A_REVERSE

            stdscr.addstr(55,4, "A keylogger?", graphics[0])
            stdscr.addstr(55,90, "Lucydrop made it up", graphics[1])

    #
            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                option5 = (option5-1)% 5

            elif key == curses.KEY_RIGHT:
                option5 = (option5+1)% 5

            elif key == ord("\n"):
                selection5 = option5

        stdscr.clear()

        if selection5 == 0:
            curses.wrapper(keylogger)

        if selection5 == 1:
            curses.wrapper(opt4s)

    except curses.error:
        pass
#selection lucydrop made it all up!

def opt4s(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(0)
    selection4s = -1
    option4s = 0

    try:

        words = """
i find it verry hard to believe. he showed the chat loggs, please dont screw me like this! my life is in danger because of this money i owe!
im not this kind of person but the only card i hav left to play is dropping 2 dozen vendor identities and thousands of customer details on
the web and the forums. i put a keylogger on lucydrops computer when he left the room one day, if u dont believe me here is lucy password info
login lucydrop
passyworld lucedad
"""

        for char in words:
            time.sleep(0.03)
            stdscr.addch(char)
            stdscr.refresh()

            stdscr.addstr(15,0, "[NOTE]apparently FriendlyChemist has placed a keylogger this could be a lie", curses.A_BLINK)

        while selection4s < 0:
            graphics = [0]*5
            graphics[option4s] = curses.A_REVERSE

            stdscr.addstr(55,4, "A keylogger?", graphics[0])
            stdscr.addstr(55,90, "I will try to contact lucydrop", graphics[1])

    #
            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                option4s = (option4s-1)% 5

            elif key == curses.KEY_RIGHT:
                option4s = (option4s+1)% 5

            elif key == ord("\n"):
                selection4s = option4s

        stdscr.clear()

        if selection4s == 0:
            curses.wrapper(keylogger)

        #if selection4s == 1:
        #    curses.wrapper(opt5)

    except curses.error:
        pass

def keylogger(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(0)
    selectionk = -1
    optionk = 0

    try:

        words = """

"""

        for char in words:
            time.sleep(0.03)
            stdscr.addch(char)
            stdscr.refresh()



        while selectionk < 0:
            graphics = [0]*5
            graphics[optionk] = curses.A_REVERSE

            stdscr.addstr(55,4, "A keylogger?", graphics[0])
            stdscr.addstr(55,90, "I will try to contact lucydrop", graphics[1])

    #
            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                optionk = (option4s-1)% 5

            elif key == curses.KEY_RIGHT:
                optionk = (optionk+1)% 5

            elif key == ord("\n"):
                selectionk = optionk

        stdscr.clear()

        if selection4s == 0:
            curses.wrapper(keylogger)

        #if selection4s == 1:
        #    curses.wrapper(opt5)

    except curses.error:
        pass
