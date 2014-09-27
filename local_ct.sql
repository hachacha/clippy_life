CREATE TABLE `clippy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `copy` varchar(999) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `datetime` (`datetime`)
) ENGINE=InnoDB AUTO_INCREMENT=13977 DEFAULT CHARSET=latin1
