import tkinter as tk
from random import choice


class SkinGenerator(tk.Frame):
    def __init__(self, champion="Ahri - The Nine-Tailed Fox", master=None):
        super().__init__(master)
        self.root = master
        self.champion, self.description = champion.split(" - ")
        self.pack()
        self.createWidgets()
        self.getSkins()
        self.loadImages()

    def createWidgets(self):
        # menu widgets
        self.menu = Menu(self)
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.helpMenu = Menu(self.menu, tearoff=0)
        self.fileMenu.add_command(label="Do something", command=None)
        self.helpMenu.add_command(label="About", command=self.displayInfo)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.menu.add_cascade(label="Help", menu=self.helpMenu)
        self.master.config(menu=self.menu)

        # interactive widgets
        self.result = tk.Button(self, state=DISABLED)
        self.result.pack()
        self.choose = tk.Button(self, text="Choose", command=self.chooseSkin)
        self.choose.pack()
        self.esc = tk.Button(self, text="Exit", command=self.root.destroy)
        self.esc.pack()

    def getSkins(self):
        self.skins = set("Default " + self.champion)
        with open(self.champion.lower() + ".txt", "r") as remoteFile:
            remoteData = remoteFile.readlines()
        for line in remoteFile:
            self.skins.add(line.replace("\n", ""))

    def loadImages(self):
        self.images = {}
        for skin in self.skins:
            self.images[skin] = tk.PhotoImage(file="%s/%s.gif" % (self.champion, skin))

    def chooseSkin(self):
        skin = choice(self.skins)
        self.result.configure(image=self.images[skin])

    ticmethod
    def displayInfo():
        about = ("Author: Elias Kempf"
				 "Contact: elias@kempf-net.de"
				 "Date: 17.02.2018"
				 "Version: 1.0.0")
		tk.messagebox.showinfo(message=about, title="About")


if __name__ == "__main__":
    root = tk.Tk()
    window = SkinGenerator(master=root)
    window.master.title(window.__class__.__name__)
    window.master.geometry("1200x675")
    window.mainloop()
