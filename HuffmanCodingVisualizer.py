import time
import tkinter
from tkinter import filedialog

#Note: the pptree library is NOT used to build a binary tree. It only prints the tree we built
#https://github.com/clemtoy/pptree
from pptree import *
from pptree import Node as treeNode

codes = dict()
treeRoot = []

class Node:
    def __init__(self, count, symbol, left=None, right=None):
        self.count = count
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

def Calculate_Codes(node, val=''):
    newVal = val + str(node.code)
    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)
    if(not node.left and not node.right):
        codes[node.symbol] = newVal     
    return codes

def get_counts(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1  

    return symbols

def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])    
    string = ''.join([str(item) for item in encoding_output])    
    return string

def space_difference(data, coding):
    before_compression = len(data) * 8 # total bit space to store the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
    print("Space usage before compression (in bits):", before_compression)    
    print("Space usage after compression (in bits):",  after_compression)

def convertToHex(str):
    decimalValue = int(str, 2)
    hexstring = hex(decimalValue)
    print("Encoded output in hex: " + hexstring)


######################### HUFFMAN ENCODING #########################
def huffman_encoding():
    print("\n--------Huffman Encoding--------")
    filename = filedialog.askopenfilename()
    print("File Selected: ", filename)

    timeA = time.time()

    with open(filename) as sample:
        data = sample.read()
    
    symbol_with_counts = get_counts(data)
    symbols = symbol_with_counts.keys()
    counts = symbol_with_counts.values()
    print("Symbols with frequencies: ", symbol_with_counts)
    
    nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_counts.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their frequency
        nodes = sorted(nodes, key=lambda x: x.count)
        # for node in nodes:  
        #      print(node.symbol, node.prob)
    
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.count+right.count, left.symbol+right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    huffman_encoding_dictionary = Calculate_Codes(nodes[0])
    timeB = time.time()
    print("symbols with codes", huffman_encoding_dictionary)
    space_difference(data, huffman_encoding_dictionary)
    encoded_output = Output_Encoded(data,huffman_encoding_dictionary)
    print("Time Elapsed (in seconds): ", round(timeB-timeA,3))
    print("Encoded output: " + encoded_output)
    convertToHex(encoded_output)


    ###### PRINT THE HUFFMAN TREE ######
    root = []
    def treeTraversal(node, parent=None):
        nodeContent = str(node.symbol) + ": " + str(node.count) #node will show "character: count"
        if len(node.symbol) > 1:
            #If the node is a parent node, only show its count 
            nodeContent = str(node.count)

        if parent is None: 
            #This is the root of the tree with no parent
            n = treeNode(nodeContent)
            root.append(n)
        else:
            n = treeNode( nodeContent, parent )
        if node.right != None:
            treeTraversal(node.right, n)
        if node.left != None:
            treeTraversal(node.left, n)

    treeTraversal(nodes[0]) #Pass the root
    print('Huffman Tree:')
    print_tree(root[0], horizontal=False)

    ###### PRINT ENCODING RESULTS TO AN OUTPUT FILE ######
    outputFile = open("encodedOutput.txt", "w")
    outputFile.write(encoded_output)

    treeRoot.append( nodes[0] ) #store the tree root in the global variable
    return encoded_output, nodes[0] 


######################### HUFFMAN DECODING #########################
#Huffman decoding can ONLY be run after huffman_encoding() has been called and built the huffman tree and encoded file
def huffman_decoding(root):
    print("\n--------Huffman Decoding--------")
    filename = filedialog.askopenfilename()
    print("File Selected: ", filename)
    timeA = time.time()

    with open(filename) as sample:
        data = sample.read()
    
    node = root #set the current node to the root of the tree
    decoded_output = ""
    #Go through each bit in the encoded data to navigate through the huffman tree
    for c in data:
        if c == '0':
            #If the left node is a leaf node, add its symbol to the output
            if (node.left.left == None) and (node.left.right == None):
                decoded_output += node.left.symbol
                node = root
            else:
                node = node.left
        else:
            #If the right node is a leaf node, add its symbol to the output
            if (node.right.left == None) and (node.right.right == None): 
                decoded_output += node.right.symbol 
                node = root
            else:
                node = node.right
        
    timeB = time.time()
    print("Time Elapsed (in seconds): ", round(timeB-timeA,3))
    print("Decoded output: " + str(decoded_output))

    ###### PRINT DECODING RESULTS TO AN OUTPUT FILE ######
    outputFile = open("decodedOutput.txt", "w")
    outputFile.write(decoded_output)

    return 


root = tkinter.Tk()

root.geometry("460x360")
frame = tkinter.Frame(root)
frame.grid()

instructions =tkinter.Label(frame, text="Press the button below and select a file for which to"+
                                        " generate a huffman tree.").grid(row=0, column=1)
HuffmanEncoding =tkinter.Button(text="run huffman encoding ", command=lambda:[huffman_encoding()]).grid(row=2, column=0)
HuffmanDecoding =tkinter.Button(text="run huffman decoding ", command=lambda:[huffman_decoding(treeRoot[0])]).grid(row=3, column=0)

exitButton =tkinter.Button(text="Emergency Exit", command=root.destroy).grid(row=4, column=0)

root.mainloop()

