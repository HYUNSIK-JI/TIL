# 사칙연산

오늘은 java를 이용하여 프로그래밍의 기초인 사칙연산을 공부 및 풀이 를 하였다.



문제: 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

그전에 Scanner에 대해 공부 해볼 예정이다.



자바를 처음 배우는 나의 입장에서는 우선 입출력 부터 배워야 한다.

 

그러므로 기초적으로 입력을 받을 수있는 Scanner에 대해 공부해보고자 한다.

 

우선 

 

자바에서도 여러가지 입력방법이 입력방법이 있는데, 그중 가장 쉬우면서도 대중적인 입력 중 대표적인 것이 바로

 

Scanner 클래스를 이용한 입력이라고 한다.

 

우선 Scanner 에 대해 자세하게 알아보자.

Scanner 클래스의 특징
기본적인 데이터 타입들을 Scanner 의 메소드를 사용하여 입력받을 수 있다.

예로 들어 100을 입력하고자 할 때, String(문자열)로 입력받고 싶으면 next() 나 nextLine() 을, int(정수)로 입력받고 싶다면 nextInt() 를 사용하여 입력받으면 알아서 해당 타입으로 입력된다.

Scanner 을 사용할 시 util 패키지를 경로의 Scanner 클래스를 호출해야 한다.

자바에서 쓰이는 대부분의 클래스는 lang 패키지가 아니라면 import 을 통해 호출해주어야 한다.
Scanner 의 경우는 java.util 패키지에 있다.

공백(띄어쓰기) 또는 개행(줄 바꿈)을 기준으로 읽는다.

Scanner 의 입력 메소드들은 대부분 공백과 개행(' ', '\t', '\r', '\n' 등등..)을 기준으로 읽는다. 이 덕분에 사용자의 편의에 따라 쉽게 입력을 받을 수 있다.
Scanner 사용해보기
앞서 Scanner 의 특징에서 언급했듯이 Scanner 클래스를 사용하기 위해서는 호출해주어야 한다고 했다.

 

자바의 경우 java.util 패키지 안에 Scanner 클래스가 있으므로 다음과 같이 import 를 쓴 후 해당 클래스 경로를 호출하도록 한다.

 

import java.util.Scanner;	// Scanner 클래스 호출
Scanner 객체 생성   

 

우리가 입력을 하기 위해 Scanner 클래스를 쓰고자 먼저 클래스를 호출했다.

그다음으로 해야 할 것이 바로 객체 생성이다.

 

기본적으로 객체 생성하는 방법은 다음과 같다.

클래스_이름  객체_이름 = new 클래스_이름();
 

즉, 우리는 Scanner 라는 클래스를 사용할 것이기 때문에 클래스 이름에는 Scanner 가 들어가야 한다.

 

객체 이름은 여러분들이 편한 대로 지정하면 된다.

(대체로 Scanner 의 경우 객체이름은 in, input, sc, scan 이렇게 4가지가 가장 많이 쓰인다.)

 

Scanner 의 경우 아래처럼 객체를 생성해주면 된다.

Scanner in = new Scanner(System.in); // Scanner 객체 생성
 

주의할 것은 Scanner 을 생성할 때 System.in 이 들어간다는 점이다.

 

System.in 은 사용자로부터 입력을 받기 위한 입력 스트림이다.

그렇기 때문에 Scanner 뿐만 아니라 다른 입력 방식들도 사용자로부터 입력을 받기 위해서는 System.in 이 들어간다.

 

필자는 일단 자바를 이제 막 접했기 때문에 어색 하지만 최선을 다해서 공부 해볼 예정이다.

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = Scanner(System.in);
        int a = nextInt();
        int b = nextInt();
        
        scan.close(); // 자바는 스캐너를 자동적으로 
        
        System.out.println(a + b); // 더하기 연산
        System.out.println(a - b); // 빼기 연산
        System.out.println(a * b); // 곱하기 연산
        System.out.println(a / b); // 나누기 연산
        System.out.println(a % b); // 나머지 연산
    }
}
```

