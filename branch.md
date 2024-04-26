# Branch
```
$ git branch : 브랜치 목록 확인
$ git branch -r  : 원격 저장소의 브랜치 목록 확인
$ git branch <브랜치 이름> : 새로운 브랜치 생성
$ git branch -d <브랜치 이름> : 병합된 브랜치만 삭제 가능
$ git branch -D <브랜치 이름> : (주의) 강제 삭제 (병합되지 않은 브랜치도 삭제 가능)
```
## Switch
현재 브랜치에서 다른 브랜치로 '**HEAD**' 를 이동 시키는 명령어
```
$ git swich <다른 브랜치 이름> : 다른 브랜치로 이동
$ git swich -c <브랜치 이름> : 브랜치를 새로 생성과 동시에 이동
$ git swich -c <브랜치 이름> <커밋 ID> : 특정 커밋 기준으로 브랜치 생성과 동시에 이동
```
## Git log
```
$ git log --oneline
$ git log --oneline --all
$ git log --oneline --all --graph
```
---
# Three types of Merge
1. Fast-Forward Merge : merge 과정 없이 단순히 브랜치의 포인터가 이동
2. 3-way-merge : 병합 시 각 브랜치의 커밋 두개와 공통 조상 커밋하나를 사용하여 병합하는 것, 부분 수정 했을 때
3. merge conflict : 병합하는 두 브랜치에서 '**같은 파일의 같은 부분**'을 수정한 경우, 사용자가 직접 최종 내용을 선택하여 충돌 해결해야한다.

# RESTORE
- ADD 하기전에 수정하지 말아야 할 부분을 수정하거나 잘못 작성했을 때
  - $ git restore 파일명
- ADD 하고 난 뒤 add 해제
  - $ git rm --cached 파일명
    - 최초 커밋이 없을 때 스테이징 되어있는 파일 삭제
  - $ git restore --staged 파일명
- 직전에 commit을 수정할때
  - $ git commit --amend

# RESET
- $ git reset --soft 커밋아이디
  - 언스테이징
- $ git reset --mixed 커밋아이디
  - 워킹디렉토리
- $ git reset --hard
  - 커밋 후의 변동사항 삭제

# REVERT  
- $ git revert 커밋아이디