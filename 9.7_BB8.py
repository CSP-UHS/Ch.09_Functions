'''
BB8 DRAWING PROGRAM
-------------------
Back to the drawing board! Get it? Let's say we want to draw many BB8 robots
of varying sizes at various locations. We can make a function called draw_BB8().
We've made some basic changes to our original drawing program. We still have the
first two lines as importing arcade and opening an arcade window. We actually took 
all of the other drawing code and put it in a function called main(). At the bottom
we call the main() function. In the main() function we call the draw_BB8() function
multiple times. We pass three parameters to it: x, y and radius. Write the code for 
the draw_BB8() function so that the resulting picture looks as close as you can get
it to the one on the website.
'''

import arcade
arcade.open_window(600, 600, "BB8")
def draw_BB8(x,y, radius):
    arcade.draw_circle_filled(x,y,radius,arcade.color.WHITE)
    arcade.draw_circle_outline(x,y,radius,arcade.color.BLACK,2)
    arcade.draw_circle_filled(x,y,radius*0.70, arcade.color.ORANGE)
    arcade.draw_circle_outline(x, y, radius*.70, arcade.color.BLACK,2)
    arcade.draw_circle_filled(x,y,radius*0.40,arcade.color.BABY_BLUE)
    arcade.draw_circle_outline(x, y, radius*0.40, arcade.color.BLACK,2)


def main():
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()

    draw_BB8(100,50,50)
    draw_BB8(300, 300, 30)
    draw_BB8(500, 100, 20)
    draw_BB8(500, 400, 60)
    draw_BB8(120, 500, 15)

    arcade.finish_render()
    arcade.run()


if __name__== "__main__":
    main()