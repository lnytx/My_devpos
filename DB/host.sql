/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : my_devpos

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2017-08-06 22:10:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `host`
-- ----------------------------
DROP TABLE IF EXISTS `host`;
CREATE TABLE `host` (
  `ip` varchar(15) NOT NULL,
  `hostname` varchar(15) DEFAULT NULL,
  `ostype` varchar(15) DEFAULT NULL,
  `application` varchar(20) DEFAULT NULL,
  `status` int(1) DEFAULT '1',
  `pwd` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `port` varchar(20) NOT NULL DEFAULT '22',
  `groupid` varchar(20) NOT NULL DEFAULT '1',
  `Createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of host
-- ----------------------------
