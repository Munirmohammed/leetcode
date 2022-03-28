class MyCircularDeque(object):

    def __init__(self, k):
        self.circularQueue=[None]*k
        self.front=0
        self.last=0
        self.size=k
        """
        :type k: int
        """

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.circularQueue[self.front-1]==None:
            self.circularQueue[self.front - 1]=value
            if self.front-1==-1:
                self.front=self.size-1
            else:
                self.front=self.front-1
            return True
        else:
            return False
        """
        :type value: int
        :rtype: bool
        """

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.circularQueue[self.last]==None:
            self.circularQueue[self.last]=value
            if self.last+1==self.size:
                self.last=0
            else:
                self.last+=1
            return True
        else:
            return False
        """
        :type value: int
        :rtype: bool
        """

    def deleteFront(self):
        temp=False
        if self.circularQueue[self.front]!=None:
            self.circularQueue[self.front]=None
            temp=True
            if self.front+1==self.size:
                self.front=0
            else:
                self.front+=1
        return temp
        """
        :rtype: bool
        """

    def deleteLast(self):
        temp=False
        if self.circularQueue[self.last-1]!=None:
            self.circularQueue[self.last-1]=None
            temp=True
            if self.last-1==-1:
                self.last=self.size-1
            else:
                self.last-=1
        return temp
        """
        :rtype: bool
        """

    def getFront(self):
        if self.circularQueue[self.front]==None:
            return -1
        else:
            return self.circularQueue[self.front]
        """
        :rtype: int
        """

    def getRear(self):
        if self.circularQueue[self.last-1]==None:
            return -1
        else:
            return self.circularQueue[self.last-1]
        """
        :rtype: int
        """

    def isEmpty(self):
        if self.circularQueue[self.front]==None:
            return True
        return False
        """
        :rtype: bool
        """

    def isFull(self):
        if self.circularQueue[self.front]!=None and self.front==self.last:
            return True
        return False
