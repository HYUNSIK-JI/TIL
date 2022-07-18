# PROJECT 01 (22.07.15)

## 📘 **오늘의 프로젝트 주제**

> Python을 활용한 데이터 수집

### 📗 공부한 내용

### [ I/O (Input/Output) ]

#### 1-1. Input

**입력 함수 `open()`**

```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

- encoding = `cp949` : 윈도우의 인코딩방식 (주로 한글은 유니코드인 `utf8`을 사용한다.)

#### 1-2. JSON to dictionary

**JSON (JavaScript Object Notation)**

> 데이터를 구조화하기 위한 구조체
>
> (파이썬에서는 딕셔너리형태와 유사하다.)

```
import json

# object를 json형태로 직렬화
json_obj = json.dump([dictionary])

# json을 python object로 변환
dict_obj = json.load([json])
```

------

**요구사항**

> 커뮤니티 서비스 개발을 위한 데이터 수집 단계로,
> 전체 데이터 중 필요한 데이터를 추출해 나가는 과정을 진행합니다.
> 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다



### ✨ 1. 첫 번째 미션!

#### > 제공되는 영화 데이터의 주요내용 수집

: json파일을 딕셔너리로 불러오는 함수가 이미 적혀있기 때문에 , 여기서 필요한 키워드만 골라 다시 새로운 딕셔너리로 반환해주는 함수를 만들어주면 된다.

```python
import json
from pprint import pprint

def movie_info(movie):
    # 0. 해당되는 key를 list에 담기
    key_list={'id','title','vote_average','overview','gener_ids'}

    # 1. 새로운 dictionary를 담을 변수 선언
    movies={}

    # 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
    for key in key_list:
        movies[key]=movie[key]

    # 3. 새롭게 재가공한 dictionary 반환
    return movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
```

**결과값**

```json
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}

```



### ✨ 2. 두 번째 미션!

#### > 제공되는 영화 데이터의 주요내용 수정

> 이전 단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔,
>
> 반환하는 함수를 완성합니다.
>
> 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

**풀이 순서**

> 1. 앞에서 만든 함수 코드를 재활용한다. - 원하는 내용만 추출하여 새로운 딕셔너리 생성을 위해
>
> 2. 새로 가공된 딕셔너리에서 genre_ids값을 추출하여, 입력된 movie에서의 id와 비교하여,
>
>    해당 딕셔너리의 key값이 'name'인 value값을 받아온다.

```python
import json
from pprint import pprint


def movie_info(movie, genres):
    ## > 장르 아이디에 일치하는 장르 이름 목록 구하기
    # 1. 입력받은 movie dictionary에서 id값 추출하여 변수에 할당
    genre_ids=movie['genre_ids'] #[18,80]

    # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 리스트 초기화
    gerne_name=[]

    # 3. genres 딕셔너리 순회(반복)
    for genre in genres:  #{'id':18, 'name':'Drama'}

        # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
        if genre['id'] in genre_ids: # if 18 in [18, 80] -> True

            # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
            gerne_name.append(genre['name'])

    ## > 딕셔너리 값 재가공하기
    # 5. dictionary에 넣을 key에 해당되는 요소를 list에 담기 (gerne_name 제외)
    key_list = ['id','title','vote_average','overview']

    # 6. 새로운 dictionary를 담을 변수 선언
    movie_info_dict = {}

    # 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
    for key in key_list:
        movie_info_dict[key] = movie[key]

    # 장르 이름 추가
    movie_info_dict['gerne_names'] = gerne_name

    return movie_info_dict
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

**출력값**

```json
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```



### ✨ 3. 세 번째 미션!

#### > 다중 데이터 분석 및 수정

> TMDB 기준 평점이 높은 20개의 영화데이터가 주어집니다.
>
> 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다.

앞에 문서와 **다른 점**은 **앞에서는 movie정보가 하나 들어왔다는 것이고, \**
\**이번 문제는 여러 개의 정보로 들어와서 리스트로 구성된다**는 점이다.

**풀이 순서**

> 1. movies를 for 반복문을 이용하여 movie로 하여, 앞에서 작성한 코드를 이용한다.
> 2. 새로 가공된 딕셔너리에서 genre_ids값을 추출하여, 입력된 movie에서의 id와 비교하여,
>    해당 딕셔너리의 key값이 'name'인 value값을 받아온다.



```python
import json
from pprint import pprint


def movie_info(movies, genres):
    # movies : 영화 전체 정보
    # genres : 장르의 id, name 정보

    # 모든 영화 정보의 딕셔너리들을 리턴해줄 리스트를 선언한다.
    movies_info=[]

    ## > 장르 아이디에 일치하는 장르 이름 목록 구하기
    #    - 이 때, movies가 리스트로 들어오기 때문에 for문을 이용하여 반복문으로 구해준다.
    for movie in movies:
        # 1. 입력받은 movie dictionary에서 id값 추출하여 변수에 할당
        genre_ids = movie['genre_ids']

        # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 리스트 초기화
        gerne_names = []

        # 3. genres 딕셔너리 순회(반복)
        for genre in genres:
            # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
            if genre['id'] in genre_ids:

                # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
                gerne_names.append(genre['name'])

        ## > 딕셔너리 값 재가공하기
        # 5. dictionary에 넣을 key에 해당되는 요소를 list에 담기 (gerne_names 제외)
        key_list = ['id','title','vote_average','overview']

        # 6. 새로운 dictionary를 담을 변수 선언
        movie_info = {}

        # 7. key_list 요소에 해당하는 정보만 추출 (for문 이용)
        for key in key_list:
            movie_info[key] = movie[key]

        # 8. 장르 이름 추가
        movie_info['gerne_names'] = gerne_names

        # 9. 재가공된 dictionary를 movies_info_dict에 추가해준다.
        movies_info.append(movie_info)
    # 10. 최종적으로 영화정보들이 담긴 리스트를 반환해준다.
    return movies_info
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

**출력값**

```json
[{'genre_names': ['Drama', 'Crime'],
  'id': 278,
  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '    
              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '    
              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '   
              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
  'title': '쇼생크 탈출',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'Crime'],
  'id': 238,
  'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
              '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
              '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
              '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '
              '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '
              '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',
  'title': '대부',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'History', 'War'],
  'id': 424,
  'overview': '2차 세계대전 당시 독일군이 점령한 폴란드. 시류에 맞춰 자신의 성공을 추구하는 기회주의자 쉰들러는 유태인이 '
              '경영하는 그릇 공장을 인수한다. 그는 공장을 인수하기 위해 나찌 당원이 되고 독일군에게 뇌물을 바치는 등 갖은 '
              '방법을 동원한다. 그러나 냉혹한 기회주의자였던 쉰들러는 유태인 회계사인 스턴과 친분을 맺으면서 냉혹한 유태인 '
              '학살에 대한 양심의 소리를 듣기 시작한다. 마침내 그는 강제 수용소로 끌려가 죽음을 맞게될 유태인들을 구해내기로 '
              '결심하고, 독일군 장교에게 빼내는 사람 숫자대로 뇌물을 주는 방법으로 유태인들을 구해내려는 계획을 세우는데...',
  'title': '쉰들러 리스트',
  'vote_average': 8.6},
...
```



## 👍 배운 점

> 이번 프로젝트에서 아래와 같은 것들을 배울 수 있었다!

- python의 IO ! json 파일을 불러오고, dictionary로 변환하는 법을 배울 수 있었다.