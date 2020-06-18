# from tkinter import *
#
# rows = []
# # col = []
# for i in range(5):
#     cols = []
#     for j in range(4):
#         e = Entry(relief=RIDGE)
#         e.grid(row=i, column=j, sticky=NSEW)
#         e.insert(END, '%d.%d' % (i, j))
#         cols.append(e)
#     rows.append(cols)
#
# def onPress():
#     for row in rows:
#         for col in row:
#             print(col.get()),
#         print()
#
# Button(text='Fetch', command=onPress).grid()
# mainloop()
from tkinter import *
import tkinter as tk
from tkinter import ttk

# def show():
#
#     tempList = [['Jilk,jjj', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5'],['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5'],['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
#     tempList.sort(key=lambda e: e[1], reverse=True)
#
#     for i, (name, score) in enumerate(tempList, start=1):
#         listBox.insert("", "end", values=(i, name, score))
#
# scores = tk.Tk()
# scores.geometry('800x400+0+0')
# label = tk.Label(scores, text="High Scores", font=("Arial",30)).pack(fill=X)
# # create Treeview with 3 columns
# cols = ('Position', 'Name', 'Score')
# listBox = ttk.Treeview(scores, columns=cols, show='headings')
# # set column headings
# for col in cols:
#     listBox.heading(col, text=col)
# listBox.pack(fill=BOTH)
#
# showScores = tk.Button(scores, text="Show scores", width=15, command=show).pack()
# closeButton = tk.Button(scores, text="Close", width=15, command=exit).pack()
#
# scores.mainloop()

import tkinter as tk
from tkinter import ttk
from random import choice




colors = ["red", "green", "black", "blue", "white", "yellow", "orange", "pink", "grey", "purple", "brown"]
def recolor():
    for child in tree.get_children():
        picked = choice(colors)
        tree.item(child, tags=(picked), values=(picked))
    for color in colors:
        tree.tag_configure(color, background=color)
    tree.tag_configure("red", background="red")


root = tk.Tk()

tree=ttk.Treeview(root)

style = ttk.Style()
style.theme_use("aqua")
style.configure("Treeview.Heading", font=(None, 20))
style.configure("Treeview", font=(None, 15))
tree["columns"]=("one","two","three")
tree.column("#0", width=60, minwidth=30, stretch=tk.NO)
tree.column("one", width=120, minwidth=30, stretch=tk.NO)

tree.heading("#0",text="0",anchor=tk.W)
tree.heading("one", text="1",anchor=tk.W)

for i in range(10):
    tree.insert("", i, text="Elem"+str(i), values=("none"))

tree.pack(side=tk.TOP,fill=tk.X)


b = tk.Button(root, text="Change", command=recolor)
b.pack()


root.mainloop()