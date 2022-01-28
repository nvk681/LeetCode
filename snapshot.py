import numpy as np

class SnapshotArray:

    def __init__(self, length: int):
        self.array = np.array(([0]*length))
        self.snap_s = []
        self.count = 0
    
    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snap_s.append(np.array(self.array))
        return len(self.snap_s)-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_s[int(snap_id)][int(index)]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(1)
param_2 = obj.snap()
param_2 = obj.snap()
obj.set(0,4)
param_2 = obj.snap()
print(param_2)
print(obj.get(0,1))
print(obj.set(0,12))
print(obj.get(0,1))
param_2 = obj.snap()
print(param_2)
print(obj.get(0,3))

# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)