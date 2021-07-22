# 정렬(Sort)

___

정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

프로그램을 효율적으로 동작시키기 위해서는 상황에 적절한 정렬 알고리즘이 필요하다. 

#### 선택정렬(Selection Sort)

데이터가 무작위로 여러 개 있을 때, 매번 가장 작은 것을 선택한 후 앞쪽의 데이터와 교체하는 과정을 반복

선택 정렬은 N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야하고, 매번 가장 작은 수를 찾기 위해서 비교 연산이 필요하다. 연산 횟수는  N+(N-1)+ ```  + 2 이고 O(N^2)으로 표현가능하다. 



```python
# 선택 정렬 소스코드
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i # 가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]
```

선택 정렬은 파이썬의 기본 정렬 라이브러비 및 다른 정렬 알고리즘에 비해 비효율적이나, 특정 리스트에서 가장 작은 데이터를 찾는 행위를 할 때 비슷한 형태로 쓰인다.



#### 삽입 정렬(Insertion Sort)

특정한 데이터를 적절한 위치에 삽입하는 정렬. 특정한 데이터가 적절한 위치에 들어가기 이전에 그 앞까지의 데이터는 이미 정렬되어있다. 또한 삽입 정렬은 필요할 때만 위치를 변경하므로 <u>데이터가 거의 정렬되어 있을 때 효율적이다.</u>

```python
# 삽입 정렬 소스코드
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
```

시간복잡도는 O(N^2)이나 데이터가 거의 정렬되어 있는 상태라면 최선의 경우 O(N)의 시간 복잡도를 가진다.



#### 퀵 정렬(Quick Sort)

기준데이터(Pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿔가며 정렬하는 알고리즘.

```python
# 퀵 정렬 소스코드
def quick_sort(array,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -=1
        if left > right: #엇갈린 경우 즉, 왼쪽이 작고 오른쪽에서 큰게 발생한 경우
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right +1 , end)
# 파이썬의 장점을 살린 퀵 정렬 소스코드

def quick_sort(array):
    if len(array)<=1:
        return array
    
    pivot=array[0]
    tail=array[1:]
    
    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]
    
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)
    
```



퀵 정렬의 시간복잡도는 O(NlogN)이다. 

pivot의 위치가 변경되어 분할이 일어날 때마다 정확히 왼쪽,오른쪽이 반반 분할되는 경우가 최선이다, 그러나 리스트의 가장 왼쪽 데이터를 Pivot으로 삼거나 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작한다. 



#### 계수 정렬(Count Sort)

특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.

데이터 개수가 N, 데이터 최댓값이 K일 때 O(N+K)를 보장한다. 그러나 <u>데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 떄만 사용가능하고</u> 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때, <u>즉 데이터의 크기가 한정되어 있고 중복된 데이터가 많을 수록 효과적이다.</u>

별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다는 특징이 있다.

먼저, 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담기는 리스트를 생성한 한다. 그 후 데이터를 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.

> 예시
>
> array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
>
> |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |
> | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
> |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  1   |  0   |  0   |
>
> 
>
> ### 반복 ...
>
> 
>
> |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |
> | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
> |  2   |  2   |  2   |  1   |  1   |  2   |  1   |  1   |  1   |  2   |
>
> 이제 리스트의 첫 번째 데이터부터 하나씩 그 인덱스 만큼 출력하면 된다.
>
> 즉, 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 로 정렬이 완료되었다. 

```python
# 계수 정렬 소스코드
count=[[0] * (max(array)+1)]

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```

