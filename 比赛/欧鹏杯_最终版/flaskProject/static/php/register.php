<!-- 验证 -->
<?php
    if(empty($_POST["name"])){
        die("用户名不能为空!!");
    }

// 设置密码输入不能小于6位，不满足条件时进行提示
    if(strlen($_POST["pass"]) < 6){
        die("密码不能小于6位!!");
    }

    if($_POST["pass"] !== $_POST["qpass"]){
        die("两次密码不一致!!");
    }

    if(!filter_var($_POST["email"],FILTER_VALIDATE_EMAIL)){
        die("请输入正确的邮箱格式！！");
    }


    // 加密,将密码加密后赋值给$pass_hash变量
    $pass_hash = password_hash($_POST["pass"],PASSWORD_DEFAULT);
    $name = $_POST["name"];
    // 将pass_hash变量的值显示在网页上
    // echo $_pass_hash;


    // 连接数据库 start
    // 使用mysqli新建一个数据库对象
    new mysqli("localhost","root","123456","aids_web_users_data");
    // 如果连接失败则抛出提示
    if($mysqli->connect_errno){
        die("数据库连接错误：".$mysqli->connect_error);
    }
    // 数据库连接 end

    if(isset($_POST["reg"])){
        $sql = "insert into users (name,email,pass_hash) values('$name','$email','$pass_hash')";
        $mysqli->query($sql);

        if($mysqli->affected_rows > 0){
            echo "<script>alert('恭喜你注册成功，马上跳转到登录页面!';window.location.href = '/html/login.html';)</script>";
        }
    }