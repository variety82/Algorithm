# [D2] 스도쿠 검증 - 1974 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq) 

### 성능 요약

메모리: 58,784 KB, 시간: 157 ms, 코드길이: 1,094 Bytes



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do


🎃회고

가로 한 줄의 합, 세로 한 줄의 합, 3by3 매트릭스의 합이 45를 모두 만족하면 된다고 생각하고 문제를 pass했다, 그러나 반례가 있다  

7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
4 8 5 6 7 4 2 1 8
5 8 8 2 1 5 4 3 9

또는 

1 1 1 5 5 5 9 9 9
5 5 5 9 9 9 1 1 1
9 9 9 1 1 1 5 5 5
1 1 1 5 5 5 9 9 9
5 5 5 9 9 9 1 1 1
9 9 9 1 1 1 5 5 5
1 1 1 5 5 5 9 9 9
5 5 5 9 9 9 1 1 1
9 9 9 1 1 1 5 5 5

다른 방법으로 검사하게 풀어봐야겠다
for문도 이렇게 여러개를 사용하면 내가 스스로 너무 헷갈린다...
