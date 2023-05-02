#!/bin/python

import sys, colorama
import os

print(f"{colorama.Fore.YELLOW}AlphaLang{colorama.Fore.RESET} interpreter.\nCoded by {colorama.Fore.BLUE}nlasted{colorama.Fore.RESET}");

try:
    filename = str(sys.argv[1])
    print(f"\n{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} File read successfully")
except:
    print(f"\n{colorama.Fore.RED}[-]{colorama.Fore.RESET} Could not open the file.")

if filename.__contains__("alp") != True:
    print("Not an alphalang file. (*.alp)")
    exit()

with open(filename, 'r') as file:
    alphacode = file.readlines()

bash = ""

print(str(len(alphacode)) + " lines total.\n")

for command in alphacode:
    match command:
        case "a\n":
            bash = bash + "a"
        case "b\n":
            bash = bash + "b"
        case "c\n":
            bash = bash + "c"
        case "d\n":
            bash = bash + "d"
        case "e\n":
            bash = bash + "e"
        case "f\n":
            bash = bash + "f"
        case "g\n":
            bash = bash + "g"
        case "h\n":
            bash = bash + "h"
        case "i\n":
            bash = bash + "i"
        case "j\n":
            bash = bash + "j"
        case "k\n":
            bash = bash + "k"
        case "l\n":
            bash = bash + "l"
        case "m\n":
            bash = bash + "m"
        case "n\n":
            bash = bash + "n"
        case "o\n":
            bash = bash + "o"
        case "p\n":
            bash = bash + "p"
        case "q\n":
            bash = bash + "q"
        case "r\n":
            bash = bash + "r"
        case "s\n":
            bash = bash + "s"
        case "t\n":
            bash = bash + "t"
        case "u\n":
            bash = bash + "u"
        case "v\n":
            bash = bash + "v"
        case "w\n":
            bash = bash + "w"
        case "x\n":
            bash = bash + "x"
        case "y\n":
            bash = bash + "y"
        case "z\n":
            bash = bash + "z"
        case "sp\n":
            bash = bash + " "
        case "dsh\n":
            bash = bash + "-"
        case "pnt\n":
            bash = bash + "."
        case "vel\n":
            bash = bash + "|"
        case "and\n":
            bash = bash + "&"
        case "sla\n":
            bash = bash + "/"
        case "reset\n":
            bash = ""
        case "start\n":
            os.system(bash)