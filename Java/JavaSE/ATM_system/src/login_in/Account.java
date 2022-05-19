package login_in;

import java.util.ArrayList;
import java.util.Random;

public class Account {
    private String user_name;
    private String password;
    private String account_num;
    private double balance;
    private double withdraw_limits;

    public Account() {
    }

    //balance do not need to initialize
    public Account(String user_name, String password, String account_num, double withdraw_limits) {
        this.user_name = user_name;
        this.password = password;
        this.account_num = account_num;
//        this.balance = balance;
        this.withdraw_limits = withdraw_limits;
    }

    public String getUser_name() {
        return user_name;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getAccount_num() {
        return account_num;
    }

    public void setAccount_num(String account_num) {
        this.account_num = account_num;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public double getWithdraw_limits() {
        return withdraw_limits;
    }

    public void setWithdraw_limits(double withdraw_limits) {
        this.withdraw_limits = withdraw_limits;
    }
}
