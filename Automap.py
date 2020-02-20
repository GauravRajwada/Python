import sys
import webbrowser

sys.argv
#Just because loaction always greater then 1 charecter
if (len(sys.argv)>1):
    location=" ".join(sys.argv[1:])
else:
    location=input("Enter the loction")

webbrowser.open("https://www.google.co.in/maps/place/"+location)