## 快速使用

### 准备材料：

- 抓包获取 user-agent
- 抓包获取 authorization

### 部署云函数：

- 创建云函数

![image-20220621141153415](https://gitee.com/xiangbeixing/img_picgo/raw/master/img/image-20220621141153415.png)

- 创建触发器：

  ![image-20220621141343661](https://gitee.com/xiangbeixing/img_picgo/raw/master/img/image-20220621141343661.png)

  

- 删除示例代码并上传新代码

  ![image-20220621141628837](https://gitee.com/xiangbeixing/img_picgo/raw/master/img/image-20220621141628837.png)

- 保存代码、部署代码进行测试

  

## 注意：

- 注意入口函数

- 按照抓包信息修改33、34行的 `user-agen`、`Authorization`

  `"User-Agent": "Mozilla/5.0 M************",`

  `"Authorization": "Bearer ey*************",`

  

- 使用方糖消息推送时需要填写对应 `SCKEY`（SCKEY在[方糖官网](https://sc.ftqq.com/3.version)获取）

