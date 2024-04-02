-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
  REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
SELECT
  *
FROM  -- 메인
  articles
INNER JOIN  -- 서브
  users
ON users.id = articles.userId;

SELECT
  *
FROM  -- 메인
  users
INNER JOIN  -- 서브
  articles
ON articles.userId = users.id;

SELECT
  articles.id, title, name, userId
FROM  -- 메인
  articles
INNER JOIN  -- 서브
  users
ON users.id = articles.userId
WHERE userId = 1;

-- LEFT JOIN
SELECT *
FROM
  articles
LEFT JOIN
  users
ON
  users.Id = articles.userId;

SELECT *
FROM
  users
LEFT JOIN
  articles
ON
  users.Id = articles.userId
WHERE
  articles.userId IS NULL;