#-*- coding: utf-8 -*-
import pyautogui as pag

#GUI操作ごとのポーズ秒数
pag.PAUSE = 2.5
x, y = (300, 300)
pag.moveTo(x, y)
print("moveTo メソッドでマウス位置{0}に移動".format((x, y)))
print("画面上にマウス位置は「{0}」"
    .format("ある" if pag.onScreen(x, y) else "ない"))
print("positionメソッドの返り値: {0}".format(pag.position()))

x, y = (1000000, 1000000)
print("moveTo メソッドでマウス位置{0}に移動".format((x, y)))
pag.moveTo(x, y)
print(" 画面上にマウス位置は「{0}」"
    .format("ある" if pag.onScreen(x, y) else "ない"))
print("position メソッドの返り値: {0}".format(pag.position()))
