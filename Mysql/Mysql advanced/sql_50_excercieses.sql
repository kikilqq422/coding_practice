-- 1、 locate students' info whose grade of course 01 is higher than that of 02
    查询"01"课程比"02"课程成绩高的学生的信息及课程分数  
-- 一定是stu_id 和 01 的分数， 02的分数一一对应，用来对比。重点是要有关联条件，消除笛卡尔积

SELECT stu.* , sc.* , sc2.* FROM student stu 
LEFT JOIN score sc on stu.s_id = sc.s_id and sc.c_id = 01
LEFT JOIN score sc2 on stu.s_id = sc2.s_id and sc2.c_id = 02
WHERE sc.s_score > sc2.s_score


-- 2、 selelct students whose course choice have 01 or 02 or none of them; 查询学生选课存在" 01 "课程但可能不存在" 02 "课程的情况（不存在时显示为 null
SELECT
	* 
FROM 
	( SELECT score.*, student.s_name, student.s_birth FROM score, student WHERE score.s_id = student.s_id AND	c_id = 01 ) t1
LEFT JOIN 
	( SELECT score.* , student.s_name, student.s_birth FROM score , student WHERE score.s_id = student.s_id AND c_id = 02 ) t2 
ON t1.s_id = t2.s_id 	


-- 3、 select students whose avarage scores are higher than 60 查询平均成绩大于等于 60 分的同学的学生编号和学生姓名和平均成绩
SELECT * ,ROUND(AVG(sc.s_score),2) AS avg_score, SUM(sc.s_score) FROM student stu 
LEFT JOIN score sc on stu.s_id = sc.s_id
GROUP BY stu.s_id
HAVING avg_score >= 60
ORDER BY avg_score desc
-- 内连接
SELECT sc.s_id,student.s_name,avg(sc.s_score) FROM score sc ,student WHERE sc.s_id = student.s_id  GROUP BY  sc.s_id  HAVING avg(sc.s_score) > 60;

-- 5、selelct all the students's student id, name, total courses and sum of scores. attention: null 查询所有同学的学生编号、学生姓名、选课总数、所有课程的成绩总和
-- ！！！易错点： count的行数一定是可能有null的，如果count id等不为空的列，则会数量不正确

SELECT * , SUM(sc.s_score) AS sum_score, COUNT(sc.s_score) AS course_num FROM student stu 
LEFT JOIN score sc on stu.s_id = sc.s_id
GROUP BY stu.s_id

-- 6、 selelct teachers whose names contain famaly name Li; 查询「李」姓老师的数量 注意通配符的顺序，"李%"， "%李%"含有李字的所有教师数量
SELECT COUNT(t_id) AS "李老师_num" FROM (
SELECT * FROM teacher WHERE teacher.t_name LIKE "李%") T

-- 7、查询学过「张三」老师授课的同学的信息。需要四表相连 
SELECT * FROM student INNER JOIN 
(SELECT score.s_id, score.s_score FROM score INNER JOIN (
SELECT teacher.t_id, course.c_id FROM teacher, course WHERE teacher.t_id = course.t_id and t_name = '张三') t1 on score.c_id = t1.c_id) t2 WHERE student.s_id = t2.s_id

-- 8、查询没有学全所有课程的同学的信息
SELECT * , SUM(sc.s_score) AS sum_score, COUNT(sc.s_score) AS course_num FROM student stu 
LEFT JOIN score sc on stu.s_id = sc.s_id
GROUP BY stu.s_id
HAVING course_num < 3 

-- 9、查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
SELECT * FROM student stu LEFT JOIN 
score sc on stu.s_id = sc.s_id 
WHERE sc.c_id in (
SELECT sc.c_id FROM student stu 
LEFT JOIN score sc on stu.s_id = sc.s_id
WHERE stu.s_id = 01) AND stu.s_id != 01
GROUP BY stu.s_id

-- !!! 9、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
-- 琢磨 网友提供的思路(厉害呦~): IF(expr1,a,b) 如果表达式成立，返回a,否则返回b
-- 为什么为OR不能是and,因为sum(if(a or b, 1,0)) > 1的情况可以保证必须为01,02，and的话，无法保证01,02,03的情况，只能保证01+02的情况
SELECT st.*, sc.c_id
FROM student st
INNER JOIN score sc ON sc.`s_id`=st.`s_id`
GROUP BY st.`s_id`
HAVING SUM(IF(sc.`c_id`="01" OR sc.`c_id`="02" ,1,0))>1

-- !!!13、查询和"01"号的同学学习的课程完全相同的其他同学的信息
select st.* from student st 
left join score sc on sc.s_id=st.s_id
group by st.s_id
having group_concat(sc.c_id) = (
select group_concat(sc2.c_id) from student st2
left join score sc2 on sc2.s_id=st2.s_id
where st2.s_id ='01' )

-- 15、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT stu.s_id, stu.s_name, AVG(sc.s_score) as avg_score, COUNT(sc.c_id) FROM student stu 
LEFT JOIN score sc on stu.s_id = sc.s_id
GROUP BY sc.s_id
HAVING (SUM(sc.s_score)/COUNT(sc.c_id))<60

select st.s_id,st.s_name,avg(sc.s_score) from student st
left join score sc on sc.s_id=st.s_id
where sc.s_id in (
select sc.s_id from score sc 
where sc.s_score<60 or sc.s_score is NULL
group by sc.s_id having COUNT(sc.s_id)>=2
)
group by st.s_id

-- 17、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
SELECT stu.s_id, stu.s_name, t1.score1, t2.score2, t3. score3, avg_t.平均成绩 as avg_score FROM student stu
LEFT JOIN
(SELECT sc.s_id, sc.s_score score1 FROM score sc WHERE c_id = 01) t1 on stu.s_id = t1.s_id
LEFT JOIN
(SELECT sc.s_id, sc.s_score score2 FROM score sc WHERE c_id = 02) t2 on stu.s_id = t2.s_id
LEFT JOIN
(SELECT sc.s_id, sc.s_score score3 FROM score sc WHERE c_id = 03) t3 on stu.s_id = t3.s_id
LEFT JOIN
(SELECT sc.s_id, ROUND(avg(sc.s_score),2) "平均成绩" FROM score sc GROUP BY sc.s_id) avg_t on stu.s_id = avg_t.s_id
ORDER BY avg_score DESC

select st.s_id,st.s_name,avg(sc4.s_score) "平均分",sc.s_score "语文",sc2.s_score "数学",sc3.s_score "英语" from student st
left join score sc on sc.s_id=st.s_id and sc.c_id="01"
left join score sc2 on sc2.s_id=st.s_id and sc2.c_id="02"
left join score sc3 on sc3.s_id=st.s_id and sc3.c_id="03"
left join score sc4 on sc4.s_id=st.s_id
group by st.s_id 
order by SUM(sc4.s_score) desc

-- 18.!!! 查询各科成绩最高分、最低分和平均分：以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
-- 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
SELECT c.c_id, c.c_name, t1.*
FROM course c INNER JOIN
(SELECT c_id, AVG(s_score) avg_score, MAX(s_score) Max, MIN(s_score) Min,
SUM(CASE when s_score >= 60 Then 1 else 0 end)/COUNT(s_score) as "及格率",
SUM(CASE when s_score >= 70 AND s_score < 80 Then 1 else 0 end)/COUNT(s_score) as "中等率",
SUM(CASE when s_score >= 80 AND s_score <90 Then 1 else 0 end)/COUNT(s_score) as "优良率",
SUM(CASE when s_score >=90 AND s_score <=100 Then 1 else 0 END)/COUNT(s_score) as "优秀率"
FROM score  
GROUP BY c_id)t1
WHERE c.c_id = t1.c_id


-- !!! 19、按各科成绩进行排序，并显示排名(实现不完全)
-- 开窗函数，partition by相当于group by 的意思，对 c_id进行排序，按照 s_score进行排序
SELECT *, ROW_NUMBER() over (partition by c_id ORDER BY s_score DESC) as 'rank' FROM score
SELECT *, rank() over (partition by c_id ORDER BY s_score DESC) as 'rank' FROM score
SELECT *, DENSE_RANK() over (partition by c_id ORDER BY s_score DESC) as 'rank' FROM score

-- ！！！排序的做法，非开窗函数，作出01的排序
select
 t1.c_id  -- 课程号
 ,t1.s_score  -- 分数
 ,(select count(distinct t2.s_score)   -- 课程去重
		from Score t2
		where t2.s_score  >= t1.s_score   -- SQL实现排序
		and t2.c_id = '01') 'rank'
from Score t1   -- 通过相同的表实现自连接
where t1.c_id = '01'
order by t1.s_score desc



-- ！！！总的排序
select * from (select 
                t1.c_id,
                t1.s_score,
                (select count(distinct t2.s_score) 
                 from Score t2 
                 where t2.s_score>=t1.s_score and t2.c_id='01') 'rank'
              from Score t1 where t1.c_id='01'
              order by t1.s_score desc) t1

union
select * from (select 
                 t1.c_id
                 ,t1.s_score
                 ,(select count(distinct t2.s_score)
                   from Score t2 
                   where t2.s_score>=t1.s_score and t2.c_id='02') 'rank'
               from Score t1 where t1.c_id='02'
               order by t1.s_score desc) t2

union
  select * from (select 
                  t1.c_id,
                  t1.s_score,
                  (select count(distinct t2.s_score) from Score t2 where t2.s_score>=t1.s_score and t2.c_id='03') 'rank'
                from Score t1 where t1.c_id='03'
                order by t1.s_score desc) t3
								
								
 
-- 20、查询学生的总成绩并进行排名
SELECT sc1.s_id, sc1.c_id, sum(sc1.s_score),
(SELECT count(DISTINCT SUM(sc2.s_score)) FROM score sc2 
WHERE count(DISTINCT SUM(sc2.s_score)) >= SUM(sc1.s_score)
GROUP BY sc2.s_id) AS "RANK"
FROM score sc1
GROUP BY sc1.s_id

FROM student stu

SELECT * FROM (
SELECT
	sc1.s_id,
	GROUP_CONCAT( sc1.c_id ) AS c_id,
	sum( sc1.s_score ) AS total
	
FROM
	score sc1 
GROUP BY
	sc1.s_id 
ORDER BY
	total DESC ) t
	
-- ！！！只是按总成绩排序，并且处理了0值
-- 这个方法只是按照成绩高低来了一个总排名
select st.s_id,st.s_name, GROUP_CONCAT(sc.c_id) as course_total ,(case when sum(sc.s_score) is null then 0 else sum(sc.s_score) end) as score_total
 from student st
left join score sc on sc.s_id=st.s_id
group by st.s_id order by sum(sc.s_score) desc	

-- ！！！不仅有总成绩展示，还有排名: 
-- 思路：1：先算出总成绩 2. 总成绩与count总成绩的排名 3. 聚合 4. 与stu表聚合
SELECT stu.s_id, stu.s_name, t2.c_id, 
(CASE WHEN t2.sum_score IS NULL THEN 0 ELSE t2.sum_score END) AS SUM_SCORE, -- 处理了null值的问题 
t2.rank
FROM student stu 
LEFT JOIN
(SELECT
	sc1.s_id,
	GROUP_CONCAT(sc1.c_id) AS c_id,
	SUM(sc1.s_score) as sum_score, 
-- 	！！！注意：因为有group by之后才回有sum(s_score)
-- 	所以要先把总成绩算出来，再count排名，不能放在一个表中，同表中：group by在where执行之后执行
		(
		SELECT COUNT(DISTINCT total) as count_num
		FROM
		(
		SELECT
			SUM(sc2.s_score) AS total
		FROM
			score sc2 
		GROUP BY
			sc2.s_id
			)t
		WHERE t.total > sum(sc1.s_score) -- 此处等同于 t.total > sum(sc1.s_score) rank不加1
		) + 1 AS "rank" 
	FROM
		score sc1 
GROUP BY
	sc1.s_id
ORDER BY SUM(sc1.s_score) DESC
) t2
ON stu.s_id = t2.s_id
