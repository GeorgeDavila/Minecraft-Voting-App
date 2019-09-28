# Copryright 2019 George Davila Durendal
#See here for OS commands to open links:   https://dwheeler.com/essays/open-files-urls.html
import os #to use system commands

#Reference script, do not use to generate your app, just edit the _windows.py, _mac.py and _.linuxandunix.py individually

print('Thanks for using the Minecraft Voter App!')

txtfilename = "VoteLinks.txt"

file1 = open( txtfilename, "r+" )

file_URLs = file1.readlines() 

'''if file1.mode == 'r':
    myURL = file1.read() 
    file_URLs = file1.readlines() 
else:
    print("something went wrong trying to open your text (.txt) file! Please check and try again!") '''



#print(myURL)

print( file1.readlines() )
#URL_list = '[' + myURL.replace('http', ', http') + ']'
#URL_list = list( URL_list.replace('[, ', '[') )

#print( file_URLs )

for i in file_URLs:
    print(i)
    os.system( "start " + i )

#Be sure to leave spaces at the end of the os.system function input string! E.g. it should be "open " not "open" for the mac command, notice the space before the quotation mark. 
#windows_cmd = "cmd /c start " 
#windows_cmd2 = "start " 
#mac_cmd = "open " 
#linux_cmd = "xdg-open "  #Also works for Unix 

#my_app_sys = "windows" #Bit redundant, can remove this if you want. Only leave it in because of personal preference.  

#os.system( "start " + myURL )



print("Opened the link!")