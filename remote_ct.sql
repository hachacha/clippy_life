CREATE TABLE `videos` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `channel` varchar(128) NOT NULL,
 `title` varchar(128) DEFAULT NULL,
 `post` varchar(20) DEFAULT NULL,
 `date_copied` datetime DEFAULT NULL,
 `file_path` varchar(256) DEFAULT NULL,
 `description` varchar(512) NOT NULL,
 `notes` varchar(256) NOT NULL DEFAULT '0',
 PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8
