-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 30, 2020 at 03:12 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shopping_cart`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cartid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `cart_qty` int(11) NOT NULL,
  `cart_total` float(10,2) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` tinyint(2) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Table structure for table `cart_products`
--

CREATE TABLE `cart_products` (
  `cartproductid` int(11) NOT NULL,
  `productid` int(11) NOT NULL,
  `cartid` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `productid` int(11) NOT NULL,
  `title` varchar(256) NOT NULL,
  `price` float(10,2) NOT NULL,
  `qty` int(11) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` tinyint(2) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`productid`, `title`, `price`, `qty`, `last_updated`, `datetime`, `status`) VALUES
(3, 'mobile', 15000.00, 5, '2020-08-29 18:44:52', '2020-08-29 18:44:52', 1),
(4, 'earphone', 599.00, 7, '2020-08-29 19:08:27', '2020-08-29 19:08:27', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(233) NOT NULL,
  `password` varchar(233) NOT NULL,
  `usertype` tinyint(1) NOT NULL DEFAULT 1,
  `last_updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` tinyint(2) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `usertype`, `last_updated`, `datetime`, `status`) VALUES
(1, 'admin', '5bc7a057e1fbd58f12bbd3f6329f57f9', 0, '2020-08-29 06:57:19', '2020-08-29 06:54:39', 1),
(2, 'customer', '91ec1f9324753048c0096d036a694f86', 1, '2020-08-29 09:21:44', '2020-08-29 09:21:44', 1),
(6, 'ana', '276b6c4692e78d4799c12ada515bc3e4', 1, '2020-08-29 17:58:06', '2020-08-29 17:58:06', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cartid`);

--
-- Indexes for table `cart_products`
--
ALTER TABLE `cart_products`
  ADD PRIMARY KEY (`cartproductid`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`productid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cartid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cart_products`
--
ALTER TABLE `cart_products`
  MODIFY `cartproductid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `productid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
