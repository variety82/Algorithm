# [D2] 조교의 성적 매기기 - 1983 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq) 

### 성능 요약

메모리: 60,432 KB, 시간: 174 ms, 코드길이: 685 Bytes



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do

🎃회고
Idea
목표는 원하는 학생의 번호가 주어지면 해당 학생의 성적을 조회하고싶다

학생들의 총점과 함께 학생번호 조회를 위해 인덱스를 동시에 저장한다

총점이 높은 순으로 정렬한다

여기서 조금 헤맸는데 리스트안에 [(인덱스, 점수), ..., (인덱스, 점수)] 로 저장을 했기에 원하는 위치와 순서 조회가 쉽지않았다, 이를 위해 차피 점수순으로 정렬을 해놨기에 tmp에 인덱스를 따로 빼주고 몇등인지 조회를 하기 위해 tmp.index(k)를 사용

해당 학점을 받는 학생 수가 (학생수 //10)로 정해져 있기에 이를 나눠준 후 학점을 계산한다
