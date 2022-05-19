package login_in;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class ATM_system {
    public static void main(String[] args) {
        //Setup an account object

        //generate accounts arraylist.all accounts objects included
        ArrayList<Account> accounts_data = new ArrayList<>();

        Scanner sc = new Scanner(System.in);

        //generally, login in comes first!!!
        System.out.println("=========================Welcome to Galaxy Bank system=================================");
        while (true){
            System.out.println("Please choice your service:");
            System.out.println("1. Login in");
            System.out.println("2. Register");
            System.out.println("Please enter 1 or 2: ");
            int command = sc.nextInt();

            switch (command){
                case 1:{
                    //check if the account_name and password is correct
                    //else: back to welcome page
                    login_in(accounts_data,sc);
                    break;
                }
                case 2:{
                    //register the acc, check for existence
                    register(accounts_data,sc);
                    break;
                }
                default:{
                    System.out.println("the action is invalid!");
                }
             }
        }
    }

    /**
     *49302403;84682020;55517612
     * @param accounts_data
     * @param sc
     * 1.user input account_num to check if it is available
     * 2.account_num checks and input the password (check the correctness)
     * 3.login success
     */
    public static void login_in(ArrayList<Account> accounts_data, Scanner sc) {
        //check if there's accounts available
        //if 0 accounts, cannot login_in directly
        if (accounts_data.size() == 0){
            System.out.println("Sorry, no accounts available, please register first");
            return;
        }
        //Test purpose: if the accounts has been added
//        for (int i = 0; i < accounts_data.size(); i++) {
//            Account acc_origin = accounts_data.get(i);
//            System.out.println(acc_origin.getAccount_num()+" " +acc_origin.getUser_name());
//        }

        //login process starts
        int count = 3;
        while (count > 0) {
            //input account_num and check for existence
            System.out.println("Please input your account_num: ");
            String account_num = sc.next();

            //check the account_num from arraylist accounts_data
            Account acc = AccountByAcc_num(accounts_data, account_num);
            if (acc != null) {
                System.out.println("Dear " + acc.getUser_name() + " ,You account number is :" + acc.getAccount_num());

                // check the password
                int i = 3;
                while (i > 0) {
                    System.out.println("Please enter your password: ");
                    String password_input = sc.next();
                    if (password_input.equals(acc.getPassword())) {
                        //login successfully
                        System.out.println("Welcome " + acc.getUser_name());
                        System.out.println("Please choose your service.");

                        //login into the menu page
                        //！！！Attention，this menu is about the account acc,hence,put it into the Menu
                        Menu(accounts_data,sc,acc);
                        return;//！！！logout of the main menu

                    } else {
                        System.out.println("Sorry, the password is not correct.");
                        System.out.println("You have " + (i - 1) + " times left.");
                    }
                    i--;
                }
            }else {
                System.out.println("Sorry, the account is invalid, "+ (count-1)+" attempts.");
                count --;
            }
        }
        return;//password is invalid
    }

    /**
     * menu page or main page
     * @param accounts_data
     * @param sc
     * 1.show all the related card info
     * 2.show all the actions
     *
     */
    public static void Menu(ArrayList<Account> accounts_data, Scanner sc,Account account){
        while (true) {
        System.out.println("==================Welcome to the menu page=========================");
            System.out.println("Please choose your service: ");
            System.out.println("1. query your information");
            System.out.println("2. deposit");
            System.out.println("3. withdraw cash");
            System.out.println("4. transfer to anther account");
            System.out.println("5. change your password");
            System.out.println("6. logout");
            System.out.println("7. close the account");
            System.out.println("Please choice your service(1-7): ");
            int command = sc.nextInt();

            switch (command){
                case 1:{
                    //query your information
                    QueryAccount(accounts_data,account);
                    break;
                }
                case 2:{
                    //deposit
                    Deposit(accounts_data,account,sc);
                    break;
                }
                case 3:{
                    //!!!withdraw cash(1. check balance >0; 2. input withdraw amount; 3. amount <= withdraw limits && <= balance)
                    WithDraw(accounts_data,account,sc);
                    break;
                }
                case 4:{
                    //transfer to another account
                    TransferMoney(accounts_data, account, sc);
                    break;
                }
                case 5:{
                    //update your password:after password has been changed, should be logged out
                    ChangePassword(accounts_data, account, sc);
                    return;//logged out re-enter password
                }
                case 6:{
                    //！！！logout, break out to login page； break go back to loop, return get out of the loop
                    System.out.println("You have been logged out!");
                    return;
                }
                case 7:{
                    //close your account， once the account has been closed, should be logged out
                    System.out.println("You are going to close your account: ");
                    System.out.println("The account is closing …… ");
                    accounts_data.remove(account);
                    return;
                }
                default:{
                    System.out.println("The input is invalid, please re-enter");
                    break;
                }
            }
        }
    }


    /**
     *
     * @param accounts_data
     * @param account
     * @param sc
     * 1、check if there is more than one accounts
     * 2、check if the account is your own account number
     * 3、check if the balance is >0;
     * 4、transfer money, check the name
     * 5、one accounts + money ; one account - money
     */
    private static void TransferMoney(ArrayList<Account> accounts_data, Account account, Scanner sc) {
        if (accounts_data.size() < 2) {
            System.out.println("Sorry, no available account in the system.");
            return;
        }
        if (account.getBalance() < 0) {
            System.out.println("Sorry, there is no enough money in the account.");
            return;
        }
        System.out.println("Dear " + account.getUser_name() + "You current balance is: " + account.getBalance());
        double balance = account.getBalance();

        while (true) {
            System.out.println("Please enter the account number you want to transfer to: ");
            String trans_acc = sc.next();
            //check if there's account num in the sye
            Account acc_transfer = AccountByAcc_num(accounts_data, trans_acc);

            if (acc_transfer != null) {
                //first confirm if the transfer is to account person self
                if (acc_transfer.getAccount_num().equals(account.getAccount_num())) {
                    System.out.println("Sorry, you cannot transfer to your own account");
                } else {
                    //begin the transfer process
                    //check the receiver's name
                    String receiver_name = "*" + acc_transfer.getUser_name().substring(1);
                    System.out.println("Please confirm the account's name:  " + receiver_name);
                    String confirm_name = sc.next();
                    if (acc_transfer.getUser_name().startsWith(confirm_name)) {
                        System.out.println("the account is confirmed, please enter amount you want to transfer: ");
                        Double trans_money = sc.nextDouble();
                        System.out.println("The account number is: " + trans_acc);
                        System.out.println("The amount of money you want to transfer is: " + trans_money);
                        if (trans_money <= account.getBalance()) {
                            account.setBalance(account.getBalance()-trans_money);
                            acc_transfer.setBalance(acc_transfer.getBalance()+trans_money);
                            //two accounts should have the same actions
                            System.out.println("Congrats," + trans_money+ " has been made." + "You current balance is: " + account.getBalance());
                            System.out.println("Do you want to make another transfer?(Y/N): ");
                            String confirm = sc.next();
                            if (confirm.equalsIgnoreCase("Y")) {
                                //make another trans
                            } else {
                                System.out.println("You are going to the menu page.");
                                return;
                            }
                        } else {
                            System.out.println("Sorry, the money is not enough, You max amount is: "+account.getBalance());
                        }
                    } else {
                        System.out.println("Sorry, the receiver's name is incorrect, please enter again");
                    }
                }
            } else {
                System.out.println("the account number is invalid, please check again.");
            }
        }
    }

    //!!! check if the balance >= 100 first
    private static void WithDraw(ArrayList<Account> accounts_data, Account account, Scanner sc) {
        if (account.getBalance() <= 100){
            System.out.println("Sorry, there is no enough money");
            return;
        }
        System.out.println("Dear "+account.getUser_name()+"You current balance is: "+account.getBalance());
        System.out.println("You withdraw limits is: "+account.getWithdraw_limits());
        Double balance = account.getBalance();
        while (balance > 0) {
            System.out.println("Please enter the amount you want to get: ");
            int withdraw = sc.nextInt();
            if (withdraw <= account.getWithdraw_limits()){
                if (withdraw <= account.getBalance()){
                    balance -= withdraw;
                    //new balance has been set into accounts
                    account.setBalance(balance);
                    System.out.println("Please take you money: "+balance+"You current amount is: "+account.getBalance());
                    System.out.println("Do you want to withdraw again?(Y/N): ");
                    String confirm = sc.next();
                    if(confirm.equalsIgnoreCase("Y")){
                        //withdraw again
                    }else {
                        return;
                    }
                }else {
                    System.out.println("Sorry, you have no enough money left. Please choose again!");
                }
            }else {
                System.out.println("Sorry, the amount surpass the withdraw limits, please enter again!");
            }
        }
        System.out.println("Sorry, there is no enough money left!");
        return;
    }

    private static void Deposit(ArrayList<Account> accounts_data, Account account, Scanner sc){
        int count = 3;
        while (count > 0) {
            System.out.println("Please enter the amount you want to save: ");
            int save = sc.nextInt();
            System.out.println("Please confirm the amount is: "+ save+"(Y/N)");
            String confirm = sc.next();
            if (confirm.equalsIgnoreCase("Y")){
                Double balance = account.getBalance();
                balance += save;
                account.setBalance(balance);
                System.out.println("The deposit has been done successfully");
                System.out.println("The current balance is: "+ account.getBalance());
                System.out.println("Do you want to make another deposit:(Y/N) ");
                String confirm2 = sc.next();
                if(confirm2.equalsIgnoreCase("Y")){
                    //to make another deposit
                }else {
                    break;
                }
            }else {
                System.out.println("You need more time to think.");
            }
            count--;
            System.out.println(count+" times to deposit.");
        }
    }

    /**
     *
     * @param accounts_data
     * @param account
     * @param sc
     * 1.change the password
     * 2.add new password to account
     */
    private static void ChangePassword(ArrayList<Account> accounts_data, Account account, Scanner sc) {
        int count = 3;
        while (count > 0) {
            System.out.println("Dear " + account.getUser_name()+", Please enter your original password: ");
            String password_to_check = sc.next();

            //compare with the old ones
            if (password_to_check.equals(account.getPassword())){
                int attempt = 3;
                while (attempt > 0) {
                    System.out.println("Please enter your new password: ");
                    String password_new1 = sc.next();
                    System.out.println("Please enter your new password again: ");
                    String password_new2 = sc.next();

                    if (password_new1.equals(password_new2)){
                        //the password is changed, and add to the Accounts
                        account.setPassword(password_new1);
                        System.out.println("Congrats, the new password is set.");
                        return;
                    }else {
                        System.out.println("Sorry, the two passwords are not match, please try again.");
                    }
                    attempt--;
                    System.out.println(attempt+" attempt.");
                }
            }else {
                System.out.println("You password is not correct, please try again.");
            } count--;
        }
    }

    /**
     * The detailed information of the user
     * @param accounts_data
     * @param account
     */
    private static void QueryAccount(ArrayList<Account> accounts_data, Account account){
        System.out.println("=================Dear " + account.getUser_name() + ",welcome========================");
        System.out.println("You account number is: "+account.getAccount_num());
        System.out.println("You account name is: "+account.getUser_name());
        System.out.println("You account balance is: "+ account.getBalance());
        System.out.println("You account withdraw limits is：" + account.getWithdraw_limits());
        return;
    }


    /**Register
     *
     * @param accounts_data
     * @param sc
     * step 1: generate all the prameters for setting up an account
     * step 2: password recheck
     * step 3: generate an 8 digits no_repeat account_num
     * step 4: put the parameters into an object
     * step 5: add them into Arraylist accounts_data
     */
    public static void register(ArrayList<Account> accounts_data, Scanner sc){
        while (true){
            //step 1: generate all the parameters
            System.out.println("Please enter the username: ");
            String user_name = sc.next();

            //password confirm
            // string password should be of the loop for later use
            String password = "";
            while (true) {
                System.out.println("Please enter your password: ");
                String password1 = sc.next();
                System.out.println("Please reenter your password: ");
                String password_check = sc.next();
                if (password_check.equals(password1)) {
                    password = password1;
                    break;
                } else {
                    System.out.println("Your passwords did not match, please re-enter");
                }
            }

            //withdraw limits set
            System.out.println("Please enter the withdraw_limits: ");
            Double withdraw_limits = sc.nextDouble();

            //8 digits account_num and check for existence
            String account_number = Account_number(accounts_data);

            //put all the parameters into an Account
            //public Account(String user_name, String password, String account_num, double withdraw_limits)
            Account account = new Account(user_name, password, account_number, withdraw_limits);

            //put into arraylist accounts_data check for existence
            Account acc_check = AccountByAcc_num(accounts_data,account_number);

            if (acc_check != null) {
                //accounts existence, re-enter all the parameters
                System.out.println("Sorry, the accounts has been exists, please re-enter.");
                break;
            } else {
                accounts_data.add(account);
                System.out.println("Dear " + account.getUser_name() + ",You account has been established!");
                System.out.println("You account number is: " + account.getAccount_num());
                break;
            }
        }
    }

    //generate 8 digits unique account_num
    public static String Account_number(ArrayList<Account> accounts_data) {
        Random r = new Random();
        String acc_num = "";
        while (true) {
            for (int i = 0; i < 8; i++) {
                acc_num += r.nextInt(10);
            }
            //check for existence
            Account acc = AccountByAcc_num(accounts_data, acc_num);
            if (acc == null) {
                //acc_num not exists
                return acc_num;
            }
        }
    }

    //check account for existence by acc_num
    public static Account AccountByAcc_num(ArrayList<Account> accounts_data, String account_num){
        for (int i = 0; i < accounts_data.size(); i++) {
            Account acc = accounts_data.get(i);
            if (acc.getAccount_num().equals(account_num)){
                return acc;
            }
        }
        return null;
    }
}
