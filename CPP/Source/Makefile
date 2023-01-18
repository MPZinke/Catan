
# Compiles
CXX=g++
FLAGS="--std=c++17 -Wall"

# Directories
SOURCE_DIR=$(PWD)
# Directories::Objects
OBJECTS_DIR=$(SOURCE_DIR)/../Objects
# Directories::Source
CPP_DIR=$(SOURCE_DIR)/CPP
# Directories::Headers
HEADERS_DIR=$(SOURCE_DIR)/Headers
# Directories::Libraries
LIBRARIES_DIR=$(SOURCE_DIR)/Libraries
# Directories::SFML
SFML_DIR=/opt/homebrew/Cellar/sfml/2.5.1_2
# Directories::SFML::INCLUDES
SFML_INCLUDE_DIR=$(SFML_DIR)/include


RECURSIVE_INCLUDES=$(shell find $(HEADERS_DIR) $(LIBRARIES_DIR) -type d -print)
INCLUDES:=$(addprefix -I,$(RECURSIVE_INCLUDES) $(SFML_INCLUDE_DIR))

LINKS=-L$(SFML_DIR)/lib -lsfml-graphics -lsfml-window -lsfml-system
# LIBRARIES:=$(addprefix -I,$(shell find $(LIBRARIES_DIR) -type d -print))

# Outputs
BINARY=Catan
OBJECTS=$(OBJECTS_DIR)/*.o

all:
	@$(MAKE) Catan.o -C $(CPP_DIR) \
	  -e CXX=$(CXX) \
	  -e FLAGS=$(FLAGS) \
	  -e CPP_DIR=$(CPP_DIR) \
	  -e INCLUDES="$(INCLUDES)" \
	  -e OBJECTS_DIR=$(OBJECTS_DIR)

	$(CXX) $(FLAGS) $(OBJECTS) $(LINKS) -o $(BINARY)
