from tkinter import filedialog
from queue import PriorityQueue
import tkinter

counts = dict()
Q = PriorityQueue()
global left
global right
left = dict()
right = dict()

def freq(fn):
    with open(fn) as sample:
        text = sample.read()

    for i in range(len(text)):
        if text[i] in counts:
            counts[text[i]] += 1
        else:
            counts[text[i]] = 1

    for i in counts.keys():
        Q.put((counts[i],i))
    

def huffman_encoding():
    filename = filedialog.askopenfilename()
    print("Selected: ", filename)

    freq(filename)

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
    
    def path(node):
        if node:
            path(left[node])
            if len(node) == 1:
                print(counts[node], node)
            else:
                print(counts[node])
            path(right[node])
    path(Q.get(1)[1])

def huffman_decoding():
    pass

def levelOrderTraversal():
    pass


root = tkinter.Tk()

root.geometry("460x360")

frame = tkinter.Frame(root)
frame.grid()

instructions =tkinter.Label(frame, text="Press the button below and select a file for which to"+
                                        " generate a huffman tree.").grid(row=0, column=1)
HuffmanEncoding =tkinter.Button(text="run huffman encoding ", command=huffman_encoding).grid(row=2, column=0)
HuffmanDecoding =tkinter.Button(text="run huffman decoding ", command=huffman_decoding).grid(row=3, column=0)
runlevelOrdertraversal =tkinter.Button(text="level order traversal ", command=levelOrderTraversal).grid(row=4, column=0)

exitButton =tkinter.Button(text="After selecting a file, click here to close the window", command=root.destroy).grid(row=1, column=0)


root.mainloop() 