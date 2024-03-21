import pygame
from algorithms.DFSAlgorithm import DFS
from algorithms.BFSAlgorithm import BFS
from algorithms.costAlgorithm import CostAlgorithm
from algorithms.greedyAlgorithm import GreedyAlgorithm
from algorithms.starAlgorithm import StarAlgorithm
import sys

BLACK = (0, 0, 0)
YELLOW = (255, 205, 104)
WHITE = (255, 255, 255)  # FREE 0
BROWN = (139, 69, 19)  # BLOCK 1
# Set the length and width of each grid cell.
LENGTHCELL = 30
HIGHCELL = 30
# Set the margin between the cells.
MARGIN = 3
algorithm = None


class Interface:

    def __init__(self, initWorld):
        self.__initWorld = initWorld
        self.__solutionWorlds = None
        self.__imgKirby = None
        self.__imgKoopa = None
        self.__imgWandana = None
        self.__imgStar = None
        self.__imgFlower = None
        self.__imgKirby = None
        


    def setSolutionWorld(self, newSolutionWorlds):
        self.__solutionWorlds = newSolutionWorlds

    def loadImages(self):
        self.__imgKirby = pygame.image.load("images/kirby.png").convert()
        self.__imgKoopa = pygame.image.load("images/koopa.png").convert()
        self.__imgWandana = pygame.image.load(
            "images/wandana.png").convert()
        self.__brown_brick = pygame.image.load("images/brown_brick.png").convert()
        self.__imgStar = pygame.image.load("images/star.jpg").convert()
        self.__imgFlower = pygame.image.load("images/flower.png").convert()
        self.__imgKirby = pygame.image.load(
            "images/kirby.png").convert()
        

    def showText(self, screen, text, color, size, x, y):
        
        font = pygame.font.Font("font/font.ttf", 25)
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.center = (x, y)

        screen.blit(surface, rect)

    def showComputingTime(self, screen, algorithm):
        computingTime = algorithm.getComputingTime()
        self.showText(screen, computingTime, WHITE, 35, 655, 230)

    def interfaceSolution(self, press, grid, i, screen, clock):
        while not press:
            # Test for button
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Draw the grid
            for row in range(15):
                for column in range(15):
                    if (grid[row, column] != 1 and grid[row, column] != 2 and grid[row, column] != 5 and grid[row, column] != 3 and grid[row, column] != 4 and grid[row, column] != 6):
                        color = WHITE
                        pygame.draw.rect(screen,
                                         color,
                                         [(MARGIN+LENGTHCELL) * column + MARGIN,
                                          (MARGIN+HIGHCELL) *
                                          row + MARGIN,
                                          LENGTHCELL,
                                          HIGHCELL])
                    if grid[row, column] == 1: 
                        resized_image = pygame.transform.scale(
                        self.__brown_brick, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])
                        
                    if grid[row, column] == 2:

                        resized_image = pygame.transform.scale(
                            self.__imgKirby, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])
                    if grid[row, column] == 5:

                        resized_image = pygame.transform.scale(
                            self.__imgKoopa, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])
                    if grid[row, column] == 3:

                        resized_image = pygame.transform.scale(
                            self.__imgStar, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])
                    if grid[row, column] == 4:

                        resized_image = pygame.transform.scale(
                            self.__imgFlower, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])
                    if grid[row, column] == 6:
                        resized_image = pygame.transform.scale(
                            self.__imgWandana, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])
                    if grid[row, column] == 8:
                        resized_image = pygame.transform.scale(
                            self.__imgKirby, (30, 30))
                        screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                    (MARGIN+HIGHCELL) *
                                                    row + MARGIN,
                                                    LENGTHCELL,
                                                    HIGHCELL])

            # Limit to 1 frames per second
            clock.tick(1.5)

            # Check that the length is not exceeded
            if (not (i >= len(self.__solutionWorlds))):
                # Update world
                grid = self.__solutionWorlds[i]
                
                i += 1
            elif (i == len(self.__solutionWorlds)):
                sound_background = pygame.mixer.Sound("music/background.wav")
                pygame.mixer.Sound.play(sound_background)
                i += 1
                press = True

            # Advance and update the screen with what we have drawn
            pygame.display.flip()

    def showInterface(self):
        # Initialize pygame
        pygame.init()

        # Initialize music
        pygame.mixer.init()
        pygame.mixer.music.load("music/backgroundMusic.mp3")
        pygame.mixer.music.play(-1)
        # Set the length and width of the screen
        WINDOW_DIMENSION = [800, 510]
        
        screen = pygame.display.set_mode(WINDOW_DIMENSION)

        # Iterate until the user presses the exit button
        press = False

        # Use it to set how fast the screen refreshes
        clock = pygame.time.Clock()

        i = 1
        self.loadImages()
        
        grid = self.__initWorld

        # Set the screen background
        screen.fill(BLACK)

        pygame.display.set_caption("Kirby smart")

        self.showCaptions(screen)

        for row in range(15):
            for column in range(15):
                if (grid[row, column] != 1 and grid[row, column] != 2 and grid[row, column] != 5 and grid[row, column] != 3 and grid[row, column] != 4 and grid[row, column] != 6):
                    color = WHITE
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN+LENGTHCELL) * column + MARGIN,
                                      (MARGIN+HIGHCELL) * row + MARGIN,
                                      LENGTHCELL,
                                      HIGHCELL])
                if grid[row, column] == 1:
                
                    resized_image = pygame.transform.scale(
                        self.__brown_brick, (30, 30))
                    
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
                    
                if grid[row, column] == 2:
                    resized_image = pygame.transform.scale(
                        self.__imgKirby, (30, 30))
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
                if grid[row, column] == 5:

                    resized_image = pygame.transform.scale(
                        self.__imgKoopa, (30, 30))
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
                if grid[row, column] == 3:

                    resized_image = pygame.transform.scale(
                        self.__imgStar, (30, 30))
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
                if grid[row, column] == 4:

                    resized_image = pygame.transform.scale(
                        self.__imgFlower, (30, 30))
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
                if grid[row, column] == 6:

                    resized_image = pygame.transform.scale(
                        self.__imgWandana, (30, 30))
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
                if grid[row, column] == 8:
                    resized_image = pygame.transform.scale(
                        self.__imgKirby, (30, 30))
                    screen.blit(resized_image, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                (MARGIN+HIGHCELL) *
                                                row + MARGIN,
                                                LENGTHCELL,
                                                HIGHCELL])
        pygame.display.flip()
        # Main Program Loop
        
        while not press:
            # Test for button
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 598 and pos[0] < 713 and pos[1] > 8 and pos[1] < 29:
                        print("Amplitude")
                        screen.fill(BLACK)
                        self.showCaptions(screen)
                        pygame.display.set_caption("Kirby smart amplitude")
                        
                        self.showText(screen, "Amplitude", YELLOW, 35, 655, 20)
                        algorithm = BFS(self.__initWorld)
                        solution = algorithm.start()
                        solutionWorld = solution[0]
                        nodeExpanded = solution[1]
                        depth = solution[2]
                        self.showComputingTime(screen, algorithm)
                        self.showText(screen, str(nodeExpanded), WHITE, 35, 655, 295)
                        self.setSolutionWorld(solutionWorld)
                        self.showText(screen,  str(depth), WHITE, 35, 655, 355)
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 581 and pos[0] < 732 and pos[1] > 42 and pos[1] < 62:
                        print("Depth")
                        screen.fill(BLACK)
                        self.showCaptions(screen)
                        pygame.display.set_caption("Kirby smart depth")
                        self.showText(screen, "Depth", YELLOW, 35, 655, 50)
                        algorithm = DFS(self.__initWorld)
                        solution = algorithm.start()
                        solutionWorld = solution[0]
                        nodeExpanded = solution[1]
                        depth = solution[2]
                        self.showComputingTime(screen, algorithm)
                        self.showText(screen,   str(nodeExpanded), WHITE, 35, 655, 295)
                        self.showText(screen,   str(depth), WHITE, 35, 655, 355)
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 618 and pos[0] < 692 and pos[1] > 70 and pos[1] < 90:
                        print("Cost")
                        screen.fill(BLACK)
                        self.showCaptions(screen)
                        pygame.display.set_caption("Kirby smart cost")
                        self.showText(screen,   "Cost", YELLOW, 35, 655, 80)
                        algorithm = CostAlgorithm(self.__initWorld)
                        solution = algorithm.start()
                        solutionWorld = solution[0]
                        nodeExpanded = solution[1]
                        depth = solution[2]
                        self.showComputingTime(screen, algorithm)
                        self.showText(screen,   str(nodeExpanded), WHITE, 35, 655, 295)
                        self.showText(screen,   str(depth), WHITE, 35, 655, 355)
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 619 and pos[0] < 692 and pos[1] > 101 and pos[1] < 123:
                        print("Greedy")
                        screen.fill(BLACK)
                        self.showCaptions(screen)
                        pygame.display.set_caption("Kirby smart greedy")
                        self.showText(screen,   "Greedy", YELLOW, 35, 655, 110)
                        algorithm = GreedyAlgorithm(self.__initWorld)
                        solution = algorithm.start()
                        solutionWorld = solution[0]
                        nodeExpanded = solution[1]
                        depth = solution[2]
                        self.showComputingTime(screen, algorithm)
                        self.showText(screen,   str(nodeExpanded), WHITE, 35, 655, 295)
                        self.showText(screen,   str(depth), WHITE, 35, 655, 355)
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 641 and pos[0] < 692 and pos[1] > 130 and pos[1] < 153:
                        print("A*")
                        screen.fill(BLACK)
                        self.showCaptions(screen)
                        pygame.display.set_caption("Kirby smart A*")               
                        self.showText(screen,   "A*", YELLOW, 35, 655, 140)
                        algorithm = StarAlgorithm(self.__initWorld)
                        solution = algorithm.start()
                        solutionWorld = solution[0]
                        nodeExpanded = solution[1]
                        depth = solution[2]
                        self.showComputingTime(screen, algorithm)
                        self.showText(screen,   str(nodeExpanded), WHITE, 35, 655, 295)
                        self.showText(screen,   str(depth), WHITE, 35, 655, 355)
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    print(pos[0])
                    print(pos[1])

    def showCaptions(self, screen):
        
        self.showText(screen, "Amplitude", WHITE, 35, 655, 20)

        self.showText(screen, "Depth", WHITE, 35, 655, 50)

        self.showText(screen,  "Cost", WHITE, 35, 655, 80)

        self.showText(screen, "Greedy", WHITE, 35, 655, 110)

        self.showText(screen,"A*", WHITE, 35, 655, 140)

        self.showText(screen,"Computing time: ", WHITE, 35, 655, 200)

        self.showText(screen,"#Expanded nodes: ", WHITE, 35, 655, 265)

        self.showText(screen,"Depth: ", WHITE, 35, 655, 325)
