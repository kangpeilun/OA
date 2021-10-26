-- MySQL dump 10.13  Distrib 5.7.29, for Win64 (x86_64)
--
-- Host: localhost    Database: oasystem
-- ------------------------------------------------------
-- Server version	5.7.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add company',7,'add_company'),(26,'Can change company',7,'change_company'),(27,'Can delete company',7,'delete_company'),(28,'Can view company',7,'view_company'),(29,'Can add manager',8,'add_manager'),(30,'Can change manager',8,'change_manager'),(31,'Can delete manager',8,'delete_manager'),(32,'Can view manager',8,'view_manager'),(33,'Can add partment',9,'add_partment'),(34,'Can change partment',9,'change_partment'),(35,'Can delete partment',9,'delete_partment'),(36,'Can view partment',9,'view_partment'),(37,'Can add role',10,'add_role'),(38,'Can change role',10,'change_role'),(39,'Can delete role',10,'delete_role'),(40,'Can view role',10,'view_role'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user'),(45,'Can add customer',12,'add_customer'),(46,'Can change customer',12,'change_customer'),(47,'Can delete customer',12,'delete_customer'),(48,'Can view customer',12,'view_customer'),(49,'Can add product',13,'add_product'),(50,'Can change product',13,'change_product'),(51,'Can delete product',13,'delete_product'),(52,'Can view product',13,'view_product');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_manage_customer`
--

DROP TABLE IF EXISTS `customer_manage_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_manage_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `briefinfo` longtext NOT NULL,
  `area` varchar(30) NOT NULL,
  `type` varchar(20) NOT NULL,
  `nature` varchar(20) NOT NULL,
  `describe` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_delete` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_manage_customer`
--

LOCK TABLES `customer_manage_customer` WRITE;
/*!40000 ALTER TABLE `customer_manage_customer` DISABLE KEYS */;
INSERT INTO `customer_manage_customer` VALUES (1,'sadas','1312','12312','1231','12312','12312','2021-10-26 13:42:14.000000','1'),(2,'sadas','1312','12312','1231','12312','12312','2021-10-26 13:42:14.000000','1'),(3,'sadas','1312','12312','1231','12312','12312','2021-10-26 13:42:14.000000','1'),(4,'sadas','1312','12312','1231','12312','12312','2021-10-26 13:42:14.000000','1'),(5,'sadas','1312','12312','1231','12312','12312','2021-10-26 13:42:14.000000','0'),(6,'李丹','12312','12312','123','1231','123','2021-10-26 05:53:22.689034','0');
/*!40000 ALTER TABLE `customer_manage_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_manage_product`
--

DROP TABLE IF EXISTS `customer_manage_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_manage_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `supplier` varchar(20) NOT NULL,
  `num` varchar(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  `price` varchar(10) NOT NULL,
  `describe` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_delete` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_manage_product`
--

LOCK TABLES `customer_manage_product` WRITE;
/*!40000 ALTER TABLE `customer_manage_product` DISABLE KEYS */;
INSERT INTO `customer_manage_product` VALUES (2,'kpl','kpl','123','23','123','啊实打实大苏打实打实大苏打实打实大苏打','2021-10-26 09:54:17.000000','0'),(3,'kpl','kpl','123','23','123','啊实打实大苏打实打实大苏打实打实大苏打','2021-10-26 09:54:18.000000','0'),(4,'kpl','kpl','123','23','123','啊实打实大苏打实打实大苏打实打实大苏打','2021-10-26 09:54:19.000000','0'),(6,'康佩伦','123','123','123','123','123','2021-10-26 03:28:11.478737','0'),(7,'kkk','14撒打算','123','213','123','123大苏打实打实','2021-10-26 03:29:13.156319','0'),(8,'ld','123','123','123','123','123','2021-10-26 03:32:03.187078','0'),(9,'哈尔滨工业大学学报','asd','阿松大','阿松大','123','asdas','2021-10-26 03:37:59.407836','0');
/*!40000 ALTER TABLE `customer_manage_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'customer_manage','customer'),(13,'customer_manage','product'),(6,'sessions','session'),(7,'system_manage','company'),(8,'system_manage','manager'),(9,'system_manage','partment'),(10,'system_manage','role'),(11,'system_manage','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-10-22 07:53:05.256685'),(2,'auth','0001_initial','2021-10-22 07:53:06.602535'),(3,'admin','0001_initial','2021-10-22 07:53:12.202115'),(4,'admin','0002_logentry_remove_auto_add','2021-10-22 07:53:13.274823'),(5,'admin','0003_logentry_add_action_flag_choices','2021-10-22 07:53:13.321262'),(6,'contenttypes','0002_remove_content_type_name','2021-10-22 07:53:14.217246'),(7,'auth','0002_alter_permission_name_max_length','2021-10-22 07:53:14.803690'),(8,'auth','0003_alter_user_email_max_length','2021-10-22 07:53:15.425498'),(9,'auth','0004_alter_user_username_opts','2021-10-22 07:53:15.460633'),(10,'auth','0005_alter_user_last_login_null','2021-10-22 07:53:15.981314'),(11,'auth','0006_require_contenttypes_0002','2021-10-22 07:53:16.008678'),(12,'auth','0007_alter_validators_add_error_messages','2021-10-22 07:53:16.042722'),(13,'auth','0008_alter_user_username_max_length','2021-10-22 07:53:16.720851'),(14,'auth','0009_alter_user_last_name_max_length','2021-10-22 07:53:17.286111'),(15,'auth','0010_alter_group_name_max_length','2021-10-22 07:53:17.847795'),(16,'auth','0011_update_proxy_permissions','2021-10-22 07:53:17.881909'),(17,'customer_manage','0001_initial','2021-10-22 07:53:18.318660'),(18,'sessions','0001_initial','2021-10-22 07:53:18.576543'),(19,'system_manage','0001_initial','2021-10-22 07:53:20.027399'),(20,'system_manage','0002_auto_20211022_1747','2021-10-22 09:47:06.844208'),(21,'customer_manage','0002_auto_20211026_1214','2021-10-26 04:14:53.745051');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('g573u6hu7x7pjhce464vnd4l81qrrb1c','ZWJkZDE3YmViNzc3ZWQ1YWY1NDlkMzk2ZjIyNzkyOTczNDQ5YjBjNDp7InVpZCI6MX0=','2021-11-09 08:47:26.470355');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_manage_company`
--

DROP TABLE IF EXISTS `system_manage_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_manage_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `fax` varchar(7) NOT NULL,
  `zipcode` varchar(6) NOT NULL,
  `site` longtext NOT NULL,
  `bankdeposit` varchar(20) NOT NULL,
  `banknum` varchar(30) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_delete` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_manage_company`
--

LOCK TABLES `system_manage_company` WRITE;
/*!40000 ALTER TABLE `system_manage_company` DISABLE KEYS */;
INSERT INTO `system_manage_company` VALUES (1,'123','123','234','123','123','123','123','2021-10-26 15:07:22.000000','1'),(2,'123','123','234','123','123','123','123','2021-10-26 15:07:22.000000','1'),(3,'123','123','234','123','123','123','123','2021-10-26 15:07:22.000000','0'),(4,'123','123','234','123','123','123','123','2021-10-26 15:07:22.000000','0'),(5,'kpl','18539175749','123','454000','123','123','123','2021-10-26 07:10:40.910999','0');
/*!40000 ALTER TABLE `system_manage_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_manage_manager`
--

DROP TABLE IF EXISTS `system_manage_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_manage_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_manage_manager`
--

LOCK TABLES `system_manage_manager` WRITE;
/*!40000 ALTER TABLE `system_manage_manager` DISABLE KEYS */;
INSERT INTO `system_manage_manager` VALUES (1,'123','123','2021-10-25 04:09:26.687696');
/*!40000 ALTER TABLE `system_manage_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_manage_partment`
--

DROP TABLE IF EXISTS `system_manage_partment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_manage_partment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `fax` varchar(7) NOT NULL,
  `function` longtext NOT NULL,
  `num` varchar(10) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_delete` varchar(1) NOT NULL,
  `company_id` int(11) NOT NULL,
  `prepartment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `system_manage_partme_company_id_6a864987_fk_system_ma` (`company_id`),
  KEY `system_manage_partme_prepartment_id_49125756_fk_system_ma` (`prepartment_id`),
  CONSTRAINT `system_manage_partme_company_id_6a864987_fk_system_ma` FOREIGN KEY (`company_id`) REFERENCES `system_manage_company` (`id`),
  CONSTRAINT `system_manage_partme_prepartment_id_49125756_fk_system_ma` FOREIGN KEY (`prepartment_id`) REFERENCES `system_manage_partment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_manage_partment`
--

LOCK TABLES `system_manage_partment` WRITE;
/*!40000 ALTER TABLE `system_manage_partment` DISABLE KEYS */;
INSERT INTO `system_manage_partment` VALUES (1,'123','123','123','123','123','2021-10-26 15:26:41.000000','1',1,1),(2,'123','123','123','123','123','2021-10-26 15:26:41.000000','1',1,2),(3,'123','123','123','123','123','2021-10-26 15:26:41.000000','1',1,1),(4,'123','123','123','123','123','2021-10-26 15:26:41.000000','1',1,2),(5,'kpl','18945099308','12','123','123','2021-10-26 07:29:16.182968','0',1,1);
/*!40000 ALTER TABLE `system_manage_partment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_manage_role`
--

DROP TABLE IF EXISTS `system_manage_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_manage_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` varchar(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_delete` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_manage_role`
--

LOCK TABLES `system_manage_role` WRITE;
/*!40000 ALTER TABLE `system_manage_role` DISABLE KEYS */;
INSERT INTO `system_manage_role` VALUES (1,'1','康佩伦','2021-10-26 14:43:51.000000','1'),(2,'12312123','123','2021-10-26 14:43:51.000000','1'),(3,'12312123','123','2021-10-26 14:43:51.000000','1'),(4,'12312123','123','2021-10-26 14:43:51.000000','0'),(5,'12312123','123','2021-10-26 14:43:51.000000','1'),(6,'324','康佩伦','2021-10-26 06:47:15.956381','1');
/*!40000 ALTER TABLE `system_manage_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_manage_user`
--

DROP TABLE IF EXISTS `system_manage_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_manage_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_delete` varchar(1) NOT NULL,
  `partment_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `system_manage_user_partment_id_e4c3504c_fk_system_ma` (`partment_id`),
  KEY `system_manage_user_role_id_315091c4_fk_system_manage_role_id` (`role_id`),
  CONSTRAINT `system_manage_user_partment_id_e4c3504c_fk_system_ma` FOREIGN KEY (`partment_id`) REFERENCES `system_manage_partment` (`id`),
  CONSTRAINT `system_manage_user_role_id_315091c4_fk_system_manage_role_id` FOREIGN KEY (`role_id`) REFERENCES `system_manage_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_manage_user`
--

LOCK TABLES `system_manage_user` WRITE;
/*!40000 ALTER TABLE `system_manage_user` DISABLE KEYS */;
INSERT INTO `system_manage_user` VALUES (1,'123','123','男','2021-10-26 15:40:55.000000','1',1,1),(2,'123','123','男','2021-10-26 15:40:55.000000','1',2,3),(3,'123','123','男','2021-10-26 15:40:55.000000','1',1,3),(4,'康佩伦','123','男','2021-10-26 15:40:55.000000','1',2,2),(5,'123','123','男','2021-10-26 15:40:55.000000','0',1,1),(6,'康佩伦','123','男','2021-10-26 07:44:01.547848','0',1,1),(7,'康佩伦','123','女','2021-10-26 08:51:26.441099','0',1,2);
/*!40000 ALTER TABLE `system_manage_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 16:52:52
