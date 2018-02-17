import tkinter as tk
from tkinter import messagebox
from random import choice
from time import sleep


class SkinGenerator(tk.Frame):
    def __init__(self, champion="Ahri - The Nine-Tailed Fox", master=None):
        super().__init__(master)
        self.champion, self.description = champion.split(" - ")
        self.pack()
        self.createWidgets()
        self.getSkins()
        self.loadImages()

    def createWidgets(self):
        # menu widgets
        self.menu = tk.Menu(self)
        self.fileMenu = tk.Menu(self.menu, tearoff=0)
        self.helpMenu = tk.Menu(self.menu, tearoff=0)
        self.fileMenu.add_command(label="Do something", command=None)
        self.helpMenu.add_command(label="About", command=self.displayInfo)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.menu.add_cascade(label="Help", menu=self.helpMenu)
        self.master.config(menu=self.menu)

        # interactive widgets
        self.mainLabel = tk.Label(self, text="%s - %s"
                                  % (self.champion, self.description),
                                  font=("Helvetica", 24))
        self.mainLabel.pack()
        self.result = tk.Button(self)
        self.result.pack()
        self.skinLabel = tk.Label(self, font=("Helvetice", 16))
        self.skinLabel.pack()
        self.choose = tk.Button(self, text="Choose", command=self.animateSkins)
        self.choose.pack()
        self.esc = tk.Button(self, text="Exit", command=self.master.destroy)
        self.esc.pack()

    def getSkins(self):
        self.skins = ["Default " + self.champion]
        with open(self.champion.lower() + ".txt", "r") as remoteFile:
            remoteData = remoteFile.readlines()
        for line in remoteData:
            self.skins.append(line.replace("\n", ""))

    def loadImages(self):
        self.images = {}
        for skin in self.skins:
            self.images[skin] = tk.PhotoImage(file="%s/%s.gif"
                                              % (self.champion, skin))

    def animateSkins(self):
        self.choose.configure(state="disabled")
        self.skinLabel.configure(text="")
        for i in range(1, 70, 10):
            for skin in self.skins:
                self.result.configure(image=self.images[skin])
                self.master.update()
                sleep((i * i * i) / 1000000)
        self.chooseSkin()
        self.choose.configure(state="active")

    def chooseSkin(self):
        skin = choice(self.skins)
        self.result.configure(image=self.images[skin])
        self.skinLabel.configure(text=skin)

    @staticmethod
    def displayInfo():
        about = ("Author: Elias Kempf\n"
                 "Contact: elias@kempf-net.de\n"
                 "Date: 17.02.2018\n"
                 "Version: 1.0.0")
        messagebox.showinfo(message=about, title="About")


if __name__ == "__main__":
    root = tk.Tk()
    window = SkinGenerator(master=root)
    window.master.title(window.__class__.__name__)
    window.master.geometry("1200x675")
    window.mainloop()
