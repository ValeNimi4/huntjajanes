def rp(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
import pygame
import os
import sys
import pygame_gui
from random import randint
while True:
    exec(open(rp("hunt-ja-janes.py"), "r", encoding="utf-8").read())
    if STOPP:
        break 