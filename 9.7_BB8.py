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

# Imports arcade module
import arcade

# Opens a 600px by 600px window and puts BB8 in the title
arcade.open_window(600, 600, "BB8")

# Function to draw BB8 robots
def draw_BB8(x,y, radius):
    #the white circle
  arcade.draw_circle_filled(x, y,radius, arcade.color.WHITE)
  arcade.draw_circle_outline(x, y,radius, arcade.color.BLACK, 1.5)
    #the orange circle
  arcade.draw_circle_filled(x, y, radius/10 * 6.5, arcade.color.ORANGE)
  arcade.draw_circle_outline(x, y, radius/10 * 6.5, arcade.color.BLACK, 1.5)
       #the blue circle
  arcade.draw_circle_filled(x, y, radius/10 * 3.5, arcade.color.LIGHT_BLUE)
  arcade.draw_circle_outline(x, y, radius/10 * 3.5, arcade.color.BLACK, 1.5)
     #ellipse circle
  arcade.draw_arc_filled(x + radius/10 * 0.1, y+radius/10 *9.5, radius+1, radius+1, arcade.color.WHITE, 0, 180, 0)
  arcade.draw_arc_outline(x + radius/10 * 0.1, y+radius/10 *9.5, radius, radius, arcade.color.BLACK, 0, 180, 2.5)
  arcade.draw_line(x-radius/10 *4.8, y+radius-2, x+radius/10 * 5, y+radius-2,arcade.color.BLACK, 2)

    #circle

  arcade.draw_circle_filled(x, y+radius/10*12,radius/10 * 1.5, arcade.color.BLUE_GRAY)
  arcade.draw_circle_outline(x, y+radius/10*12,radius/10 * 1.5, arcade.color.BLACK, 2)
# The main function where we set background color, start and finish rendering and run.
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

# Calls the main function
main()
