# Eclipes(이클립스) Maven Project 만들기 및 Maven(메이븐)이란 무엇일까?

<img src="C:\Users\현식\Desktop\이미지모음\메이븐1.png" alt="메이븐1" style="zoom: 80%;" />

**[1] Maven이란 무엇일까? **

Maven은 지금까지 애플리케이션을 개발하기 위해 반복적으로 진행해왔던 작업들을 지원하기 위하여 등장한 도구이다.

Maven을 사용하면 빌드, 패키징, 문서화, 테스트와 테스트 리포팅, git, 의존성관리, svn등과 같은 형상관리서버와 연동(SCMs), 배포 등의 작업을 손쉽게 할 수 있다.



Maven을 이해하려면 CoC(Convention over Configuration)라는 단어를 먼저 이해해야 하는데

CoC란 일종의 관습으로서 예를 들자면 프로그램의 소스파일은 어떤 위치에 있어야 하고, 소스가 컴파일된 파일들은 어떤 위치에 있어야 하고 등을 미리 정해놓는 것을 의미한다.

결국 관습에 이미 익숙한 사용자는 쉽게 Maven을 사용할 수 있지만 관습에 익숙하지 않은 사용자는 거부감을 느낄 수 있다. Maven을 사용한다는 것은 이러한 관습 즉 CoC에 대해서 알아나가는 것이라고도 말할 수 있겠다.

**[2] Maven의 장점**

Maven의 장점 중에는 편리한 의존성 라이브러리 관리가 있다.

예를들어 JSTL을 사용하기 위해서는 몇 가지 파일을 다운로드 하여 /WEB-INF/lib폴더에 복사하여 사용했었는데

이러한 라이브러리가 많아질수록 관리가 어려워진다.

하지만 Maven을 사용하면 설정 파일에 몇 줄 적어줌으로써 직접 다운로드 받거나 하는 것을 하지 않아도 라이브러리를 사용할 수 있다.

특히 다수가 참여하는 프로젝트에서는 프로젝트를 빌드하는 방법에 대하여 가이드하는 것이 복잡해지는데

Maven을 사용하게 되면 Maven에 설정한 대로 모든 개발자가 일관된 방식으로 빌드를 수행할 수 있으며 또한 다양한 플러그인을 통한 여러가지 일들을 자동화 할 수 있다.

**[3]Eclipes에서 Maven Project생성 방법**

file-new-mavenproject선택

![메이븐2](C:\Users\현식\Desktop\이미지모음\메이븐2.png)

next 클릭

![메이븐3](C:\Users\현식\Desktop\이미지모음\메이븐3.png)

원하는 내용을 선택후 Next 버튼

만약 웹페이지를 만들고자 한다면 quickstart가 아니라 스크롤을 내리면 나오는 web-app을 선택해야한다



![메이븐4](C:\Users\현식\Desktop\이미지모음\메이븐4.png)

Group id와 Article id 입력하고 finish버튼을 누르면 생성이 완료된다.

(Group id는 보통 회사나 팀의 도메인주소를 a.b.c 형태로 거꾸로 입력)

(Article id는 보통 프로젝트의 이름을 적는다)

생성된 Maven 프로젝트에는 pom.xml파일이 생성되며 pom.xml파일을 통해 여러가지 라이브러리를

추가할 수있다.

![메이븐5](C:\Users\현식\Desktop\이미지모음\메이븐5.png)

**[4] Maven Project 디렉토리 설명**

![메이븐6](C:\Users\현식\Desktop\이미지모음\메이븐6.png)

<ul>
    <li>src/main/java : 자바 소스 파일 위치 시킵니다. 이 하위에 org.gliderwiki ... 와 같은 패키지를 배치합니다.</li>
    <li>src/main/resources : 프로퍼티나 XML 등 리소스 파일이 위치합니다.</li>
    <li>src/main/resources : 프로퍼티나 XML 등 리소스 파일이 위치합니다.</li>
    <li>src/main/webapp : Web Project 일 경우 WEB-INF등 웹 어플리케이션 리소스를 위치시킵니다.</li>
    <li>src/test/java : JUnit등의 테스트 파일이 위치하게 됩니다.</li>
    <li>src/test/resources : 테스트시에 필요한 resource 파일이 위치하게 됩니다.</li>

cf)src 하위에 main 부분과 test부분을 경로가 나뉘는 이유는 개발과 동시에 테스트 코드를 작성하기 위함 입니다.

</ul>

**[5]POM.xml 파일의 구조**

![메이븐7](C:\Users\현식\Desktop\이미지모음\메이븐7.PNG)



**project** : pom.xml 파일의 최상위 루트 엘리먼트

**modelVersion** : POM model의 버전

**groupId** : 프로젝트를 생성하는 조직의 고유 아이디를 결정. 일반적으로 도메인 이름을 거꾸로 적는다.

**artifactId** : 해당 프로젝트에 의하여 생성되는 artifact의 고유 아이디를 결정. Maven을 이용하여 pom.xml을 빌드할 경우 다음과 같은 규칙으로 artifact가 생성. artifactid-version.packaging. 위 예의 경우 빌드할 경우 examples-1.0-SNAPSHOT.jar 파일이 생성.

**packaging** : 해당 프로젝트를 어떤 형태로 packaging 할 것인지 결정. jar, war, ear 등이 해당됨.

**version** : 프로젝트의 현재 버전. 추후 살펴보겠지만 프로젝트가 개발 중일 때는 SNAPSHOT을 접미사로 사용하는데

이러한 Maven의 버전 관리 기능은 라이브러리 관리를 편하게 한다.

**name** : 프로젝트의 이름

**url** : 프로젝트 사이트가 있다면 사이트 URL을 등록하는 것이 가능





여기서 가장 중요한 것은 dependency 입니다.

여기에 원하는 라이브러리에 대한 버전이나 기타 등등의 양식을 입력하면 자동으로 라이브러리가 추가되어 사용할 수 있습니다. 예를들어 jdbc를 이용하여 mysql을 사용하고 싶으면 <dependencies></dependencies> 안에 다음과 같은 코드를 삽입하면 됩니다.![메이븐8](C:\Users\현식\Desktop\이미지모음\메이븐8.PNG)