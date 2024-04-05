#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.03                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION: Creates a grid of hexagons at a specified size within a give area.                                    #
#                Notably for all formulae, √3 will signify (√3) or 3^0.5. Any trailing values are not a part of the    #
#                square root.                                                                                          #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################




import math
from typing import Tuple


from gui import Hexagon


Coordinate = Tuple[float, float]


class HexagonGrid:
	r"""
	Creates a grid of hexagons at a specified size within a give area.
	---
	When measuring from the center of a hexagon to a vertice as depicted in Figure 1, the following formula can be
	 applied:
		w = 2s, h = (√3)s
	Figure 1.
	  |<---- 2s ----->|  
	      _________      _
	     /         \     ↑
	    /           \    |
	   /      ___S___\  (√3)s
	   \             /   |
	    \           /    |
	     \_________/     ↓
	                     ‾
		
	Therefore, we determine the ratio of 
		w : h => 2s : (√3)s

	Applying this for measuring from the center of a hexagon to a side as depicted in Figure 2, the following is
	 derived:
		    y = .5 h     ==     2y = h
		=>  y = .5 (√3)s
		=> 2y = (√3)s
		=> 2y/√3 = s
	Using w = 2s,
		   w = 2(2y/√3)
		=> w = 4y/√3

	Figure 2.
	  |<--- 4y/√3 --->|  —
	      _________      ↑
	     /    |    \     |
	    /     y     \    |
	   /      |      \  2y
	   \             /   |
	    \           /    |
	     \_________/     ↓
	                     ‾

	Additional important distances between hexagon centers in the grid shown below are as follow:
		   horizontal distance = (3/4)w
		   vertical distance   = (1/2)h
		=> horizontal distance = (3/4)(4y/√3)
		   vertical distance   = (1/2)(2y)
		=> horizontal distance = (3y/√3) => (√3)y
		   vertical distance   = y

	Figure 3.
	      _________
	     /         \
	    /           \
	   /      .      \_____     _
	   \             /          ↑
	    \           /           y
	     \_________/       .    ↓
	               \            ‾
	                \       
	          |<-- (√3)y ->|


	Finally, first hexagon will start in the top left settlement with its top side against the top of the area and the left
	 settlement against the left side. Numbering starts at [0, 0]. The first hexagon of the odd rows will be shifted down
	 by `y` units and to the right by `(√3)y` units.

	Links:
	- https://www.redblobgames.com/grids/hexagons/
	"""
	ONE_THIRD = 1 / 3
	SQUAREROOT_3 = math.sqrt(3)

	def __init__(self, width: int, height: int, hexagon_size: int):
		self.width: int = width
		self.height: int = height
		self.hexagon_size: int = hexagon_size

		self.hexagons: list[list[Hexagon]] = []

		# ———— Create hexagons ———— #
		height_index_count: Tuple[int, int] = HexagonGrid.number_of_indexes_for_height(height, hexagon_size)
		width_index_count: int = HexagonGrid.number_of_indexes_for_width(width, hexagon_size)
		for x_index in range(width_index_count):
			self.hexagons.append([])
			for y_index in range(height_index_count[x_index & 0b1]):  # Select the height for an even or odd column.
				x_position: int = HexagonGrid.x_position_for_index(x_index, hexagon_size)
				y_position: int = HexagonGrid.y_position_for_index(y_index, hexagon_size, x_index & 0b1)
				current_position = [x_position, y_position]

				self.hexagons[-1].append(Hexagon(current_position, hexagon_size))


	@staticmethod
	def x_position_for_index(x_index: int, hexagon_size: int) -> int:
		"""
		Determines a hexagon's center x_position give an index.
		---
		The distance from a settlement to the center of a hexagon can be expressed by,
			Where `d` is the distance from a settlement to the center and `y` is the size of the hexagon from center to side
			   d = (2y)/√3
		For every additional column of flat hexagons we add, the width will increase by 3/4 the width of a hexagon.
		 Because the columns shall start with their left settlement flush with the area left road, the given width of a
		 hexagon, the following is derived as,
			Where `d` is the distance from the area left wall, `i` is the x index, and `y` is the size of the hexagon
			 from center to side
			   d = (2y)/√3 + (3/4)i(4y)/√3
			=> d = (2y)/√3 + (3yi)/√3
			=> d = (2y + 3yi)/√3
			=> d = y(2 + 3i)/√3
		"""
		incremental_increase: float = 2 + (3 * x_index)
		size_multiplier: float = hexagon_size * incremental_increase / HexagonGrid.SQUAREROOT_3
		x_position = int(size_multiplier)
		# x_position = int(slope * (x_index + HexagonGrid.ONE_THIRD) + 2 + offset)

		return x_position


	@staticmethod
	def y_position_for_index(y_index: int, hexagon_size: int, is_odd_column_index: bool) -> int:
		"""
		Determines a hexagon's center y_position give an index.
		---
		"""
		distance_to_top: int = hexagon_size * 2 * y_index  # The span to the current hexagon's top.
		distance_to_center: int = distance_to_top + hexagon_size  # Adds size to get to center.
		offset_for_column_index: int = hexagon_size * is_odd_column_index
		y_position = distance_to_center + offset_for_column_index
		return y_position


	@staticmethod
	def number_of_indexes_for_height(height: int, hexagon_size: int) -> Tuple[int, int]:
		"""
		Determines the number of hexagon indexes for a given height and the hexagon size from center to side.
		---
		If the hexagon size is half the height of a hexagon then,
			Where `h` is the height of a hexagon and `y` is the size of a hexagon from center to side
			   h = 2y
		Even columns are columns of hexagons that start with the top side flush with the top area boundary.
		 Therefore, for even columns,
			Where `i` is the number of indexes and h is the height of the area and `y` is the size of a hexagon from
			center to side
			   i = h/(2s)

		Odds columns are columns of hexagons that start with the top side offset by the hexagon size from the top area
		 boundary. Therefore, for odd columns,
			Where `i` is the number of indexes and h is the height of the area and `y` is the size of a hexagon from
			 center to side
			   i = (h-y)/(2y)
			=> i = h/(2y) - y/(2y)
			=> i = h/(2y) - 0.5
		"""
		hexagon_size_times_2 = hexagon_size * 2
		raw_height_indexes = height / hexagon_size_times_2

		even_row_indexes = int(raw_height_indexes)
		odd_row_indexes = int(raw_height_indexes - 0.5)
		return [even_row_indexes, odd_row_indexes]


	@staticmethod
	def number_of_indexes_for_width(width: int, hexagon_size: int) -> int:
		"""
		Determines the number of hexagon indexes for a given width and the hexagon size from center to side.
		---
		For the progression in Figure 1, one can derive:
			Where `w` is the width and `i` is the number of indexes
			   w = 4y/√3 + (i-1)(√3)y
			=> w - 4y/√3 = (i-1)(√3)y
			=> w/((√3)y) - (4y/√3)/((√3)y) = i-1    =>    w/((√3)y) - 4/3 = i-1
			=> w/((√3)y) - 4/3 + 1 = i
			=> w/((√3)y) - 1/3 = i

		Figure 1.
			||    wi    ||       w1       |       w2       |       w3       |       w4       ||
			||----------||----------------|----------------|----------------|----------------||
			|| width fn ||      4y/√3     |  4y/√3 + (√3)y | 4y/√3 + 2(√3)y | 4y/√3 + 3(√3)y ||

		Notably, `w/((√3)y)` is left as a radical, so to save an extra instruction
		"""
		numerator = width
		denominator = HexagonGrid.SQUAREROOT_3 * hexagon_size
		width_index_count: float = numerator / denominator - HexagonGrid.ONE_THIRD

		return int(width_index_count)
