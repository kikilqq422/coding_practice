package com.qq;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
//@MapperScan("com.qq.mapper")
public class SpringBoot06MybatisApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBoot06MybatisApplication.class, args);
    }

}
