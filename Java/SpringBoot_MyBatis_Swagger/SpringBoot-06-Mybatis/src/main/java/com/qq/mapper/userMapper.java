package com.qq.mapper;

import com.qq.swagger.pojo.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper      //mybatis mapper层
@Repository //Dao层，如果不配置，不会被注入bean
public interface userMapper {
    public List<User> users();

    public User selectById(int id);

    public int updateUser(User user);

    public int addUser(User user);

    public int deleteUserById(int id);
}
