- **Insertion Sort [삽입 정렬]**

 

삽입 정렬은 현재 비교하고자 하는 target(타겟)과 그 이전의 원소들과 비교하며 자리를 교환(swap)하는 정렬 방법이다.

 

말로만 설명하기에는 어려울 수 있으나 그림으로 보면 이해하기 쉬우니 일단 삽입 정렬에 대한 특징만 짚고 넘어가보자.

 

삽입 정렬은 데이터를 '비교'하면서 찾기 때문에 **'비교 정렬'**이며 정렬의 대상이 되는 데이터 외에 추가적인 공간을 필요로 하지 않기 때문에 **'제자리 정렬(in-place sort)'**이기도 하다. 정확히는 데이터를 서로 교환하는 과정(swap)에서 임시 변수를 필요로 하나, 이는 충분히 무시할 만큼 적은 양이기 때문에 제자리 정렬로 보는 것이다. 이는 선택정렬과도 같은 부분이다.

 

------





- **정렬 방법**



삽입 정렬의 경우 원리 자체는 간단하다. 앞에서부터 해당 원소가 위치 할 곳을 탐색하고 해당 위치에 삽입하는 것이다.



삽입 정렬의 전체적인 과정은 이렇다. (오름차순을 기준으로 설명)



**1. 현재 타겟이 되는 숫자와 이전 위치에 있는 원소들을 비교한다. (첫 번째 타겟은 두 번째 원소부터 시작한다.)**

**2. 타겟이 되는 숫자가 이전 위치에 있던 원소보다 작다면 위치를 서로 교환한다.**

**3. 그 다음 타겟을 찾아 위와 같은 방법으로 반복한다.** 

 

 

즉, 그림으로 보면 다음과 같은 과정을 거친다.

 

![img](https://blog.kakaocdn.net/dn/KRty3/btqOKXNAGUh/IfdJIJDJWeAfbNDHQ6eyh0/img.png)

![img](https://blog.kakaocdn.net/dn/ehsinU/btqOvRVOqgO/zWJLt4EO3fpevtjrVkyjdK/img.png)

 첫 번째 원소는 타겟이 되어도 비교 할 원소가 없기 때문에 처음 원소부터 타겟이 될 필요가 없고 두 번째 원소부터 타겟이 되면 된다.

 

전체적인 흐름을 보자면 다음과 같은 형태로 정렬 한다.

 

![img](https://blog.kakaocdn.net/dn/bxvpd6/btqOuH69gZU/s5NmD45Lo0HaI80sK9QXt1/img.gif)https://en.wikipedia.org/wiki/Insertion_sort

 

 

![img](https://blog.kakaocdn.net/dn/K4Jt3/btqOvfCAm1O/Svkc3I62lPZk7wSWV0TozK/img.gif)https://ko.wikipedia.org/wiki/삽입_정렬

 

 

 ```java
 public class Insertion_Sort {
  
 	public static void insertion_sort(int[] a) {
 		insertion_sort(a, a.length);
 	}
 	
 	private static void insertion_sort(int[] a, int size) {
 		
 		for(int i = 1; i < size; i++) {
 			// 타겟 넘버
 			int target = a[i];
 			
 			int j = i - 1;
 			
 			// 타겟이 이전 원소보다 크기 전 까지 반복
 			while(j >= 0 && target < a[j]) {
 				a[j + 1] = a[j];	// 이전 원소를 한 칸씩 뒤로 미룬다.
 				j--;
 			}
 			
 			/*
 			 * 위 반복문에서 탈출 하는 경우 앞의 원소가 타겟보다 작다는 의미이므로
 			 * 타겟 원소는 j번째 원소 뒤에 와야한다.
 			 * 그러므로 타겟은 j + 1 에 위치하게 된다.
 			 */
 			a[j + 1] = target;	
 		}
 		
 	}
 }
 ```



- **삽입 정렬의 장점 및 단점**

**[장점]**

1. 추가적인 메모리 소비가 작다.

2. 거의 정렬 된 경우 매우 효율적이다. 즉, 최선의 경우 O(N)의 시간복잡도를 갖는다.

3. 안장정렬이 가능하다.

 

**[단점]**

1. 역순에 가까울 수록 매우 비효율적이다. 즉, 최악의 경우 O(N2)의 시간 복잡도를 갖는다.

2. 데이터의 상태에 따라서 성능 편차가 매우 크다. 

 ![자바 정렬시간복잡도](C:\Users\user\Desktop\CS저장소\자바 정렬시간복잡도.png)





참조: https://st-lab.tistory.com/179