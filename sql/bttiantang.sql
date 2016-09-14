/*
Navicat MySQL Data Transfer

Source Server         : 47.88.1.153_3307
Source Server Version : 50173
Source Host           : localhost:3307
Source Database       : bttiantang

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2016-09-01 14:50:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bttiantang_category
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_category`;
CREATE TABLE `bttiantang_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bttiantang_content
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_content`;
CREATE TABLE `bttiantang_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `names_chn` text NOT NULL,
  `names_eng` text NOT NULL,
  `names_nick` text NOT NULL,
  `imgs` varchar(255) NOT NULL,
  `tags` text NOT NULL COMMENT '标签',
  `areas` varchar(255) NOT NULL COMMENT '地区',
  `years` varchar(255) NOT NULL COMMENT '年份',
  `directors` text NOT NULL COMMENT '导演',
  `writers` text NOT NULL COMMENT '编剧',
  `casts` text NOT NULL COMMENT '主演',
  `imdbs` varchar(255) NOT NULL COMMENT 'imdb',
  `details` varchar(255) NOT NULL COMMENT '详情',
  `download` text NOT NULL,
  `created_at` datetime NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique` (`url`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=23742 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bttiantang_content_copy
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_content_copy`;
CREATE TABLE `bttiantang_content_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `names_chn` text NOT NULL,
  `names_eng` text NOT NULL,
  `imgs` varchar(255) NOT NULL,
  `tags` text NOT NULL COMMENT '标签',
  `areas` varchar(255) NOT NULL COMMENT '地区',
  `years` varchar(255) NOT NULL COMMENT '年份',
  `directors` text NOT NULL COMMENT '导演',
  `writers` text NOT NULL COMMENT '编剧',
  `casts` text NOT NULL COMMENT '主演',
  `imdbs` varchar(255) NOT NULL COMMENT 'imdb',
  `details` varchar(255) NOT NULL COMMENT '详情',
  `download` text NOT NULL,
  `created_at` datetime NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique` (`url`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21955 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bttiantang_options
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_options`;
CREATE TABLE `bttiantang_options` (
  `option_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `option_name` varchar(64) NOT NULL COMMENT '配置名',
  `option_value` longtext NOT NULL COMMENT '配置值',
  `autoload` int(2) NOT NULL DEFAULT '1' COMMENT '是否自动加载',
  PRIMARY KEY (`option_id`),
  UNIQUE KEY `option_name` (`option_name`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='全站配置表';

-- ----------------------------
-- Table structure for bttiantang_plugins
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_plugins`;
CREATE TABLE `bttiantang_plugins` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `name` varchar(50) NOT NULL COMMENT '插件名，英文',
  `title` varchar(50) NOT NULL DEFAULT '' COMMENT '插件名称',
  `description` text COMMENT '插件描述',
  `type` tinyint(2) DEFAULT '0' COMMENT '插件类型, 1:网站；8;微信',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态；1开启；',
  `config` text COMMENT '插件配置',
  `hooks` varchar(255) DEFAULT NULL COMMENT '实现的钩子;以“，”分隔',
  `has_admin` tinyint(2) DEFAULT '0' COMMENT '插件是否有后台管理界面',
  `author` varchar(50) DEFAULT '' COMMENT '插件作者',
  `version` varchar(20) DEFAULT '' COMMENT '插件版本号',
  `createtime` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '插件安装时间',
  `listorder` smallint(6) NOT NULL DEFAULT '0' COMMENT '排序',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='插件表';

-- ----------------------------
-- Table structure for bttiantang_route
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_route`;
CREATE TABLE `bttiantang_route` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '路由id',
  `full_url` varchar(255) DEFAULT NULL COMMENT '完整url， 如：portal/list/index?id=1',
  `url` varchar(255) DEFAULT NULL COMMENT '实际显示的url',
  `listorder` int(5) DEFAULT '0' COMMENT '排序，优先级，越小优先级越高',
  `status` tinyint(1) DEFAULT '1' COMMENT '状态，1：启用 ;0：不启用',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=62 DEFAULT CHARSET=utf8 COMMENT='url路由表';

-- ----------------------------
-- Table structure for bttiantang_url
-- ----------------------------
DROP TABLE IF EXISTS `bttiantang_url`;
CREATE TABLE `bttiantang_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Unique` (`url`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=22053 DEFAULT CHARSET=utf8;
