package com.qq.swagger.controller;

import com.qq.mapper.userMapper;
import com.qq.swagger.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class userController {
    @Autowired
    userMapper mapper;

    @RequestMapping("/user/users")
    public List<User> selectUsers(){
        List<User> users = mapper.users();
        return users;
    }

    @GetMapping("/user/selectbyid/{id}")
    public User selectByid(@PathVariable("id") int id){
        User user = mapper.selectById(id);
        return user;
    }

    @RequestMapping("/user/update")
    public String updateuser(User user){
        User u = new User(3, "xiaohua", "12456");
        int i = mapper.updateUser(u);
        return "ok";
    }

    @RequestMapping("/user/adduser")
    public String adduser(User user){
        int i = mapper.addUser(new User(8, "xiaohuahua", "12456123"));
        return "ok";
    }

    @GetMapping("/user/delectbyid/{id}")
    public String deleteByid(@PathVariable("id") int id){
        int user = mapper.deleteUserById(id);
        return ""+user;
    }
}
