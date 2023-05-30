import config
import pickle
import os
import sys
import random
def loadlist():
    #TODO here get the list of files from the path 
 #now it generates the random booklist
    n = 5
    randomlist = []
    for i in range(0,5):
        n = random.randint(1,300)
        randomlist.append(str(n))
    return randomlist
def booktostring(bookname):
    #TODO this function takes in the book name returns the pickle binary string 
    response=pickle.dumps(bookname)
    return sys.getsizeof(response),response
def deletebook(bookname):
    #TODO delete the book from shared folder
    pass
def create(name,binary):
    #TODO take in the book binary and write it to a file 
    pass