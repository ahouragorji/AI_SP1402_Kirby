from node import Node, rightMovement, leftMovement, downMovement, upMovement


def find_possible_moves(currentNode):
    kirbyPos = currentNode.getKirbyPos()
    possible_moves = []

    # Check if right side is free
    if not (kirbyPos[1] + 1 > 14) and currentNode.getState()[kirbyPos[0], kirbyPos[1] + 1] != 1:
        son = Node(currentNode.getState(), currentNode,
                   "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                   currentNode.getFlower())

        right = rightMovement(kirbyPos)
        son.setNewCost(right)
        son.setKirbyPos(right)
        son.moveRight(kirbyPos)
        if son.avoidGoBack2(right) and son.compareCircles2(right):
            possible_moves.append(son)

    # Check if left side is free
    if not (kirbyPos[1] - 1 < 0) and currentNode.getState()[kirbyPos[0], kirbyPos[1] - 1] != 1:
        son = Node(currentNode.getState(), currentNode,
                   "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                   currentNode.getFlower())

        left = leftMovement(kirbyPos)
        son.setNewCost(left)
        son.setKirbyPos(left)
        son.moveLeft(kirbyPos)
        if son.avoidGoBack2(left) and son.compareCircles2(left):
            possible_moves.append(son)

    # Check if downside is free
    if not (kirbyPos[0] + 1 > 14) and currentNode.getState()[kirbyPos[0] + 1, kirbyPos[1]] != 1:
        son = Node(currentNode.getState(), currentNode,
                   "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                   currentNode.getFlower())

        down = downMovement(kirbyPos)
        son.setNewCost(down)
        son.setKirbyPos(down)
        son.moveDown(kirbyPos)
        if son.avoidGoBack2(down) and son.compareCircles2(down):
            possible_moves.append(son)

    # Check if upside is free
    if not (kirbyPos[0] - 1 < 0) and currentNode.getState()[kirbyPos[0] - 1, kirbyPos[1]] != 1:
        son = Node(currentNode.getState(), currentNode,
                   "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(),
                   currentNode.getFlower())

        up = upMovement(kirbyPos)
        son.setNewCost(up)
        son.setKirbyPos(up)
        son.moveUp(kirbyPos)
        if son.avoidGoBack2(up) and son.compareCircles2(up):
            possible_moves.append(son)

    return possible_moves
