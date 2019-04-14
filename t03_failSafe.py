#-*- coding: utf-8 -*-

import pyautogui as pag

pag.PAUSE = 2.5

try:
    print("2.4秒以内にマウスカーソルを一番左上端に持って行ってください")
    pag.moveTo(100, 100)
    pag.moveTo(500, 500)
except pag.FailSafeException as e:
    # フェイルセーフ例外が発生した時の処理
    print("フェイルセーフ例外が発生しました")
    print(e)
