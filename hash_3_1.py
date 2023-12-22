import time

#Please note that the size of the table is set 15 000,
#results presented in table(in template) were done with size of 10 000.
class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.tail=Node(None,None)
        self.head=Node(None, self.tail)
        self.len=0

    def append(self, data):
        pointer=self.head.next
        for i in range(0,self.len-1):
            if pointer.data==data: #no duplicates allowed
                return
            pointer=pointer.next
        if pointer.data==data: #no duplicates allowed
            return
        pointer.next=Node(data,self.tail)
        self.len+=1
        return

    def print(self): #Print the contents of the linked list
        pointer=self.head.next
        for j in range(0,self.len):
            if j!=self.len-1:
                print(pointer.data, end=" -> ")
            else:
                print(pointer.data)
            pointer=pointer.next
        return
    
    def searchindex(self, value): #returns index of a certain value from the linked list
        index=0
        pointer=self.head.next
        while pointer!=None: 
            if pointer.data==value:
                return index
            pointer=pointer.next
            index+=1
        return -1 #return -1 if asked value does not exist
        
    def delete(self, index): #Delete value from the linked list
        pointer=self.head
        if index==0: 
            pointer.next=pointer.next.next
            self.len-=1
            return 
        for m in range(0,index):
            pointer=pointer.next
        if m<self.len-1:        
            pointer.next=pointer.next.next
            self.len-=1
        return



class Openhash:
    def __init__(self, S):
        self.size = S              # table size
        self.table=[None]*self.size


    def stringfolding(self,data):
        sum = 0
        strdata=str(data) #convert data to string to perform the calculations
        for i in range(0,len(strdata)):
            sum+=ord(strdata[i])*256**(i%4)
        return int(sum)%self.size
    
 
    def insert(self, data):
        index=self.stringfolding(data)
        if self.table[index]==None: #First key in this slot --> create the linked list
            self.table[index]=LinkedList()
            self.table[index].head.next=Node(data,self.table[index].tail)
            self.table[index].len+=1
        else:
            self.table[index].append(data)
        return

    
    def delete(self,data):
        index=self.stringfolding(data) 
        if self.table[index]!=None:
            linkedi=self.table[index].searchindex(data)
            if linkedi==-1: #--> there is nothing to delete
                return
            self.table[index].delete(linkedi)
            if self.table[index].len==0: #if the list is empty after deleting the value, we will delete it
                self.table[index]=None
        return

    def search(self,value): #Returns boolean "True" if given value is stored and "False" otherwise
        index=self.stringfolding(value) #Get the location of the linked list, where the value could be.
        if self.table[index]!=None:
            linkedi=self.table[index].searchindex(value)
            if linkedi==-1: #Value is not stored in hash table.
                return False
            return True

    def print(self): #Prints the contents of the hash table
        print("Contents of the Hash Table:")
        for i in range(len(self.table)):
            print(i,end=": ")
            if self.table[i]==None: #Empty slot
                print("")
                continue
            self.table[i].print()
        print("")
        return

def HashOpener():
    time1=time.perf_counter()
    table=Openhash(15000)
    time2=time.perf_counter()
    print("It took",time2-time1,"seconds to initialize the hash table.")
    return table

def HashInserter(table): #Time for inserting words from the file
    time1=time.perf_counter()
    file=open("words_alpha.txt","r") #read the words from the file
    words=file.read()
    words=words.split("\n")
    file.close()
    for word in words:
        table.insert(word)
    time2=time.perf_counter()
    print("It took",round(time2-time1,3),"seconds to store all the words to the hash table.")
    return

def HashCommonSearcher(table): #Time for searching common words from the other file
    time1=time.perf_counter()
    file=open("kaikkisanat.txt","r")
    n=0
    while (True): #Searching the common words
        word=file.readline()
        if word=="":
            break
        if table.search(word[:-1])==True:
            n+=1
    time2=time.perf_counter()
    print("It took",round(time2-time1,3)," to search all the common words between the files.")
    print("Number of common words:",n,end=".\n")
    return



if __name__ == "__main__":
    
    table=HashOpener()
    HashInserter(table)
    HashCommonSearcher(table)
    
   
