from node import Node, upMovement, calculateHeuristic, downMovement, leftMovement, rightMovement
from time import process_time


def getNodeMinHeuristic(stack):
    minNode = min(stack, key=lambda node: node.getHeuristic())
    return minNode


class GreedyAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.kirbyPos = self.firstNode.searchForKirby()
        self.wandanaPos = self.searchForWandana(world)
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def searchForWandana(self, world):
        wandanaPos = []
        for i in range(15):
            for j in range(15):
                if world[i, j] == self.firstNode.Wandana:
                    wandanaPos.append(i)
                    wandanaPos.append(j)
        return wandanaPos

    def find_possible_moves_greedy(self, currentNode):
        kirbyPos = currentNode.getKirbyPos()
        possible_moves = []

        if not (kirbyPos[1] + 1 > 14) and currentNode.getState()[kirbyPos[0], kirbyPos[1] + 1] != 1:
            son = Node(currentNode.getState(), currentNode,
                       "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                       currentNode.getFlower())

            right = rightMovement(kirbyPos)
            son.setNewCost(right)
            son.setKirbyPos(right)
            sonManhattanDistance = son.calculateManhattanDistance(
                self.wandanaPos)
            sonHeuristic = calculateHeuristic(sonManhattanDistance)
            son.setHeuristic(sonHeuristic)
            son.moveRight(kirbyPos)
            if son.compareCircles2(right):
                possible_moves.append(son)

        # Check if left side is free
        if not (kirbyPos[1] - 1 < 0) and currentNode.getState()[kirbyPos[0], kirbyPos[1] - 1] != 1:
            son = Node(currentNode.getState(), currentNode,
                       "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                       currentNode.getFlower())

            left = leftMovement(kirbyPos)
            son.setNewCost(left)
            son.setKirbyPos(left)
            sonManhattanDistance = son.calculateManhattanDistance(
                self.wandanaPos)
            sonHeuristic = calculateHeuristic(sonManhattanDistance)
            son.setHeuristic(sonHeuristic)
            son.moveLeft(kirbyPos)
            if son.compareCircles2(left):
                possible_moves.append(son)

        # Check if downside is free
        if not (kirbyPos[0] + 1 > 14) and currentNode.getState()[kirbyPos[0] + 1, kirbyPos[1]] != 1:
            son = Node(currentNode.getState(), currentNode,
                       "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                       currentNode.getFlower())

            down = downMovement(kirbyPos)
            son.setNewCost(down)
            son.setKirbyPos(down)
            sonManhattanDistance = son.calculateManhattanDistance(
                self.wandanaPos)
            sonHeuristic = calculateHeuristic(sonManhattanDistance)
            son.setHeuristic(sonHeuristic)
            son.moveDown(kirbyPos)
            if son.compareCircles2(down):
                possible_moves.append(son)

        # Check if upside is free
        if not (kirbyPos[0] - 1 < 0) and currentNode.getState()[kirbyPos[0] - 1, kirbyPos[1]] != 1:
            son = Node(currentNode.getState(), currentNode,
                       "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                       currentNode.getFlower())

            up = upMovement(kirbyPos)
            son.setNewCost(up)
            son.setKirbyPos(up)
            sonManhattanDistance = son.calculateManhattanDistance(
                self.wandanaPos)
            sonHeuristic = calculateHeuristic(sonManhattanDistance)
            son.setHeuristic(sonHeuristic)
            son.moveUp(kirbyPos)
            if son.compareCircles2(up):
                possible_moves.append(son)

        return possible_moves

    def start(self):
        startTime = process_time()

        stack = self.stack
        currentNode = stack[0]
        expandedNodes = 0
        depth = 0

        while not (currentNode.isGoal()):
            possible_moves = self.find_possible_moves_greedy(currentNode)
            stack += possible_moves

            stack.remove(currentNode)

            currentNode = getNodeMinHeuristic(stack)
            expandedNodes += 1

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Meta heuristic:", currentNode.getHeuristic())
        print("Expanded nodes: ", expandedNodes+1)  # Good
        print("Depth: ", depth)
        print("The final cost of the solution is: " + str(currentNode.getCost()))
        print("Times it went right:", currentNode.getRightCount())
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes+1, depth]
