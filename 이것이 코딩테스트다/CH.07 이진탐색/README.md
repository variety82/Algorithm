# 이진탐색(Binary Search)

___

배열 내부의 데이터가 <u>정렬되어 있어야</u> 사용가능한 알고리즘, 탐색 범위를 절반씩 좁혀가면서 탐색해 매우 빠름. 

찾으려는 데이터와 중간점(시작점과 끝점의 가운데) 위치에 있는 데이터를 반복적으로 비교해서 탐색해 나간다.

단계마다 절반의 사이즈, 즉 2로 나누는 것과 동일해 O(logN)의 시간 복잡도를 가진다. 



```python
# 재귀를 이용한 이진 탐색 소스코드

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2 
    
    if(array[mid]==target):
        return mid
    elif array[mid]>target:
        binary_search(array,target,start,mid-1)
    else:
        binary_search(array,target,mid+1,end)
        
# 반복문을 이용한 이진 탐색 소스코드

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif(array[mid]>target):
            end=mid-1
        else:
            start=mid+1
    return None
```



🎅산타할아버지가 주는 tip! <br> <u>- 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진탐색같이 O(logN)의 속도를 내야하는 알고리즘을 떠올리기</u>

- 데이터 개수가 1,000만개가 넘거나 탐색 범위의 크기가 1,000억 이상이면 input()을 사용하면 동작속도가 느리다 따라서 sys 라이브러리의 readline()함수를 이용하자. jupyter같은 IDE에서는 stdin이 구성되지 않아 실행이 안된다...

```python
import sys

input_data = sys.stdin.readline().rstrip()
```





  #### **이진 탐색 트리**

트리 자료구조 중에서 가장 간단한 형태이며 이진 탐색이 동작 할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조.

이진 탐색 트리의 특징

- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 도느가 크다.
- 서브트리 또한 이진 탐색 트리이다.

