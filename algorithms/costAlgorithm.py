from node import Node, upMovement, downMovement, leftMovement, rightMovement
from time import process_time


def getNodeMinCost(stack):
    minNode = min(stack, key=lambda node: node.getCost())
    return minNode


class CostAlgorithm:
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
                son.moveRight(kirbyPos)
                if son.avoidGoBack2(right):
                    # TODO: Update the stack
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            if not (kirbyPos[1] - 1 < 0) and currentNode.getState()[kirbyPos[0], kirbyPos[1] - 1] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                left = leftMovement(kirbyPos)
                son.setNewCost(left)
                son.setKirbyPos(left)
                son.moveLeft(kirbyPos)
                if son.avoidGoBack2(left):
                    # TODO: Update the stack
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            if not (kirbyPos[0] + 1 > 14) and currentNode.getState()[kirbyPos[0] + 1, kirbyPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                down = downMovement(kirbyPos)
                son.setNewCost(down)
                son.setKirbyPos(down)
                son.moveDown(kirbyPos)
                if son.avoidGoBack2(down):
                    # TODO: Update the stack
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            if not (kirbyPos[0] - 1 < 0) and currentNode.getState()[kirbyPos[0] - 1, kirbyPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                up = upMovement(kirbyPos)
                son.setNewCost(up)
                son.setKirbyPos(up)
                son.moveUp(kirbyPos)
                if son.avoidGoBack2(up):
                    # TODO: Update the stack
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            # TODO: Update the stack

            # TODO: Implement your code here
            currentNode = None

            expandedNodes += 1
            kirbyPos = currentNode.getKirbyPos()

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Expanded Nodes: ", expandedNodes + 1)
        print("Depth: ", depth)
        print("Final Cost: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes+1, depth]
