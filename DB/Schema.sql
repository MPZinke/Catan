
DROP TABLE IF EXISTS "ResourceTypes" CASCADE;
DROP TABLE IF EXISTS "Boards" CASCADE;
DROP TABLE IF EXISTS "BoardsPorts" CASCADE;
DROP TABLE IF EXISTS "BoardsRoads" CASCADE;
DROP TABLE IF EXISTS "BoardsSettlements" CASCADE;
DROP TABLE IF EXISTS "BoardsTiles" CASCADE;
DROP TABLE IF EXISTS "Games" CASCADE;
DROP TABLE IF EXISTS "Ports" CASCADE;
DROP TABLE IF EXISTS "Roads" CASCADE;
DROP TABLE IF EXISTS "SettlementsTypes" CASCADE;
DROP TABLE IF EXISTS "Settlements" CASCADE;
DROP TABLE IF EXISTS "Tiles" CASCADE;



CREATE TABLE "ResourceTypes"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);



-- ————————————————————————————————————————————————————— BOARDS ————————————————————————————————————————————————————— --

-- A template used to create a Game from.
CREATE TABLE "Boards"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"name" VARCHAR(32) NOT NULL UNIQUE
);


CREATE TABLE "BoardsPorts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	-- Settlements
	"Settlements::TOP_LEFT" INT DEFAULT NULL,
	"Settlements::TOP_RIGHT" INT DEFAULT NULL,
	"Settlements::RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_LEFT" INT DEFAULT NULL,
	"Settlements::LEFT" INT DEFAULT NULL
);


CREATE TABLE "BoardsRoads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,

	-- Settlements
	"Settlements::LEFT" INT DEFAULT NULL,
	"Settlements::RIGHT" INT DEFAULT NULL,

	-- Tiles
	"Tiles::TOP" INT DEFAULT NULL,
	"Tiles::BOTTOM" INT DEFAULT NULL
);


CREATE TABLE "BoardsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	-- Ports
	"Ports::TOP" INT DEFAULT NULL,
	"Ports::SIDE" INT DEFAULT NULL,
	"Ports::BOTTOM" INT DEFAULT NULL,
	-- Roads
	"Roads::TOP" INT DEFAULT NULL,
	"Roads::SIDE" INT DEFAULT NULL,
	"Roads::BOTTOM" INT DEFAULT NULL,
	-- Tiles
	"Tiles::TOP" INT DEFAULT NULL,
	"Tiles::SIDE" INT DEFAULT NULL,
	"Tiles::BOTTOM" INT DEFAULT NULL
);


CREATE TABLE "BoardsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL,
	-- Roads
	"Roads::TOP" INT DEFAULT NULL,
	"Roads::TOP_RIGHT" INT DEFAULT NULL,
	"Roads::BOTTOM_RIGHT" INT DEFAULT NULL,
	"Roads::BOTTOM_LEFT" INT DEFAULT NULL,
	"Roads::BOTTOM" INT DEFAULT NULL,
	"Roads::TOP_LEFT" INT DEFAULT NULL,
	-- Settlements
	"Settlements::TOP_LEFT" INT DEFAULT NULL,
	"Settlements::TOP_RIGHT" INT DEFAULT NULL,
	"Settlements::RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_LEFT" INT DEFAULT NULL,
	"Settlements::LEFT" INT DEFAULT NULL
);


ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Boards.id_fk" FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id");
ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Settlements::TOP_LEFT_fk" FOREIGN KEY ("Settlements::TOP_LEFT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Settlements::TOP_RIGHT_fk" FOREIGN KEY ("Settlements::TOP_RIGHT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Settlements::RIGHT_fk" FOREIGN KEY ("Settlements::RIGHT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Settlements::BOTTOM_RIGHT_fk" FOREIGN KEY ("Settlements::BOTTOM_RIGHT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Settlements::BOTTOM_LEFT_fk" FOREIGN KEY ("Settlements::BOTTOM_LEFT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsPorts" ADD CONSTRAINT "BoardsPorts_Settlements::LEFT_fk" FOREIGN KEY ("Settlements::LEFT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsRoads" ADD CONSTRAINT "BoardsRoads_Boards.id_fk" FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id");
ALTER TABLE "BoardsRoads" ADD CONSTRAINT "BoardsRoads_Settlements::LEFT_fk" FOREIGN KEY ("Settlements::LEFT") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsRoads" ADD CONSTRAINT "BoardsRoads_Settlements::RIGHT_fk" FOREIGN KEY ("Settlements::RIGHT") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsRoads" ADD CONSTRAINT "BoardsRoads_Tiles::TOP_fk" FOREIGN KEY ("Tiles::TOP") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsRoads" ADD CONSTRAINT "BoardsRoads_Tiles::BOTTOM_fk" FOREIGN KEY ("Tiles::BOTTOM") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Boards.id_fk" FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Ports::TOP_fk" FOREIGN KEY ("Ports::TOP") REFERENCES "BoardsPorts"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Ports::SIDE_fk" FOREIGN KEY ("Ports::SIDE") REFERENCES "BoardsPorts"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Ports::BOTTOM_fk" FOREIGN KEY ("Ports::BOTTOM") REFERENCES "BoardsPorts"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Roads::TOP_fk" FOREIGN KEY ("Roads::TOP") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Roads::SIDE_fk" FOREIGN KEY ("Roads::SIDE") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Roads::BOTTOM_fk" FOREIGN KEY ("Roads::BOTTOM") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Tiles::TOP_fk" FOREIGN KEY ("Tiles::TOP") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Tiles::SIDE_fk" FOREIGN KEY ("Tiles::SIDE") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsSettlements" ADD CONSTRAINT "BoardsSettlements_Tiles::BOTTOM_fk" FOREIGN KEY ("Tiles::BOTTOM") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Boards.id_fk" FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Roads::TOP_fk" FOREIGN KEY ("Roads::TOP") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Roads::TOP_RIGHT_fk" FOREIGN KEY ("Roads::TOP_RIGHT") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Roads::BOTTOM_RIGHT_fk" FOREIGN KEY ("Roads::BOTTOM_RIGHT") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Roads::BOTTOM_LEFT_fk" FOREIGN KEY ("Roads::BOTTOM_LEFT") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Roads::BOTTOM_fk" FOREIGN KEY ("Roads::BOTTOM") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Roads::TOP_LEFT_fk" FOREIGN KEY ("Roads::TOP_LEFT") REFERENCES "BoardsRoads"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Settlements::TOP_LEFT_fk" FOREIGN KEY ("Settlements::TOP_LEFT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Settlements::TOP_RIGHT_fk" FOREIGN KEY ("Settlements::TOP_RIGHT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Settlements::RIGHT_fk" FOREIGN KEY ("Settlements::RIGHT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Settlements::BOTTOM_RIGHT_fk" FOREIGN KEY ("Settlements::BOTTOM_RIGHT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Settlements::BOTTOM_LEFT_fk" FOREIGN KEY ("Settlements::BOTTOM_LEFT") REFERENCES "BoardsSettlements"("id");
ALTER TABLE "BoardsTiles" ADD CONSTRAINT "BoardsTiles_Settlements::LEFT_fk" FOREIGN KEY ("Settlements::LEFT") REFERENCES "BoardsSettlements"("id");



-- —————————————————————————————————————————————————————— GAME —————————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "Games"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"started" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"finished" TIMESTAMP DEFAULT NULL,
	"Boards.id" INT DEFAULT NULL
);


-- ————————————————————————————————————————————————————— PORTS —————————————————————————————————————————————————————  --

CREATE TABLE "Ports"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"ResourceTypes.id" INT NOT NULL,
	-- Settlements
	"Settlements::TOP_LEFT" INT DEFAULT NULL,
	"Settlements::TOP_RIGHT" INT DEFAULT NULL,
	"Settlements::RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_LEFT" INT DEFAULT NULL,
	"Settlements::LEFT" INT DEFAULT NULL
);

-- ————————————————————————————————————————————————————— ROADS —————————————————————————————————————————————————————  --

CREATE TABLE "Roads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	-- "Players.id" INT NOT NULL,
	-- Settlements
	"Settlements::LEFT" INT DEFAULT NULL,
	"Settlements::RIGHT" INT DEFAULT NULL,
	-- Tiles
	"Tiles::TOP" INT DEFAULT NULL,
	"Tiles::BOTTOM" INT DEFAULT NULL
);

-- —————————————————————————————————————————————————— SETTLEMENTS ——————————————————————————————————————————————————  --

CREATE TABLE "SettlementsTypes"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE,
	"multiplier" INT NOT NULL DEFAULT 0 CHECK("multiplier" < 3)
);


CREATE TABLE "Settlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	-- "Players.id" INT NOT NULL,
	"SettlementsTypes.id" INT NOT NULL,
	-- Ports
	"Ports::TOP" INT DEFAULT NULL,
	"Ports::SIDE" INT DEFAULT NULL,
	"Ports::BOTTOM" INT DEFAULT NULL,
	-- Roads
	"Roads::TOP" INT DEFAULT NULL,
	"Roads::SIDE" INT DEFAULT NULL,
	"Roads::BOTTOM" INT DEFAULT NULL,
	-- Tiles
	"Tiles::TOP" INT DEFAULT NULL,
	"Tiles::SIDE" INT DEFAULT NULL,
	"Tiles::BOTTOM" INT DEFAULT NULL
);


-- ————————————————————————————————————————————————————— TILES —————————————————————————————————————————————————————  --

CREATE TABLE "Tiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL,
	"value" INT NOT NULL CHECK("value" <= 12 AND 0 <= "value"),
	"ResourceTypes.id" INT NOT NULL,
	-- Roads
	"Roads::TOP" INT DEFAULT NULL,
	"Roads::TOP_RIGHT" INT DEFAULT NULL,
	"Roads::BOTTOM_RIGHT" INT DEFAULT NULL,
	"Roads::BOTTOM_LEFT" INT DEFAULT NULL,
	"Roads::BOTTOM" INT DEFAULT NULL,
	"Roads::TOP_LEFT" INT DEFAULT NULL,
	-- Settlements
	"Settlements::TOP_LEFT" INT DEFAULT NULL,
	"Settlements::TOP_RIGHT" INT DEFAULT NULL,
	"Settlements::RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_RIGHT" INT DEFAULT NULL,
	"Settlements::BOTTOM_LEFT" INT DEFAULT NULL,
	"Settlements::LEFT" INT DEFAULT NULL
);


ALTER TABLE "Games" ADD CONSTRAINT "Games_Boards.id_fk" FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Games.id_fk" FOREIGN KEY ("Games.id") REFERENCES "Games"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Settlements::TOP_LEFT_fk" FOREIGN KEY ("Settlements::TOP_LEFT") REFERENCES "Settlements"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Settlements::TOP_RIGHT_fk" FOREIGN KEY ("Settlements::TOP_RIGHT") REFERENCES "Settlements"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Settlements::RIGHT_fk" FOREIGN KEY ("Settlements::RIGHT") REFERENCES "Settlements"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Settlements::BOTTOM_RIGHT_fk" FOREIGN KEY ("Settlements::BOTTOM_RIGHT") REFERENCES "Settlements"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Settlements::BOTTOM_LEFT_fk" FOREIGN KEY ("Settlements::BOTTOM_LEFT") REFERENCES "Settlements"("id");
ALTER TABLE "Ports" ADD CONSTRAINT "Ports_Settlements::LEFT_fk" FOREIGN KEY ("Settlements::LEFT") REFERENCES "Settlements"("id");
ALTER TABLE "Roads" ADD CONSTRAINT "Roads_Games.id_fk" FOREIGN KEY ("Games.id") REFERENCES "Games"("id");
ALTER TABLE "Roads" ADD CONSTRAINT "Roads_Settlements::LEFT_fk" FOREIGN KEY ("Settlements::LEFT") REFERENCES "Roads"("id");
ALTER TABLE "Roads" ADD CONSTRAINT "Roads_Settlements::RIGHT_fk" FOREIGN KEY ("Settlements::RIGHT") REFERENCES "Roads"("id");
ALTER TABLE "Roads" ADD CONSTRAINT "Roads_Tiles::TOP_fk" FOREIGN KEY ("Tiles::TOP") REFERENCES "Roads"("id");
ALTER TABLE "Roads" ADD CONSTRAINT "Roads_Tiles::BOTTOM_fk" FOREIGN KEY ("Tiles::BOTTOM") REFERENCES "Roads"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Games.id_fk" FOREIGN KEY ("Games.id") REFERENCES "Games"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Ports::TOP_fk" FOREIGN KEY ("Ports::TOP") REFERENCES "Ports"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Ports::SIDE_fk" FOREIGN KEY ("Ports::SIDE") REFERENCES "Ports"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Ports::BOTTOM_fk" FOREIGN KEY ("Ports::BOTTOM") REFERENCES "Ports"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Roads::TOP_fk" FOREIGN KEY ("Roads::TOP") REFERENCES "Roads"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Roads::SIDE_fk" FOREIGN KEY ("Roads::SIDE") REFERENCES "Roads"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Roads::BOTTOM_fk" FOREIGN KEY ("Roads::BOTTOM") REFERENCES "Roads"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Tiles::TOP_fk" FOREIGN KEY ("Tiles::TOP") REFERENCES "Roads"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Tiles::SIDE_fk" FOREIGN KEY ("Tiles::SIDE") REFERENCES "Roads"("id");
ALTER TABLE "Settlements" ADD CONSTRAINT "Settlements_Tiles::BOTTOM_fk" FOREIGN KEY ("Tiles::BOTTOM") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Games.id_fk" FOREIGN KEY ("Games.id") REFERENCES "Games"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Roads::TOP_fk" FOREIGN KEY ("Roads::TOP") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Roads::TOP_RIGHT_fk" FOREIGN KEY ("Roads::TOP_RIGHT") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Roads::BOTTOM_RIGHT_fk" FOREIGN KEY ("Roads::BOTTOM_RIGHT") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Roads::BOTTOM_LEFT_fk" FOREIGN KEY ("Roads::BOTTOM_LEFT") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Roads::BOTTOM_fk" FOREIGN KEY ("Roads::BOTTOM") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Roads::TOP_LEFT_fk" FOREIGN KEY ("Roads::TOP_LEFT") REFERENCES "Roads"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Settlements::TOP_LEFT_fk" FOREIGN KEY ("Settlements::TOP_LEFT") REFERENCES "Settlements"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Settlements::TOP_RIGHT_fk" FOREIGN KEY ("Settlements::TOP_RIGHT") REFERENCES "Settlements"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Settlements::RIGHT_fk" FOREIGN KEY ("Settlements::RIGHT") REFERENCES "Settlements"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Settlements::BOTTOM_RIGHT_fk" FOREIGN KEY ("Settlements::BOTTOM_RIGHT") REFERENCES "Settlements"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Settlements::BOTTOM_LEFT_fk" FOREIGN KEY ("Settlements::BOTTOM_LEFT") REFERENCES "Settlements"("id");
ALTER TABLE "Tiles" ADD CONSTRAINT "Tiles_Settlements::LEFT_fk" FOREIGN KEY ("Settlements::LEFT") REFERENCES "Settlements"("id");

