# [Java\] 빠른 입출력을 위한 BufferedReader, BufferedWriter, StringTokenizer, StringBuilder]



## **BufferedReader / BufferedWriter**

**BufferedReader와 BufferdWriter는 버퍼를 사용하여 읽기와 쓰기를 하는 함수이다.**

 

**버퍼를 사용하지 않는 입력**은, 키보드의 입력이 키를 누르는 즉시 바로 프로그램에 전달된다.

반면 **버퍼를 사용하는 입력**은, 키보드의 입력이 있을 때마다 한 문자씩 버퍼로 전송한다. ***버퍼가 가득 차거나 혹은 개행 문자가 나타나면 버퍼의 내용을 한 번에 프로그램에 전달***한다.

 

한번 버퍼를 거쳐 출력되는 것보다, 키보드의 입력을 받는 즉시 출력하는 것이 더 빠른 것이 아닌가 생각할수 있다.

하드디스크는 속도가 느리다. 그리고 외부 장치(키보드, 모니터 등)와 데이터 입출력도 생각보다 시간이 오래 걸린다. 그렇기 때문에 키보드의 입력이 있을 때마다 바로 이동시키는 것 보다는, ***중간에 버퍼를 두어 한번에 묶어 보내는 것이 더 효율적이고 빠른 방법***이다.

 

쓰레기통을 비우는 일이라고 생각하면 이해가 쉽다. 쓰레기가 생길 때마다 하나하나 밖에 내다버리는 것보다, 집의 쓰레기통에 하나하나 모았다가, 꽉 차면 한번에 밖에 버리는게 훨씬 효율적인 것과 비슷한 개념이라고 생각하면 된다,

 

### **Scanner**

BufferdReader 를 보기 전에 먼저 Scanner를 살펴보자.

대부분 Java를 처음 배울때, Scanner를 통한 입출력을 먼저 배우게 될 것이다.

**Scanner**는 **띄어쓰기**와 **개행문자**를 경계로 하여 입력 값을 인식한다. 그렇기 때문에 **따로 가공할 필요가 없어 편리**하다.

 

가공할 필요가 없다는 뜻은, 가령 int형 변수를 입력 받고자 하면, int x = scanner.nextInt() 를 사용해 바로 원하는 타입의 입력을 받을 수 있다. 하지만 다음에 살펴볼 BufferedReader은 입력 받은 데이터가 String으로 고정되기 때문에 입력받은 데이터를 원하는 타입으로 가공하는 작업이 필요하다.

 

Scanner는 지원해주는 메소드가 많고, 사용하기 쉽기 때문에 많이 사용하지만, 버퍼 사이즈가 1024 char이기 때문에

***많은 입력을 필요로 할 경우에는 성능상 좋지 못한 결과를 불러온다.***

####  

### **BufferedReader**

Scanner와 달리 BufferedReader는 개행문자만 경계로 인식하고 입력받은 데이터가 String으로 고정된다. 그렇기 때문에 따로 데이터를 가공해야하는 경우가 많다. 하지만 Scanner보다 속도가 빠르다!

 

BufferedRead와 Scanner의 속도 차이를 잘 보여주는 예시가 있어 가져와 보았다.

10,000,000개의 0~1023 범위의 정수를 한 줄씩 읽고, 입력으로 받은 정수의 합을 출력하는 프로그램을 각각 BufferedReader와 Scanner로 구현할 때의 수행시간이다. [[1\]](https://algospot.com/forum/read/2496/)

| 입력 방식              | 수행시간(초) |
| ---------------------- | ------------ |
| java.util.Scanner      | 6.068        |
| java.io.BufferedReader | 0.934        |

 

그리고 버퍼 사이즈도 Scanner가 1024 char인데 비해, BufferedReader는 8192 char(16,384byte) 이기 때문에 입력이 많을 때 BufferedReader가 유리하다.

 

또한 BufferedReader는 동기화 되기 때문에 멀티 쓰레드 환경에서 안전하고, Scanner는 동기화가 되지 않기 때문에 멀티 쓰레드 환경에서 안전하지 않다. *(멀티 쓰레드에 대한 설명은 생략한다.)*

 

#### **- BufferedReader 사용법**

```
BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
String s = br.readLine();
int i = Integer.parseInt(br.readLine());
```

선언의 위의 사용법과 같이 하면된다.

**입력**은 **readLine();**이라는 메소드를 사용한다. ***String으로 리턴 값이 고정***되어 있기 때문에, ***다른 타입***으로 입력을 받고자 한다면 ***반드시 형변환이 필요***하다. 그리고, ***예외처리를 반드시 필요***로 한다. readLine()시 마다 try/catch문으로 감싸주어도 되고, throws IOException 을 통한 예외처리를 해도 된다.(대부분의 경우에 후자를 사용한다.)

 

#### **- 데이터 가공**

BufferedReader를 통해 읽어온 데이터는 개행문자 단위(Line 단위)로 나누어진다. 만약 이를 공백 단위로 데이터를 가공하고자 하면 따로 작업을 해주어야 한다. 이때 사용하는 것이 StringTokenizer나 String.split() 함수이다.

 

```
// StringTokenizer 
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
StringTokenizer st = new StringTokenizer(br.readLine());
int N = Integer.parseInt(st.nextToken());
int M = Integer.parseInt(st.nextToken());

// String.split() 함수
String arr[] = s.split(" ");
```

**StringTokenizer**의 nextToken() 함수를 쓰면 readLine()을 통해 입력 받은 값을 공백 단위로 구분하여 순서대로 호출할 수 있다.

**String.split()** 함수를 사용하면, 배열에 공백단위로 끊어 데이터를 저장하여 사용할 수 있다.

 

 

#### **- BufferedReader 클래스의 메인 함수들**

| **Modifier and Type** | **Method and Description**                                   |
| --------------------- | ------------------------------------------------------------ |
| **void**              | **close()** 입력 스트림을 닫고, 사용하던 자원을 해제         |
| **void**              | **mark(int , readAheadLimit)** 스트림의 현재 위치를 마킹     |
| **int**               | **read()** 한 글자만 읽어 정수형으로 반환 (e.g ,'3'을 읽어 정수형인 (int)'3' = 51로 반환) |
| **String**            | **readLine()** 한 줄을 읽음                                  |
| **boolean**           | **ready()** 입력 스트림이 사용할 준비가 되었는지 확인 (1이 준비 완료) |

 

------

### **BufferedWriter**

일반적으로 출력을 할 때, System.out.println(""); 을 사용한다. 적은 양의 출력에서는 편리하고, 그렇게 큰 성능 차이 없이 사용할 수 있다. 하지만 우리가 늘 고려해야하는 경우는 양이 많을 경우이다. 많은 양의 출력을 할 때는, 입력과 동일하게 버퍼를 사용하는 것이 좋다.

#### **- BufferedWriter 사용법**

```
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // 선언
String str = "abcdef"; // 출력할 문자열
bw.write(s); // 출력
bw.newLine(); // 줄바꿈
bw.flush(); // 남아있는 데이터 모두 출력
bw.close();
```

BufferedWriter는 System.out.println(""); 처럼 출력과 개행을 동시해 해주지 않기 때문에, 개행을 위해선

따로 newLine(); 혹은 bw.write("\n");을 사용해야한다. 그리고 BufferedWriter의 경우 버퍼를 잡아 놓았기 때문에 반드시 사용한 후에, flush()/ close()를 해주어야 한다. close()를 하게되면, 출력 스트림을 아예 닫아버리기 때문에 한번 출력후, 다른 것도 출력하고자 한다면 flush()를 사용하면 된다.

 

#### **- BuffereWriter 클래스의 메인 함수들**

| **Modifier and Type** | **Method and Description**                                   |
| --------------------- | ------------------------------------------------------------ |
| **void**              | **close()** 스트림을 닫음. 닫기 전 flush().                  |
| **void**              | **flush()** 스트림을 비움                                    |
| **void**              | **newLine()** 개행 문자 역할                                 |
| **void**              | **write(char[] buf, int offset, int length )** 버퍼 offset 위치부터 length 크기 만큼 write |
| **void**              | **write(int c)** 한 글자 쓰기                                |
| **void**              | **write(String s, int offset, int length) **문자열에서 offset에서부터 일정 길이만큼 write |

 

 

------

###  

### **StringBuilder**

알고리즘 연습 문제를 풀다보면, BufferdReader/BufferedWriter만큼 StringBuilder도 많이 사용하는 것을 볼 수 있다. 그래서 이 StringBuiler는 무엇인지, String과 StringBuffer와의 차이점은 무엇인지 알아보자.

 

우선 String과 StringBuffer/StringBuilder의 차이를 간단하게 알아보자. 

이들의 가장 큰 차이점은, String은 불변 속성을 갖고, StringBuffer/StringBuilder는 그렇지 않다는 것이다.

 

String이 불변성을 갖는 다는 의미는, concat이나 + 연산을 통해 값을 변경하면, 원래 기존의 String 메모리에서 값이 바뀌는 것이 아니라, 기존의 String에 들어있던 값을 버리고 새로운 값을 재할당하게 된다. 처음에 할당한 String의 메모리 영역은 Garbage로 남아있다가 GarbageCollection)에 의해 없어진다.

 

String은 불변성을 가지기 때문에 변하지 않는 문자열을 자주 읽어들이는 경우 사용하면 유리하다. 하지만 문자열 추가, 삭제, 수정 등의 연산이 자주 일어나는 경우에 String을 사용하면, 힙 메모리에 많은 Garbage가 생성되고, 이는 힙 메모리 부족으로 이어져 프로그램의 성능에 치명적 영향을 미칠 수 있다.

 

이를 해결하기 위해 나온 것이 StringBuffer/StringBuilder이다.

StringBuffer/StringBuilder는 가변성을 가지기 때문에, .append() , .delete()등 동일 객체 내에서 문자열을 변경하는 것이 가능하다. 그렇게 때문에 문자열의 추가, 수정, 삭제가 빈번하게 발생할 경우 사용해야 한다.

 

아래의 사진은 문자열을 합치는 연산을 할 때의, 각각의 수행 시간을 보여주는 표이다.

String의 concat을 사용하면, 나머지 StringBuffer와 StringBuilder의 append() 보다 속도가 현저히 느린 것을 볼 수 있다.



![img](https://blog.kakaocdn.net/dn/cog8fW/btq0c2EzgQF/Hmr8Fz7qEY0XkXOs0VNQsk/img.png)출처 : javapapers.com



**- StringBuffer vs StringBuilder**

**StringBuffer** : 동기화를 지원하여 멀티 쓰레드 환경에서 안전하다.

**StringBuilder** : 동기화를 지원하지 않아 멀티 쓰레드 환경에 사용하기 적합하지 않다. 대신, 동기화를 지원하지 않기에 단일쓰레드에서는 

​            StringBuffer보다 성능이 뛰어나다.

 

정리하자면, StringBuilder는 문자열의 연산이 자주 일어나는 단일 쓰레드 환경에서 사용하는 것이 유리하다.

 

#### **- StringBuilder 사용법**

```
StringBuilder sb = new StringBuilder();
sb.append("a");
sb.append("b").append(" ");
sb.append("c").append("\n");
```

 

 

#### **- StringBuilder 주요 메소드**

- **StringBuilder append(String s) : StringBuilder 뒤에 값을 붙임**
- **StringBuilder delete(int start , int end) : 특정 인덱스부터 인덱스까지를 삭제
  **
- **StringBuilder insert(int offet, any primitive of a char[]) : 문자를 삽입함**
- **StringBuilder replace(int start , int end , String s) : 일부를 String 객체로 치환**
- **StringBuilder reverse() : 순서를 뒤집음**
- **StringBuilder setCharAt(int index , char ch) : 주어진 문자를 치환**
- ***\*StringBuilder indexOf(String s) : 값이 어느 인덱스에 들어있는지 확인\****
- *StringBuilder subString(int start, int end) : start와 end 사이의 값을 잘라옴.*



*◎ 참고자료*

*[jhnyang.tistory.com/92](https://jhnyang.tistory.com/92)*

*[coding-factory.tistory.com/251](https://coding-factory.tistory.com/251)*

*[mebadong.tistory.com/12](https://mebadong.tistory.com/12)*

*[ryulth.com/devnote/2019/06/17/java-io-tips/](https://ryulth.com/devnote/2019/06/17/java-io-tips/)*