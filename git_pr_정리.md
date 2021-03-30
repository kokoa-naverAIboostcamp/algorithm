# git 정리

**( 원본레포 원격저장소 : upstream, fork해온 내 레포 원격저장소: origin 라고 하자)**

## upstream 내용을 origin에 동기화하기

- 원본 레포를 fork해오기

- 로컬로 origin 가져오기

  `git clone origin의_주소`

- 로컬 origin에 upstream레포 등록

  `git remote add upstream 원본레포주소(https://~~)`

- 등록 잘 되었는지 확인

  `git remote -v   `

- upstream 레포 로컬에 최신화

  `git fetch upstream`

- upstream의 원하는 브랜치로부터 origin/main(or master)로 merge

  `git checkout BRANCH_NAME #로컬 origin의 원하는 브랜치로 이동`

  `git merge upstream 원하는브랜치`

​		=> 여기까지 origin의 로컬상태를 최신화 한 것

​		=> 위 두 단계를 다음 명령어로 줄일 수 있음 : `git pull upstream BRANCH_NAME`

- origin 원격 저장소에 올리기

  `git push origin BRANCH_NAME`

## pr보내기

origin에서 upstream의 파일을 수정하고자 할 때, pr을 보내 upstream의 권한자가 수정여부를 결정할 수 있게 함

### pr 보낼 때

- origin에서 파일 수정하고 add, commit

- push 하기 전에

  `diff`

  `diff-check`

  확인하고 push하기!

---

- origin레포로 들어가서(웹) pull request -> new pull request -> create pull request -> pr 메세지 작성

  ![image-20210225223414751](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225223414751.png)

  ![image-20210225223458680](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225223458680.png)

  ![image-20210225223534012](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225223534012.png)

- 또는 command 라인에서

  `git request-pull upstream/브랜치이름 BRANCH_NAME`

  ref : https://midnightcow.tistory.com/135

  -> git request-pull upstream/main origin/main 했더니..

![image-20210225223134368](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225223134368.png)

​			오류남 command에서는 어떻게 pr보내는지 ㅠ

---

### pr을 받았을 때, pr 내용 변경하기

![image-20210225232230138](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225232230138.png)

- pr의 Files changed에 pr의 가장 최신 상태가 나옴

- 여기서 파란 플러스 누른채 영역 드래그하면 그 영역을 수정가능

- 아래 사진과 같은 칸이 생기는데, 여기서 insert suggestion(빨간 동그라미)를 눌르고 그 안에 코드를 제안할 수 있음

  ![image-20210225233248468](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225233248468.png)
  -> 예시에서는 `#네오` 를 추가하고자 함

  -> `Add single comment`는 단순 코멘트(알람 일일이 감)

  -> `Start review`는  코멘트+리뷰 로 `submit review` 해야 일괄로 반영됨

- 위에서 코드를 `Start review`하면 제안이 `pending`되고 다른사람들이 Conversation 탭에서 다음과 같이 확인가능

  ![image-20210225233630754](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225233630754.png)

  -> 위 초록부분 아래 부분에 빨간부분(아까 드래그한 부분)을 아래 초록부분(제안한 코드)으로  수정하겠다는 뜻

- 위 suggestion에 대해 원본레포에서 권한이 있는 참여자들이 3가지 액션 취할 수 있음(제안한 본인은 못함)

  **내용 차이**

  `comment ` : pr에 대한 단순 코멘트 -> 특별한 경우가 아니면 사용하지 않음(일반코멘트 아니고 여기서만)

  `approve` : 내가 너의 pr을 읽었고 승인했다는 뜻 -> 이게 투표! ex. 회사 내규로 n명이상의 approve를 받으면 merge할 수 있다

  `request change` : pr내용을 반드시 수정해야한다는 뜻

- suggestion이 받아들여지면(위 사진의 Commit suggestion), pr이 수정되고 그에 해당하는 commit이 생김 

- 만약 pr이 merge되기 전 수정내용을 이전으로 돌리고 싶으면, pr을 보낸자가 로컬에서 돌리고 싶은 커밋으로 reset하면 됨

  `git reset --hard 이동하고자_하는_커밋해쉬코드`

  => pr의 커밋은 origin에서 관리하는 것!

- reset 하고 다시 push(오류 나니까 강제 '+' 해줘야 함)

  `git push origin +현재브랜치`

---

### pr 받았을 때, upstream에 merge하기

ref : https://evan-moon.github.io/2019/08/30/commit-history-merge-strategy/

- pr에 대한 모든 수정이 끝나면, upstream의 권한자가 pr을 merge할 수 있음

  `create a merge commit`: pr의 모든 커밋상태를 upstream 커밋 히스토리에 모두 반영

  ​	-> 개발자가 과거의 모든 기록을 알 수 있다는 장점이 있음

  ​	-> 너무 자세한 히스토리가 남기 때문에 머지가 많아지면 커밋 히스토리 그래프의 가독성이 떨어질 수 있음

  ![image-20210225235200050](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225235200050.png)

  `squash and merge` : pr의 모든 커밋을 하나로 합쳐서 upstream 커밋 히스토리에 반영

  ​	-> 가독성이 좋아지지만, 자세한 정보를 알 수 없음

  ![image-20210225235354466](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210225235354466.png)

  `rebase and merge` : pr의 커밋을 upstream에서 커밋한 것처럼 rebase

  ​	-> rebase and merge해도 커밋 히스토리에 pr의 브랜치와 커밋히스토리들이 남긴 함

  ​	-> 그러나 upstream 타임라인에도 똑같은 커밋 히스토리가 남고, pr의 브랜치를 삭제하면 처음부터 upstream 내에서 커밋한 것처럼 깔끔한 커밋히스토리를 얻을 수 있음 

- 보통  기본 `create a merge commit` 만 사용함

  -> 이전 커밋들을 합친 머지커밋이나 rebase를 사용했을 때 conflict나면 해결이 어렵기 때문에!

### issue 활용하기

- 해당 레포나 특정 pr에 대해서 issue를 생성하여 토론할 수 있음
- issue 수가 많아져서 찾기 어려울 때를 위해 Labels 사용

- Milestones로 최대 3개의 이슈까지 그룹화하여 관리할 수 있음

ref : https://yagom.net/forums/topic/github-issue-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/

