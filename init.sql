CREATE TABLE `Estacao` (
  `Codigo` int(11) NOT NULL,
  `SiglaLocal` varchar(100) DEFAULT NULL,
  `Latitude` decimal(15,5) DEFAULT NULL,
  `Longitude` decimal(15,5) DEFAULT NULL,
  `NomeEstacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Codigo`),
  UNIQUE KEY `Estacao_UN` (`SiglaLocal`)
);

CREATE TABLE `Analise` (
  `Analise_id` int(11) NOT NULL AUTO_INCREMENT,
  `Data_e_hora` datetime NOT NULL,
  `CO` decimal(15,5) DEFAULT NULL,
  `CH4` decimal(15,5) DEFAULT NULL,
  `NO` decimal(15,5) DEFAULT NULL,
  `NO2` decimal(15,5) DEFAULT NULL,
  `NOx` decimal(15,5) DEFAULT NULL,
  `PM_10` decimal(15,5) DEFAULT NULL,
  `PM_2_5` decimal(15,5) DEFAULT NULL,
  `Temperatura` decimal(15,5) DEFAULT NULL,
  `Chuva` decimal(15,5) DEFAULT NULL,
  `Pressao` decimal(15,5) DEFAULT NULL,
  `RadiacaoSolar` decimal(15,5) DEFAULT NULL,
  `UmidadeRelativaDoAr` decimal(15,5) DEFAULT NULL,
  `DirecaoVento` decimal(15,5) DEFAULT NULL,
  `VelocidadeVento` decimal(15,5) DEFAULT NULL,
  `EstacaoCodigo` int(11) NOT NULL,
  PRIMARY KEY (`Analise_id`),
  KEY `Analise_FK` (`EstacaoCodigo`),
  CONSTRAINT `Analise_FK` FOREIGN KEY (`EstacaoCodigo`) REFERENCES `Estacao` (`Codigo`) ON UPDATE CASCADE
);

CREATE TABLE `QualidadeDoAr` (
  `ID` int(11) NOT NULL,
  `IQAR` int(10) unsigned DEFAULT NULL,
  `Data` datetime DEFAULT NULL,
  `Poluente` varchar(100) DEFAULT NULL,
  `Classificacao` varchar(100) DEFAULT NULL,
  `SiglaLocalEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `QualidadeDoAr_FK` (`SiglaLocalEstacao`),
  CONSTRAINT `QualidadeDoAr_FK` FOREIGN KEY (`SiglaLocalEstacao`) REFERENCES `Estacao` (`SiglaLocal`) ON UPDATE CASCADE
);

CREATE TABLE `Zona` (
  `Zona_id` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) DEFAULT NULL,
  `Latitude` decimal(15,10) DEFAULT NULL,
  `Longitude` decimal(15,10) DEFAULT NULL,
  `Raio` decimal(15,10) DEFAULT NULL,
  PRIMARY KEY (`Zona_id`)
);

CREATE TABLE `Tag` (
  `Tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `Tag` varchar(100) DEFAULT NULL,
  `Zona_id` int(11) NOT NULL,
  PRIMARY KEY (`Tag_id`),
  KEY `Tag_FK` (`Zona_id`),
  CONSTRAINT `Tag_FK` FOREIGN KEY (`Zona_id`) REFERENCES `Zona` (`Zona_id`)
);

CREATE TABLE `EstacaoZona` (
  `EstacaoCodigo` int(11) NOT NULL,
  `Zona_id` int(11) NOT NULL,
  PRIMARY KEY (`EstacaoCodigo`,`Zona_id`),
  KEY `EstacaoZona_FK_1` (`Zona_id`),
  CONSTRAINT `EstacaoZona_FK` FOREIGN KEY (`EstacaoCodigo`) REFERENCES `Estacao` (`Codigo`) ON UPDATE CASCADE,
  CONSTRAINT `EstacaoZona_FK_1` FOREIGN KEY (`Zona_id`) REFERENCES `Zona` (`Zona_id`) ON UPDATE CASCADE
);