from node import Node
from algorithms.common import find_possible_moves
from time import process_time


class BFS:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.kirbyPos = self.firstNode.searchForKirby()
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def start(self):
        startTime = process_time()
        expandedNodes = 0
        depth = 0

        # TODO: define required variables here
        currentNode = None

        while not currentNode.isGoal():
            possible_moves = find_possible_moves(currentNode)
            for move in possible_moves:
                # TODO: Implement your code here

                # Don't alter this
                if move.getDepth() > depth:
                    depth = move.getDepth()

            # TODO: Implement your code here
            currentNode = None

            # Don't alter this
            expandedNodes += 1

        # Don't alter this
        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Expanded nodes: ", expandedNodes + 1)  # Good
        print("Depth: ", depth)
        print("The final cost of the solution is: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes + 1, depth]


