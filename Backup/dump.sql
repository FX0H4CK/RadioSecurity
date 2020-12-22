-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: localhost    Database: radio_mon
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB-3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ssids`
--

DROP TABLE IF EXISTS `ssids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ssids` (
  `bssid` char(50) NOT NULL,
  `first_seen` datetime DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `channel` int(11) DEFAULT NULL,
  `speed` int(11) DEFAULT NULL,
  `privacy` char(10) DEFAULT NULL,
  `cipher` char(10) DEFAULT NULL,
  `auth` char(19) DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `beacons` int(11) DEFAULT NULL,
  `iv` int(11) DEFAULT NULL,
  `ip` char(50) DEFAULT NULL,
  `length` int(11) DEFAULT NULL,
  `essid` char(50) NOT NULL,
  `vendor` char(50) DEFAULT NULL,
  PRIMARY KEY (`essid`,`bssid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ssids`
--

LOCK TABLES `ssids` WRITE;
/*!40000 ALTER TABLE `ssids` DISABLE KEYS */;
INSERT INTO `ssids` VALUES ('00:A0:57:38:74:36','2020-12-22 19:23:16','2020-12-22 19:23:16',44,270,' WPA2',' CCMP',' PSK',-50,1,0,'   0.  0.  0.  0',1,'','LANCOM Systems GmbH'),('78:28:CA:C3:F7:17','2020-12-22 13:32:53','2020-12-22 13:32:57',6,-1,' WPA','','',-1,0,89,'   0.  0.  0.  0',0,'','Sonos, Inc.'),('38:EA:A7:C8:D8:97','2020-12-22 13:32:52','2020-12-22 13:32:56',1,58,' OPN','','',-71,8,0,'   0.  0.  0.  0',27,' HP-Print-97-Photosmart 5520','Hewlett Packard'),('00:A0:57:35:AA:F6','2020-12-22 19:23:16','2020-12-22 19:23:16',44,270,' WPA2',' CCMP',' PSK',-63,0,0,'   0.  0.  0.  0',6,' LANCOM','LANCOM Systems GmbH'),('00:A0:57:3B:59:0E','2020-12-22 13:32:52','2020-12-22 13:32:56',1,195,' WPA2',' CCMP',' PSK',-48,5,3,'   0.  0.  0.  0',6,' LANCOM','LANCOM Systems GmbH'),('02:A0:57:38:74:36','2020-12-22 19:23:16','2020-12-22 19:23:16',44,270,' WPA2',' CCMP',' PSK',-50,1,1,'   0.  0.  0.  0',6,' LANCOM','{\"errors\":{\"detail\":\"Not Found\"}}');
/*!40000 ALTER TABLE `ssids` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-22 19:28:28
