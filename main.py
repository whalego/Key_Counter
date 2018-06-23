# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
from pyhooked import Hook,KeyboardEvent
import threading
import csv
import os

SCREEN_SIZE = (500, 500)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(u'counter')


ID_TO_COUNT = {'Back':0,
'Tab':0,
'Return':0,
'Capital':0,
'Escape':0,
'Space':0,
'Prior':0,
'Next':0,
'End':0,
'Home':0,
'Left':0,
'Up':0,
'Right':0,
'Down':0,
'PrtScr':0,
'Delete':0,
'0':0,
'1':0,
'2':0,
'3':0,
'4':0,
'5':0,
'6':0,
'7':0,
'8':0,
'9':0,
'A':0,
'B':0,
'C':0,
'D':0,
'E':0,
'F':0,
'G':0,
'H':0,
'I':0,
'J':0,
'K':0,
'L':0,
'M':0,
'N':0,
'O':0,
'P':0,
'Q':0,
'R':0,
'S':0,
'T':0,
'U':0,
'V':0,
'W':0,
'X':0,
'Y':0,
'Z':0,
'Lwin':0,
'Rwin':0,
'App':0,
'Sleep':0,
'Numpad0':0,
'Numpad1':0,
'Numpad2':0,
'Numpad3':0,
'Numpad4':0,
'Numpad5':0,
'Numpad6':0,
'Numpad7':0,
'Numpad8':0,
'Numpad9':0,
'Multiply':0,
'Add':0,
'Subtract':0,
'Decimal':0,
'Divide':0,
'F1':0,
'F2':0,
'F3':0,
'F4':0,
'F5':0,
'F6':0,
'F7':0,
'F8':0,
'F9':0,
'F10':0,
'F11':0,
'F12':0,
'Numlock':0,
'Lshift':0,
'Rshift':0,
'Lcontrol':0,
'Rcontrol':0,
'Lmenu':0,
'Rmenu':0,
'Oem_1':0,
'Oem_Plus':0,
'Oem_Comma':0,
'Oem_Minus':0,
'Oem_Period':0,
'Oem_2':0,
'Oem_3':0,
'Oem_4':0,
'Oem_5':0,
'Oem_6':0,
'Oem_7':0,
'Ctrl':0,
'Alt':0,
'Shift':0,
'Win':0,
}

class MainWindow():

    def __init__(self):

        if os.path.isfile('./file.csv'): self.CSV_Setter()

        hk = Hook()
        hk.handler = self.Handle_Events
        thread = threading.Thread(target=hk.hook)
        thread.setDaemon(True)
        thread.start()

        while True:
            pygame.display.update()
            screen.fill((100, 100, 100))

            call_count = 0

            for key, value in ID_TO_COUNT.items():
                keyAndValue = str(key) + ' : ' + str(value)
                call_count = call_count + 1
                self.Txt_Label(keyAndValue, call_count)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.CSV_Writer()
                    sys.exit()

    def Txt_Label(self, text, row):
        sysFont = pygame.font.SysFont(None, 18)
        label = sysFont.render(text, True, (0, 0, 0))
        column = 0

        if row > 80:
            column = 300
            row = row - 80

        elif row > 40:
            column = 150
            row = row - 40

        screen.blit(label, (20 + column,  5 + row * 11.5))

    def Handle_Events(self, args):
        if args.event_type == 'key up':
            self.Counter(args.current_key)

    def Counter(self, code):
        for codeKey, codeValue in ID_TO_COUNT.items():
            if codeKey == code:
                ID_TO_COUNT[codeKey] = int(ID_TO_COUNT[codeKey]) + 1
                #print (codeKey,codeValue)

    def CSV_Setter(self):
        with open('file.csv', newline='', encoding='utf-8') as csvFile:
            csvReader = csv.DictReader(csvFile)

            for row in csvReader:
                for codeKey, codeValue in ID_TO_COUNT.items():
                    if row['Key'] == codeKey:
                        ID_TO_COUNT[codeKey] = row['Code']


    def CSV_Writer(self):
        with open('file.csv', 'w', newline='', encoding='utf-8') as csvFile:
            fieldNames = ['Key', 'Code']
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldNames)
            csvWriter.writeheader()

            for key, value in ID_TO_COUNT.items():
                csvWriter.writerow({'Key': key, 'Code': value})


if __name__ == '__main__':
    w = MainWindow()
    w.show()
