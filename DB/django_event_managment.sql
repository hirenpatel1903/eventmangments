-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 06, 2022 at 08:15 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.4.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_event_managment`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_basemodel`
--

CREATE TABLE `app_basemodel` (
  `id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `updated_by` varchar(10) DEFAULT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `deleted_by` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_basemodel`
--

INSERT INTO `app_basemodel` (`id`, `created_at`, `created_by`, `updated_at`, `updated_by`, `deleted_at`, `deleted_by`) VALUES
(1, '2022-06-06 10:18:00.000000', NULL, '2022-06-06 10:18:00.000000', NULL, NULL, NULL),
(2, '2022-06-06 10:23:00.000000', NULL, '2022-06-06 10:23:00.000000', NULL, NULL, NULL),
(4, '2022-06-06 10:41:00.000000', NULL, '2022-06-06 10:41:00.000000', NULL, NULL, NULL),
(5, '2022-06-06 10:42:00.000000', NULL, '2022-06-06 10:42:00.000000', NULL, NULL, NULL),
(6, '2022-06-06 10:42:00.000000', NULL, '2022-06-06 10:42:00.000000', NULL, NULL, NULL),
(7, '2022-06-06 10:42:00.000000', NULL, '2022-06-06 10:42:00.000000', NULL, NULL, NULL),
(8, '2022-06-06 10:42:00.000000', NULL, '2022-06-06 10:42:00.000000', NULL, NULL, NULL),
(9, '2022-06-06 10:43:00.000000', NULL, '2022-06-06 10:43:00.000000', NULL, NULL, NULL),
(10, '2022-06-06 10:43:00.000000', NULL, '2022-06-06 10:43:00.000000', NULL, NULL, NULL),
(11, '2022-06-06 10:43:00.000000', NULL, '2022-06-06 10:43:00.000000', NULL, NULL, NULL),
(12, '2022-06-06 10:43:00.000000', NULL, '2022-06-06 10:43:00.000000', NULL, NULL, NULL),
(13, '2022-06-06 10:44:00.000000', NULL, '2022-06-06 10:44:00.000000', NULL, NULL, NULL),
(14, '2022-06-06 10:44:00.000000', NULL, '2022-06-06 10:44:00.000000', NULL, NULL, NULL),
(15, '2022-06-06 10:44:00.000000', NULL, '2022-06-06 10:44:00.000000', NULL, NULL, NULL),
(16, '2022-06-06 10:44:00.000000', NULL, '2022-06-06 10:44:00.000000', NULL, NULL, NULL),
(17, '2022-06-06 10:44:00.000000', NULL, '2022-06-06 10:44:00.000000', NULL, NULL, NULL),
(18, '2022-06-06 10:45:00.000000', NULL, '2022-06-06 10:45:00.000000', NULL, NULL, NULL),
(19, '2022-06-06 10:45:00.000000', NULL, '2022-06-06 10:45:00.000000', NULL, NULL, NULL),
(20, '2022-06-06 10:45:00.000000', NULL, '2022-06-06 10:45:00.000000', NULL, NULL, NULL),
(21, '2022-06-06 10:45:00.000000', NULL, '2022-06-06 10:45:00.000000', NULL, NULL, NULL),
(22, '2022-06-06 10:45:00.000000', NULL, '2022-06-06 10:45:00.000000', NULL, NULL, NULL),
(23, '2022-06-06 10:46:00.000000', NULL, '2022-06-06 10:46:00.000000', NULL, NULL, NULL),
(24, '2022-06-06 10:46:00.000000', NULL, '2022-06-06 10:46:00.000000', NULL, NULL, NULL),
(25, '2022-06-06 10:46:00.000000', NULL, '2022-06-06 10:46:00.000000', NULL, NULL, NULL),
(26, '2022-06-06 10:46:00.000000', NULL, '2022-06-06 10:46:00.000000', NULL, NULL, NULL),
(27, '2022-06-06 10:46:00.000000', NULL, '2022-06-06 10:46:00.000000', NULL, NULL, NULL),
(28, '2022-06-06 10:46:00.000000', NULL, '2022-06-06 10:46:00.000000', NULL, NULL, NULL),
(29, '2022-06-06 10:47:00.000000', NULL, '2022-06-06 10:47:00.000000', NULL, NULL, NULL),
(30, '2022-06-06 10:47:00.000000', NULL, '2022-06-06 10:47:00.000000', NULL, NULL, NULL),
(31, '2022-06-06 10:47:00.000000', NULL, '2022-06-06 10:47:00.000000', NULL, NULL, NULL),
(32, '2022-06-06 10:47:00.000000', NULL, '2022-06-06 10:47:00.000000', NULL, NULL, NULL),
(33, '2022-06-06 10:47:00.000000', NULL, '2022-06-06 10:47:00.000000', NULL, NULL, NULL),
(34, '2022-06-06 10:48:00.000000', NULL, '2022-06-06 10:48:00.000000', NULL, NULL, NULL),
(35, '2022-06-06 10:48:00.000000', NULL, '2022-06-06 10:48:00.000000', NULL, NULL, NULL),
(36, '2022-06-06 10:48:00.000000', NULL, '2022-06-06 10:48:00.000000', NULL, NULL, NULL),
(37, '2022-06-06 10:48:00.000000', NULL, '2022-06-06 10:48:00.000000', NULL, NULL, NULL),
(38, '2022-06-06 10:48:00.000000', NULL, '2022-06-06 10:48:00.000000', NULL, NULL, NULL),
(39, '2022-06-06 10:48:00.000000', NULL, '2022-06-06 10:48:00.000000', NULL, NULL, NULL),
(40, '2022-06-06 10:49:00.000000', NULL, '2022-06-06 10:49:00.000000', NULL, NULL, NULL),
(41, '2022-06-06 11:03:45.659701', NULL, '2022-06-06 11:03:45.659701', NULL, NULL, NULL),
(42, '2022-06-06 11:03:50.841192', NULL, '2022-06-06 11:03:50.841192', NULL, NULL, NULL),
(43, '2022-06-06 11:03:50.858082', NULL, '2022-06-06 11:03:50.858082', NULL, NULL, NULL),
(44, '2022-06-06 11:15:10.970041', NULL, '2022-06-06 11:15:10.970041', NULL, NULL, NULL),
(45, '2022-06-06 11:19:31.224421', NULL, '2022-06-06 11:19:31.224421', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `app_lead`
--

CREATE TABLE `app_lead` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `description` varchar(255) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  `vendor_count` int(11) NOT NULL,
  `date_of_event` date DEFAULT NULL,
  `time_of_event` time(6) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_lead`
--

INSERT INTO `app_lead` (`basemodel_ptr_id`, `name`, `mobile_number`, `email`, `description`, `city`, `vendor_count`, `date_of_event`, `time_of_event`, `address`, `country`, `state`) VALUES
(44, 'birthday party', '8978897889', 'birthday@einzigartige.in', 'birthday celibration', 'surat', 0, '2022-06-08', '11:15:00.000000', 'surat near', 'india', 'gujarat');

-- --------------------------------------------------------

--
-- Table structure for table `app_lead_assign`
--

CREATE TABLE `app_lead_assign` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `vendorID_id` bigint(20) DEFAULT NULL,
  `leadID_id` bigint(20) DEFAULT NULL,
  `lead_status_id` bigint(20) DEFAULT NULL,
  `last_status_updated_time` datetime(6) NOT NULL,
  `last_comments` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_lead_assign`
--

INSERT INTO `app_lead_assign` (`basemodel_ptr_id`, `vendorID_id`, `leadID_id`, `lead_status_id`, `last_status_updated_time`, `last_comments`) VALUES
(45, 41, 44, 40, '2022-06-06 11:19:31.224421', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `app_lead_comment`
--

CREATE TABLE `app_lead_comment` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `leadID_id` bigint(20) DEFAULT NULL,
  `leadAssignedId_id` bigint(20) DEFAULT NULL,
  `vendorID_id` bigint(20) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  `comments` varchar(200) DEFAULT NULL,
  `datetime` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app_lookup`
--

CREATE TABLE `app_lookup` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL,
  `numeric_value` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_lookup`
--

INSERT INTO `app_lookup` (`basemodel_ptr_id`, `type`, `value`, `numeric_value`) VALUES
(4, 'category', 'Event Planner', NULL),
(5, 'category', 'Hotel', NULL),
(6, 'category', 'Resort', NULL),
(7, 'category', 'Banquet Hall', NULL),
(8, 'category', 'Caterer', NULL),
(9, 'category', 'Decorator', NULL),
(10, 'catering', 'yes', NULL),
(11, 'catering', 'no', NULL),
(12, 'max_capacity', '25', 25),
(13, 'max_capacity', '50', 50),
(14, 'max_capacity', '100', 100),
(15, 'max_capacity', '150', 150),
(16, 'max_capacity', '200', 200),
(17, 'max_capacity', '250', 250),
(18, 'max_capacity', '300', 300),
(19, 'max_capacity', '500', 500),
(20, 'max_capacity', '1000', 1000),
(21, 'max_capacity', '1000+', 1001),
(22, 'number_of_events', '25', 25),
(23, 'number_of_events', '50', 50),
(24, 'number_of_events', '100', 100),
(25, 'number_of_events', '250', 250),
(26, 'number_of_events', '500', 500),
(27, 'number_of_events', '500+', 501),
(28, 'lead_status', 'Accepted', NULL),
(29, 'lead_status', 'Rejected', NULL),
(30, 'lead_status', 'New', NULL),
(31, 'lead_status', 'Called and research in progress', NULL),
(32, 'lead_status', 'Called and customer declined services', NULL),
(33, 'lead_status', 'Customer didn\'t respond', NULL),
(34, 'lead_status', 'Quote sent', NULL),
(35, 'lead_status', 'Event finalized', NULL),
(36, 'lead_status', 'Advance received', NULL),
(37, 'lead_status', 'Event completed', NULL),
(38, 'lead_status', 'Invoice paid in full', NULL),
(39, 'lead_status', 'Closed', NULL),
(40, 'lead_status', 'Pending', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `app_media`
--

CREATE TABLE `app_media` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `url` varchar(255) NOT NULL,
  `size` int(11) NOT NULL,
  `userID_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_media`
--

INSERT INTO `app_media` (`basemodel_ptr_id`, `url`, `size`, `userID_id`) VALUES
(42, 'photo-1604668915840-580c30026e5f.jpg', 94231, 41),
(43, '81nU6clDgEL._SL1200_.jpg', 299149, 41);

-- --------------------------------------------------------

--
-- Table structure for table `app_user`
--

CREATE TABLE `app_user` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `role` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `mobile_number` varchar(15) DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  `catering` varchar(10) DEFAULT NULL,
  `max_capacity` varchar(10) DEFAULT NULL,
  `number_of_events` varchar(10) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `is_verify` varchar(250) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_user`
--

INSERT INTO `app_user` (`basemodel_ptr_id`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `name`, `password`, `role`, `email`, `city`, `description`, `mobile_number`, `category`, `catering`, `max_capacity`, `number_of_events`, `status`, `is_verify`, `address`, `country`, `state`) VALUES
(1, '2022-06-06 10:38:30.929342', 1, 'superadmin', 'superadmin', '', 1, 1, '2022-06-06 10:18:00.000000', 'superadmin', 'pbkdf2_sha256$260000$YdlhcFtCkaTIrSucbHkxAI$jBS6UafQOqa1ga764I+3jif+pL215W93MNlus70vUfI=', 'ADMIN', 'superadmin@einzgartige.in', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ACTIVE', '1', NULL, NULL, NULL),
(2, '2022-06-06 11:06:17.880473', 0, 'admin', 'admin', '', 0, 1, '2022-06-06 10:23:00.000000', 'admin', 'pbkdf2_sha256$260000$YdlhcFtCkaTIrSucbHkxAI$jBS6UafQOqa1ga764I+3jif+pL215W93MNlus70vUfI=', 'ADMIN', 'admin@einzigartige.in', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ACTIVE', '1', NULL, NULL, NULL),
(41, '2022-06-06 11:20:08.838552', 0, 'U9878897889', '', '', 0, 1, '2022-06-06 11:03:45.659701', 'hiren', 'pbkdf2_sha256$260000$TuqVIERcjELLpWGlRDCzHt$Qr12QuLk50IaO8KjtK4b3wNItTAigJj+aHDUinC5+1A=', 'VENDOR', 'hiren@einzigartige.com', 'ahmedabad', 'birthday party', '9878897889', '4', '10', '13', '25', 'ACTIVE', '1', 'ahmedabad', 'india', 'gujarat');

-- --------------------------------------------------------

--
-- Table structure for table `app_user_groups`
--

CREATE TABLE `app_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app_user_user_permissions`
--

CREATE TABLE `app_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app_verification_token`
--

CREATE TABLE `app_verification_token` (
  `basemodel_ptr_id` bigint(20) NOT NULL,
  `token` varchar(100) NOT NULL,
  `vendorID_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add base model', 6, 'add_basemodel'),
(22, 'Can change base model', 6, 'change_basemodel'),
(23, 'Can delete base model', 6, 'delete_basemodel'),
(24, 'Can view base model', 6, 'view_basemodel'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add lead', 8, 'add_lead'),
(30, 'Can change lead', 8, 'change_lead'),
(31, 'Can delete lead', 8, 'delete_lead'),
(32, 'Can view lead', 8, 'view_lead'),
(33, 'Can add lookup', 9, 'add_lookup'),
(34, 'Can change lookup', 9, 'change_lookup'),
(35, 'Can delete lookup', 9, 'delete_lookup'),
(36, 'Can view lookup', 9, 'view_lookup'),
(37, 'Can add media', 10, 'add_media'),
(38, 'Can change media', 10, 'change_media'),
(39, 'Can delete media', 10, 'delete_media'),
(40, 'Can view media', 10, 'view_media'),
(41, 'Can add lead_ assign', 11, 'add_lead_assign'),
(42, 'Can change lead_ assign', 11, 'change_lead_assign'),
(43, 'Can delete lead_ assign', 11, 'delete_lead_assign'),
(44, 'Can view lead_ assign', 11, 'view_lead_assign'),
(45, 'Can add lead_ comment', 12, 'add_lead_comment'),
(46, 'Can change lead_ comment', 12, 'change_lead_comment'),
(47, 'Can delete lead_ comment', 12, 'delete_lead_comment'),
(48, 'Can view lead_ comment', 12, 'view_lead_comment'),
(49, 'Can add verification_ token', 13, 'add_verification_token'),
(50, 'Can change verification_ token', 13, 'change_verification_token'),
(51, 'Can delete verification_ token', 13, 'delete_verification_token'),
(52, 'Can view verification_ token', 13, 'view_verification_token');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-06-06 10:23:41.749522', '1', 'superadmin-superadmin@einzgartige.in-VENDOR', 2, '[{\"changed\": {\"fields\": [\"Last login\", \"First name\", \"Name\"]}}]', 7, 1),
(2, '2022-06-06 10:25:01.667795', '2', 'admin-admin@einzigartige.in-ADMIN', 1, '[{\"added\": {}}]', 7, 1),
(3, '2022-06-06 10:42:21.762245', '4', '4-category-Event Planner', 1, '[{\"added\": {}}]', 9, 1),
(4, '2022-06-06 10:42:32.054980', '5', '5-category-Hotel', 1, '[{\"added\": {}}]', 9, 1),
(5, '2022-06-06 10:42:43.690817', '6', '6-category-Resort', 1, '[{\"added\": {}}]', 9, 1),
(6, '2022-06-06 10:42:54.647146', '7', '7-category-Banquet Hall', 1, '[{\"added\": {}}]', 9, 1),
(7, '2022-06-06 10:43:05.205077', '8', '8-category-Caterer', 1, '[{\"added\": {}}]', 9, 1),
(8, '2022-06-06 10:43:15.602473', '9', '9-category-Decorator', 1, '[{\"added\": {}}]', 9, 1),
(9, '2022-06-06 10:43:27.526011', '10', '10-catering-yes', 1, '[{\"added\": {}}]', 9, 1),
(10, '2022-06-06 10:43:37.863158', '11', '11-catering-no', 1, '[{\"added\": {}}]', 9, 1),
(11, '2022-06-06 10:43:59.923100', '12', '12-max_capacity-25', 1, '[{\"added\": {}}]', 9, 1),
(12, '2022-06-06 10:44:12.746752', '13', '13-max_capacity-50', 1, '[{\"added\": {}}]', 9, 1),
(13, '2022-06-06 10:44:23.355636', '14', '14-max_capacity-100', 1, '[{\"added\": {}}]', 9, 1),
(14, '2022-06-06 10:44:41.472420', '15', '15-max_capacity-150', 1, '[{\"added\": {}}]', 9, 1),
(15, '2022-06-06 10:44:51.718283', '16', '16-max_capacity-200', 1, '[{\"added\": {}}]', 9, 1),
(16, '2022-06-06 10:45:02.038794', '17', '17-max_capacity-250', 1, '[{\"added\": {}}]', 9, 1),
(17, '2022-06-06 10:45:12.217043', '18', '18-max_capacity-300', 1, '[{\"added\": {}}]', 9, 1),
(18, '2022-06-06 10:45:22.337017', '19', '19-max_capacity-500', 1, '[{\"added\": {}}]', 9, 1),
(19, '2022-06-06 10:45:33.447103', '20', '20-max_capacity-1000', 1, '[{\"added\": {}}]', 9, 1),
(20, '2022-06-06 10:45:47.906827', '21', '21-max_capacity-1000+', 1, '[{\"added\": {}}]', 9, 1),
(21, '2022-06-06 10:46:00.742393', '22', '22-number_of_events-25', 1, '[{\"added\": {}}]', 9, 1),
(22, '2022-06-06 10:46:12.856074', '23', '23-number_of_events-50', 1, '[{\"added\": {}}]', 9, 1),
(23, '2022-06-06 10:46:23.371770', '24', '24-number_of_events-100', 1, '[{\"added\": {}}]', 9, 1),
(24, '2022-06-06 10:46:33.899657', '25', '25-number_of_events-250', 1, '[{\"added\": {}}]', 9, 1),
(25, '2022-06-06 10:46:45.450285', '26', '26-number_of_events-500', 1, '[{\"added\": {}}]', 9, 1),
(26, '2022-06-06 10:46:57.325225', '27', '27-number_of_events-500+', 1, '[{\"added\": {}}]', 9, 1),
(27, '2022-06-06 10:47:10.153440', '28', '28-lead_status-Accepted', 1, '[{\"added\": {}}]', 9, 1),
(28, '2022-06-06 10:47:19.771622', '29', '29-lead_status-Rejected', 1, '[{\"added\": {}}]', 9, 1),
(29, '2022-06-06 10:47:28.886430', '30', '30-lead_status-New', 1, '[{\"added\": {}}]', 9, 1),
(30, '2022-06-06 10:47:39.889224', '31', '31-lead_status-Called and research in progress', 1, '[{\"added\": {}}]', 9, 1),
(31, '2022-06-06 10:47:49.501677', '32', '32-lead_status-Called and customer declined services', 1, '[{\"added\": {}}]', 9, 1),
(32, '2022-06-06 10:48:00.419273', '33', '33-lead_status-Customer didn\'t respond', 1, '[{\"added\": {}}]', 9, 1),
(33, '2022-06-06 10:48:09.493043', '34', '34-lead_status-Quote sent', 1, '[{\"added\": {}}]', 9, 1),
(34, '2022-06-06 10:48:18.888339', '35', '35-lead_status-Event finalized', 1, '[{\"added\": {}}]', 9, 1),
(35, '2022-06-06 10:48:29.097894', '36', '36-lead_status-Advance received', 1, '[{\"added\": {}}]', 9, 1),
(36, '2022-06-06 10:48:39.165700', '37', '37-lead_status-Event completed', 1, '[{\"added\": {}}]', 9, 1),
(37, '2022-06-06 10:48:49.898569', '38', '38-lead_status-Invoice paid in full', 1, '[{\"added\": {}}]', 9, 1),
(38, '2022-06-06 10:48:59.972195', '39', '39-lead_status-Closed', 1, '[{\"added\": {}}]', 9, 1),
(39, '2022-06-06 10:49:10.105928', '40', '40-lead_status-Pending', 1, '[{\"added\": {}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(6, 'app', 'basemodel'),
(8, 'app', 'lead'),
(11, 'app', 'lead_assign'),
(12, 'app', 'lead_comment'),
(9, 'app', 'lookup'),
(10, 'app', 'media'),
(7, 'app', 'user'),
(13, 'app', 'verification_token'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-06-06 10:17:29.822301'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-06-06 10:17:29.891895'),
(3, 'auth', '0001_initial', '2022-06-06 10:17:30.220504'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-06-06 10:17:30.280173'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-06-06 10:17:30.291143'),
(6, 'auth', '0004_alter_user_username_opts', '2022-06-06 10:17:30.299122'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-06-06 10:17:30.311091'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-06-06 10:17:30.315080'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-06-06 10:17:30.327050'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-06-06 10:17:30.338019'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-06-06 10:17:30.347993'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-06-06 10:17:30.371314'),
(13, 'auth', '0011_update_proxy_permissions', '2022-06-06 10:17:30.383283'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-06-06 10:17:30.393256'),
(15, 'app', '0001_initial', '2022-06-06 10:17:31.583274'),
(16, 'admin', '0001_initial', '2022-06-06 10:17:31.795375'),
(17, 'admin', '0002_logentry_remove_auto_add', '2022-06-06 10:17:31.826730'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-06-06 10:17:31.843685'),
(19, 'app', '0002_alter_lead_status_assignlead', '2022-06-06 10:17:32.046573'),
(20, 'app', '0003_alter_assignlead_userid_alter_lead_status', '2022-06-06 10:17:32.214374'),
(21, 'app', '0004_alter_assignlead_leadid', '2022-06-06 10:17:32.350618'),
(22, 'app', '0005_profile', '2022-06-06 10:17:32.510057'),
(23, 'app', '0006_rename_userid_assignlead_vendorid_and_more', '2022-06-06 10:17:32.653673'),
(24, 'app', '0007_lead_assign_lead_comment_remove_lead_status_and_more', '2022-06-06 10:17:33.107227'),
(25, 'app', '0008_alter_lead_assign_leadid_alter_lead_assign_vendorid_and_more', '2022-06-06 10:17:33.772812'),
(26, 'app', '0009_alter_lookup_type', '2022-06-06 10:17:33.793245'),
(27, 'app', '0010_alter_lead_assign_lead_status_and_more', '2022-06-06 10:17:34.073410'),
(28, 'app', '0011_user_is_token_alter_lookup_type', '2022-06-06 10:17:34.152585'),
(29, 'app', '0012_rename_profile_verification_token_and_more', '2022-06-06 10:17:34.313402'),
(30, 'app', '0013_rename_is_token_user_is_verify', '2022-06-06 10:17:34.351487'),
(31, 'app', '0014_rename_email_verification_token_vendorid', '2022-06-06 10:17:34.475745'),
(32, 'app', '0015_lead_date_of_event_lead_time_of_event', '2022-06-06 10:17:34.564506'),
(33, 'app', '0016_auto_20220518_1559', '2022-06-06 10:17:34.696769'),
(34, 'app', '0017_user_terms_confirmed', '2022-06-06 10:17:34.748347'),
(35, 'app', '0018_alter_user_terms_confirmed', '2022-06-06 10:17:34.814823'),
(36, 'app', '0019_auto_20220518_1714', '2022-06-06 10:17:34.917710'),
(37, 'app', '0020_remove_user_terms_confirmed', '2022-06-06 10:17:34.962269'),
(38, 'sessions', '0001_initial', '2022-06-06 10:17:35.031671');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_basemodel`
--
ALTER TABLE `app_basemodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_lead`
--
ALTER TABLE `app_lead`
  ADD PRIMARY KEY (`basemodel_ptr_id`);

--
-- Indexes for table `app_lead_assign`
--
ALTER TABLE `app_lead_assign`
  ADD PRIMARY KEY (`basemodel_ptr_id`),
  ADD KEY `app_lead_assign_leadID_id_afce86ca` (`leadID_id`),
  ADD KEY `app_lead_assign_vendorID_id_055e82dd` (`vendorID_id`),
  ADD KEY `app_lead_assign_lead_status_id_eb4a05c3` (`lead_status_id`);

--
-- Indexes for table `app_lead_comment`
--
ALTER TABLE `app_lead_comment`
  ADD PRIMARY KEY (`basemodel_ptr_id`),
  ADD KEY `app_lead_comment_leadAssignedId_id_222d98ec` (`leadAssignedId_id`),
  ADD KEY `app_lead_comment_leadID_id_20c7b5c6` (`leadID_id`),
  ADD KEY `app_lead_comment_vendorID_id_ec6572e6` (`vendorID_id`),
  ADD KEY `app_lead_comment_status_id_a60fd6e9` (`status_id`);

--
-- Indexes for table `app_lookup`
--
ALTER TABLE `app_lookup`
  ADD PRIMARY KEY (`basemodel_ptr_id`);

--
-- Indexes for table `app_media`
--
ALTER TABLE `app_media`
  ADD PRIMARY KEY (`basemodel_ptr_id`),
  ADD KEY `app_media_userID_id_1bc381f7_fk_app_user_basemodel_ptr_id` (`userID_id`);

--
-- Indexes for table `app_user`
--
ALTER TABLE `app_user`
  ADD PRIMARY KEY (`basemodel_ptr_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `mobile_number` (`mobile_number`);

--
-- Indexes for table `app_user_groups`
--
ALTER TABLE `app_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_user_groups_user_id_group_id_73b8e940_uniq` (`user_id`,`group_id`),
  ADD KEY `app_user_groups_group_id_e774d92c_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `app_user_user_permissions`
--
ALTER TABLE `app_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_user_user_permissions_user_id_permission_id_7c8316ce_uniq` (`user_id`,`permission_id`),
  ADD KEY `app_user_user_permis_permission_id_4ef8e133_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `app_verification_token`
--
ALTER TABLE `app_verification_token`
  ADD PRIMARY KEY (`basemodel_ptr_id`),
  ADD UNIQUE KEY `email_id` (`vendorID_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_app_user_basemodel_ptr_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_basemodel`
--
ALTER TABLE `app_basemodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `app_user_groups`
--
ALTER TABLE `app_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_user_user_permissions`
--
ALTER TABLE `app_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_lead`
--
ALTER TABLE `app_lead`
  ADD CONSTRAINT `app_lead_basemodel_ptr_id_cc9e2b25_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`);

--
-- Constraints for table `app_lead_assign`
--
ALTER TABLE `app_lead_assign`
  ADD CONSTRAINT `app_lead_assign_basemodel_ptr_id_b8f2f04b_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`),
  ADD CONSTRAINT `app_lead_assign_leadID_id_afce86ca_fk_app_lead_basemodel_ptr_id` FOREIGN KEY (`leadID_id`) REFERENCES `app_lead` (`basemodel_ptr_id`),
  ADD CONSTRAINT `app_lead_assign_lead_status_id_eb4a05c3_fk_app_looku` FOREIGN KEY (`lead_status_id`) REFERENCES `app_lookup` (`basemodel_ptr_id`),
  ADD CONSTRAINT `app_lead_assign_vendorID_id_055e82dd_fk_app_user_` FOREIGN KEY (`vendorID_id`) REFERENCES `app_user` (`basemodel_ptr_id`);

--
-- Constraints for table `app_lead_comment`
--
ALTER TABLE `app_lead_comment`
  ADD CONSTRAINT `app_lead_comment_basemodel_ptr_id_0281b25d_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`),
  ADD CONSTRAINT `app_lead_comment_leadAssignedId_id_222d98ec_fk_app_lead_` FOREIGN KEY (`leadAssignedId_id`) REFERENCES `app_lead_assign` (`basemodel_ptr_id`),
  ADD CONSTRAINT `app_lead_comment_leadID_id_20c7b5c6_fk_app_lead_basemodel_ptr_id` FOREIGN KEY (`leadID_id`) REFERENCES `app_lead` (`basemodel_ptr_id`),
  ADD CONSTRAINT `app_lead_comment_status_id_a60fd6e9_fk_app_looku` FOREIGN KEY (`status_id`) REFERENCES `app_lookup` (`basemodel_ptr_id`),
  ADD CONSTRAINT `app_lead_comment_vendorID_id_ec6572e6_fk_app_user_` FOREIGN KEY (`vendorID_id`) REFERENCES `app_user` (`basemodel_ptr_id`);

--
-- Constraints for table `app_lookup`
--
ALTER TABLE `app_lookup`
  ADD CONSTRAINT `app_lookup_basemodel_ptr_id_cd23a7ff_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`);

--
-- Constraints for table `app_media`
--
ALTER TABLE `app_media`
  ADD CONSTRAINT `app_media_basemodel_ptr_id_f195fd2b_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`),
  ADD CONSTRAINT `app_media_userID_id_1bc381f7_fk_app_user_basemodel_ptr_id` FOREIGN KEY (`userID_id`) REFERENCES `app_user` (`basemodel_ptr_id`);

--
-- Constraints for table `app_user`
--
ALTER TABLE `app_user`
  ADD CONSTRAINT `app_user_basemodel_ptr_id_8eeb1ee3_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`);

--
-- Constraints for table `app_user_groups`
--
ALTER TABLE `app_user_groups`
  ADD CONSTRAINT `app_user_groups_group_id_e774d92c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `app_user_groups_user_id_e6f878f6_fk_app_user_basemodel_ptr_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`basemodel_ptr_id`);

--
-- Constraints for table `app_user_user_permissions`
--
ALTER TABLE `app_user_user_permissions`
  ADD CONSTRAINT `app_user_user_permis_permission_id_4ef8e133_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `app_user_user_permis_user_id_24780b52_fk_app_user_` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`basemodel_ptr_id`);

--
-- Constraints for table `app_verification_token`
--
ALTER TABLE `app_verification_token`
  ADD CONSTRAINT `app_profile_basemodel_ptr_id_3072a02c_fk_app_basemodel_id` FOREIGN KEY (`basemodel_ptr_id`) REFERENCES `app_basemodel` (`id`),
  ADD CONSTRAINT `app_verification_tok_vendorID_id_6261fd87_fk_app_user_` FOREIGN KEY (`vendorID_id`) REFERENCES `app_user` (`basemodel_ptr_id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_app_user_basemodel_ptr_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`basemodel_ptr_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
