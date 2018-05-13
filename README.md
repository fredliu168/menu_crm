
# 微信小程序点餐后台管理

> 2018.4.25 启动微信小程序点餐开发


#开发环境:

```
iMAC  macOS High Sierra 10.13.2
python 3.6   
mysql 5.7.21
Sequel pro: 数据操作软件
```


# cmd 提交代码到git

```
git add *
git commit -m "微信小程序点餐"
git push origin master
```


## python 生成项目依赖文件

```cmd
(venv)$ pip freeze >requirement.txt
```
安装依赖文件

```cmd
(venv)$ pip install -r requirement.txt
```




使用Docker安装mysql搭建数据库开发环境

> 容器相关操作可以参考该文章<Docker — 从入门到实践> https://www.gitbook.com/book/yeasy/docker_practice

Mysql Docker 操作指南

> https://hub.docker.com/_/mysql
 

数据库存放本地目录

> /Users/fred/PycharmProjects/docker_v/mysql/data

```cmd
拉取mysql

docker pull mysql:5.7.21

docker run --name fred-mysql -p 3306:3306 -v /Users/fredliu/Documents/PycharmProjects/docker_v/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=fred123456 -d mysql:5.7.21

-p 3306:3306：将容器的3306端口映射到主机的3306端口


查看容器启动情况

docker ps 

```




docker容器常用操作


启动配置的容器
```html
docker start fred-mysql
docker start mynginx
```

列出镜像
docker images

删除悬空none镜像

docker rmi $(docker images -f "dangling=true" -q)

删除容器

docker rm container_id

删除镜像

docker image rm image_id
 

2.启动终止状态的容器
```cmd
docker container start fred-mysql
```

3.将一个运行态的容器终止，然后再重新启动它

```cmd
docker container restart  fred-mysql 

```


# 数据结构定义

使用mysql存储数据

> 数据库名称 menu_book

## BANNER 标题栏滚动图片

```
#20180330 暂时未启用
    id  int
    name VARCHAR(256) 标题栏图片名称
    title VARCHAR(256) 标题栏图片标题
    description VARCHAR(10240) 内容描述
    post_time datetime 发布时间
    start_time  datetime  --开始展示时间
    end_time    datetime  --结束展示时间

```

## USER 发布用户信息

```
    # 字段信息
    # 用户信息   
    id          int          # 自增加值 
    sha_id      VARCHAR(32) # md5(purePhoneNumber)
    nickName    VARCHAR(64)  # 用户昵称
    gender      int #用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
    city        VARCHAR(64)# 用户所在城市
    province    VARCHAR(64)# 用户所在省份
    country     VARCHAR(64)# 用户所在国家
    language    VARCHAR(64)# 用户的语言，简体中文为zh_CN
    
    unionId      VARCHAR(256) #用户信息

    phoneNumber       VARCHAR(64)  # 用户绑定的手机号（国外手机号会有区号）
    purePhoneNumber VARCHAR(16) #没有区号的手机号
    countryCode VARCHAR(16) # 区号
    
    password    VARCHAR(256) # 用户登录密码
   
    #
    avatarUrl    VARCHAR(256)  # 用户头像信息 上传到qiniu,md5值
    verify      int  # 用户是否认证 0 未认证, 1 认证
    description  varchar(1024) #其他描述信息
    point int #积分
 
    
```
## role_name 角色表

```
id      int
title   VARCHAR(32) -- 角色名称
sha_id  VARCHAR(32) -- 角色id
description  varchar(1024) #其他描述信息

```

## user_role 用户角色

```
 id          int          # 自增加值 
 user_sha_id     VARCHAR(32) # 用户id
 rold_sha_id     VARCHAR(32)        #角色id
 
```

## menu_type 菜单分类

```
id int --自增id 
sha_id varchar(32) --菜单md5(title)值
title      varchar(128)  --菜单分类名称 
modify_time datatime --修改时间
image_id      varchar(128) --分类图片id
type_index int --菜单分类排序
```

## foods 菜品

```
   -- 发布信息
    id           int --自增id
    sha_id       varchar(32) --md5(title)
    title        varchar(256) -- 标题
    #  
    post_time   datetime  -- 发布时间   
    modify_time    datetime  --修改时间
    #    
    
    # 基本信息
    price       float  # 价格
    discount_price   float #折扣价
    unit        varchar(36)   # 计量单位 份/瓶
    total_num int  # 总库存 
    description        varchar(10240) #其他描述信息
    food_index      INT # 排序
    # 图片介绍
    main_img_sha_id # 主显示图id

```

## food_images 菜品的图片

```
id int
food_sha_id varchar(32) # 菜品id
img_sha_id varchar(32) # 图片id

```

## images 图片信息

```
id int
sha_id  varchar(32) # 图片哈希值
path varchar(512) #图片存放路径 
post_time datetime # 上传时间

```

## menutype_foods 菜品对应的菜单分类

```
id  int
menu_sha_id varchar(32) # 菜单分类id
foods_sha_id varchar(32) # 菜品id


```

## restaurant_tables 餐厅餐桌编号

```
id int
title varchar(256) --餐桌名称
sha_id varchar(32) -- md5(title+number)
number   int --编号



```

# 当前订单信息

## foods_order_items 订单
```
  id int --自增id
  order_sha_id varchar(32) --订单编号 foods_order order_sha_id
  item_sha_id varchar(32) --清单 order_item item_sha_id

```
## foods_order 订单信息

``` 
    id              int      --自增id
    order_sha_id    varchar(32) --订单编号 
    nickName        varchar(128) -- 用户名 
    purePhoneNumber varchar(20) -- 用户联系方式,关联用户 外键
    table_sha_id    varchar(32) --餐桌sha_id
    table_no        int --餐桌编号
    table_title     varchar(128) --餐桌名 
    #lock            int --订单是否锁定,锁定后无法修改 
    # settlement    int --订单是否结算
    state           int --订单状态 0 可编辑 1 已在备菜 2 无效 3 订单异常
    post_time       datetime  -- 订单生成时间
    description     varchar(1024) #其他描述信息 
    
```
 

## order_items 订单清单信息
```
   id           int --自增id
   item_sha_id  varchar(32) --MD5(post_time+str(orderItem.num )+str(orderItem.price)+orderItem.title+orderItem.food_sha_id)
   food_sha_id  varchar(32) -- 菜品id
   title        varchar(256) -- 菜品标题  
   num          int     -- 数量
   price        float -- 价格 
   #
   post_time    datetime  -- 发送时间    
    
```


# 历史订单信息(订单结账后自动归档到历史清单里面)

## history_foods_order_item 订单
```
  id int --自增id
  order_sha_id varchar(32) --订单编号
  item_sha_id varchar(32) --清单

```
## history_foods_order 订单信息

``` 
    id int --自增id
    order_sha_id varchar(32) --订单编号
    post_time   datetime  -- 订单生成时间
    phone        varchar(20) -- 用户联系方式,关联用户 外键
    table_no     int --餐桌编号
    user_name    varchar(128) -- 用户名 
    lock         int --订单是否锁定,锁定后无法修改 
    settlement   int --订单是否结算
    description        varchar(10240) #其他描述信息
    
```
 

## history_order_item 订单清单信息
```
   id           int --自增id
   item_sha_id       varchar(32) md5(table_no+post_time+title) 
   title        varchar(256) -- 菜品标题  
   price        float -- 价格 
   #
   post_time   datetime  -- 发送时间   
   description        varchar(10240) #其他描述信息
    
```

# 实现步骤:

1.设计字段

2.录入数据库

3.数据展示

4.提供数据接口

5.小程序开发




# 怎么搭建微信小程序的本地测试服务器

##问题的提出

Mac环境

> 方便快捷地搭建小程序的测试服务器

> 小程序对于网络请求的URL的特殊要求

> 不能出现端口号

> 不能用localhost

> 必须用https


安装nginx

```
docker run -d --name weixin-nginx -v /Users/fred/PycharmProjects/docker_v/nginx/conf/nginx.conf:/etc/nginx/nginx.conf:ro nginx

```

Git pull 强制覆盖本地文件

```
git fetch --all
git reset --hard origin/master
git pull
```

