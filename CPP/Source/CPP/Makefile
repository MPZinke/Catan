# Directories
# Directories::Source


Catan.o: Corner.o Edge.o Hexagon.o Resources.o Settlement.o
	@$(eval CATAN_OBJ:=$(OBJECTS_DIR)/Catan.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Catan.cpp -o $(CATAN_OBJ)


Corner.o:
	@$(eval CORNER_OBJ:=$(OBJECTS_DIR)/Corner.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Corner.cpp -o $(CORNER_OBJ)


Edge.o:
	@$(eval EDGE_OBJ:=$(OBJECTS_DIR)/Edge.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Edge.cpp -o $(EDGE_OBJ)


Hexagon.o:
	@$(eval HEXAGON_OBJ:=$(OBJECTS_DIR)/Hexagon.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Hexagon.cpp -o $(HEXAGON_OBJ)


Resources.o:
	@$(eval RESOURCES_OBJ:=$(OBJECTS_DIR)/Resources.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Resources.cpp -o $(RESOURCES_OBJ)


Settlement.o:
	@$(eval SETTLEMENT_OBJ:=$(OBJECTS_DIR)/Settlement.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Settlement.cpp -o $(SETTLEMENT_OBJ)
