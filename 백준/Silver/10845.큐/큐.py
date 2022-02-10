from collections import deque
import sys

n = int(sys.stdin.readline())

q = deque()

for _ in range(n):
    
    tmp = sys.stdin.readline().split()
    cmd = tmp[0] 
    
    if cmd == 'push':
        q.append(int(tmp[1]))
        
    elif cmd == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
            
    elif cmd == 'size':
        print(len(q))
        
    elif cmd == 'empty':
        if len(q) != 0 :
            print(0)
        else:
            print(1)
            
    elif cmd == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    else :
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)