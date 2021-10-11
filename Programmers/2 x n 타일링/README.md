# 코딩테스트 연습 - 3단계 



## 2 X n 타일링

출처 : https://programmers.co.kr/learn/courses/30/lessons/12900



###### 문제 설명

가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우

예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

![Imgur](https://i.imgur.com/29ANX0f.png)

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

##### 제한사항

- 가로의 길이 n은 60,000이하의 자연수 입니다.
- 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

------

##### 입출력 예

| n    | result |
| ---- | ------ |
| 4    | 5      |

##### 입출력 예 설명

입출력 예 #1
다음과 같이 5가지 방법이 있다.

![Imgur](https://i.imgur.com/keiKrD3.png)

![Imgur](https://i.imgur.com/O9GdTE0.png)

![Imgur](https://i.imgur.com/IZBmc6M.png)

![Imgur](https://i.imgur.com/29LWVzK.png)

![Imgur](https://i.imgur.com/z64JbNf.png)



```python
# 코드

'''
2021-07-28

idea : i번째를 기준으로 i-1번째는 무조건 세로타일이 올 수 밖에 없고 i-2번째는 가로타일이 두개오는 경우 밖에 존재하지 않는다. 이를 이용해 DP테이블을 만든다 
'''

def solution(n): 
    dp=[0]*60000
    dp[0]=1
    dp[1]=2

    
    for i in range(2,n):
        dp[i]=(dp[i-1]+dp[i-2])%1000000007
        
    return dp[n-1]

'''
회고 : return 부분에 나머지 처리를 하니 효율성부분이 떨어졌다, 처음부터 DP테이블을 구성할때 나머지 처리를 하면 크기가 줄어들어 개선이 가능하였다. 
'''
```

