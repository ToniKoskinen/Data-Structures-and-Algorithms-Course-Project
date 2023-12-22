import time
def Listinsert():
    time1=time.perf_counter()
    file=open("words_alpha.txt","r") #read the words from the file
    words=file.read()
    words=words.split("\n")
    file.close()
    time2=time.perf_counter()
    print("It took",time2-time1,"seconds to store all the words to the list.")
    return words

def ListCommonSearcher(words):
    time1=time.perf_counter()
    file=open("kaikkisanat.txt","r")
    n=0
    while (True): #Searching the common words
        word2=file.readline()
        if word2=="":
            break
        if word2[:-1] in words:
            n+=1
            
    time2=time.perf_counter()
    print("It took",time2-time1,"to search all the common words between the files.")
    print("Number of common words:",n,end=".\n")

if __name__ == "__main__":

    words=Listinsert()
    ListCommonSearcher(words)