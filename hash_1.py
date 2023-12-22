class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.tail=Node(None,None)
        self.head=Node(None, self.tail)
        self.len=0

    def append(self, data): #Insert new key to a linked list
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

    def print(self): #Print contents of the linked list
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
        return -1 #return -1 if asked input value is not stored
        
    def delete(self, index): #Delete value from the linked list based on location
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
        strdata=str(data) #convert given data to string to perform calculations
        for i in range(0,len(strdata)):
            sum+=ord(strdata[i])*256**(i%4)
        return sum%self.size
    
 
    def insert(self, data):
        index=self.stringfolding(data) #Hash value
        if self.table[index]==None: #First key in this slot --> create the linked list
            self.table[index]=LinkedList()
            self.table[index].head.next=Node(data,self.table[index].tail)
            self.table[index].len+=1
        else:
            self.table[index].append(data)
        return

    
    def delete(self,data): #Delete value from the hash table
        index=self.stringfolding(data) #Get the hash value
        if self.table[index]!=None:
            linkedi=self.table[index].searchindex(data)
            if linkedi==-1: #--> there is nothing to delete
                return
            self.table[index].delete(linkedi)
            if self.table[index].len==0: #if the list is empty after deleting the value, we will delete it
                self.table[index]=None
        return

    def search(self,value): #Returns boolean "True" if given input value exists and "False" otherwise
        index=self.stringfolding(value)
        if self.table[index]!=None:
            linkedi=self.table[index].searchindex(value)
            if linkedi==-1: 
                return False
            else:
                return True
        return False #If slot is empty return False

    def print(self): #Print the hash table
        print("Contents of the Hash Table:")
        for i in range(len(self.table)):
            print(i,end=": ")
            if self.table[i]==None:
                print("")
                continue
            self.table[i].print()
        print("")
        return
        

if __name__ == "__main__":
    table=Openhash(5)
    keys=["abc",123,32,"dog.java","Hello world"]
    for key in keys:
        table.insert(key)
    table.print()
