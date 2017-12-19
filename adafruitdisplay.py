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
  message = sys.argv[1]+"\n"
  message = message.replace("{", "\n")
  if len(sys.argv) >= 3:
    count = int(sys.argv[2]) % 10
    count = abs(count - 5)
    for dummy in range(count):
      message += " "
    if len(sys.argv) == 3:
      message += "."
    else:
      message += "*"
  lcd.message(message)
else:
  for line in sys.stdin.readlines():
    lcd.message(line)
