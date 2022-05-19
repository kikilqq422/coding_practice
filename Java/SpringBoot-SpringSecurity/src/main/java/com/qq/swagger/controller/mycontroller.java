package com.qq.swagger.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class mycontroller {
    // ！！！直达首页，有两个路径配置
    @RequestMapping({"/","/index"})
    public String getindex(){
        return "index";
    }

    // 登录页面
    @RequestMapping("/toLogin")
    public String toLogin(){
        return "/views/login";
    }
    // 很重要的编程思想，代码的复用，因为level1,2,3下面的页面完全一样，所以可以用传入id的方式来调节到达的页面
    @RequestMapping("/level1/{id}")
    public String tolevel1(@PathVariable("id") int id){
        return "/views/level1/"+id;
    }

    @RequestMapping("/level2/{id}")
    public String tolevel2(@PathVariable("id") int id){
        return "/views/level2/"+id;
    }

    @RequestMapping("/level3/{id}")
    public String tolevel3(@PathVariable("id") int id){
        return "/views/level3/"+id;
    }

}
