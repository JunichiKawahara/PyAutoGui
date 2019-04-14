#-*- coding: utf-8 -*-

import pyautogui as pag

"""
t04_mouseMoveTo.py
p.154
Copyright (C) 2019 J.Kawahara
2019.4.14 J.Kawahara 新規作成
"""

# マウスの移動（絶対座標）
# moveTo(X, Y, Sec, Toween)

def print_position(pag):
    print("position{0}".format(pag.position()))


pag.PAUSE = 2.5

# マウスの移動
pag.moveTo(100, 100)
print_position(pag)

# 2秒かけて移動
pag.moveTo(200, 200, 2)
print_position(pag)

# 3.5秒かけてXのみ移動
pag.moveTo(500, None, 3.5)
print_position(pag)

# 定義されている移動時間の最小値
print("pyautogui.MINIMUM_DURATION: {0}".format(pag.MINIMUM_DURATION))

# Yのみ移動。移動時間を最小値未満にした場合は最小値になる
pag.moveTo(None, 500, 0.005)

# 開始は遅く、終了は早く
print("pyautogui.easeInQuad")
pag.moveTo(None, 100, 5, pag.easeInQuad)

# 開始は早く、終了は遅く
print("pyautogui.easeOutQuad")
pag.moveTo(100, None, 5, pag.easeOutQuad)

# 開始と終了は早く、途中は遅い
print("pyautogui.easeInOutQuad")
pag.moveTo(None, 500, 5, pag.easeInOutQuad)

# 終了の時にバウンドする
print("pyautogui.easeInBounce")
pag.moveTo(500, None, 5, pag.easeInBounce)

# 終了の時に輪ゴムを伸ばして離したような動き
print("pyautogui.easeInElastic")
pag.moveTo(100, 100, 5, pag.easeInElastic)
