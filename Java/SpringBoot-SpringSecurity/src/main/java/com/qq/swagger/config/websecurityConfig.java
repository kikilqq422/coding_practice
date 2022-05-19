package com.qq.swagger.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Configuration
@EnableWebSecurity
public class websecurityConfig extends WebSecurityConfigurerAdapter {
    //配置权限，链式配置
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // 验证，訪問權限的設置
        http.authorizeRequests()
                // index than can be visted by every user
                .antMatchers("/", "/index").permitAll()
                .antMatchers("/level1/**").hasRole("vip1")
                .antMatchers("/level2/**").hasRole("vip2")
                .antMatchers("/level3/**").hasRole("vip3")
                .and()
                //开启自动配置的登录功能：如果没有权限，就会跳转到登录页面！
                // /login 请求来到登录页
                // /login?error 重定向到这里表示登录失败
                .formLogin()
                    //!!!自定义前端参数：与前端login.html中的username，password的name属性相搭配
                    .usernameParameter("user")
                    .passwordParameter("pwd")
                    .loginPage("/toLogin")
                    .loginProcessingUrl("/login")//自定义的登录页面表单提交的url.如果不配置，则要跟loginPage("url")保持一致
                    .permitAll();

        // 源码注释： logout.deleteCookies("remove")
        //         .invalidateHttpSession(false)
        //         .logoutUrl("/custom-logout")
        //         .logoutSuccessUrl("/logout-success")
	   	// 注销功能：
        http.csrf().disable();//!!!导致登录失败可能的原因:关闭csrf功能:跨站请求伪造,默认只能通过post方式提交logout请求
        http.logout()
                    .deleteCookies("remove") //自定义：是否注销cookie
                    .invalidateHttpSession(false)
                    // .logoutUrl("/toLogout") //默认为/logout;自定义logout的url与index.html上面的必须匹配一致
                    .logoutSuccessUrl("/"); //自定义：logout之后的跳转页面redirect

        //增加rememberme功能，注意rememberMeParameter("remember")一定要与前端的name属性相搭配
        http.rememberMe().rememberMeParameter("remember");
    }

    //权限设置
    //在内存中定义，也可以在jdbc中去拿....
    //Spring security 5.0中新增了多种加密方式，也改变了密码的格式。
    //要想我们的项目还能够正常登陆，需要修改一下configure中的代码。我们要将前端传过来的密码进行某种方式加密
    //spring security 官方推荐的是使用bcrypt加密方式。
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        // 从数据库中拿
        // auth.jdbcAuthentication();
        auth.inMemoryAuthentication().passwordEncoder(new BCryptPasswordEncoder()).
                withUser("admin").password(new BCryptPasswordEncoder().encode("123456")).roles("vip1", "vip2", "vip3").
                and().
                withUser("kiki").password(new BCryptPasswordEncoder().encode("234")).roles("vip1").
                and().
                withUser("guest").password(new BCryptPasswordEncoder().encode("123")).roles("vip3");
    }

}