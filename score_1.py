#!usr/bin/python
# Example using a character adaLCD plate.


import time
import Adafruit_CharLCD as adaLCD

# Initialize the adaLCD using the pins
lcd = adaLCD.Adafruit_CharLCDPlate()
lcd.blink(False)

# buttons(	(adaLCD.select,	select)
# 			(adaLCD.Right,		right)
# 			(adaLCD.Down, 		down)
# 			(adaLCD.Up, 		up)
# 			(adaLCD.Left, 		left))

select, right, down, up, left = (adaLCD.SELECT, adaLCD.RIGHT, adaLCD.DOWN, adaLCD.UP, adaLCD.LEFT)

cc = None
x = 65
y = 65
y_2 = None
x_2 = None
cycle = True

while cycle:
    part = 1
    while True:
        # Part 1
        # This part is for the name of player1
        if part == 1:
            if lcd.is_pressed(select):
                part += 1

            # To continue to part2
            if lcd.is_pressed(up):
                x += 1
                cc = ord(x)
                x_2 = cc

                if x_2 > 90:
                    x_2 -= 25
                # For moving from Z to A
                lcd.message(chr(x_2))

            # moving the characters up 1 (A, B, C....)
            if lcd.is_pressed(down):
                x -= 1
                cc = ord(x)
                x_2 = cc

                if x_2 < 65:
                    x_2 += 25

                # For moving from A to Z
                lcd.message(chr(x_2))

            # moving the characters down 1 Z, X, Y....)
            if lcd.is_pressed(left):
                lcd.move_left()
                x = 65

            # moving the editable character to the left
            if lcd.is_pressed(right):
                lcd.move_right()
                x = 65

        # moving the editable character to the right
        # Part 2
        # This part is for the name of player2
        if part == 2:
            if lcd.is_pressed(select):
                part += 1

            # To continue to the next part (visualise the names)
            if lcd.is_pressed(up):
                y += 1
                cc = ord(y)
                y_2 = cc

                if y_2 > 90:
                    y_2 -= 25
                # For moving from Z to A
                lcd.message(chr(y_2))

            # moving the characters up 1 (A, B, C....)
            if lcd.is_pressed(down):
                y -= 1
                cc = ord(y)
                y_2 = cc

                if y_2 < 65:
                    y_2 += 25
                # For moving from A to Z
                lcd.message(chr(y_2))

            # moving the characters down 1 (Z, X, Y....)
            if lcd.is_pressed(left):
                lcd.move_left()
                y = 65

            # moving the editable character to the left
            if lcd.is_pressed(right):
                lcd.move_right()
                y = 65

        # moving the editable character to the right Part 3
        # This part is for displaying the first 7 Characters of the
        # names   (16/2=8  8-1=7 (this is for the spacing between the names) ) 
        if part == 3:
            # Here must go the array to display the first and the second name
            pass
