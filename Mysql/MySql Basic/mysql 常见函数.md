一、数学函数：

1. Round

```js
SELECT ROUND(-1.55) ---- -2
SELECT ROUND(-1.45) ---- -1
```

2.  CEIL 向上取整：返回>=参数的最小整数
```js
SELECT CEIL(1.02) ------ 2 
SELECT CEIL(-1.02) ----- -1 #复数可以取证后
```
3. FLOOR 向下取整：返回<=参数的最大整数
```JS
SELECT FLOOR(-9.99) ------ -10 
```
4. TRUNCATE 截断（小数， 位数）
```JS
SELECT TRUNCATE(1.6999, 2); \------ 1.6
```
5. MOD(a, b) 
```js
#【取余公式：a- a/b*b】#a/b➗ 都为整数的话，除号两边结果取整
# 取巧的话： 跟被除数-10的符号有关
SELECT MOD(-10, -3)
```
6. RAND()
- 随机获取一条数据：ORDER BY RAND() ;  
```js
# 要从tablename表中随机提取一条记录，大家一般的写法就是：
SELECT * FROM tablename ORDER BY RAND() LIMIT 1;
```
- 获取随机数0-1范围：SELECT RAND() ;  
- 取整  
	 - SELECT CEIL(RAND());         #1
	 - SELECT CEILING(RAND());   #1
	 - SELECT FLOOR(RAND());     #0
	 - CEIL(RAND()*N)的取值范围：1-N
	 ```js
	 SELECT （CEIL(RAND()*51） + 99) #取随机100-150的数字
	 ```
	 - FLOOR(RAND()*N+1)的取值范围：1-N的值 
	 - 实现一定区域范围的的随机数
	 ```js
	 #i ≤ R ≤ j 这个范围得到一个随机整数 R
	 SELECT FLOOR ((RAND()*（j-i+1）) + i)
	 ```
	 