
import tkinter as tkin
from tkinter import Toplevel, filedialog
import turtle
from queue import PriorityQueue


globalFileName = ""

def HuffmanCoding():
    counts = dict()
    Q = PriorityQueue()
    
    OpenVisualizer()

    filename = filedialog.askopenfilename()
    print("Selected: ", filename)
    globalFileName = filename

    with open(globalFileName) as sample:
        text = sample.read()

    for i in range(len(text)):
        if text[i] in counts:
            counts[text[i]] += 1
        else:
            counts[text[i]] = 1

    for i in counts.keys():
        Q.put((counts[i],i))

    left = dict.fromkeys(counts, None)
    right = dict.fromkeys(counts, None)

    for i in range(len(counts)-1):
        x = Q.get(1)
        y = Q.get(1)
        z = x[0] + y[0]
        letters = x[1] + y[1]
        counts[letters] = z
        left[letters] = x[1]
        right[letters] = y[1]
        Q.put((z, letters))

    curr = Q.get(1)[1]

    def path(node):
        if node:
            path(left[node])
            if len(node) == 1:
                print(counts[node], node)
            else:
                print(counts[node])
            path(right[node])

    path(curr)



root = tkin.Tk()

def OpenVisualizer():
    s= turtle.getscreen()



root.geometry("1280x720")

frame = tkin.Frame(root)
frame.grid()

instructions =tkin.Label(frame, text="Press the button below and select a file for which to"+
                                        " generate a huffman tree.").grid(row=0, column=1)
exitButton =tkin.Button(text="Quit retard", command=root.destroy).grid(row=1, column=1)
runHuffmanCoding =tkin.Button(text="run huffman coding retard", command=HuffmanCoding).grid(row=2, column=1)

root.mainloop() 