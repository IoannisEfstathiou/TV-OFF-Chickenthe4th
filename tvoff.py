import webbrowser
import time

def open_tabs():
    #Open the tabs that match the lyrics. Inbetween, pause to let the user read.
    webbrowser.open("https://www.google.com/search?q=Hey....")
    time.sleep(2)
    webbrowser.open("https://www.google.com/search?q=HEY!")
    time.sleep(2)
    webbrowser.open("https://www.google.com/search?q=mustard+on+the+beat+hoe")
    time.sleep(2)

def open_A_tabs():
    #Open "MUST-" tab
    webbrowser.open("https://www.google.com/search?q=MUST")
    time.sleep(0.1) #Wait 0.1 seconds
    for i in range(50):
        webbrowser.open("https://www.google.com/search?q=AAAAAAAAAAAAAAAAAAAAA") #Open "AAAAAAAA" tabs 50 times
    webbrowser.open("https://www.google.com/search?q=RD%21") # End the word with "RD"

def main():
    open_tabs()
    open_A_tabs()

if __name__ == "__main__":
    main()