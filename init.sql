CREATE TABLE Estacao (
  Codigo VARCHAR PRIMARY KEY,
  Bairro VARCHAR,
  Latitude DOUBLE,
  Longitude DOUBLE
);

CREATE TABLE Analise (
  DataHora DATE PRIMARY KEY,
  fk_Estacao_Codigo VARCHAR,
  C_O FLOAT,
  N_O FLOAT,
  N_O2 FLOAT,
  N_Ox FLOAT,
  PM_10 FLOAT,
  PM_2_5 FLOAT,
  GrauC FLOAT,
  Chuva FLOAT,
  Pressao FLOAT,
  Radiacao_Solar FLOAT,
  Umidade_relativa FLOAT,
  Direcao FLOAT,
  Velocidade FLOAT
);

CREATE TABLE Zona (
  Nome VARCHAR,
  fk_Tags_Tags_PK INT,
  ID INT PRIMARY KEY,
  Raio FLOAT,
  Latitude FLOAT,
  Longitude FLOAT
);

CREATE TABLE Tags (
  Tags_PK INT NOT NULL PRIMARY KEY,
  Tags VARCHAR
);

CREATE TABLE pertence (
  fk_Estacao_Codigo VARCHAR,
  fk_Zona_ID INT
);

ALTER TABLE Analise ADD CONSTRAINT FK_Analise_2
  FOREIGN KEY (fk_Estacao_Codigo)
  REFERENCES Estacao (Codigo)
  ON DELETE CASCADE;

ALTER TABLE Zona ADD CONSTRAINT FK_Zona_2
  FOREIGN KEY (fk_Tags_Tags_PK)
  REFERENCES Tags (Tags_PK)
  ON DELETE NO ACTION;


ALTER TABLE pertence ADD CONSTRAINT FK_pertence_1
  FOREIGN KEY (fk_Estacao_Codigo)
  REFERENCES Estacao (Codigo)
  ON DELETE SET NULL;

ALTER TABLE pertence ADD CONSTRAINT FK_pertence_2
  FOREIGN KEY (fk_Zona_ID)
  REFERENCES Zona (ID)
  ON DELETE SET NULL;