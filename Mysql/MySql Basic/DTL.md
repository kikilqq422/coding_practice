
事务之中的
delete 和 truncate 的区别：是否可以ROLLBACK

[SET AUTOCOMMIT = 0 ;
 START TRANSACTION;
 DELETE FROM major;                            TRANCATE FROM major;
 ROLLBACK （成功）]                             ROLLBACK(失败) ]
 
 