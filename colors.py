import numpy as np


lower_white = np.array([0, 0, 210])
upper_white = np.array([179, 55, 255])

lower_yellow = np.array([20, 55, 0])
upper_yellow = np.array([45, 255, 255])

lower_orange = np.array([0, 80, 170])
upper_orange = np.array([25, 255, 255])

lower_green = np.array([50, 80, 220])
upper_green = np.array([80, 230, 255])

lower_blue = np.array([85, 90, 0])
upper_blue = np.array([120, 200, 255])

# lower_red = np.array([156, 234, 0])
# upper_red = np.array([179, 255, 255])

lower_red1 = np.array([160, 100, 170])
upper_red1 = np.array([179, 255, 255])

lower_red2 = np.array([0, 100, 50])
upper_red2 = np.array([10, 255, 255])


pieces_colors = {
    1: 'W',
    2: 'R',
    3: 'G',
    4: 'Y',
    5: 'O',
    6: 'B'
}

rgb_colors = {
    1: (255, 255, 255),
    2: (0, 0, 255),
    3: (0, 255, 0),
    4: (0, 255, 255),
    5: (0, 140, 255),
    6: (255, 0, 0)
}

kociemba_colors = {
    1: 'U',
    2: 'R',
    3: 'F',
    4: 'D',
    5: 'L',
    6: 'B'
}

