class Node : 
    def __init__ (self, key , val):
        self.key = key 
        self.val = val 
        self.next = None 
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):

        # initialize capacity and hashmap 
        self.cap = capacity 
        self.cache = {} 

        #Initializing the left and right node 

        self.left = Node(0,0)
        self.right = Node(0,0)

        #poiting the nodes to each other 

        self.left.next = self.right
        self.right.prev = self.left 

    # helper to remove a node 
    def remove(self, node):
        prev =  node.prev
        next = node.next 

        prev.next = next 
        next.prev = prev 



    # helper to add a node 
    def insert(self,node):
        
        prev = self.right.prev
        next = self.right


        prev.next = node 
        next.prev = node 
        node.prev = prev 
        node.next = next  


    def get(self, key: int) -> int:
    # getting the val from the hashmap if present 
        if key in self.cache : 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1 

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache: 
            self.remove(self.cache[key])
        
        # adding the key and its node to the hashmap 
        self.cache[key] = Node(key, value)
        # inserting it to the left right doubly linked list 
        self.insert(self.cache[key])

        if len(self.cache) > self.cap : 
            lru = self.left.next 

            # remove the lru 
            self.remove(lru)

            # remove from hashmap as well 
            del  self.cache[lru.key]


        


        
