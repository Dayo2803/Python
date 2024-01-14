import math

def paint(height, width, cover):
    area = height * width
    number_cans = math.ceil(area / cover)
    print(f"You will need {number_cans} cans of paint")
wall_h = int(input("Height of wall: "))
wall_w = int(input("Width of wall: "))
cov_can = 5
paint(height=wall_h, width=wall_w, cover=cov_can)