
- 2021-07-13
- 실전 문제 큰수의 법칙

- idea : 단순 그리디 문제
         리스트를 내림차순으로 정렬 후 제일 큰 원소를 K번 더하면 그 다음 원소를 더함
         


N,M,K=map(int,input().split())
_list=sorted(list(map(int,input().split())),reverse=True)
cnt=0 #K번을 셀 친구 
answer=0
for i in range(M):
    if(cnt==K):
        answer+=_list[1]
        cnt=0
    else:
        answer+=_list[0]
        cnt+=1
print(answer)

#문제 해설 답안
first=data[n-1]
second=data[n-2]
result=0
while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result +=second
    m-=1
print(result)


