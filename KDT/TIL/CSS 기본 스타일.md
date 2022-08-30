## CSS 기본 스타일

#### 기본 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 픽셀 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지않음
  - 최상위요소(html)의 사이즈를 기준으로 배수 단위를 가짐

#### 크기 단위(viewport)

- 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
- 예) vw, vh, vmin, vmax

#### 색상 단위

- 색상 키워드(background-color: red;)
- RGB 색상(background-color: rgb(0, 255, 0);)
  - '#' + 16진수 표기법
  - rgb() 함수형 표기법
- HSL 색상(background-color: hsl(0, 100%, 50%);)
  - 색상, 채도, 명도
- a는 alpha(투명도)

#### 선택자(Selector) 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자



## CSS 적용 우선순위(cascading order)

1. 중요도(Importance) : 사용시 주의
   - !important
2. 우선 순위(Specificity)
   - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

```
<! -- 
적용 우선순위 

* : 가장 쉽다. 모든 것에 된다.
요소 선택 : * 보다는 덜함
클래스 : 요소보다는 덜함..
id : 문서 하나!
인라인 스타일 : 너가 굳이 그렇게 하겠다면.. 우선순위가 높은 것이길 바라.. 재사용도 못하고 완전 쓰레긴데.. 굳이굳이 그러고싶다면 우선순위 높혀줄게..
!important : 핵폭탄
=> 외부 라이브러리에서 많이 쓰는 패턴.
외부라이브러리 입장에서는 내가 적용돼야 이걸 쓰는 의미가 있으니까
-->
```



#### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식 속성에게 상속한다.
  - 속성 중에는 상속이 되는 것과 되지 않는것들이 있다.
  - 상속 되는 것 예시
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것 예시
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소(position, top/right/bottom/left, z-index등)
- 더 필요한 사항은 MDN에서 상속 파트 참조



## BOX model

CSS 원칙 I

모든 요소는 **네모(박스모델)\**이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.\**(좌측 상단에 배치)**



- 모든 html 요소는 box 형태로 이루어져있음
- 하나의 box는 네 영역으로 이루어짐
  - Margin : 외부 여백
  - Border : 테두리 영역
  - Padding : 내부 여백
  - Content : 실제 영역

#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box

  - padding을 제외한 순수 contents 영역만을 box로 지정

- 다만, 우리가 일반적으로 영역을 볼 때는 border 까지의 너비를 100px 보는 것을 원함

  - 그 경우 box-sizing을 border-box로 설정

  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      .box {
        margin: 1rem;
        padding: 1rem;
        background-color: bisque;
        border: 1px solid black;
      }
      .cicle {
        width: 5rem;
        height: 5rem;
        background-color: brown;
        border-radius: 50%;
        border: 1px solid black;
      }
      .border-box {
        box-sizing: border-box
      }
    </style>
  </head>
  
  <body>
    <div class="box">123</div>
    <!-- 82px -->
    <div class="circle"></div>
    <!-- 80px -->
    <div class="circle border-box"></div>  
  </body>
  </html>
  ```



## CSS Display

- display: block

  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

- display: inline

  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom 을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.

- display: inline-block

  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

- display: none

  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      .box {
        margin: 1rem;
        width: 5rem;
        height: 5rem;
        background-color: bisque;
      }
    </style>
  </head>
  <body>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box" /*style="display: inline-block"*/></div>
    <!-- 아래 3개의 박스는 출력이 안됨 
  			위의 block 요소인 div가 화면 크기 전체 가로폭을 차지해 span을 화면 아래로 밀어 내려버리기때문. div의 style을 inline-block으로 바꿔야 함.
  	-->
    <span class="box"></span>
    <span class="box"></span>
    <span class="box"></span>
  </body>
  </html>
  ```



- 대표적인 블록 레벨 요소
  - div / ul, ol, li / p / hr / form
- 대표적인 인라인 레벨 요소
  - span / a / img / input, label / b, em, i, strong

#### 속성에 따른 수평 정렬

- 블록 요소
  - margin-right: auto;
  - margin-left: auto;
  - margin-right: auto; margin-left: auto;(가운데 정렬)
- 인라인 요소
  - text-align : left;
  - text-align : right;
  - text-align : center;