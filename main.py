import curses

def menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(0)
    selection = -1
    option = 0

    while selection < 0:
        graphics = [0]*5
        graphics[option] = curses.A_REVERSE

        stdscr.addstr(10,20, """

                                                  .-""...
                                                 F   .-'
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


        """)

        stdscr.addstr(32,53, "PLAY", graphics[0])
        stdscr.addstr(33,52, "ABOUT", graphics[1])
        stdscr.addstr(34, 50, "CREATOR", graphics[2])
        stdscr.addstr(35, 49, "EXIT", graphics[3])
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

        selection2 = -1
        option2 = 0

        while selection2 < 0:
            graphics = [0]*5
            graphics[option] = curses.A_REVERSE

            stdscr.addstr(5,5 ,"INCOMING MESSAGE")
            stdscr.addstr(60,5, "ACCEPT", graphics[0])
            stdscr.addstr(60,100, "ACCEPT", graphics[0])

            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_UP:
                option2 = (option-1)% 5

            elif key == curses.KEY_DOWN:
                option2 = (option+1)% 5

            elif key == ord("\n"):
                selection2 = option2

        stdscr.clear()

        if selection == 0:
            pass

if (__name__ == "__main__"):
    curses.wrapper(menu)
