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
            print(get_mouth_sprite(value))
            strips.append(SpriteStripAnim('image/lips.png',get_mouth_sprite(value), 3, 1, False, queue["lapse"]))

    return strips

def get_mouth_sprite(value):
    if value == "A":
        return (0, 0, 155, 155)
    if value == "B":
        return (0, 155, 155, 155)
    if value == "C":
        return (0, 310, 155, 155)
    if value == "D":
        return (0, 0, 155, 155)
    if value == "E":
        return (0, 0, 155, 155)
    if value == "F":
        return (0, 0, 155, 155)
    if value == "G":
        return (0, 0, 155, 155)
    if value == "H":
        return (0, 0, 155, 155)
    if value == "X":
        return (0, 0, 155, 155)



# strips = [
#     SpriteStripAnim('image/lips.png', (0, 0,   155, 155), 3, 1, False, frames),
#     SpriteStripAnim('image/lips.png', (0, 155, 155, 155), 3, 1, False, frames)
#     # SpriteStripAnim('image/lips.png', (0, 310, 155, 155), 3, 1, True, frames),

# ]