#!/usr/bin/python

import sys,os
err_noparam ="""Error:No parameters
Please, use --help to view HOW TO USE info"""

help_inf="""===================
How to use:
python main.py "Path to bash script file" "Output file name"
Example:
python main.py "/home/me/bash.sh" "Hello"
==================="""

C_start ="""#include <stdio.h>
#include <stdlib.h>
#define SHELLSCRIPT \"\\
"""
C_end = """
int main()
{
    system(SHELLSCRIPT);
    return 0;
}
"""
def file_parser(*args):
  if len(args) == 1:#If script have 1 arg
    #print(args[0])    
    file = open(args[0],"r")#Open file for reading.
    bash_source = file.read()#Read text from file to bash_source
    file.close()#Close file.
    bash_source = bash_source.replace("\"","\\\"")#Replacing " with \"
    bash_source = bash_source.replace("\n","\\n\\\n")#Replacing new line(\n) with \n\
    bash_source +="\\n\\ \n\""#Adding \n\" to end
    bash_source = C_start +bash_source+C_end #Make our code as C using magic
    #print(bash_source)
    file = open("a.c","w")#Open temp file
    file.write(bash_source)#Write our bash_source
    file.close()#Close file
    os.system("gcc a.c")#run gcc and compile out temp a.c file
    os.system("rm a.c")#remove our temp file
    
  elif len(args) == 2:
    #print(args[0],args[1])
    file = open(args[0],"r")#Open file for reading.
    bash_source = file.read()#Read text from file to bash_source
    file.close()#Close file.
    bash_source = bash_source.replace("\"","\\\"")#Replacing " with \"
    bash_source = bash_source.replace("\n","\\n\\\n")#Replacing new line(\n) with \n\
    bash_source +="\\n\\ \n\""#Adding \n\" to end
    bash_source = C_start +bash_source+C_end
    #print(bash_source)
    file = open(str(args[1])+".c","w")#Open our file using filename+c.If no file.c -> create
    file.write(bash_source)#Write our bash_source
    file.close()#Close file
    os.system("gcc "+str(args[1])+".c"+" -o "+str(args[1])+".out") #Run gcc + filename.c with output filename.out
    os.system("rm "+str(args[1])+".c")#remove our filename.c
  
def main():
  if len(sys.argv) < 2:#If script have less that 2 argv
    print(err_noparam)#Print Error message
  elif len(sys.argv) == 2:#if argv is 2
    if sys.argv[1] == "--help":#if argv is "--help" then do
      print(help_inf)#print help 
    else:#if argv not --help
      #print(sys.argv[1])
      file_parser(sys.argv[1])#Run function with param
  elif len(sys.argv) == 3:#if argv is 3
    file_parser(sys.argv[1],sys.argv[2])#Run function with param

if  __name__ ==  "__main__" :
  main()
