#-*- coding: utf-8 -*-

import pyautogui as pag

# 画面の解像度を表示する
print("解像度{0}".format(pag.size()))

# マウス位置を取得する
coord = pag.position()
print(type(coord))

print(coord)
