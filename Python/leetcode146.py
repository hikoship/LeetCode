# LRU Cache

# Create a double-linked list; maintain a hash map of key and nodes for fast access

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.nodes = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.nodes:
            return -1
        value = self.nodes[key].value
        self.put(key, value) # move forward
        return value



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.nodes:
            self.remove(key)
        elif len(self.nodes) >= self.capacity:
            self.removeLast()
        self.addFirst(key, value)


    def addFirst(self, key, value):
        if len(self.nodes) == self.capacity:
            return False
        node = ListNode(key, value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

        self.nodes[key] = node
        return True


    def remove(self, key):
        if not key in self.nodes:
            return False
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.nodes[key]
        return True


    def removeLast(self):
        node = self.tail.prev
        if node == self.head:
            return False
        return self.remove(node.key)


class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.od = collections.OrderedDict()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.od:
            return -1
        value = self.od.pop(key)
        self.od[key] = value
        return value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.od:
            del self.od[key]
        if len(self.od) == self.capacity:
            self.od.popitem(last = False)
        self.od[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
