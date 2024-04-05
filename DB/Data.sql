



INSERT INTO "Corner's Edges" ("label") VALUES  -- The edges of a corne.
('TOP'),
('BOTTOM'),
('SIDE');


INSERT INTO "Corner's Sides" ("label") VALUES  -- The sides of a corner.
('TOP'),
('BOTTOM'),
('SIDE');


INSERT INTO "Edge's Corners" ("label") VALUES  -- The corners of a edge.
('LEFT'),
('RIGHT');


INSERT INTO "Edge's Sides" ("label") VALUES  -- The sides of a edge.
('TOP'),
('BOTTOM');


INSERT INTO "Side's Corners" ("label") VALUES  -- The corners of a side.
('TOP_LEFT'),
('TOP_RIGHT'),
('RIGHT'),
('BOTTOM_RIGHT'),
('BOTTOM_LEFT'),
('LEFT');


INSERT INTO "Side's Edges" ("label") VALUES  -- The edges of a side.
('TOP'),
('TOP_RIGHT'),
('BOTTOM_RIGHT'),
('BOTTOM'),
('BOTTOM_LEFT'),
('TOP_LEFT');


INSERT INTO "SettlementTypes" ("label", "multiplier") VALUES
('UNENHABITED', 0),
('VILLAGE', 1),
('CITY', 2);