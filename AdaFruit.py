from digitalio import DigitalInOut
from pulseio import PWMOut
from busio import I2C
import adafruit_character_lcd.character_lcd as charlcd
import adafruit_character_lcd.character_lcd_i2c as i2cmono
import adafruit_character_lcd.character_lcd_rgb_i2c as i2crgb


class ButtonController:
    def __init__(self, scl_pin, sda_pin):
        self.i2c = I2C(scl_pin, sda_pin)


class Display:
    def __init__(
            self,
            rows: int, columns: int,

            rs_pin: DigitalInOut,
            en_pin: DigitalInOut,
            d7_pin: DigitalInOut,
            d6_pin: DigitalInOut,
            d5_pin: DigitalInOut,
            d4_pin: DigitalInOut,

            colour_lcd: bool,
            i2c_enabled: bool,

            red_pin: PWMOut = None,
            green_pin: PWMOut = None,
            blue_pin: PWMOut = None,

            backlight_pin: DigitalInOut = None,

            button_controller: ButtonController = None
    ):
        """
        Create a Display object to simplify LCD operations.

        The pins need to be specified as following:
        digitalio.DigitalInOut( board.<PIN> )

        For colours:
        pulseio.PWMOut( board.<PIN> )

        If it's a colour LCD, the pins for RED, GREEN and BLUE must be specified. backlight_pin can remain None.
        If it's a mono LCD, the backlight pin has to be specified.

        :param rows: Amount of rows on the LCD.
        :param columns: Amount of columns on the LCD.
        :param rs_pin: Location where the RS pin is connected on the board.
        :param en_pin: Location where the EN pin is connected on the board.
        :param d7_pin: Location where the D7 pin is connected on the board.
        :param d6_pin: Location where the D6 pin is connected on the board.
        :param d5_pin: Location where the D5 pin is connected on the board.
        :param d4_pin: Location where the D4 pin is connected on the board.

        :param colour_lcd: Whether it's a colour display or not.
        :param i2c_enabled: Whether the screen has buttons or not.

        :param red_pin: Location where the RED pin is connected on the board.
        :param blue_pin: Location where the BLUE pin is connected on the board.
        :param green_pin: Location where the GREEN pin is connected on the board.

        :param backlight_pin: Location where the backlight pin is connected on the board.

        :param button_controller: A Button Controller class.
        """

        # Set a global variable for checking if it's a colour LCD or not.
        # Then set the colour tuple for a blue screen.
        self.is_colour_lcd = colour_lcd
        self.is_i2c = i2c_enabled
        self.colour = None
        self.set_colour(0, 0, 100)

        # Set a global variable with the dimensions
        self.dimensions = (columns, rows)

        if self.is_i2c:
            if self.is_colour_lcd:
                self.lcd = i2crgb.Character_LCD_RGB_I2C(
                    button_controller.i2c,
                    columns, rows
                )
            else:
                self.lcd = i2cmono.Character_LCD_I2C(
                    button_controller.i2c,
                    columns, rows
                )
        else:
            # Initialise the LCD screen (type depending on the type of screen).
            if self.is_colour_lcd:
                self.lcd = charlcd.Character_LCD_RGB(
                    rs_pin, en_pin, d4_pin, d5_pin, d6_pin, d7_pin,
                    columns, rows,
                    red_pin, blue_pin, green_pin
                )
            else:
                self.lcd = charlcd.Character_LCD_Mono(
                    rs_pin, en_pin, d4_pin, d5_pin, d6_pin, d7_pin,
                    columns, rows,
                    backlight_pin
                )

    def change_text(self, message: str, left_to_right: bool):
        """
        Change the text displayed on the screen. If the text is too long, move the screen as following:
        <Display>.lcd.move_left() and <Display>.lcd.move_right()

        :param message: The text to display.
        :param left_to_right: Display text from left to right, or not.
        """

        # Set text direction
        if left_to_right:
            self.lcd.text_direction = self.lcd.LEFT_TO_RIGHT
        else:
            self.lcd.text_direction = self.lcd.RIGHT_TO_LEFT

        # Display message
        self.lcd.message = message

    def clear_screen(self):
        """
        Clears the LCD screen.
        """

        self.lcd.clear()

    def set_blink(self, blinking_cursor: bool):
        """
        Enable or disable the blinking cursor

        :param blinking_cursor: On or off.
        """

        # Set the cursor variable
        self.lcd.cursor = blinking_cursor

    def move_cursor(self, x: int, y: int):
        """
        Move the cursor in a grid-like manner to a position.

        :param x: The column to move the cursor to.
        :param y: The row to move the cursor to.
        """

        def __minmax(check_x, check_y):  # A helper-function to make sure values are in range
            if check_x >= self.dimensions[0]:  # dimensions[0] is the amount of columns
                return_x = self.dimensions[0] - 1
            elif check_x < 0:
                return_x = 0
            else:
                return_x = check_x

            if check_y >= self.dimensions[1]:  # dimensions[1] is the amount of rows
                return_y = self.dimensions[1] - 1
            elif check_y < 0:
                return_y = 0
            else:
                return_y = check_y

            return return_x, return_y

        # Make sure values are in range
        x, y = map(__minmax, (x,), (y,))

        # Update the cursor position
        self.lcd.cursor_position(x, y)

    def set_colour(self, red: int, green: int, blue: int):
        """
        Sets the colour of the LCD with RGB values.

        :param red: Amount of red (0 - 100)
        :param green: Amount of green (0 - 100)
        :param blue: Amount of blue (0 - 100)
        """

        def __minmax(x):  # A helper-function to make sure values are in range
            if x < 0:
                return 0
            if x > 100:
                return 100
            return x

        # Cannot change colour if it's not a colour LCD
        if not self.is_colour_lcd:
            return

        # Make sure values are in the correct range (0 - 100)
        red, green, blue = map(__minmax, [red, green, blue])

        # Set the colour tuple
        self.colour = (red, green, blue)

        # Update the LCD
        self.lcd.color = self.colour

    def turn_backlight(self, on: bool):
        """
        Turn the backlight on or off.

        :param on: False is off, True is on.
        :return:
        """

        # Cannot update backlight if it's a colour LCD. Update the color if it is.
        if self.is_colour_lcd:
            return

        # Update the backlight
        self.lcd.backlight = on
