CREATE DATABASE `plug` /*!40100 DEFAULT CHARACTER SET latin1 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `Project_id` varchar(200) DEFAULT NULL,
  `Title` varchar(200) DEFAULT NULL,
  `TxtContent` varchar(1000) DEFAULT NULL,
  `Img_id` varchar(200) DEFAULT NULL,
  `Vid_id` varchar(200) DEFAULT NULL,
  `Doc_id` varchar(200) DEFAULT NULL,
  `Requests` varchar(200) DEFAULT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Project_id` (`Project_id`),
  UNIQUE KEY `Title` (`Title`),
  UNIQUE KEY `TxtContent` (`TxtContent`),
  UNIQUE KEY `Img_id` (`Img_id`),
  UNIQUE KEY `Vid_id` (`Vid_id`),
  UNIQUE KEY `Doc_id` (`Doc_id`),
  UNIQUE KEY `Requests` (`Requests`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

CREATE TABLE `skilltag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `skill` varchar(999) NOT NULL,
  `s_uid` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Firstname` varchar(20) NOT NULL,
  `Secondname` varchar(120) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(120) NOT NULL,
  `image_file` varchar(20) NOT NULL,
  `password` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
