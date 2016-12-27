import psutil
import RPi.GPIO as GPIO
import time

from lcd import LCD

if __name__ == '__main__':
  lcd = LCD(LCD_RS=18, LCD_E=23, LCD_D4=24, LCD_D5=25, LCD_D6=8, LCD_D7=7)
  try:
    while True:
      line1="CPU: %s%%" % psutil.cpu_percent()
      line2="Free Mem: %sMb" % (psutil.virtual_memory().free / 1048576)
      lcd.show(line1, line2)
      time.sleep(1)
  except KeyboardInterrupt:
    pass
  finally:
    lcd.show("")
    GPIO.cleanup()
