-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2025 at 06:44 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_m`
--

-- --------------------------------------------------------

create database library_m;

use database library_m;

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `borrowed` tinyint(4) DEFAULT 0,
  `borrower_name` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `title`, `author`, `year`, `borrowed`, `borrower_name`, `created_at`) VALUES
(8, 'Borrow Test Book', 'Tester', 2025, 1, 'John Doe', '2025-12-09 16:30:53'),
(10, 'Borrow Test Book', 'Tester', 2025, 1, 'John Doe', '2025-12-09 16:55:11'),
(11, 'Selenium Book', 'Tester', 2025, 0, NULL, '2025-12-09 17:07:27'),
(13, 'Borrow Test Book', 'Tester', 2025, 0, NULL, '2025-12-09 17:28:01'),
(15, 'Borrow Test Book', 'Tester', 2025, 0, NULL, '2025-12-09 17:31:12');

-- --------------------------------------------------------

--
-- Table structure for table `borrow_log`
--

CREATE TABLE `borrow_log` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `borrower_name` varchar(255) DEFAULT NULL,
  `action` enum('borrow','return') NOT NULL,
  `action_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrow_log`
--

INSERT INTO `borrow_log` (`id`, `book_id`, `borrower_name`, `action`, `action_date`) VALUES
(1, 6, 'Cris', 'borrow', '2025-12-09 15:44:28'),
(2, 6, 'Cris', 'return', '2025-12-09 15:45:27'),
(3, 6, 'Cris', 'borrow', '2025-12-09 15:58:35'),
(4, 6, 'Cris', 'return', '2025-12-09 15:58:40'),
(5, 6, 'Cris', 'borrow', '2025-12-09 16:06:09'),
(6, 6, 'Cris', 'return', '2025-12-09 16:06:19'),
(7, 6, 'Cris', 'borrow', '2025-12-09 16:10:41'),
(8, 6, 'Cris', 'return', '2025-12-09 16:10:51'),
(9, 8, 'John Doe', 'borrow', '2025-12-09 16:30:55'),
(10, 10, 'John Doe', 'borrow', '2025-12-09 16:55:13'),
(11, 13, 'John Doe', 'borrow', '2025-12-09 17:28:02'),
(12, 13, 'John Doe', 'return', '2025-12-09 17:28:02'),
(13, 15, 'John Doe', 'borrow', '2025-12-09 17:31:21'),
(14, 15, 'John Doe', 'return', '2025-12-09 17:31:26');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `borrow_log`
--
ALTER TABLE `borrow_log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `borrow_log`
--
ALTER TABLE `borrow_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
