import pygame, random
from structures import *
from entities import *

#ROAD PARAMATERS: Position and Orientation

#CAR PARAMETERS: Position and Orientation

def level(level):
    roads = pygame.sprite.Group()
    cars = pygame.sprite.Group()
    lights = pygame.sprite.Group()
    intersections = pygame.sprite.Group()
    buildings = pygame.sprite.Group()
    objectives = {}
    if level == "freeplay":
        objectives = {"objective": "freeplay", "amount": "freeplay", "time": "freeplay", "tod": 6}
        roads.add(road([170, 0], "vertical"))
        roads.add(road([570, 0], "vertical"))
        roads.add(road([0, 170], "horizontal"))
        roads.add(road([0, 370], "horizontal"))
        intersections.add(intersection([170, 170]))
        intersections.add(intersection([570, 170]))
        intersections.add(intersection([170, 370]))
        intersections.add(intersection([570, 370]))
        lights.add(light([170, 150], "vertical", False, 1))
        lights.add(light([570, 150], "vertical", False, 2))
        lights.add(light([150, 170], "horizontal", False, 3))
        lights.add(light([550, 170], "horizontal", False, 4))
        #up
        lights.add(light([170, 350], "vertical", False, 5))
        lights.add(light([570, 350], "vertical", False, 6))
        lights.add(light([150, 370], "horizontal", False, 7))
        lights.add(light([550, 370], "horizontal", False, 8))
    if level == "survival":
        objectives = {"objective": "survival", "amount": "survival", "time": 0, "tod": 6}
        roads.add(road([170, 0], "vertical"))
        roads.add(road([570, 0], "vertical"))
        roads.add(road([0, 170], "horizontal"))
        roads.add(road([0, 370], "horizontal"))
        intersections.add(intersection([170, 170]))
        intersections.add(intersection([570, 170]))
        intersections.add(intersection([170, 370]))
        intersections.add(intersection([570, 370]))
        lights.add(light([170, 150], "vertical", False, 1))
        lights.add(light([570, 150], "vertical", False, 2))
        lights.add(light([150, 170], "horizontal", False, 3))
        lights.add(light([550, 170], "horizontal", False, 4))
        # up
        lights.add(light([170, 350], "vertical", False, 5))
        lights.add(light([570, 350], "vertical", False, 6))
        lights.add(light([150, 370], "horizontal", False, 7))
        lights.add(light([550, 370], "horizontal", False, 8))
    if level == 0:
        objectives = {"objective": "cars", "amount": 99, "time": 10, "tod": 14}
        roads.add(road([470, 0], "vertical"))
    if level == 1:
        objectives = {"objective": "cars", "amount": 15, "time": 120, "tod": 10}
        roads.add(road([370, 0], "vertical"))
        roads.add(road([0, 270], "horizontal"))
        lights.add(light([370, 250], "vertical", False, 1))
        lights.add(light([350, 270], "horizontal", False, 2))
        intersections.add(intersection([370, 270]))
    if level == 2:
        objectives = {"objective": "cars", "amount": 25, "time": 60, "tod": 12}
        roads.add(road([370, 0], "vertical"))
        roads.add(road([0, 370], "horizontal"))
        lights.add(light([370, 350], "vertical", False, 1))
        lights.add(light([370, 150], "vertical", False, 2))
        lights.add(light([350, 370], "horizontal", False, 3))
        lights.add(light([350, 170], "horizontal", False, 4))
        roads.add(road([0, 170], "horizontal"))
        intersections.add(intersection([370, 370]))
        intersections.add(intersection([370, 170]))
    if level == 3:
        objectives = {"objective": "cars", "amount": 30, "time": 45, "tod": 13}
        roads.add(road([170, 0], "vertical"))
        roads.add(road([570, 0], "vertical"))
        roads.add(road([0, 270], "horizontal"))
        lights.add(light([170, 250], "vertical", False, 1))
        lights.add(light([570, 250], "vertical", False, 2))
        lights.add(light([150, 270], "horizontal", False, 3))
        lights.add(light([550, 270], "horizontal", False, 4))
        intersections.add(intersection([170, 270]))
        intersections.add(intersection([570, 270]))
    if level == 4:
        objectives = {"objective": "cars", "amount": 40, "time": 60, "tod": 14}
        roads.add(road([0, 120], "horizontal"))
        roads.add(road([0, 420], "horizontal"))
        roads.add(road([170, 0], "vertical"))
        roads.add(road([570, 0], "vertical"))
        intersections.add(intersection([170, 120]))
        intersections.add(intersection([570, 420]))
        intersections.add(intersection([170, 420]))
        intersections.add(intersection([570, 120]))
        lights.add(light([170, 100], "vertical", False, 1))
        lights.add(light([170, 100], "vertical", False, 2))
        lights.add(light([150, 120], "horizontal", False, 3))
        lights.add(light([150, 120], "horizontal", False, 4))
        lights.add(light([170, 400], "vertical", False, 1))
        lights.add(light([170, 400], "vertical", False, 2))
        lights.add(light([150, 420], "horizontal", False, 3))
        lights.add(light([150, 420], "horizontal", False, 4))
        lights.add(light([570, 100], "vertical", False, 1))
        lights.add(light([570, 100], "vertical", False, 2))
        lights.add(light([550, 120], "horizontal", False, 3))
        lights.add(light([550, 120], "horizontal", False, 4))
        lights.add(light([570, 400], "vertical", False, 1))
        lights.add(light([570, 400], "vertical", False, 2))
        lights.add(light([550, 420], "horizontal", False, 3))
        lights.add(light([550, 420], "horizontal", False, 4))
    if level == 5:
        objectives = {"objective": "crashes", "amount": 10, "time": 60, "tod": 15}
        roads.add(road([0, 270], "horizontal"))
        roads.add(road([300, 0], "vertical"))
        roads.add(road([500, 0], "vertical"))
        intersections.add(intersection([300, 270]))
        intersections.add(intersection([500, 270]))
        lights.add(light([300, 250], "vertical", False, 1))
        lights.add(light([500, 250], "vertical", False, 2))
        lights.add(light([280, 270], "horizontal", False, 3))
        lights.add(light([480, 270], "horizontal", False, 4))
    if level == 6:
        objectives = {"objective": "crashes", "amount": 10, "time": 90, "tod": 16}
        roads.add(road([370, 0], "vertical"))
        roads.add(road([0, 180], "horizontal"))
        roads.add(road([0, 360], "horizontal"))
        intersections.add(intersection([370, 360]))
        intersections.add(intersection([370, 180]))
        lights.add(light([350, 180], "horizontal", False, 3))
        lights.add(light([350, 360], "horizontal", False, 4))
    if level == 7:
        objectives = {"objective": "crashes", "amount": 7, "time": 120, "tod": 17}
        roads.add(road([370, 0], "vertical"))
        roads.add(road([550, 0], "vertical"))
        roads.add(road([150, 0], "vertical"))
        roads.add(road([0, 270], "horizontal"))
        intersections.add(intersection([370, 270]))
        intersections.add(intersection([550, 270]))
        intersections.add(intersection([150, 270]))
        lights.add(light([350, 270], "horizontal", False, 3))
        lights.add(light([530, 270], "horizontal", False, 4))
        lights.add(light([130, 270], "horizontal", False, 4))
        lights.add(light([550, 250], "vertical", False, 4))
        lights.add(light([150, 250], "vertical", False, 4))
    if level == 8:
        objectives = {"objective": "crashes", "amount": 5, "time": 180, "tod": 19}
        roads.add(road([180, 0], "vertical"))
        roads.add(road([540, 0], "vertical"))
        roads.add(road([0, 180], "horizontal"))
        roads.add(road([0, 360], "horizontal"))
        intersections.add(intersection([180, 180]))
        intersections.add(intersection([540, 180]))
        intersections.add(intersection([180, 360]))
        intersections.add(intersection([540, 360]))
        lights.add(light([160, 180], "horizontal", False, 3))
        lights.add(light([520, 180], "horizontal", False, 4))
        lights.add(light([160, 360], "horizontal", False, 4))
        lights.add(light([520, 360], "horizontal", False, 4))
    if level == 10:
        objectives = {"objective": "anger", "amount": 10, "time": 150, "tod": 0}
        roads.add(road([180, 0], "vertical"))
        roads.add(road([300, 0], "vertical"))
        roads.add(road([420, 0], "vertical"))
        roads.add(road([540, 0], "vertical"))
        roads.add(road([0, 180], "horizontal"))
        roads.add(road([0, 360], "horizontal"))
        intersections.add(intersection([180, 180]))
        intersections.add(intersection([300, 180]))
        intersections.add(intersection([420, 180]))
        intersections.add(intersection([540, 180]))
        intersections.add(intersection([180, 360]))
        intersections.add(intersection([300, 360]))
        intersections.add(intersection([420, 360]))
        intersections.add(intersection([540, 360]))

    return roads, cars, lights, intersections, buildings, objectives