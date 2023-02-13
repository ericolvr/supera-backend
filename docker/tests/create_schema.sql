DROP TABLE IF EXISTS `reseller`;

CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `score` int DEFAULT NULL,
  `image` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_products_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `products` (`id`, `name`, `price`, `score`, `image`, `created_at`) VALUES
(11, 'caneta', 10.00, 20, 'qwe.jpg', '2023-02-09 21:43:45'),
(22, 'lapis', 10.00, 20, 'path/lapis.jpg', '2023-02-09 23:46:31'),
(33, 'call of dutty', 10.00, 20, 'path/lapis.jpg', '2023-02-10 01:42:57'),
(44, 'Modern Warfare', 10.00, 20, '/Users/erico/Downloads/PS-Python-React-master/assets/call-of-duty-wwii.png', '2023-02-10 01:42:57');


DROP TABLE IF EXISTS `user`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(100) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `role` enum('CLIENT','ADMIN') DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `ix_users_fullname` (`fullname`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `users` (`id`, `fullname`, `mobile`, `email`, `password`, `role`, `created_at`) VALUES
(1, 'Mary Jane', '11 988776655', 'mary@jane.com', '$2b$12$aHnTXHD9BR8PPl.wVfhGp.SPH2VGoA.9VQkGGxva3jnSCshKiVT8C', 'ADMIN', '2023-02-09 22:16:35'),
(2, 'John Doe', '11 987679878', 'john@doe.com', '$2b$12$rXcKGeEe9Rsxdd4PM5/ETusYKEqQjQB0lDX9yhFXKaHjLEjU6DEtK', 'CLIENT', '2023-02-09 22:29:11');



DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `status` enum('UNPROCESSED','PROCESSED') DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_cart_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `cart` (`id`, `user_id`, `product_id`, `quantity`, `created_at`, `status`, `product_name`, `product_price`) VALUES
(131, NULL, 11, 15, '2023-02-11 22:51:35', 'UNPROCESSED', 'caneta', 10.01),
(132, NULL, 22, 3, '2023-02-11 22:51:37', 'UNPROCESSED', 'lapis', 10.99),
(133, NULL, 33, 2, '2023-02-11 22:51:39', 'UNPROCESSED', 'call of dutty', 10.00),
(134, NULL, 44, 2, '2023-02-11 22:51:40', 'UNPROCESSED', 'Modern Warfare', 10.00);

