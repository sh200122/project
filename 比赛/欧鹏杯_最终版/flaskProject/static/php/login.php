<?php
    // 连接数据库 start
    // 使用mysqli新建一个数据库对象
    new mysqli("localhost","root","123456","aids_web_users_data");
    // 如果连接失败则抛出提示
    if($mysqli->connect_errno){
        die("数据库连接错误：".$mysqli->connect_error);
    }
    // 数据库连接 end


    // 加密,将密码加密后赋值给$pass_hash变量
    $pass_hash = password_hash($_POST["pass"],PASSWORD_DEFAULT);
    $name = $_POST["name"];

    if(isset($_POST["login"])){
        $sql = "select pass_hash from users where name='$name'";
        $rel = $mysqli->query($sql)->fetch_assoc();

        if($res){
            if(password_verify($_POST["pass"],$res["pass_hash"])){
                echo "<script>window.location.href='user.php?uname=$name';</script>";
            }else{
                echo "<script>alert('密码输入有误！！');history.go(-1);</script>";
            }
        }else{
            echo "<script>alert('用户不存在！！');history.go(-1);</script>";
        }
    }



