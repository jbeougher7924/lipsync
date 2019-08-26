import numpy
import random
import json
from sprite_strip_anim import SpriteStripAnim

def get_mouthqueue_list(file):
    mouth_lapse = {}
    strips = []
    with open(file) as action_file:
        action_data = json.load(action_file)

        mouthQues_data = action_data["mouthCues"]

        for queue in mouthQues_data:
            value =  queue["value"]
            if len(strips) == 0:
                strips.append(SpriteStripAnim('image/lips.png', get_mouth_sprite(value), 1, 1, False, int(queue["lapse"] * 240)))
            else:
                # len(strips)
                strips[0] += (SpriteStripAnim('image/lips.png', get_mouth_sprite(value), 1, 1, False, int(queue["lapse"] * 240)))
            # strips.append(SpriteStripAnim('image/lips.png', get_mouth_sprite(value), count=1,colorkey=1, loop=False, frames=int(queue["lapse"] * 60)))
            # strips.append(SpriteStripAnim('image/lips.png', get_mouth_sprite(value), 1, 1, False, 10))
            # colorkey = None, loop = False, frames = 1


    return strips

def get_mouth_sprite(value):
    if value == "A":
        return (125, 310, 155, 155) #Done
    if value == "B":
        return (125, 125, 165, 155) #Done
    if value == "C":
        return (310, 0, 155, 155)
    if value == "D":
        return (0, 0, 155, 155)
    if value == "E":
        return (140, 0, 125, 125) #Done
    if value == "F":
        return (0, 310, 155, 155) #Done
    if value == "G":
        return (300, 300, 165, 155) #Done
    if value == "H":
        return (300, 125, 155, 155) #Done
    if value == "X":
        return (125, 310, 155, 155)  # Done



# strips = [
#     SpriteStripAnim('image/lips.png', (0, 0,   155, 155), 3, 1, False, frames),
#     SpriteStripAnim('image/lips.png', (0, 155, 155, 155), 3, 1, False, frames)
#     # SpriteStripAnim('image/lips.png', (0, 310, 155, 155), 3, 1, True, frames),

# ]
