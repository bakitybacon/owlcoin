#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD
import sys

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()

if(len(sys.argv) > 1):
	lcd.message(sys.argv[1])
else:
	lcd.message(sys.stdin.readlines()[0])
