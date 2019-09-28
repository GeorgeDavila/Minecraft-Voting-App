# Copryright 2019 George Davila Durendal
#See here for OS commands to open links:   https://dwheeler.com/essays/open-files-urls.html
import os #to use system commands

print('Thanks for using the Minecraft Voter App!')

txtfilename = "VoteLinks.txt"

file1 = open( txtfilename, "r+" ) #Make sure to use r+ as the option for open

file_URLs = file1.readlines() 

for i in file_URLs:
    print(i)
    if "xdg-open " + i == "xdg-open ":
        print("Something went wrong trying to open your text (.txt) file! Did you remember to put the links in? Please check and try again!")
    else: 
        os.system( "xdg-open " + i )

#Be sure to leave spaces at the end of the os.system function input string! E.g. it should be "open " not "open" for the mac command, notice the space before the quotation mark. 
#The os.system() function won't take a variable as an input -as it basically writes right to the command line- so we use different scripts for different systems
