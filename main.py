#Cloud Computing Docker Assignment 
import os
import os.path
import operator
import socket

#a.	List name of all the text file at location: /home/data
def findTxt(mypath):
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f))]
    txtFiles=[]
    for x in files:
        if x.endswith('.txt'):
            txtFiles.append(x)
    return txtFiles

def countWord(x):
    with open(x,'r') as f:
        data = f.read()
        num = data.split()
        wordcount = len(num)
        return wordcount

def convertToDict(txt,words):
    dictFiles = dict(zip(txtFiles,countWords))
    return dictFiles

def getIP():
    IPAddr = socket.gethostbyname('localhost')
    return IPAddr

if __name__ == "__main__":
    mypath = './home/data/'

    #list of files
    txtFiles = findTxt(mypath)

    #Get Number of Words
    countWords = []
    for x in txtFiles:
        num = countWord(os.path.join(mypath,x))
        countWords.append(num)

    #Total Num of Words in All Files
    TotalWords = sum(countWords)

    #Create Dictionary
    dictFiles = convertToDict(txtFiles,countWords)

    #Get Max Key
    maxVal = max(dictFiles.values())
    maxKey = [k for k, v in dictFiles.items() if v == maxVal]

    #Ip Address 
    IPaddr = getIP()

    resultPath = '/home/output/result.txt'

    #Write Result file to /home/output   instead /data
    os.makedirs(os.path.dirname(resultPath),exist_ok=True)
    with open(resultPath,"w") as result:
        result.write("Vasu Bhog\n")
        result.write("Files in Directory: ") 
        for x in txtFiles:
            result.write("\n    " + (str(x)))
        for a in dictFiles:
            for b in [dictFiles[a]]:
                result.write("\nFile: " + str(a) + ", Word Count: " + str(b))
        result.write("\nGrand Total of Words in All Files: " + str(TotalWords))
        result.write("\n" + "File with Max Num of Words: " + str(maxKey[0]))
        result.write("\nIP Address: " + IPaddr + "\n")

    #Print Output
    f = open(resultPath,'r')
    content = f.read()
    print("\n" + content)

