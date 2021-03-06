CREATE TABLE `datapoll_packetreceipt` (
  `packet_datetime` datetime(6) NOT NULL,
  `rss` smallint NOT NULL,
  `mac_address_id` int NOT NULL,
  `router_id` int NOT NULL,
  PRIMARY KEY (`packet_datetime`,`mac_address_id`,`router_id`),
  KEY `idx_datapoll_packetreceipt_mac_address_id` (`mac_address_id`)
) ENGINE=InnoDB
/*!50100 PARTITION BY RANGE (to_days(`packet_datetime`))
(PARTITION p20200819 VALUES LESS THAN (738022) ENGINE = InnoDB,
 PARTITION p20200820 VALUES LESS THAN (738023) ENGINE = InnoDB,
 PARTITION p20200821 VALUES LESS THAN (738024) ENGINE = InnoDB,
 PARTITION p20200822 VALUES LESS THAN (738025) ENGINE = InnoDB,
 PARTITION p20200823 VALUES LESS THAN (738026) ENGINE = InnoDB,
 PARTITION p20200824 VALUES LESS THAN (738027) ENGINE = InnoDB,
 PARTITION p20200825 VALUES LESS THAN (738028) ENGINE = InnoDB,
 PARTITION p20200826 VALUES LESS THAN (738029) ENGINE = InnoDB,
 PARTITION p20200827 VALUES LESS THAN (738030) ENGINE = InnoDB,
 PARTITION p20200828 VALUES LESS THAN (738031) ENGINE = InnoDB,
 PARTITION p20200829 VALUES LESS THAN (738032) ENGINE = InnoDB,
 PARTITION p20200830 VALUES LESS THAN (738033) ENGINE = InnoDB,
 PARTITION p20200831 VALUES LESS THAN (738034) ENGINE = InnoDB,
 PARTITION p20200901 VALUES LESS THAN (738035) ENGINE = InnoDB,
 PARTITION p20200902 VALUES LESS THAN (738036) ENGINE = InnoDB,
 PARTITION p20200903 VALUES LESS THAN (738037) ENGINE = InnoDB,
 PARTITION p20200904 VALUES LESS THAN (738038) ENGINE = InnoDB,
 PARTITION p20200905 VALUES LESS THAN (738039) ENGINE = InnoDB,
 PARTITION p20200906 VALUES LESS THAN (738040) ENGINE = InnoDB,
 PARTITION p20200907 VALUES LESS THAN (738041) ENGINE = InnoDB,
 PARTITION p20200908 VALUES LESS THAN (738042) ENGINE = InnoDB,
 PARTITION p20200909 VALUES LESS THAN (738043) ENGINE = InnoDB,
 PARTITION p20200910 VALUES LESS THAN (738044) ENGINE = InnoDB,
 PARTITION p20200911 VALUES LESS THAN (738045) ENGINE = InnoDB,
 PARTITION p20200912 VALUES LESS THAN (738046) ENGINE = InnoDB,
 PARTITION p20200913 VALUES LESS THAN (738047) ENGINE = InnoDB,
 PARTITION p20200914 VALUES LESS THAN (738048) ENGINE = InnoDB,
 PARTITION p20200915 VALUES LESS THAN (738049) ENGINE = InnoDB,
 PARTITION p20200916 VALUES LESS THAN (738050) ENGINE = InnoDB,
 PARTITION p20200917 VALUES LESS THAN (738051) ENGINE = InnoDB,
 PARTITION p20200918 VALUES LESS THAN (738052) ENGINE = InnoDB,
 PARTITION p20200919 VALUES LESS THAN (738053) ENGINE = InnoDB,
 PARTITION p20200920 VALUES LESS THAN (738054) ENGINE = InnoDB,
 PARTITION p20200921 VALUES LESS THAN (738055) ENGINE = InnoDB,
 PARTITION p20200922 VALUES LESS THAN (738056) ENGINE = InnoDB,
 PARTITION p20200923 VALUES LESS THAN (738057) ENGINE = InnoDB,
 PARTITION p20200924 VALUES LESS THAN (738058) ENGINE = InnoDB,
 PARTITION p20200925 VALUES LESS THAN (738059) ENGINE = InnoDB,
 PARTITION p20200926 VALUES LESS THAN (738060) ENGINE = InnoDB,
 PARTITION p20200927 VALUES LESS THAN (738061) ENGINE = InnoDB,
 PARTITION p20200928 VALUES LESS THAN (738062) ENGINE = InnoDB,
 PARTITION p20200929 VALUES LESS THAN (738063) ENGINE = InnoDB,
 PARTITION p20200930 VALUES LESS THAN (738064) ENGINE = InnoDB,
 PARTITION future VALUES LESS THAN MAXVALUE ENGINE = InnoDB) */

