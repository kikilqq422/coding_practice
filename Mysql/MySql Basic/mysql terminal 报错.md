**MySQL开启bin-log后，调用存储过程或者函数以及触发器时，会出现错误号为1418的错误:**
```js
ERROR 1418 (HY000): This function has none of DETERMINISTIC, NO SQL,or READS SQL DATA in its declaration and binary logging is enabled(you \*might\* want to use the less safe log\_bin\_trust\_function\_creators variable)
```

**原因分析:**
```js
CREATE PROCEDURE, CREATE FUNCTION, ALTER PROCEDURE,ALTER FUNCTION,CALL, DROP PROCEDURE, DROP FUNCTION等语句都会被写进二进制日志,然后在从服务器上执行。
```
但是，一个执行更新的不确定子程序(存储过程、函数、触发器)是不可重复的，在从服务器上执行(相对与主服务器是重复执行)可能会造成恢复的数据与原始数据不同，从服务器不同于主服务器的情况。

为了解决这个问题，MySQL强制要求：  
在主服务器上，除非子程序被声明为确定性的或者不更改数据，否则创建或者替换子程序将被拒绝。  
这意味着当创建一个子程序的时候，必须要么声明它是确定性的，要么它不改变数据。

声明方式有两种,  
##### 第一种:声明是否是确定性的  
DETERMINISTIC和NOT DETERMINISTIC指出一个子程序是否对给定的输入总是产生同样的结果。  
如果没有给定任一特征，默认是NOT DETERMINISTIC，所以必须明确指定DETERMINISTIC来声明一个子程序是确定性的。  
这里要说明的是:使用NOW() 函数（或它的同义）或者RAND() 函数不会使一个子程序变成非确定性的。对NOW()而言，二进制日志包括时间戳并会被正确的执行。RAND()只要在一个子程序内被调用一次也可以被正确的复制。所以，www.linuxidc.com可以认为时间戳和随机数种子是子程序的确定性输入，它们在主服务器和从服务器上是一样的。

##### 第二种:声明是否会改变数据   
CONTAINS SQL, NO SQL, READS SQL DATA, MODIFIES SQL用来指出子程序是读还是写数据的。  
无论NO SQL还是READS SQL DATA都指出，子程序没有改变数据，但是必须明确地指定其中一个，因为如果任何指定，默认的指定是CONTAINS SQL。

第一种是在创建子程序(存储过程、函数、触发器)时，声明为DETERMINISTIC或NO SQL与READS SQL DATA中的一个，  
例如:
```js
CREATE DEFINER = CURRENT\_USER PROCEDURE \`NewProc\`()  
    DETERMINISTIC  
BEGIN  
 #Routine body goes here...  
END;
```
第二种是信任子程序的创建者，禁止创建、修改子程序时对SUPER权限的要求，设置log\_bin\_trust\_routine\_creators全局系统变量为1。
##### 设置方法:  
1. 在客户端上执行SET GLOBAL log\_bin\_trust\_function\_creators = 1;  
1. MySQL启动时，加上--log-bin-trust-function-creators选贤，参数设置为1  
1. 在MySQL配置文件my.ini或my.cnf中的\[mysqld\]段上加log-bin-trust-function-creators=1

### 我的成功经验：
```JS
mysql> set global log\_bin\_trust\_function\_creators=TRUE$

Query OK, 0 rows affected (0.00 sec)
```
### 创建function时, 出错信息：
```JS
ERROR 1418 (HY000): This function has none of DETERMINISTIC, NO SQL, or READS SQL DATA in its declaration and binary logging is enabled (you \*might\* want to use the less safe log\_bin\_trust\_function\_creators variable)
```
原因：

这是我们开启了bin-log, 我们就必须指定我们的函数是否是  
1. DETERMINISTIC 不确定的  
2. NO SQL 没有SQl语句，当然也不会修改数据  
3. READS SQL DATA 只是读取数据，当然也不会修改数据  
4. MODIFIES SQL DATA 要修改数据  
5. CONTAINS SQL 包含了SQL语句  
  
其中在function里面，只有 DETERMINISTIC, NO SQL 和 READS SQL DATA 被支持。如果我们开启了 bin-log, 我们就必须为我们的function指定一个参数。  
```JS
在MySQL中创建函数时出现这种错误的解决方法：  
set global log\_bin\_trust\_function\_creators=TRUE;
```
