#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import dataset

# connecting to a SQLite database
db = dataset.connect('sqlite:///sg1.db')


class MenuBar(Menu):
    def __init__(self, master):
        Menu.__init__(self, master)

        file_menu = Menu(self)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=callback)
        file_menu.add_command(label="Open...", command=callback)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=callback)

        help_menu = Menu(self)
        self.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=callback)


class ToolBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        b = Button(self, text="new", width=6, command=callback)
        b.pack(side=LEFT, padx=2, pady=2)

        b = Button(self, text="open", width=6, command=callback)
        b.pack(side=LEFT, padx=2, pady=2)


class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


class KingList(Listbox):
    def __init__(self, master):
        Listbox.__init__(self, master)
        self.kings = []
        self.update_kings()
        self.bind("<ButtonRelease-1>", self.king_selected)

    def update_kings(self):
        self.kings = db['KING'].all()
        for king in self.kings:
            self.insert(END, king['NAME'])

    @staticmethod
    def king_selected(selection):
        now = selection.widget
        king = db['KING'].find_one(NAME=now.get(now.curselection()))
        print now.curselection(), now.get(now.curselection()), king
        king_detail.name.set(king['NAME'])
        king_detail.flagnum.set(king['FLAGNUM'])


class KingDetail(PanedWindow):
    def __init__(self, master):
        PanedWindow.__init__(self, master)

        Label(self, text="NAME").grid(row=0, sticky=W)
        self.name = StringVar(self, "")
        name_entry = Entry(self, textvariable=self.name)
        name_entry.bind("<KeyRelease>", self.name_changed)
        name_entry.grid(row=0, column=1)

        Label(self, text="FLAGNUM").grid(row=1, sticky=W)
        self.flagnum = StringVar(self, "")
        flagnum_entry = Entry(self, textvariable=self.flagnum)
        flagnum_entry.bind("<KeyRelease>", self.flagnum_changed)
        flagnum_entry.grid(row=1, column=1)

    def name_changed(self, item):
        print item, "name is", self.name.get()

    def flagnum_changed(self, item):
        print item, "flagnum is", self.flagnum.get()


def callback():
    print "called the callback!"


def selected(event):
    print event


if __name__ == '__main__':
    root = Tk()
    root.bind_all("<Double-Button-1>", selected)

    # create a menu
    menu = MenuBar(root)
    root.config(menu=menu)

    # create a toolbar
    toolbar = ToolBar(root)
    toolbar.pack(side=TOP, fill=X)

    # create a statusBar
    status = StatusBar(root)
    status.set("%s dasd %s", 1, 2)
    status.pack(side=BOTTOM, fill=X)

    main_pane = PanedWindow()
    main_pane.pack(fill=BOTH, expand=1)

    king_list = KingList(main_pane)
    main_pane.add(king_list)

    king_detail = KingDetail(main_pane)
    main_pane.add(king_detail)

    mainloop()
