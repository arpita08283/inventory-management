-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 07, 2021 at 11:37 AM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `QF53HUUBsI`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminregister`
--

CREATE TABLE `adminregister` (
  `regid` int(100) NOT NULL,
  `name` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `adminregister`
--

INSERT INTO `adminregister` (`regid`, `name`, `password`, `email`) VALUES
(17, 'arpita', 'arpita', 'arpitahegde8819@gmail.com'),
(19, 'prakash', 'prakash', 'hegde1317@gmail.com'),
(20, 'tara', 'tara', 'arpitaprakashhegde@gmail.com'),
(21, 'sanju', 'sanju', 'hegdesanjay22@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `productid` int(100) NOT NULL,
  `productname` text NOT NULL,
  `productdesc` text NOT NULL,
  `price` text NOT NULL,
  `qty` text NOT NULL,
  `total` text NOT NULL,
  `avlqty` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `productid` int(100) NOT NULL,
  `username` text NOT NULL,
  `date` text NOT NULL,
  `totalqty` text NOT NULL,
  `totalprice` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`productid`, `username`, `date`, `totalqty`, `totalprice`) VALUES
(1, '', '', '200.0', '1.0'),
(24, 'sanju', '2021-05-07', '3000.0', '10.0'),
(25, 'sanju', '2021-05-08', '5200.0', '30.0');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `productid` int(100) NOT NULL,
  `username` text NOT NULL,
  `productname` text NOT NULL,
  `productdesc` text NOT NULL,
  `price` text NOT NULL,
  `units` text NOT NULL,
  `avlqty` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`productid`, `username`, `productname`, `productdesc`, `price`, `units`, `avlqty`) VALUES
(37, '', 'rice', 'basumathi', '200', 'per kg', '20'),
(39, 'arpita', 'rice', 'basumathi', '200', 'per kg', '6.0'),
(45, 'tara', 'coat', 'wood', '1000', 'per piece', '10.0'),
(46, 'sandeep', 'gdsfhg', 'hdsfbn', '34', '1', '123'),
(48, 'prakash', 'rice', 'basumathi', '200', 'per kg', '10.0'),
(50, 'prakash', 'desk', 'wood', '200', 'per piece', '10.0'),
(51, 'arpita', 'coat', 'wood', '2', 'per piece', '5.0'),
(53, 'tara', 'rice', 'basumathi', '200', 'per kg', '10.0'),
(54, 'sanju', 'belt', 'lather', '300', 'per piece', '9.0'),
(55, 'sanju', 'T-shirt', 'red color', '100', 'per piece', '0.0');

-- --------------------------------------------------------

--
-- Table structure for table `track`
--

CREATE TABLE `track` (
  `productid` int(100) NOT NULL,
  `productname` text NOT NULL,
  `productdesc` text NOT NULL,
  `price` text NOT NULL,
  `qty` text NOT NULL,
  `total` text NOT NULL,
  `avlqty` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminregister`
--
ALTER TABLE `adminregister`
  ADD PRIMARY KEY (`regid`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`productid`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`productid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`productid`);

--
-- Indexes for table `track`
--
ALTER TABLE `track`
  ADD PRIMARY KEY (`productid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminregister`
--
ALTER TABLE `adminregister`
  MODIFY `regid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `productid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `productid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `track`
--
ALTER TABLE `track`
  MODIFY `productid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=133;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
