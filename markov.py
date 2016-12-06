# -*- coding: utf-8 -*-

def make_command (s):
    if s=='>end':
        return s
    else: 
        if s.find("->") != -1:
            i = s.find("->")
            return (s[0:i], "->", s[i+2:])
        elif s.find("=>") != -1:
            i = s.find("=>")
            return (s[0:i], "=>", s[i+2:])
        else:
            return ('e', "Error", 'e')

def newfile ():
    filename = str( input("Please enter the name of a new Markov algorithm file (file extension will be added automatically):\n") ) + str('.txt')
    file = open(filename, "wt")
    print("Enter commands for algorhithm (or enter '>end' if you entered all needed commands)\n")
    i = 1
    command = []
    s = ""
    while True:
        s = input(str(i) + ". ")
        if s!='>end':
            com = make_command(s)
            if com[1] == "Error":
                print("Invalid command. Try again:\n")
                continue
            else:
                file.write(str(s)+str('\n'))
                command.append(com)
                i += 1
        else:
            break
    file.close()
#    print("")
    return command

def readfile():
    filename = str( input("Please enter the name of a Markov algorithm file you want to open (file extension will be added automatically):\n") ) + str('.txt')
    import os.path
    while not os.path.isfile(filename):
        filename = str(input("File doesn't exist. Try another name:\n")) + str('.txt')
    file = open(filename, "rt")
    command = []
    s = ""
    print("")
    i = 0
    while True:
        s = file.readline()
        if s!='': 
            if s[-1] == '\n':
                com = make_command(s[0:-1])
            else:
                com = make_command(s)
            command.append(com)
            if com[1] == "Error":
                input("Error: file contains an invalid command. Press 'Enter' to exit the program\n")
                file.close()
                return command
            else:
                print ( str(i+1) + '. ' + str(command[i][0]) + str(command[i][1]) + str(command[i][2]) )
                i += 1
        else:
            break
    file.close()
    return command

def print_hint(f, str):
    if str != '':
        print( f*' ' + len(str)*'^')
    else:
        print("")
    pass

def run(command):
    line = []
    while True:
        line = []
        line.append(input("\nEnter a line (or '>end' for exit):\n\n"))
        print("")
        if line[-1] == '>end':
            break
        j = 1
        while j == 1:
            j = 0
            for i in range(0, len(command)):
                if command[i][0] == '':
                    newline = str( command[i][2] ) + str( line[-1] )
                    print(newline)
                    print_hint(0, command[i][2])
                    if len(line) >= 2 and (newline == line[-1] or newline == line[-2]):
                            input("Your algorithm contains an infinite loop. Press 'Enter' to exit the program")
                            pass
                    line.append(newline)
                    if command[i][1] == '->':
                        j = 1
                    else:
                        j = 0
                    break
                else:
                    f = line[-1].find( command[i][0] )
                    if f != -1:
                        newline = str( line[-1][0:f] ) + str( command[i][2] ) + str( line[-1][f+len(command[i][0]):] )
                        print(newline)
                        print_hint(f, command[i][2])
                        if len(line) >= 2 and (newline == line[-1] or newline == line[-2]):
                            input("Your algorithm contains an infinite loop. Press 'Enter' to exit the program")
                            pass
                        line.append(newline)
                        if command[i][1] == '->':
                            j = 1
                        else:
                            j = 0
                        break
    pass
#----------------------------------------------------------------------------------------------------------------------------

while True:
    mode = int(input("Welcome to Markov algorithm interpreter!\nIf you want to create a new algorithm enter\t'1'\nTo open existing algorithm enter\t\t'2'\n"))
    if mode == 1:
        run(newfile())
        break
    elif mode == 2:
        command = readfile()
        if command[(len(command)-1)][1] != "Error":
            run(command)
            break
        else:
            break
    else:
        print ("Error, try again...")