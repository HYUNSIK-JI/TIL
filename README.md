# 👻Today I Learend
Today I Learned
<details>
<summary>😲2022년 07월 05일😲:🖥 문법 배웠어용 🖥</summary>

## 마크다운 문법 -Heading

- Heading은 문서의 제목이나 소제목으로 사용
  - **#의 개수에 따라 대응되는 수준(Heading level)이 있으며, h1 ~ h6까지 표현 가능**
  - **문서의 구조를 위해 작성되며 글자 크기를 조절하기 위해 사용되어서는 안됨**
    ![177242084-c3fec308-f206-41e7-8a2c-247262557979](https://user-images.githubusercontent.com/59475851/177470702-7fa6e79e-ea85-4c26-8eb2-fb283dd6fdd9.png)



[참조](https://www.markdownguide.org/basic-syntax/#headings)

## 마크다운 문법 -List

- List는 순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성
  - **순서가 있는 ol 설명**
    ![177243010-36fc8846-bc11-4308-a9c4-ef40a7597d21](https://user-images.githubusercontent.com/59475851/177470745-09c1e6a2-e13e-4211-898c-92b1a4d6ff1d.png)




  - **순서가 없는 ul 설명**
    ![177243014-ba64a4e9-4064-4b2e-ba2f-60676a097e41](https://user-images.githubusercontent.com/59475851/177470769-78edc233-9ae3-4ba9-8e06-0182d065eca2.png)


[참조](https://www.markdownguide.org/basic-syntax/#lists-1)

## 마크다운 문법 -Fenced Code block

- **코드 블록은 backtick 기호 3개를 활용하여 작성(```)**

- **코드 블록에 특정 언어를 명시하면 Syntax Highlighting 적용 가능**

  >일부 환경에서는 적용이 되지 않을 수 있음
  >![177268115-527eb0af-3fe2-4ffb-9b04-b2b8c4bc4b9f](https://user-images.githubusercontent.com/59475851/177470801-910d9be3-c320-431d-ac5a-0219edb57292.png)


  >![177268122-10e918ee-c463-4b9d-b718-fdd8c86670bb](https://user-images.githubusercontent.com/59475851/177470825-eb6c1b08-f29e-4ec7-8433-370bbff98a9e.png)


[참조](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)

## 마크다운 문법 – Inline Code block

- 코드 블록은 backtick 기호 1개를 인라인에 활용하여 작성(`)
  ![177268736-43bfe8a4-1330-48ca-8603-4c33574db073](https://user-images.githubusercontent.com/59475851/177470887-9b070ff9-ed48-46f0-bb72-540157e02d11.png)


[참조](https://www.markdownguide.org/basic-syntax/#code)

## 마크다운 문법 – Blockquotes (인용문)

- ">"를 통해 인용문을 작성

>![177269109-5986bfe6-796b-4701-b611-3971279413f4](https://user-images.githubusercontent.com/59475851/177470930-1c3a1675-1c72-4e8b-bd41-f34e162b3f4a.png)


[참조](https://www.markdownguide.org/basic-syntax/#blockquotes-1)

## 마크다운 문법 – 이미지

- ![문자열](C:\Users\user\Desktop\san-juan-mountains)을 통해 이미지를 사용 가능
  - 특정 파일들 포함하여 연결 시킬 수도 있음

## 마크다운 문법 – text 강조

- 굵게(bold), 기울임(Italic)을 통해 특정 글자들을 강조

  - **굵게(bold)**
  ![177269753-9c22fdb6-311d-4d88-967e-c89383b4a4d6](https://user-images.githubusercontent.com/59475851/177470965-2a955498-34dc-4066-8de9-e07f8f37ef04.png)




  - **기울임(Italic))**
  ![177269832-ca851855-d05b-4ba5-a964-aec28a72d3c4](https://user-images.githubusercontent.com/59475851/177471001-a6177c0d-cf39-470d-be83-26f3aab09224.png)
</details>

<details>
<summary>🖥2022년 07월 06일🖥: 🤔Git??🤔</summary>

# Interface

인터페이스 : 무언가를 조작하는 전면



### GUI (Graphic User Interface)

: 그래픽으로 유저가 조작한다.

  - `새로 만들기` > `폴더`	

    *이 대상에 이름이 'test1'인 폴더가 이미 있습니다.* 

    

### CLI (Command Line Interface)

: 명령을 줄단위로 조작한다. 

- Windows - CMD, Powershell / MacOS - Terminal

- 명령 프롬프트에서 `$ mkdir 폴더명` 입력

  *mkdir: cannot create directory 'test1': File exists*





# 디렉토리 관리

디렉토리 (directory) : 폴더

$ 뒤에 명령어를 입력하여 사용



### CLI 기초 명령어

- `pwd` (*print working directory*) : 현재 디렉토리 출력
- `cd` `____` (*change directory*) : 디렉토리 이동
  - `폴더명`
  - `.` : 현재 디렉토리
  - `..` : 상위 디렉토리
- `ls` (*list*) : 목록
- `mkdir` `폴더명` (*make directory*) : 디렉토리 생성
- `rm` `파일명` (*remove*) : 파일 제거
- `rm -r` `폴더명` : 디렉토리 제거
  - `-r` : 반복
    - 디렉토리 제거의 경우 디렉토리 안의 모든 파일을 지워야 디렉토리가 제거되므로 -r을 사용함
- `touch` : 0바이트의 빈 파일 생성. 파일의 날짜와 시간을 수정 
- `첫 글자` + `Tab` : 자동완성
- `clear` / `ctrl` + `l` : 전체 삭제





# 버전 관리

버전 (Version) : 컴퓨터 소프트웨어의 특정 상태

버전 관리 : 동일 정보에 대한 여러 버전을 관리하는 것

- 버전 간 차이(diff)와 수정 이유를 메세지로 남길 수 있음 = 커밋 메세지
- 현대 파일들을 안전한 상태로 과거 모습 그대로 복원 가능 (반대의 경우 O)



### 분산 버전 관리 시스템 (DVCS)

- 중앙 집중식 버전 관리 시스템은 중앙에서 버전을 관리하고 파일을 받아서 사용한다
- 분산 버전 관리 시스템은 원격 저장소(Remote Repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유한다





# Git 

### 개요

분산 버전 관리 시스템으로 코드의 버전을 관리하는 도구 

- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발

- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율



### 특징

- Git은 데이터를 파일 시스템의 스냅샷으로 관리하며 크기가 매우 작다
- 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않는다
- 기존의 델타 기반 버전 관리 시스템과 가장 큰 차이를 가진다



## 기본 흐름 

1. 작업을 하고
2. 변경된 파일을 모아 (add) 
3. 버전으로 남긴다 (commit)



Working Directory → Staging area → Repository

(Untracked)―――→ (Staged) ――→ (Commited)

- Working Directory : 파일의 변경사항이 있는 공간

- Staging Area : 버전으로 기록하기 위한 파일 변경사항의 목록이자 해당 파일들이 모이는 임시 공간

- Repository : 커밋(버전)들이 기록되는 공간



커밋 = SW의 경우 반드시 작동 가능한 상태여야 함

→ 임시저장용으로 사용하지 말 것!



### Working Directory (Untracked)

`$ git init`

: **repository를 생성**하는 명령어

- 디렉토리 내에 **.git** 이라는 숨김 폴더를 생성
- (master) : git으로 관리되고 있는 폴더
- `$ git unit` 을 선언하기 전 반드시 대상 디렉토리 경로 확인



### Staging Area (Staged)

`$ git add <file>`

: working directory 상의 변경 내용을 **staging area에 추가**하는 명령어 

디렉토리 내 요소 전체를 staged 상태로 만들 때에는 파일명 대신 `.` (현재 디렉토리) 사용 가능

- untracked → staged
- modified → staged



### Repository (Commited)

`$ git commit -m '<커밋메세지>'`

: staged 상태의 파일들을 커밋을 통해 **버전으로 기록(=커밋)**하는 명령어

- SHA-1 해시를 사용하여 40자 길이의 체크섬을 생성하고, 이를 통해 고유한 커밋을 표기
- 커밋 메시지는 변경 사항을 알아볼 수 있도록 명확하게 작성



### Status 

`$ git status`

: **현재 상태를 확인**하는 명령어 

- Git 저장소에 있는 **파일의 상태**를 확인하기 위하여 사용

  - Untracked Files

  - Changes not staged for commit

  - Changes to be comitted

  - Nothing to commit, working tree clean

    


##### $ git status 로 확인할 수 있는 파일의 상태 

- Tracked : 이전부터 버전으로 관리되고 있는 파일

  - Unmodified : git status에 나타나지 않음
  - Modified : Changes not staged for commit 
  - Staged : Changes to be commited

- Untracked : 버전으로 관리된 적 없는 파일 (파일을 새로 만든 경우)

  

  - modified : 파일이 수정된 상태 


  (add 명령어를 통하여 Staging Area로)

  - staged : 수정된 파일을 곧 커밋할 것이라고 표시한 상태 


  (commit 명령어를 통해 Repository로)

  - commited : 커밋이 된 상태




### Log

`$ git log` 

: 현재 저장소에 기록된 **커밋**을 조회(=**버전 확인**)

- 다양한 옵션을 통해 로그를 조회할 수 있음

  ​	`$ git log` `-1` : 직전 커밋을 조회 

  ​	`$ git log` `-oneline` : 한 줄로 표시

  ​	`$ git log` `-2 --oneline` : 최근 두 커밋을 한 줄로 표시





# GitHub

**원격 저장소** (Remote Repository) : 네트워크를 활용한 저장소

-  *GitHub, GitLab, Bitbucket*
- Git과 같이 GitHub도 **버전**을 관리한다.



## 기본 흐름

1. 원격 저장소를 만들고 저장소 설정을 한다 `$ git remote add`
2. 로컬 저장소의 버전을 원격 저장소로 보낸다 `$ git push`
3. 원격 저장소의 버전을 로컬 저장소로 가져온다 `$ git pull`



원격 저장소의 주소

https://`github.com`/`GitHubUsername`/`RepositoryName`.git

*[My TIL Repository](https://github.com/soyolee-dev/TIL.git)*



### Remote  

`$ git` `remote` `add origin` ` <url.git>`

- `$ git` : Git에게 명령
- `remote` `add origin` : 원격 저장소를 origin으로 추가
  - 일반적으로 origin으로 사용



`$ git` `remote` `-v` : 원격 저장소 정보 확인

`$ git` `remote` `rm` `<원격 저장소 이름>` : 원격 저장소 삭제



### Push

`$ git push` `<원격 저장소 이름>` `<브랜치 이름>`

- 원격 저장소로 로컬 저장소 변경 사항(commit)을 올림(push)
- 로컬 폴더의 파일/폴더가 아닌 저장소의 **커밋**(버전)이 올라감



#### Push Error

```bash 
! [rejected]			master -> master (fetch first)

error: failed to push some refs to 'url'
```

- 로컬-원격 저장소 간 커밋 이력이 다른 경우 발생
- 원격 저장소의 커밋을 원격 



### Pull

`$ git pull` `<원격 저장소 이름>` `<브랜치 이름>`

- 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합



### Clone

`$ git clone` `<url>`

- 원격 저장소를 복제하여 모든 버전을 가져옴

- 원격 저장소 이름의 폴더로 이동해서 활용

  



## 프로젝트에서의 활용

- **init** : 로컬에서 새로운 프로젝트를 시작

- **push** : 내가 한 로컬 프로젝트 개발 공유

- **pull** : 원격 저장소의 커밋 가져오기

​				*프로젝트 개발 중 다른 사람의 커밋 받아오기*

- **clone** : 원격 저장소를 복제

​				*원격에 있는 프로젝트 시작, 협업 프로젝트, 외부 오픈소스 참여, Git 저장소를 GitHub에서 생성 후 시작...*



## Git 파일 관리 심화

### .gitignore 

- 일반적인 개발 프로젝트에서 버전 관리와 관계 없는 파일이나 디렉토리가 발생

  - [gitignore.io](https://github.com/github/gitignore)에서 개발 언어, 개발 환경(OS, IDE) 등을 설정하여 파일을 생성할 수 있다

- Git 저장소에 **.gitignore 파일을 생성**하여 해당 내용을 관리

  - 특정 파일 : *a.txt* (모든 a.txt) 	

  ​					*test/a.txt* (test 폴더의 a.txt)

  - 특정 디렉토리 : */my_secret*
  - 특정 확장자 : **.exe*
  - 예외 처리 : ***!**b.exe*
  </details>
