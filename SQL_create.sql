
CREATE TABLE `Taipei` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

LOAD DATA 
INFILE 'd:/data_sports/data_sports_TPE.csv'
INTO TABLE Taipei  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `changhua` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_CWH.csv'
INTO TABLE changhua  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';


CREATE TABLE `chiayi` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_CYI.csv'
INTO TABLE chiayi  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `chiayi_county` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

LOAD DATA 
INFILE 'd:/data_sports/data_sports_CHY.csv'
INTO TABLE chiayi_county  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `hsinchu` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_HSC.csv'
INTO TABLE hsinchu  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `hsinchu_county` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_HSH.csv'
INTO TABLE hsinchu_county  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `hualien` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_HWA.csv'
INTO TABLE hualien  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
;
CREATE TABLE `kaohsiung` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_KHH.csv'
INTO TABLE kaohsiung  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `keelung` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_KLU.csv'
INTO TABLE keelung  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `kinmen` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_KMN.csv'
INTO TABLE kinmen  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `miaoli` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_MAL.csv'
INTO TABLE miaoli  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `nantou` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_NTO.csv'
INTO TABLE nantou  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `new_taipei` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_TPH.csv'
INTO TABLE new_taipei  character set 'utf8mb4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `penghu` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_PEH.csv'
INTO TABLE penghu  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `pingtung` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_IUH.csv'
INTO TABLE pingtung  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `taichung` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_TXG.csv'
INTO TABLE taichung  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `tainan` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_TNN.csv'
INTO TABLE tainan  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `taitung` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_TTT.csv'
INTO TABLE taitung  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `taoyuan` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_TYC.csv'
INTO TABLE taoyuan  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `yilan` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_ILN.csv'
INTO TABLE yilan  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE `yunlin` (
  `id` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `shop_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `shop_url` varchar(2508) COLLATE utf8_bin DEFAULT NULL,
  `shop_address` varchar(2555) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
LOAD DATA 
INFILE 'd:/data_sports/data_sports_YLH.csv'
INTO TABLE yunlin  character set 'UTF8MB4'
FIELDS TERMINATED BY ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';
