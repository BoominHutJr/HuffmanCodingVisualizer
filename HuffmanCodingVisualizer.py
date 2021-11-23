
import tkinter as tkin
from tkinter import filedialog
from queue import PriorityQueue


globalFileName = ""

def HuffmanCoding():
    counts = dict()
    Q = PriorityQueue()
    
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

root.geometry("480x360")

frame = tkin.Frame(root)
frame.grid()

instructions =tkin.Label(frame, text="Press the button below and select a file for which to"+
                                        " generate a huffman tree.").grid(row=0, column=1)
runHuffmanCoding =tkin.Button(text="run huffman coding ", command=HuffmanCoding).grid(row=2, column=0)
exitButton =tkin.Button(text="After selecting a file, click here to close the window", command=root.destroy).grid(row=1, column=0)


root.mainloop() 