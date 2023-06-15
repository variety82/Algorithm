import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False] * (N * 2)


def is_end():
    zero_cnt = 0
    for i in range(2 * N):
        if(belt[i] == 0):
            zero_cnt += 1
        if(zero_cnt == K):
            return True
    return False


cnt = 0
while True:
    if(is_end()):
        break

    temp = belt.pop()
    belt.insert(0, temp)
    temp = robot.pop()
    robot.insert(0, temp)
    
    if(robot[N - 1]):
        robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        # if(i == N - 2 and robot[i]):
            # robot[i] = False
        if(robot[i] and not robot[i + 1] and belt[i + 1] > 0):
            robot[i + 1] = True
            robot[i] = False
            belt[i + 1] -= 1
        robot[-1] = False
    if(belt[0] > 0 and not robot[0]):
        robot[0] = True
        belt[0] -= 1
    cnt += 1

print(cnt)
