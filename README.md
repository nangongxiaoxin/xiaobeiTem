# 你该打卡了！


## 快速使用

### 准备材料：

- 抓包获取 user-agent
- 抓包获取 authorization

### 部署云函数：

- 创建云函数

![image-20220621141153415](https://cdn.jsdelivr.net/gh/nangongxiaoxin/img@962affa6eb48df0dd05227d76398c816997e5862/2022/06/22/dbb229f7c66befe39339c4945c921a34.png)

- 创建触发器：

  

  ![image-20220621141343661](https://cdn.jsdelivr.net/gh/nangongxiaoxin/img@fd8439b4bda8f0f065ccc2f7a2f81d73593c4c23/2022/06/22/4cb129c7b7d385702e33ac7945e97957.png)

- 删除示例代码并上传新代码

  

  ![image-20220621141628837](https://cdn.jsdelivr.net/gh/nangongxiaoxin/img@26e67d0e4ab408cbe42f6bd67061042cb5286071/2022/06/22/739ca4d7be527a7e444d14c262577906.png)

- 保存代码、部署代码进行测试

  

## 注意：

- 注意入口函数

- 按照抓包信息修改33、34行的 `user-agen`、`Authorization`

  `"User-Agent": "Mozilla/5.0 M************",`

  `"Authorization": "Bearer ey*************",`

  

- 使用方糖消息推送时需要填写对应 `SCKEY`（SCKEY在[方糖官网](https://sc.ftqq.com/3.version)获取）

