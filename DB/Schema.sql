

DROP TABLE IF EXISTS "ResourceTypes" CASCADE;
DROP TABLE IF EXISTS "Corner's Edges" CASCADE;
DROP TABLE IF EXISTS "Corner's Sides" CASCADE;
DROP TABLE IF EXISTS "Edge's Corners" CASCADE;
DROP TABLE IF EXISTS "Edge's Sides" CASCADE;
DROP TABLE IF EXISTS "Side's Corners" CASCADE;
DROP TABLE IF EXISTS "Side's Edges" CASCADE;
DROP TABLE IF EXISTS "Boards" CASCADE;
DROP TABLE IF EXISTS "BoardsPorts" CASCADE;
DROP TABLE IF EXISTS "BoardsRoads" CASCADE;
DROP TABLE IF EXISTS "BoardsSettlements" CASCADE;
DROP TABLE IF EXISTS "BoardsTiles" CASCADE;
DROP TABLE IF EXISTS "BoardsPortsSettlements" CASCADE;
DROP TABLE IF EXISTS "BoardsRoadsSettlements" CASCADE;
DROP TABLE IF EXISTS "BoardsRoadsTiles" CASCADE;
DROP TABLE IF EXISTS "BoardsSettlementsTiles" CASCADE;
DROP TABLE IF EXISTS "Games" CASCADE;
DROP TABLE IF EXISTS "Ports" CASCADE;
DROP TABLE IF EXISTS "Roads" CASCADE;
DROP TABLE IF EXISTS "SettlementTypes" CASCADE;
DROP TABLE IF EXISTS "Settlements" CASCADE;
DROP TABLE IF EXISTS "Tiles" CASCADE;
DROP TABLE IF EXISTS "PortsSettlements" CASCADE;
DROP TABLE IF EXISTS "RoadsSettlements" CASCADE;
DROP TABLE IF EXISTS "RoadsTiles" CASCADE;
DROP TABLE IF EXISTS "SettlementsTiles" CASCADE;



CREATE TABLE "ResourceTypes"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


-- ——————————————————————————————————————————————————— DIRECTIONS ——————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "Corner's Edges"  -- The edges of a corne.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Corner's Sides"  -- The sides of a corner.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Edge's Corners"  -- The corners of a edge.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Edge's Sides"  -- The sides of a edge.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);

CREATE TABLE "Side's Corners"  -- The corners of a side.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Side's Edges"  -- The edges of a side.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


-- ————————————————————————————————————————————————————— BOARDS ————————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

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
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "BoardsRoads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "BoardsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "BoardsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL
);


-- ——————————————————————————————————————————————— BOARDS ASSOCIATION ——————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "BoardsPortsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"BoardsSettlements.id" INT NOT NULL,
	"BoardsPorts.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("BoardsSettlements.id") REFERENCES "BoardsSettlements"("id"),
	FOREIGN KEY ("BoardsPorts.id") REFERENCES "BoardsPorts"("id")
);


CREATE TABLE "BoardsRoadsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"Corner's Edges.id" INT NOT NULL,
	"Edge's Corners.id" INT NOT NULL,
	"BoardsRoads.id" INT NOT NULL,
	"BoardsSettlements.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Corner's Edges.id") REFERENCES "Corner's Edges"("id"),
	FOREIGN KEY ("Edge's Corners.id") REFERENCES "Edge's Corners"("id"),
	FOREIGN KEY ("BoardsRoads.id") REFERENCES "BoardsRoads"("id"),
	FOREIGN KEY ("BoardsSettlements.id") REFERENCES "BoardsSettlements"("id")
);


CREATE TABLE "BoardsRoadsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"Edge's Sides.id" INT NOT NULL,
	"Side's Edges.id" INT NOT NULL,
	"BoardsRoads.id" INT NOT NULL,
	"BoardsTiles.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Edge's Sides.id") REFERENCES "Edge's Sides"("id"),
	FOREIGN KEY ("Side's Edges.id") REFERENCES "Side's Edges"("id"),
	FOREIGN KEY ("BoardsRoads.id") REFERENCES "BoardsRoads"("id"),
	FOREIGN KEY ("BoardsTiles.id") REFERENCES "BoardsTiles"("id")
);


CREATE TABLE "BoardsSettlementsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"Boards.id" INT NOT NULL,
	"BoardsSettlements.id" INT NOT NULL,
	"BoardsTiles.id" INT NOT NULL,
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("BoardsSettlements.id") REFERENCES "BoardsSettlements"("id"),
	FOREIGN KEY ("BoardsTiles.id") REFERENCES "BoardsTiles"("id")
);


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
	"ResourceTypes.id" INT NOT NULL
);

-- ————————————————————————————————————————————————————— ROADS —————————————————————————————————————————————————————  --

CREATE TABLE "Roads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL  -- ,
	-- "Players.id" INT NOT NULL
);

-- —————————————————————————————————————————————————— SETTLEMENTS ——————————————————————————————————————————————————  --

CREATE TABLE "SettlementTypes"
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
	"SettlementsTypes.id" INT NOT NULL
);


-- ————————————————————————————————————————————————————— TILES —————————————————————————————————————————————————————  --

CREATE TABLE "Tiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL,
	"value" INT NOT NULL CHECK("value" <= 12 AND 0 <= "value"),
	"ResourceTypes.id" INT NOT NULL
);


-- ———————————————————————————————————————————————— GAME ASSOCIATION ———————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "PortsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"Settlements.id" INT NOT NULL,
	"Ports.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id"),
	FOREIGN KEY ("Ports.id") REFERENCES "Ports"("id")
);


CREATE TABLE "RoadsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Corner's Edges.id" INT NOT NULL,
	"Edge's Corners.id" INT NOT NULL,
	"Roads.id" INT NOT NULL,
	"Settlements.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Corner's Edges.id") REFERENCES "Corner's Edges"("id"),
	FOREIGN KEY ("Edge's Corners.id") REFERENCES "Edge's Corners"("id"),
	FOREIGN KEY ("Roads.id") REFERENCES "Roads"("id"),
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id")
);


CREATE TABLE "RoadsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Edge's Sides.id" INT NOT NULL,
	"Side's Edges.id" INT NOT NULL,
	"Roads.id" INT NOT NULL,
	"Tiles.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Edge's Sides.id") REFERENCES "Edge's Sides"("id"),
	FOREIGN KEY ("Side's Edges.id") REFERENCES "Side's Edges"("id"),
	FOREIGN KEY ("Roads.id") REFERENCES "Roads"("id"),
	FOREIGN KEY ("Tiles.id") REFERENCES "Tiles"("id")
);


CREATE TABLE "SettlementsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"Settlements.id" INT NOT NULL,
	"Tiles.id" INT NOT NULL,
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id"),
	FOREIGN KEY ("Tiles.id") REFERENCES "Tiles"("id")
);
