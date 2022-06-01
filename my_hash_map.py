class MyHashMap:

    def __init__(self):
        self.my_map = {}

    def put(self, key: int, value: int) -> None:
        self.my_map[key] = value

    def get(self, key: int) -> int:
        return self.my_map[key] if key in self.my_map else -1

    def remove(self, key: int) -> None:
        if key in self.my_map: 
            del self.my_map[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)