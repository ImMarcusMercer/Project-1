import csv
from Track import Track

class Queue:
    """Creates a Queue"""
    
    def __init__(self,size:int=50):
        self.queue=[None]*size
        self.size=0
        self.curr = 0
        self.repeat = False

    def increaseSize(self):
        self.size +=1

    def getSize(self):
        return self.size

    def enqueue(self,song:Track):
        index=self.size
        self.queue[index]=song
        self.increaseSize()
        
    def dequeue(self):
        if self.size==0:
            return None
        else:
            item=self.queue[0]
            self.queue=self.queue[1:]
            self.size-=1
            return item

#           title,artistname, album, duration
    #still under development
    def addtoStorage(self, name):
        """Adds the queue into the csv file
        Arguments: Name(Set a custom name for the queue)"""
        name=[[name]]
        manage=open('Library.csv', 'a',newline='') #open manager
        write= csv.writer(manage)
        write.writerows(name)
        write.writerows(self.convert()) #Adding of new data
        manage.close()   #close manager

    def getContent(self):
        str=f""
        index=0
        while index < len(self.queue):
            if self.queue[index]==None:
                break
            str+=f"[{self.queue[index]}]\n"
            index+=1
        return str
    
    def convert(self):
        """Convert content into list for storing data into csv file"""
        s=[]
        for items in self.queue:
            if items == None:
                break
            s += [[items]]
        return s
    
    def convertTime(self):
        time=self.duration
        minutes, seconds = map(int, time.split(":"))
        total_seconds = minutes * 60 + seconds
        return total_seconds
    
    def getTotalDuration(self):
        """Returns total duration of the Queue"""
        """Complete this method"""
        total_seconds = 0

        for items in self.queue:
            if items is None:
                break
            minutes, seconds = map(int, items.duration.split(":"))
            total_seconds += minutes * 60 + seconds

        total_minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        return f"{total_minutes}:{remaining_seconds:02d}"
    
    def showQueue(self):
        if self.size==0:
            print("The queue is empty.")
        else:
            print("<------Songs in Queue------>")
            for i in range(self.size):
                print(f"\n{self.queue[i]}\n")
            print("<---------End of Queue--------->")
    
    def toggleRepeat(self):
        self.repeat = True

    def skipTrack(self):
        if self.curr != -1 and self.curr < self.size - 1:
            self.curr += 1
            self.playTrack()
        else:
            if self.repeat:
                self.curr = 0
                self.playTrack()
            else:
                print("No more tracks left.")
                self.curr = -1  
    
    def playTrack(self):
        if self.curr == -1:
            self.curr = 0
        if self.curr < self.size and self.queue[self.curr] is not None:
            print(f"Now playing: {self.queue[self.curr]}")
        else:
            print(f"No more tracks left.")

    def prevTrack(self):

        if self.curr > 0:
            self.curr -= 1
            self.playTrack()
        else:
            if self.repeat:
                self.curr = self.size - 1
                self.playTrack()
            else:
                self.playTrack()
                self.curr = -1
        
    def __str__(self):
        """Should return items in the queue"""
        str="<------Songs in Queue----->"
        index=0
        while index < len(self.queue):
            if self.queue[index]==None:
                break
            str+=f"\n{self.queue[index]}\n"
            index+=1
        str+="\n<---------End of Queue--------->"
        
        return str
    
queue = Queue()

song1 = Track("Nikes", "Frank Ocean", "Blonde", "5:14")
song2 = Track("Heartless", "The Weeknd", "After Hours", "3:18")
song3 = Track("Thinkin Bout You", "Frank Ocean", "Channel Orange", "3:21")
queue.enqueue(song1)
queue.enqueue(song2)
queue.enqueue(song3)

queue.toggleRepeat()

queue.playTrack() #Play 1st song

queue.skipTrack() #Skip to 2nd song
# queue.playTrack() #PLay 2nd song
queue.prevTrack()
queue.prevTrack()
queue.prevTrack()

# queue.skipTrack() #Skip to 3rd song
# queue.skipTrack()
# queue.skipTrack()
# queue.skipTrack()
# queue.playTrack() #Play 3rd song
# queue.skipTrack()
# queue.skipTrack()
# queue.skipTrack()
# queue.skipTrack()
# queue.playTrack()
# queue.playTrack()

# queue.prevTrack() #Go back to 2nd song
# queue.playTrack() #Play 2nd song

# queue.prevTrack() #Go back to 1st song
# queue.playTrack() #Play 1st song

# queue.prevTrack() #Go back to the last song in the queue
# queue.playTrack() #Play last song