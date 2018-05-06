-- 20189426

CREATE TABLE `menu_type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL DEFAULT '' COMMENT '菜单分类名称 ',
  `image_id` varchar(128) DEFAULT NULL COMMENT '分类图片id',
  `type_index` int(11) unsigned DEFAULT '0' COMMENT '菜单分类排序',
  `modify_time` datetime DEFAULT NULL COMMENT '修改时间',
  `sha_id` varchar(32) NOT NULL DEFAULT '' COMMENT '菜单md5(title)值',
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='菜单分类';


CREATE TABLE `foods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sha_id` varchar(32) NOT NULL DEFAULT '',
  `title` varchar(256) NOT NULL DEFAULT '' COMMENT '标题',
  `post_time` datetime DEFAULT NULL COMMENT '发布时间',
  `modify_time` datetime DEFAULT NULL COMMENT '修改时间',
  `price` float NOT NULL DEFAULT '0' COMMENT '价格',
  `discount_price` float DEFAULT NULL COMMENT '折扣价',
  `Unit` varchar(36) DEFAULT NULL COMMENT '计量单位 份/瓶',
  `total_num` int(11) NOT NULL DEFAULT '1' COMMENT '总库存',
  `description` varchar(10240) DEFAULT NULL COMMENT '其他描述信息',
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `sha_id` (`sha_id`),
  KEY `sha_id_index` (`sha_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='菜品';


CREATE TABLE `menutype_foods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `menu_sha_id` varchar(32) NOT NULL DEFAULT '' COMMENT '菜单分类id',
  `foods_sha_id` varchar(32) NOT NULL DEFAULT '' COMMENT '菜品id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='菜单分类对应的菜品';

CREATE TABLE `restaurant_tables` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL DEFAULT '' COMMENT '餐桌名称',
  `number` int(11) NOT NULL COMMENT '编号',
  `sha_id` varchar(32) NOT NULL COMMENT 'md5(title+number)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `sha_id` (`sha_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='餐桌信息';

CREATE TABLE `foods_order` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `order_sha_id` varchar(32) NOT NULL DEFAULT '' COMMENT '订单编号',
  `nickName` varchar(128) DEFAULT NULL COMMENT '用户名',
  `purePhoneNumber` varchar(20) DEFAULT NULL COMMENT '用户联系方式',
  `table_sha_id` varchar(32) DEFAULT NULL COMMENT '餐桌sha_id',
  `table_no` int(11) DEFAULT NULL COMMENT '餐桌编号',
  `table_title` varchar(128) DEFAULT NULL COMMENT '餐桌名',
  `state` int(11) DEFAULT NULL COMMENT '订单状态 0 可编辑 1 已在备菜 2 无效 3 订单异常',
  `post_time` datetime DEFAULT NULL COMMENT '订单生成时间',
  `description` varchar(1024) DEFAULT NULL COMMENT '其他描述信息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单信息';

CREATE TABLE `order_items` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `item_sha_id` varchar(32) DEFAULT NULL,
  `title` varchar(256) DEFAULT NULL COMMENT '菜品标题',
  `price` float DEFAULT NULL COMMENT '价格',
  `post_time` datetime DEFAULT NULL COMMENT '发送时间',
  `num` int(11) DEFAULT '0' COMMENT '数量',
  PRIMARY KEY (`id`),
  KEY `item_sha_id` (`item_sha_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单详情';

CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sha_id` varchar(32) NOT NULL DEFAULT '' COMMENT ' md5(purePhoneNumber)',
  `nickName` varchar(64) DEFAULT NULL COMMENT '用户昵称',
  `gender` int(11) DEFAULT NULL COMMENT '用户的性别，值为1时是男性，值为2时是女性，值为0时是未知',
  `city` varchar(64) DEFAULT NULL COMMENT '用户所在城市',
  `province` varchar(64) DEFAULT NULL COMMENT '用户所在省份',
  `country` varchar(64) DEFAULT NULL COMMENT '用户所在国家',
  `language` varchar(64) DEFAULT NULL COMMENT '用户的语言，简体中文为zh_CN',
  `unionId` varchar(256) DEFAULT NULL COMMENT '用户信息',
  `phoneNumber` varchar(20) DEFAULT NULL COMMENT ' 用户绑定的手机号（国外手机号会有区号）',
  `purePhoneNumber` varchar(20) DEFAULT NULL COMMENT '没有区号的手机号',
  `countryCode` varchar(64) DEFAULT NULL COMMENT '区号',
  `password` varchar(256) DEFAULT NULL COMMENT '用户登录密码',
  `avatarUrl` varchar(256) DEFAULT NULL COMMENT '用户头像信息',
  `description` varchar(1024) DEFAULT NULL COMMENT '其他描述信息',
  `point` int(11) DEFAULT '0' COMMENT '积分',
  PRIMARY KEY (`id`),
  KEY `sha_id` (`sha_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户信息表';