from time import clock
from State import State
import heapq

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class Solver:

	
	def __init__(self,initialState):
		self.initialState = initialState
		self.explored = set()
		self.depth = 0
		self.expandedNodes = 0
		


	def solve(self):
		before = clock()
		frontier = [self.initialState]
		self.initialState.getFManhattan()
		self.explored.add(self.initialState.id)
		while frontier:
			self.expandedNodes += 1
			state = heapq.heappop(frontier)
			if (state.board == goalTest):
				self.finalState = state
				self.runningTime = clock() - before
				return True
			if state.depth+1 > self.depth:
				self.depth = state.depth+1
			for neighbor in state.neighbors():
				if not ((neighbor.id in self.explored)):
					self.explored.add(neighbor.id)
					neighbor.getFManhattan()
					heapq.heappush(frontier,neighbor)
		self.runningTime = clock() - before
		return False

