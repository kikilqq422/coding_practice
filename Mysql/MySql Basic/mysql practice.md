1. 显示出表 employees 的全部列，各个列之间用逗号连接，列头显示成 OUT_PUT
```js
CONCAT ()
SELECT CONCAT(employee_id,',',email,',',last_name,',', first_name,',') OUT_PUT
FROM employees;
```
2. 以‘e’结尾的员工名
```js
SELECT first_name
FROM employees 
WHERE first_name LIKE '%e'; #'e%'以e开头； ‘%e%’包含e
```
3. 查询各个管理者手下员工的最低工资，其中最低工资不能低于6000，没有管理者的员工不计算在内
```js
SELECT MIN(salary),manager_id
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING MIN(salary)>=6000;
#(注意having 和 where的 顺序和位置)
```
4. 查询员工表中的最大入职时间和最小入职时间的相差天数(DIFFRENCE)
```js
SELECT DATEDIFF(MAX(hiredate), MIN(hiredate)) DIFFERENCE 
FROM employees;

SELECT DATEDIFF('1995-2-7','1995-2-6');
```
5.  将字符通过格式转为指定的日期 （应用场景广）
```js
SELECT DATE_FORMAT('1995-7-2', '%Y-%d-%m'); 
#将字符按照其格式和代表的年月日解析 ,注意‘’符号 -- 1995-2-7
```
6. DATE_FORMAT 将日期换成字符
```js
SELECT DATE_FORMAT(NOW(), ‘%Y年%m月%d日’) AS output;
```
7. 外连接：外连接的查询结果为主表中所有的记录和从表中
    查询一个表中有一个表中没有的记录。
                  外连接的查询结果=内连接结果+主表有而从表没有的记录
				  （查询信息主要来自XXX表则为主表）
	左外连接：LEFT左边为主
	右外连接：RIGHT右边为主
e.g. 查询编号>3 并且男朋友为NULL的女神的男朋友信息（查询为女神，所以主表为女）
```js
SELECT ba.name, b.*
FROM beauty ba LEFT JOIN boys b
ON ba.boyfriend_id = b.id
WHERE ba.id > 3 AND b.id IS NULL;  
#选择为NULL的对象做塞选，id为主键且唯一，比较适合； 
#注意两个条件中用'AND'连接，不是‘，’
```
## 常见连接的总结：
![[Pasted image 20210111153225.png]]
![[Pasted image 20210111153658.png]]
#外联+条件
![[Pasted image 20210111153506.png]]
#全外，在mysql里面不支持，但是在其他比如Oracle里面常用
#如果想查非交集部分，直接加条件
8. 插入表数据的时候，如果id列为自增长， 插入values 想要忽略id列，则需要用下面的插入方法：
```js
INSERT INTO 表名(列名1,列名2,列名3......)VALUES(值1,值2,值3........) 
INSERT INTO 表名(列名1,列名2,列名3......) SELECT 值1,值2,值3........ FROM 表名
#一定要对应列出需要插入数值的列名，不列类型
#下面不插入列名，只有数值的时候，会报错：Column count doesn't match value count at row 1
INSERT INTO my_employees VALUES ('patel', 'Ralph', 'Rpatel', '895'), 
#这种方法，在有自增长列的情况下，❌   ('Dance', 'Betty', 'Bdancs', '860'),
							    ('Biri', 'Ben', 'Bbiri', '1100'),
								('Newman', 'Chad', 'Cnewman', '750'),
							    ('Ropeburn', 'Audrey', 'Aropebur', '1550');
								
INSERT INTO 表名 VALUES(值1,值2,值3........) #这种方法，在有自增长列的情况下，❌ 
```

