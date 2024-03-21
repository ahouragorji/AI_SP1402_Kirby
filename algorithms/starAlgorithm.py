from node import Node, upMovement, calculateHeuristic, downMovement, leftMovement, rightMovement
from time import process_time


def getNodeMinSumCostHeuristic(stack):
    minNode = min(stack, key=lambda node: node.getSumCostHeuristic())
    return minNode


class StarAlgorithm:
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

    def start(self):
        startTime = process_time()
        stack = self.stack
        kirbyPos = self.kirbyPos
        expandedNodes = 0
        depth = 0

        # TODO: define currentNode
        currentNode = None

        while not (currentNode.isGoal()):
            if not (kirbyPos[1] + 1 > 14) and currentNode.getState()[kirbyPos[0], kirbyPos[1] + 1] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                right = rightMovement(kirbyPos)
                son.setNewCost(right)
                son.setKirbyPos(right)
                # TODO: implement the heuristic logic
                son.moveRight(kirbyPos)
                if son.avoidGoBack2(right):
                    stack.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            if not (kirbyPos[1] - 1 < 0) and currentNode.getState()[kirbyPos[0], kirbyPos[1] - 1] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                left = leftMovement(kirbyPos)
                son.setNewCost(left)
                son.setKirbyPos(left)
                # TODO: implement the heuristic logic
                son.moveLeft(kirbyPos)
                if son.avoidGoBack2(left):
                    stack.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            if not (kirbyPos[0] + 1 > 14) and currentNode.getState()[kirbyPos[0] + 1, kirbyPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                down = downMovement(kirbyPos)
                son.setNewCost(down)
                son.setKirbyPos(down)
                # TODO: implement the heuristic logic
                son.moveDown(kirbyPos)
                if son.avoidGoBack2(down):
                    stack.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            if not (kirbyPos[0] - 1 < 0) and currentNode.getState()[kirbyPos[0] - 1, kirbyPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                up = upMovement(kirbyPos)
                son.setNewCost(up)
                son.setKirbyPos(up)
                # TODO: implement the heuristic logic
                son.moveUp(kirbyPos)
                if son.avoidGoBack2(up):
                    stack.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            # TODO Update the stack

            # TODO: define currentNode
            currentNode = None

            expandedNodes += 1
            kirbyPos = currentNode.getKirbyPos()

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Heuristic: ", currentNode.getHeuristic())
        print("Expanded Nodes: ", expandedNodes+1)  # Good
        print("Depth: ", depth)
        print("Final Cost: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes+1, depth]
