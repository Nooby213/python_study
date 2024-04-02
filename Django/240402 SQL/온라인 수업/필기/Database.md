# Database
- 체계적인 데이터 모음
- 데이터
  - 저장이나 처리에 효율적인 형태로 변환된 정보
---
### 기존의 데이터 저장 방식
1. 파일 이용
  - 어디서나 쉽게 사용 가능
  - 데이터를 구조적으로 관리하기 어려움
2. 스프레드 시트 이용
  - 테이블의 열과 행을 사용해 데이터를 구조적으로 관리가능
- 스프레드 시트의 한계
- 크기
  - 일반적으로 약 100만 행까지만 저장가능
- 보안
  - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
- 정확성
  - 여러 시트에 분산된 정보의 변경이 어렵다
---
- 데이터베이스 역할
  - 데이터를 저장하고 조작 (CRUD)
---
## 관계형 데이터베이스
- 데이터 간의 관계가 있는 데이터 항목들의 모음
- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
---
- 관계
  - 여러 에티블 간의 논리적 연결
  - 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음(특정 날짜 구매 고객, 배송지연된 고객 조회 등)
---
### 관계형 데이터베이스 관련 키워드
1. Table (Relation)
  - 데이터를 기록하는 곳
2. Field (Column, Attribute)
  - 각 필드에는 고유한 데이터 형식(타입)이 지정됨
3. Record(Row, Tuple)
  - 각 레크드에는 구체적인 데이터 값이 저장됨
4. Database(Schma)
  - 테이블의 집합
5. Primary Key (PK)
  - 각 레코드의 고유한 값
  - 관계형 데이터베이스에서 레크드의 식별자로 활용
6. Foreign Key (외래 키, FK)
  - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
  - 다른 테이블의 기본 키를 참조
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는데 사용
---
## RDBMS
- DBMS
  - 데이터베이스를 관리하는 소프트웨어 프로그램
  - 데이터 저장 및 관리를 용이하게 하는 시트템
  - 데이터베이스와 사용자 간의 인터페이스 역할
  - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
---
- RDBMS
  - 관계형 데이터 베이스를 관리하는 소프트웨어 프로그램
  - 종류
    - SQLite
    - MYSQL
    - PostgreSQL
    - Oracle Database
---
- SQLite
  - 경량의 오픈 소스 데이터베이스 관리 시스템
  - 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공
---
#### 데이터베이스 정리
- Table은 데이터가 기록되는 곳
- Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
- 데이터는 기본 키 또는 외래 키를 통해 **결합(join)**될 수 있는 여러 테이블에 걸쳐 구조화 됨
---
## SQL
- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의
---
### SQL Syntax
1. SQL 키워드는 대소문자를 구분하지 않음
  - 하지만 대문자로 작성하는 것을 권장 (명시적 구분)
2. 각 SQL Statemetns의 끝에는 세미콜론(';')이 필요
  - 세미콜론은 각 SQL Statements을 구부하는 방법 (명령어의 마침표)
---
### SQL Statements
- SQL을 구성하는 갖아 기본적인 코드 블록
```python
SELECT column_name FROM table_name
```
- 해당 예시 코드는  SELECT Statement 라 부름
- 이 Statement는 SELECT, FROM 2개의 keyword로 구성 됨
---
#### 수행 목적에 따른 SQL Statements 4가지 유형
1. DDL - 데이터 정의
2. DQL - 데이터 검색
3. DML - 데이터 조작
4. DCL - 데이터 제어

![유형](/이미지/유형.PNG)
--- 
## QUERY
- 데이터베이스로부터 정보를 요청하는 것
- 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
- SQL 표준
  - SQL은 미국 국립 표준 협회와 국제 표준화 기구에 의해 표준이 채택 됨
  - 모든 RDBMS에서 SQL 표준을 지원
  - 다만 각 RDBMS마다 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의
---
## Querying data
### SELECT
- 테이블에서 데이터를 조회
  ```sql
  SELECT
   Name, Milliseconds / 60000 AS '재생 시간(분)'
  From
   tracks;
  ```
- SELCET 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
- 테이블의 데이터를 조회 및 반환
- '*' 를 사용하여 몯느 필드 선택
---
### Sorting data
- ORDER BY statement
- 조회 결과의 레코드를 정렬
- NULL 값이 존재할 경우 오름차순 정렬시 먼저 출력됨
---
### Filtering data
- Clause
  - DISTINCT
    ```sql
    -- DISTINCT
    SELECT DISTINCT
      Country
    FROM
      customers
    ORDER BY
      Country;
    ```
  - WHERE
    ```sql
    -- WHERE
    SELECT
      LastName, FirstName, Company, Country
    FROM
      customers
    WHERE
      Company IS NULL
      AND Country = 'USA';
    ```
  - LIMIT
    ```sql
    SELECT
      TrackId, Name, Bytes
    FROM
      tracks
    ORDER BY
      Bytes DESC
    -- 7개까지
    -- LIMIT
    --   7;

    -- 4번째부터 4개 출력
    -- LIMIT
    --   3, 4;
    LIMIT 4 OFFSET 3;
    ```
- Operator
  - BETWEEN
    ```sql
    -- BETWEEN
    SELECT
      Name, Bytes
    FROM
      tracks
    WHERE
      -- Bytes >= 100000
      -- AND Bytes <= 500000;
      Bytes BETWEEN 100000 AND 500000
    -- ORDER BY 는 WHERE 뒤에 위치해야 됨
    ORDER BY
      Bytes;
      ```
  - IN
    ```sql
    SELECT
      LastName, FirstName, Country
    FROM
      customers
    WHERE
      -- Country = 'Canada'
      -- OR Country = 'Germany'
      -- OR Country = 'France';
      Country IN ('Canada', 'Germany', 'France');
    ```
  - LIKE
    ```sql
    SELECT
      LastName, FirstName
    FROM
      customers
    WHERE
      -- % 0 개이상의 문자열과 일치하는지 확인
      LastName LIKE '%son';
    
    SELECT
      LastName, FirstName
    FROM
      customers
    WHERE
      -- '_' 단일 문자와 일치하는지 확인
      -- 4글자이며 a로 끝나는
      FirstName LIKE '___a';
    ```
  - Comparison
  - Logical
---
## Grouping data
- GROUP BY clause
  - 레코드를 그룹화하여 요약본 생성
  - 집계 함수와 함께 사용
  - FROM 및 WHERE 절 뒤에 배치
  - GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
---
- Aggregation Functions
  - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
  - SUM, AVG, MAX, MIN, COUNT ...
  ```sql
  SELECT
    Composer,
    AVG(Bytes) AS avgOfBytes
  FROM
    tracks
  GROUP BY
    Composer
  ORDER BY
    avgOfBytes DESC;

  SELECT
    Composer,
    AVG(Milliseconds / 60000) as avgOfMinute
  FROM
    tracks
  GROUP BY
    Composer
  HAVING
    avgOfMinute < 10;
  ```
---
## Create a table
- 테이블 생성
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(constraints) 작성
---
### PRAGMA
- 테이블 schema(구조) 확인
```sql
-- Table 구조 확인
PRAGMA table_info('examples');
```
![PRAGMA](/이미지/PRAGMA.PNG)

- cid
  - Column ID를 의미하며 각 컬럼의 고유한 식별자를 나타내는 정수 값
  - 직접 사용하지 않으며 PRAGMA 명령과 같은 메타데이터 조회에서 출력 값으로 활용됨
- 데이터 타입
  1. NULL : 아무 값도 포함하지 않음을 나타냄
  2. INTEGER : 정수
  3. REAL : 부동 소수점
  4. TEXT : 문자열
  5. BLOB : 이미지, 동영상, 문서 등의 바이너리 데이터
---
### Constarints 제약조건
- 테이블의 필드에 적용되는 규칙 또는 제한 사항
- 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장

#### 대표 제약 조건 3가지
- PRIMARY KEY
  - 해당 필드를 기본 키로 지정
  - INTEGER 타입이만 적용되며, INT, BIGINT 등과 같은 다른 정수 유형은 적용되지 않음
- NOT NULL
  - 해당 필드에 NULL 값을 허용하지 않도록 지정
- FOREIGN KEY
  - 다른 테이블과의 외래 키 관계를 정의
---
#### AUTOINCREMENT keyword
- 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
- 특징
  - 필드의 자동 증가를 나타내는 특수한 키워드
  - 주로 primary key 필드에 적용
  - INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
  - 삭제된 값은 무시되며 재사용할 수 없게 됨 

---
### Modifying table fields

#### Alter Table
- 테이블 및 필드 조작

