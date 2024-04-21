import sys

PIN = sys.stdin.readline
POUT = sys.stdout.write

class heap:
  def __init__(self):
    self.array = []
    self.size = 0

  def top(self) -> int:
    return self.array[0]

  def push(self, data : int) -> None:
    self.array.append(data)
    idx = self.size
    self.size += 1
    # up heap
    while (idx > 0 and self.array[idx // 2] < self.array[idx]):
      self.array[idx // 2] , self.array[idx] = self.array[idx], self.array[idx // 2]
      idx = idx // 2
  
  def pop(self) -> int:
    if self.size == 0:
      return 0
    self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
    ret : int = self.array[self.size - 1]
    self.array.pop()
    self.size -= 1
    idx : int = 0
    # down heap
    while (idx << 1) < self.size:
      left_child_idx = idx << 1
      right_child_idx = left_child_idx | 1
      maximam = idx

      if left_child_idx < self.size and self.array[left_child_idx] > self.array[maximam]:
        maximam = left_child_idx
      if right_child_idx < self.size and self.array[right_child_idx] > self.array[maximam]:
        maximam = right_child_idx

      if maximam != idx:
        self.array[idx], self.array[maximam] = self.array[maximam], self.array[idx]
        idx = maximam        
      else:
        break
    return ret
      
N = int(PIN().rstrip())
H = heap()
for _ in range(N):
  x = int(PIN().rstrip())
  if x == 0:
    POUT(str(H.pop()) + '\n')
  else:
    H.push(x)
