class Freqnode:
    def __init__(self, count):
        self.count = count
        self.next = None
        self.prev = None
        self.kids = collections.OrderedDict()
        
    def link(self, nextnode):
        self.next = nextnode
        nextnode.prev = self
        
class LFUCache(object):
    def __init__(self, capacity):
        self.dict_key_to_freqnode = {}
        self.cap = capacity
        self.head = Freqnode(0)
        self.head.link(Freqnode(0)) # link with a dummy tail

    def get(self, key):
        node = self.dict_key_to_freqnode.get(key)
        if node:
            value = node.kids[key]
            self._updateKey(key, value)
            return value
        return -1
        
    def _updateKey(self, key, value):
        oldfnode = self.dict_key_to_freqnode[key]
        newfnode = self._getNextFreqnode(oldfnode, key, value)
        del oldfnode.kids[key]
        self._removeFreqnodeIfEmpty(oldfnode)
        
    def set(self, key, value):
        if self.cap == 0: return
        if len(self.dict_key_to_freqnode) == self.cap and key not in self.dict_key_to_freqnode:
            # reaching cap, need to kick out least recently used key with the least frequent use count.
            node = self.head.next
            lru_key = node.kids.popitem(False)
            del self.dict_key_to_freqnode[lru_key[0]]
            self._removeFreqnodeIfEmpty(node)
                
        if key in self.dict_key_to_freqnode:
            self._updateKey(key, value)
        else:
            self._getNextFreqnode(self.head, key, value)
            
    def _removeFreqnodeIfEmpty(self, fnode):
        if len(fnode.kids) == 0:
            fnode.prev.link(fnode.next)
        
    def _getNextFreqnode(self, fnode, key, value):
        # create a new node if the +1 count doesn't exist
        if fnode.next.count != fnode.count + 1:
            node = Freqnode(fnode.count+1)
            node.link(fnode.next)
            fnode.link(node)
        self.dict_key_to_freqnode[key] = fnode.next
        fnode.next.kids[key] = value
        return fnode.next
