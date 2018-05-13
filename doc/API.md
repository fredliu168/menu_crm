
# 对外提供的接口

> 整理时间 2018-04-26

# 1.分类菜单 

## 1.获取菜单分类

GET /menu_type

```json

{
    "code": 10000,
    "msg": "获取数据成功",
    "value": [
        {
            "id": 1,
            "image_id": null,
            "modify_time": null,
            "sha_id": "c7efa94c6ecbe6dafe685fced7341d9f",
            "title": "家常菜",
            "type_index": 0
        }

    ]
}
```

## 2.添加菜单

POST /menu-type
```json
{
 "title":"特色小吃"
}
```

## 3.删除

DELETE /menu-type/<sha_id>

## 4.修改

PUT /menu-type/<sha_id>

```json
{
 "title":"特色小吃"
}
```

# 2.菜品

## 1.添加

POST /food

```json
{
 "title":"全猪肉",
 "price":60,
 "unit":"份",
 "total_num":10,
 "description":"测试"
}

```

# 3.菜单对应的菜品

## 1.添加

POST /food-type

```json
{
 "menu_sha_id":"22f0b4efe54e3d6e6dcc719c79da1f6a",
 "foods_sha_id":"7851f678761ff645f104e1bb9c3280b2"
}
```

## 2.删除

DELETE /food-type/<sha_id>

## 3.获取

GET /food-type
```

[
    {
        "menu_title":"家常菜",
        "sha_id":"c7efa94c6ecbe6dafe685fced7341d9f",
        "foods":[{
         "food_title":"地瓜馒头",
         "total_num":10,
         "price":10,
         "unit":"份",
         "sha_id":"7851f678761ff645f104e1bb9c3280b2"
         },
         {
         
         }
        ]
    },
    {
        "menu_title":"特色小吃",
        "sha_id":"1d56b32bd2554fb84b34cd6f11cb4995",
        "foods":[{
         "food_title":"地瓜馒头",
          "total_num":10,
         "price":10,
         "unit":"份",
         "sha_id":"7851f678761ff645f104e1bb9c3280b2"
         },
         {
         
         }
        ]
    }

]
```

# 3.餐桌

## 1.添加

POST /table

```
{
 "title":"石牛山",
 "number":3
}

```

## 2.获取列表

GET /table

## 3.修改

PUT /table/<sha_id>

```
{
 "title":"石牛山",
 "number":3
}

```


## 4.删除
DELETE /table/<sha_id>



# 4.订单操作

## 1.下订单

POST /order
```
{
 "table_sha_id":"31d35b09fed59da6f5b266cb9943e27d", #餐桌id
 "user_sha_id":"5ba73254e39b2e129de7539aaed43930", # 用户信息
 "description":"test", # 描述信息
 "foods":[
    {
     "sha_id":"22f0b4efe54e3d6e6dcc719c79da1f6a", # 菜品id
     "num":2 # 数量
    },
    {
     "sha_id":"5fbf343679d5bd1449fb280c2ce987ab", # 菜品id
     "num":10 # 数量
    }
]
}

```
