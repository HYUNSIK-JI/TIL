#### **1. DI(Dependency Injection)란?**

DI는 말 그대로 의존성을 주입한다 라는 뜻이다. 쉽게 설명하면 JAVA에서 객체를 new를 이용하여 생성하는데 이렇게 사용하지 않고 외부에서 생성한 객체를 세터 또는 생성자를 통해 사용하겠다는 의미이다. 이를 의존성 주입이라 한다. 의존성 주입 방법에는 **세터를 이용하거나 생성자**를 이용한 방법 두가지가 있다. 예제로는 생성자를 이용한 방법으로 예제를 공부하겠다

![메이븐7](C:\Users\현식\Desktop\이미지모음\메이븐7.PNG)

그림처럼 DI를 이용하지 않고 new를 사용하여 객체를 생성하게 되면 PetOwner와 Dog간 강한 결합이 생기게 되어 도그를 수정하면 PetOwner가 수정될 수 있다.

![DI2](C:\Users\현식\Desktop\이미지모음\DI2.png)

반면 다음과 같이 Bean Container를 이용하여 객체를 생성하고 의존성 주입을 시켜주면 결합이 강하지 않다는 장점이 생긴다. 이때 **Bean Container는 XML로 이루어져 있다.**

![DI3](C:\Users\현식\Desktop\이미지모음\DI3.png)

다음 그림처럼 메인함수에서는 ApplicationContext라는 BeanContainer를 생성하고 미리 작성된 xml에 따라 ApplicationContext는 Dog, Cat, PetOwner라는 객체를 생성하고 Dog, Cat을 PetOwner에 의존성 주입한다. 스프링은 new방식 대신 DI방식을 권장한다.



#### **2. 의존성 주입 실습**

**#1 프로젝트 생성**

**File > New > Spring Legacy Project**를 클릭하고 다음과 같은 **Simple Spring Maven** 프로젝트를 생성한다. 프로젝트명은 원하는 프로젝트명을 사용해도 무방하다. 이 실습에서는 helloDI라는 프로젝트명을 사용하겠다.

![DI4](C:\Users\현식\Desktop\이미지모음\DI4.png)

**#2 AnimalType, Cat, Dog 생성하기**

src/main/java에 클래스와 인터페이스를 담을 패키지를 생성한다 패키지명은 자유로워도 좋다. 패키지를 생성하였다면 패키지 아래에 AnimalType.java라는 인터페이스를 생성한다

인터페이스 코드는 다음과 같다 인터페이스를 implements할 cat, dog클래스들이 사용할 sound라는 메소드를 정의하고 있다.

**AnimalType.java**

``` JAVA
package kr.ac.hansung.helloDI;

public interface AnimalType {

	public void sound();

}
```

다음으로 Cat.java라는 클래스를 생성한다. 게터와 세터가 만들어져 있으며 AnimalType의 sound메소드를 사용하고 있다.



**Cat.java**

```JAVA
package kr.ac.hansung.helloDI;

public class Cat implements AnimalType {

	public String getMyName() {
		return myName;
	}

	public void setMyName(String myName) {
		this.myName = myName;
	}

	private String myName;

	@Override
	public void sound() {
		
		System.out.println("Cat name = " + myName + ":" + "Meow");
	}

}
```

마지막으로 Dog.java라는 클래스를 생성한다. 게터와 세터가 만들어져 있으며 AnimalType의 sound메소드를 사용하고 있다.



**Dog.java**

```java
ackage kr.ac.hansung.helloDI;

public class Dog implements AnimalType {

	public String getMyName() {
		return myName;
	}

	public void setMyName(String myName) {
		this.myName = myName;
	}

	private String myName;

	@Override
	public void sound() {
		
		System.out.println("Dog name = " + myName + ":" + "Bow Wow");
	}

}
```

**#3 PetOwner클래스 생성하기**

petOwner클래스는 AnimalType의 animal을 받는다 이는 cat이나 dog를 받아서 사용하겠다는 의미이고 play라는 메소드와 생성자를 정의했다.



**PetOWner.java**

```java
package kr.ac.hansung.helloDI;

public class PetOwner {

		private AnimalType animal;

		public PetOwner(AnimalType animal) {
			this.animal = animal;
		}
		
		public void play() {
			
			animal.sound();
		
		}
}
```

**#4 animal.xml 생성하기**

Bean Container가 생성하기 위해 참고할 xml파일을 생성한다 코드는 다음가 같다.

<bean id = "dog"> 부분이 dog라는 클래스의 객체를, <bean id = "cat"> 부분이 cat이라는 클래스의 객체를 <bean id = petOwner"> 부분이 petOwner의 객체를 생성하고 <constructor-arg ref = "dog">는 dog객체를 의존성 주입하겠다 라는 의미이며, <property name="myName" value="poddle">는 도그의 myName의 값을 poodle로 주겠다는 의미이다.



**animal.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
	<bean id="dog" class="kr.ac.hansung.helloDI.Dog">
		<property name="myName" value="poodle"></property>
	</bean>

	<bean id="cat" class="kr.ac.hansung.helloDI.Cat">
		<property name="myName" value="bella"></property>
	</bean>

	<bean id="petOwner" class="kr.ac.hansung.helloDI.PetOwner">
		<constructor-arg ref="dog"></constructor-arg>
	</bean>
</beans>
```



**#5 MainApp.java작성**

마지막으로 메인 함수인 MainApp.java를 다음과 같이 작성한다. ApplicationContext가 animal.xml을 바라보게 하고

petOwner의 person이 context의 getBean함수를 통해 객체를 가져와 사용하는 모습이다.

```java
package kr.ac.hansung.helloDI;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {

	public static void main(String[] args) {

		ClassPathXmlApplicationContext context = 
				new ClassPathXmlApplicationContext("/kr/ac/hansung/helloDI/conf/animal.xml");
		
		PetOwner person = (PetOwner) context.getBean("petOwner");
		person.play();
		
		context.close();
	}

}
```



**#5 프로젝트 Run**

프로젝트를 Run 하게 되면 다음과 같은 결과를 확인할 수 있다.

![DI5](C:\Users\현식\Desktop\이미지모음\DI5.png)

**마무리**

사용자는 animal.xml에서 정의한 대로 dog, cat, petOwner의 객체를 먼저 생성하고, 이후 dog를 petOwner에 주입하였으니 결과 화면에는 dog가 보이게 된다 만약 cat을 주입하고 싶다면 **constructor-arg의 ref = cat**으로 수정해주면 된다



참조(https://diqmwl-programming.tistory.com/29)