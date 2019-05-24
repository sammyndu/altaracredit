-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2019 at 12:35 AM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cbtexamtable`
--

-- --------------------------------------------------------

--
-- Table structure for table `library`
--

CREATE TABLE `library` (
  `id` int(11) NOT NULL,
  `book_title` varchar(50) NOT NULL,
  `book_description` varchar(50) NOT NULL,
  `book_author` varchar(50) NOT NULL,
  `book_file` varchar(50) DEFAULT NULL,
  `book_status` varchar(50) NOT NULL,
  `active` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `library`
--

INSERT INTO `library` (`id`, `book_title`, `book_description`, `book_author`, `book_file`, `book_status`, `active`) VALUES
(1, 'math', 'mthematicss', 'sam', '15-Toughest-Interview-Questions-and-Answers.pdf', 'Available', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `password`, `usertype`) VALUES
(1, 'Samuel', 'Ndu', 'samndu2@gmail.com', '60winner', 'user'),
(2, 'ndu', 'mike', 'samo@y.com', '111', 'user'),
(3, 'ugonna', 'marths', 'man@w.com', '222', 'user'),
(4, 'walter', 'fred', 'naomi@gmail.com', '123', 'user'),
(5, 'admin', 'admin', 'admin', 'admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `library`
--
ALTER TABLE `library`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `library`
--
ALTER TABLE `library`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
