JAVA Basic : Dictionary & Map 클래스



**Map 클래스와 일반 배열과의 차이점**



|             | **Map클래스**                                                | **배열**                                              |
| ----------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| 패키지      | java.util                                                    | java.lang                                             |
| 클래스 정의 | Map<String, String> ht = new HashMap<String, String>();      | String[] array = new String[n]  ← n자리수의 배열 정의 |
| 크기        | 크기가 정해져 있지 않다. 확장성 용이                         | 한번 배열클래스를 정의하면 크기 고정.                 |
| 순서        | 순서가 없다.                                                 | 순서가 있다.                                          |
| 입출력형태  | Key-Value 형태로 입출력을 한다.                              | 배열의 Index 숫자를 지정해서 입출력을 한다.           |
| 반복출력 시 | 순서없이 뒤죽박죽 출력된다.Key와 Value는 한 쌍이기때문에 Key&Value는 안섞인다. | 배열 Index번호대로 차례대로 출력된다.                 |



```java
Map의 주요 메소드

Map<String, String> ht = new HashMap<String, String>();        

ht.put("a", "에이");

ht.put("b", "비");

System.out.println("get : " + ht.get("a"));

System.out.println("keyset : " + ht.keySet());

System.out.println("values : " + ht.values());

System.out.println("containsKey : " + ht.containsKey("a"));

System.out.println("containsValue : " + ht.containsValue("에이"));

System.out.println("toString : " + ht.toString());

System.out.println();

        

// keySet() 메서드 이용한 데이터 출력. 

// 리턴타입이 Set 인터페이스라서 Set인터페이스에 집어넣음. 

Set<String> keys=ht.keySet();

//신형 for문 : keys값을 모두 String key변수에 반복하여 넣는다.

for(String key : keys){ 	

System.out.println("Set을 이용한 반복 : " + key + "=" + ht.get(key));

} //end for

# 출력 결과
    
//get : 에이

//keyset : [a, b]

//values : [에이, 비]

//containsKey : true

//containsValue : true

//toString : {a=에이, b=비}



//Set을 이용한 반복 : a=에이

//Set을 이용한 반복 : b=비
```

