***五、视图view的更新
SELECT * FROM myv1;
#插入
INSERT INTO myv1 VALUES ('zhangfei', 'zf@qq.com' );
#修改
[UPDATE myv1 SET last_name = 'zhangwj' WHERE last_name = 'zhangfei']; 
#删除
[DELETE FROM myv1 WHERE last_name = 'zhangwj';]

#具备以下特点的视图不允许更新：
#包含GROUP BY, DISTINCT, 包含子查询，JOIN, From后+不可更新的视图中，HAVING, UNION
#常量视图
CREATE OR REPLACE view myv1 
AS 
SELECT 'john' name;
UPDATE myv1 SET name = 'lucy';
#找出manager的信息并做view；
[[CREATE OR REPLACE VIEW myv3
AS
SELECT last_name, email, salary
FROM employees 
WHERE department_id IN (
							SELECT manager_id 
							FROM employees 
							WHERE manager_id IS NOT NULL
);
SELECT * FROM myv3;]]

*视图和表的区别
                                                 是否实际占有物理空间               使用  
视图  CREATE VIEW                 否，只是保持了sql的逻辑        增删改查，一般不用增删改查
表      CREATE TABLE               保存了数据                              增删改查



