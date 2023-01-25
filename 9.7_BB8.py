"""
BB8 DRAWING PROGRAM
-------------------
Back to the drawing board! Get it? Let's say we want to draw many BB8 robots
of varying sizes at various locations. We can make a function called draw_BB8().
We've made some basic changes to our original drawing program. We still have the
first two lines as importing arcade and opening an arcade window. We actually took
all the other drawing code and put it in a function called main(). At the bottom
we call the main() function. In the main() function we call the draw_BB8() function
multiple times. We pass three parameters to it: x, y and radius. Write the code for
the draw_BB8() function so that the resulting picture looks as close as you can get
it to the one on the website.
"""

# Imports arcade module
import arcade

# Opens a 600px by 600px window and puts BB8 in the title
arcade.open_window(600, 600, "BB8")

# Function to draw BB8 robots


def draw_BB8(x, y, radius):
    # Body of BB8
    # - large white circle + outline
    radius1 = radius/1.5
    arcade.draw_circle_filled(x, y, radius1, arcade.color.WHITE)
    arcade.draw_circle_outline(x, y, radius1, arcade.color.BLACK, 1.25)
    # - orange circle + outline
    radius1 = radius/2.5
    arcade.draw_circle_filled(x, y, radius1, arcade.color.ORANGE)
    arcade.draw_circle_outline(x, y, radius1, arcade.color.BLACK, 1.25)
    # - light blue circle (not the head of BB8) + outline
    radius1 = radius/4.5
    arcade.draw_circle_filled(x, y, radius1, arcade.color.LIGHT_SKY_BLUE)
    arcade.draw_circle_outline(x, y, radius1, arcade.color.BLACK, 1.25)
    # Head of BB8 #######################
    # - Half circle (white) + outline
    radius1 = radius/5.5
    radius2 = radius/1.5
    arcade.draw_arc_outline(x, radius2+y-5, radius, radius, (0, 0, 0), 420, 600, 2, 301)
    arcade.draw_arc_filled(x, radius2+y-5, radius-3, radius-3, arcade.color.WHITE, 420, 600, 300, 120)
    # - light blue circle (head of BB8) + outline
    if radius >= 50:
        divide1 = radius2+y+7
    elif 30 <= radius < 50:
        divide1 = radius2+y+2
    else:
        divide1 = radius2+y-2
    arcade.draw_circle_filled(x, divide1, radius1, (85, 144, 237))
    arcade.draw_circle_outline(x, divide1, radius1, arcade.color.BLACK, 1.25)
    if radius <= 20:
        d = 2.5
    elif 50 > radius > 20:
        d = 2.1
    else:
        d = 1.8
    arcade.draw_line(x-(radius/2), y+(radius/d), x+(radius/2), y+(radius/d), (0, 0, 0), 1.5)


# The main function where we set background color, start and finish rendering and run.
def main():
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()

    draw_BB8(100, 50, 50)   # bottom left better one (maybe a little higher)
    draw_BB8(300, 300, 30)  # middle lower
    draw_BB8(500, 100, 20)  # bottom right lower
    draw_BB8(500, 400, 60)  # top right higher
    draw_BB8(120, 500, 15)  # top left lower

    arcade.finish_render()
    arcade.run()


# Calls the main function
if __name__ == "__main__":
    main()
