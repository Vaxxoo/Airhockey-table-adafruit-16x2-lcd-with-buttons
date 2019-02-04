#!usr/bin/python
# Example using a character LCD plate.


import time
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# buttons(	(LCD.select,	select)
# 			(LCD.Right,		right)
# 			(LCD.Down, 		down)
# 			(LCD.Up, 		up)
# 			(LCD.Left, 		left))

select, right, down, up, left = (LCD.select, LCD.Right, LCD.Down, LCD.Up, LCD.Left)
button = (select, right, down, up, left)

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
            if lcd.is_pressed(button[0]):
                if (button[1]) == select:
                    part += 1
                # To continue to part2
                if (button[1]) == up:

                    lcd.noblink
                    x += 1
                    cc = ord(x)
                    x_2 = cc

                    if x_2 > 90:
                        x_2 -= 25
                    # For moving from Z to A
                    lcd.message(chr(x_2))
                # moving the characters up 1 (A, B, C....)
                if (button[1]) == down:

                    lcd.noblink
                    x -= 1
                    cc = ord(x)
                    x_2 = cc

                    if x_2 < 65:
                        x_2 += 25

                    # For moving from A to Z
                    lcd.message(chr(x_2))
                # moving the characters down 1 Z, X, Y....)
                if (button[1]) == left:
                    remove(x_2)
                    lcd.move_left
                    x = 65
                # moving the editable character to the left
                if (button[1]) == right:
                    append(x_2)
                    lcd.move_right
                    x = 65

        # moving the editable character to the right
        # Part 2
        # This part is for the name of player2
        if part == 2:
            if lcd.is_pressed(button[0]):
                if (button[1]) == select:
                    part += 1
                # To continue to the next part (visualis the names)

                if (button[1]) == up:

                    lcd.noblink
                    y += 1
                    cc = ord(y)
                    y_2 = cc

                    if y_2 > 90:
                        y_2 -= 25
                    # For moving from Z to A
                    lcd.message(chr(y_2))
                # moving the characters up 1 (A, B, C....)
                if (button[1]) == down:

                    lcd.noblink
                    y -= 1
                    cc = ord(y)
                    y_2 = cc

                    if y_2 < 65:
                        y_2 += 25
                    # For moving from A to Z
                    lcd.message(chr(y_2))
                # moving the characters down 1 (Z, X, Y....)
                if (button[1]) == left:
                    remove(y_2)
                    lcd.move_left
                    y = 65
                # moving the editable character to the left
                if (button[0]) == right:
                    append(y_2)
                    lcd.move_right
                    y = 65
        # moving the editable character to the right
        # Part 3
        # This part is for displaying the first 7 Characters of the names   (16/2=8  8-1=7 (this is for the spacing between the names) )
        if part == 3:
            # Here must go the array to display the first and the second name
            pass
