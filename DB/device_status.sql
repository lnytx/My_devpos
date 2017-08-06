/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50703
Source Host           : localhost:3306
Source Database       : my_devpos

Target Server Type    : MYSQL
Target Server Version : 50703
File Encoding         : 65001

Date: 2017-08-06 22:11:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `device_status`
-- ----------------------------
DROP TABLE IF EXISTS `device_status`;
CREATE TABLE `device_status` (
  `ip` varchar(20) NOT NULL,
  `cpu` varchar(20) DEFAULT NULL,
  `memory` varchar(20) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `product` varchar(50) DEFAULT NULL,
  `platform` varchar(50) DEFAULT NULL,
  `sn` varchar(50) DEFAULT NULL,
  `Createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of device_status
-- ----------------------------
