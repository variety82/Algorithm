''''
2021/11/14 idea: 변환하는 숫자가 1,2,4 세개 뿐이므로 3진법으로 변환~ 변환 후 1->1 2->3 3->4 로 변환하면 된다.
그러나 3진법으로 변환하는 과정에서 0이 발생할 수 있는데 이 경우 상위 수에서 borrow를 해서 상위 수는 -1 빌림한 자리는 3으로 처리한다.
그 후 3을 모두 4로 바꿔주면 된다.
'''

def changeNumber(n, q):
    base = ''
    while n > 0:
        n, r = divmod(n, q)
        if r==0:
            n -=1
            base += str(3)
        else:
            base += str(r)
    return base[::-1]


def solution(n):
    answer = changeNumber(n, 3).replace('3', '4')
    return answer
