

INSERT INTO "PlayerColors" ("rgb", "label") VALUES
(ARRAY[206, 156, 198]::INT[8], 'Pink'),
(ARRAY[ 88, 193,  98]::INT[8], 'Green'),
(ARRAY[ 48, 110, 178]::INT[8], 'Blue'),
(ARRAY[245, 196,  67]::INT[8], 'Yellow'),
(ARRAY[214,  75,  70]::INT[8], 'Red'),
(ARRAY[ 83,  53,  68]::INT[8], 'Purple');


INSERT INTO "ResourceTypes" ("label") VALUES
('DESERT'),
('WHEAT'),
('WOOD'),
('SHEEP'),
('STONE'),
('BRICK');



/*
- 1: TOP
- 2: SIDE
- 3: BOTTOM
  _____/.............\
  ~~~~~\............./
  ~~~~~~1.........../
  ~~~~~~~\___2_____/
  ~~~~~~~/°°°°°°°°°\
  ~~~~~~3°°°°°°°°°°°\
  _____/°°°°°°°°°°°°°\
       \°°°°°°°°°°°°°/

  /.............\_____
  \............./~~~~~
   \...........1~~~~~~
    \_____2___/~~~~~~~
    /°°°°°°°°°\~~~~~~~
   /°°°°°°°°°°°3~~~~~~
  /°°°°°°°°°°°°°\_____
  \°°°°°°°°°°°°°/
*/
INSERT INTO "Corner's Edges" ("label") VALUES  -- The edges of a corne.
('TOP'),
('BOTTOM'),
('SIDE');


/*
Below are depictions of tiles relative to settlements.
  _____/.............\
  ~~~~~\.....TOP...../
  ~~~~~~\.........../
  ~SIDE~~\_________/
  ~~~~~~~/°°°°°°°°°\
  ~~~~~~/°°BOTTOM°°°\
  _____/°°°°°°°°°°°°°\
       \°°°°°°°°°°°°°/

  /.............\_____
  \.....TOP...../~~~~~
   \.........../~~~~~~
    \_________/~SIDE~~
    /°°°°°°°°°\~~~~~~~
   /°°BOTTOM°°°\~~~~~~
  /°°°°°°°°°°°°°\_____
  \°°°°°°°°°°°°°/

*/
INSERT INTO "Corner's Sides" ("label") VALUES  -- The sides of a corner.
('TOP'),
('BOTTOM'),
('SIDE');


/*
Given Figure 1 for the tile and its settlements,
      1_________2   
      /.........\   
     /...........\  
   6/.............\3
    \............./ 
     \.........../  
      \_________/   
      5         4   

For the line 1–2 settlement 1 is left and 2 right, while for line 4–5, 4 is right and 5 is left.
    1_________2           \.........../  
    /.........\            \_________/   
   /...........\           5         4   

For the line 1–6 settlement 1 is right and 6 left, while for line 3–4, 3 is right and 4 is left.
      1_____          .......\3
      /.....          ......./ 
     /......          ....../  
   6/.......          _____/   
    \.......               4   

For the line 2–3 settlement 2 is left and 3 right, while for line 5–6, 5 is right and 6 is left.
   _____2             6/.......
   .....\              \.......
   ......\              \......
   .......\3             \_____
   ......./              5     
*/
INSERT INTO "Edge's Corners" ("label") VALUES  -- The corners of a edge.
('LEFT'),
('RIGHT');


/*
Below are depictions of tiles relative to settlements.

   \.....TOP...../
    \.........../
     \_________/ 
     /~~~~~~~~~\ 
    /~~BOTTOM~~~\
   /~~~~~~~~~~~~~\ 

   ......\
   .......\______
   ..TOP../~~~~~~
   ....../~~~~~~~
   _____/~~BOTTOM
        \~~~~~~~~
         \~~~~~~~

          /......
   ______/.......
   ~~~~~~\..TOP..
   ~~~~~~~\......
   BOTTOM~~\_____
   ~~~~~~~~/     
   ~~~~~~~/
*/
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