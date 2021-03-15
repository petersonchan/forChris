class mahjong:
    def __init__(self, tag, index_of_mj):
        self.tag = tag
        img = cv2.imread("mahjong2x.jpg")
        row = int((index_of_mj - index_of_mj % 17) / 17)
        column = index_of_mj % 17
        self.image = img[initial_point_y + mj_height*row: initial_point_y + mj_height*(row+1), initial_point_x + mj_width*column:initial_point_x + mj_width*(column+1)]

    def show_image(self):
        cv2.imshow('image',self.image)


import cv2
import numpy as np
import random


mj_height = 86
mj_width = 58
initial_point_x = 35
initial_point_y = 183

mahjong_list = []
mahjong_tag = ['4p','fai','7s','4p','north','4m','1p','3p','south','5s','6m','3m','3s','8m','chong','6m','5p',
               '5p','1p','4s','chong','6s','9p','white','9m','3p','7p','2p','west','3s','1m','6m','7s','4p',
               '4m','white','8s','6p','west','2s','8s','9s','chong','7m','2m','north','4p','7p','5p','7p','east',
               '6p','fai','1p','8m','4s','5s','1s','2s','9p','9m','4s','5m','east','8s','3m','7s','1m',
               '6s','1s','6p','1s','2m','8s','1m','3p','7s','6s','fai','7m','8p','5m','4s','south','7m',
               '9s','3m','1s','north','8p','9m','9m','east','chong','3s','5m','7p','6p','2p','white','3p','east',
               '5m','1m','6s','1p','2m','west','3m','9s','2m','fai','6m','8p','south','fai','west','3s','8m',
               'south','4m','white','9s','2p','2s','9p','2p','5p','9p','7m','5s','north','5s','8p','2s','8m']

for i in range(136): #0 to 135
    mahjong_list.append(mahjong(mahjong_tag[i],i))

################On Hand & River Generation###################
num_of_total_observed_mahjong = random.randint(14,137)
total_observed_mahjong = random.sample(range(136), num_of_total_observed_mahjong)
print(total_observed_mahjong)

on_hand_mahjong = []
river_mahjong = []

for i in range(13):
    on_hand_mahjong.append(mahjong_list[total_observed_mahjong[i]].image)
tuple(on_hand_mahjong)
on_hand_mahjong_img = np.hstack(on_hand_mahjong)

for i in range(14,len(total_observed_mahjong)):
    river_mahjong.append(mahjong_list[total_observed_mahjong[i]].image)
tuple(river_mahjong)
river_mahjong_img = np.hstack(river_mahjong)

##########################################################

cv2.imshow('On Hand', on_hand_mahjong_img)
cv2.imshow('River', river_mahjong_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




