# LRU Cache

# OrderedDict is great
# A raw solution is using hashmap + double-linked List
# The hashmap maps key and the NODE (instead of value)
# The list stores key and value (and two pointers: prev and next)
# get(key):
# if not key in d:
#     return -1
# node = d[key]
# delete(node) # node.prev.next, node.next.prev = node.next, node.prev
# prepend(node)
# return node.value
#
# set(key, value):
# if key in d:
#     node = d[key]
#     node.value = value
#     move node to head
#     d[key] = node
# else:
    # node = node(key, value)
    # prepend(node)
    # d[key] = node
    # if list.length > capacity:
    #     tail = list.poptail
    #     del d[tail.key]

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
