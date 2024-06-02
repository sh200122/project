const express = require('express');  
const router = express.Router();  
const jwt = require('jsonwebtoken'); // 假设使用JWT进行用户认证  
const User = require('../models/User'); // 假设你有一个用户模型  
  
// 获取用户个人信息  
router.get('/', authenticateToken, (req, res) => {  
    User.findById(req.user._id) // 假设req.user包含了已认证用户的_id  
        .then(user => {  
            res.json(user);  
        })  
        .catch(error => {  
            res.status(500).send('Error retrieving user profile');  
        });  
});  
  
// 用于中间件的认证函数（简化版）  
function authenticateToken(req, res, next) {  
    const authHeader = req.headers['authorization'];  
    const token = authHeader && authHeader.split(' ')[1];  
  
    if (token == null) return res.sendStatus(401); // 如果没有提供token，返回401  
  
    jwt.verify(token, 'your-secret-key', (err, user) => {  
        if (err) return res.sendStatus(403); // 如果token无效，返回403  
        req.user = user; // 将已认证的用户附加到请求上，供后续中间件和路由使用  
        next(); // 继续处理请求  
    });  
}  
  
module.exports = router;