#/bin/bash 
my_name=$(zenity --entry --text="Enter your name")
zenity --info --text="$my_name\nWellcome to my test."
