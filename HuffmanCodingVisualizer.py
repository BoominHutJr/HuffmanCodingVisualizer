
import tkinter as tkin
from tkinter import filedialog
from queue import PriorityQueue


globalFileName =""

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
        if node is None:
            return None
        else:
            path(left[node])
            if len(node) == 1:
                print(counts[node], node)
            else:
                print(counts[node])
            path(right[node])

    path(curr)

root = tkin.Tk()
root.geometry("1280x720")
frame = tkin.Frame(root)
frame.grid()

greeting =tkin.Label(frame, text="Hello dickwad").grid(row=0, column=0)
exitButton =tkin.Button(text="Quit retard", command=root.destroy).grid(row=1, column=0)
runHuffmanCoding =tkin.Button(text="run huffman coding retard", command=HuffmanCoding).grid(row=3, column=0)

root.mainloop()


