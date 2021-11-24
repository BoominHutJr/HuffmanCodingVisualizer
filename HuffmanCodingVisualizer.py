from tkinter import filedialog
from queue import PriorityQueue
import tkinter

Q = PriorityQueue()
global counts, left, right
counts = dict()
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
    '''   
    def path(node):
        if node:
            path(left[node])
            if len(node) == 1:
                print(counts[node], node)
            else:
                print(counts[node])
            path(right[node])
    path(Q.get(1)[1])

    '''
    #fully implemented traversal function
    def levelOrderTraversal(node):
        def printLevel(node, level):
            if(node is None):
                return False
            if(level == 1):
                if (left[node] is None and right[node] is None):
                    print("{"+str(counts[node])+ " "+ str(node) +"} ", end= '')
                else:    
                    print(str(counts[node])+ " ", end= '')
                return True
            lChild = printLevel(left[node], level-1)
            rChild = printLevel(right[node], level-1)

            return rChild or lChild

        level = 1
        while printLevel(node, level):
            print("\n")
            level +=1

    levelOrderTraversal(Q.get(1)[1])

#TODO implement huffman decoding
def huffman_decoding():
    pass

#TODO implement writing tree to a file
def fileOutput():
    pass

#sets up GUI interface
root = tkinter.Tk()

root.geometry("460x360")
frame = tkinter.Frame(root)
frame.grid()

instructions =tkinter.Label(frame, text="Press the button below and select a file for which to"+
                                        " generate a huffman tree.").grid(row=0, column=1)
HuffmanEncoding =tkinter.Button(text="run huffman encoding ", command=lambda:[huffman_encoding(), root.destroy()]).grid(row=2, column=0)
HuffmanDecoding =tkinter.Button(text="run huffman decoding ", command=lambda:[huffman_decoding(), root.destroy()]).grid(row=3, column=0)

exitButton =tkinter.Button(text="Emergency Exit", command=root.destroy).grid(row=4, column=0)

root.mainloop()