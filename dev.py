import tkinter as tk
import merl


root = tk.Tk()
root.title("Merl Tester")

# Set window size (width x height)
root.geometry("800x300")

def sendtomerl():
    #clear text
    Merlspeak = tk.Label(root, text = "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ")
    Merlspeak.place(x = 100, y = 0)




    #CHANGE TEXT
    Merlspeak = tk.Label(root, text = merl.sendRaw(str(Intext.get())))
    Merlspeak.place(x = 100, y = 0)
    print(merl.sendRaw(str(Intext.get())))

Intext = tk.Entry(root)
Send = tk.Button(root, command = sendtomerl, text = "Send")
Merlspeak = tk.Label(root, text = "Merl Speaks here!")
Githubmerllink = tk.Label(root, text = "https://github.com/O9Creeps/merl")




Intext.place(x = 0, y = 0)
Send.place(x = 0, y = 25)
Githubmerllink.place(x = 0, y = 75)
Merlspeak.place(x = 150, y = 0)
root.mainloop()
