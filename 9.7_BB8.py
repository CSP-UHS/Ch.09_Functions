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
import random
import time

# Opens a 600px by 600px window and puts BB8 in the title
times = 0
first = True
movers = []
track = 0
# Function to draw BB8 robots
def draw_BB8(x,y, radius, move=False):
    thick = 3
    if radius <= 20:
        thick = 2
    if move:
        movers.append([x, y, radius])
    arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)  # big circle body
    arcade.draw_circle_outline(x, y, radius, arcade.color.BLACK, thick)  # outline
    arcade.draw_circle_filled(x, y, radius*(2/3), arcade.color.ORANGE)  # smaller circle in body
    arcade.draw_circle_outline(x,y, radius*(2/3), arcade.color.BLACK, thick)  # outline
    arcade.draw_circle_filled(x, y, (radius*(2/3))/2, arcade.color.LIGHT_BLUE)  # smallest circle in body
    arcade.draw_circle_outline(x, y, (radius*(2/3))/2, arcade.color.BLACK, thick)  # outline
    arcade.draw_arc_filled(x, y+radius-(radius*.16666667), radius*1.5, radius*1.5, arcade.color.WHITE, 0, 180)
    arcade.draw_arc_outline(x, y+radius-(radius*.16666667), radius*1.5, radius*1.5, arcade.color.BLACK, 0, 180, thick+2)
    arcade.draw_line(x-radius*1.5/2, y+radius*(5/6), x-radius*1.5*-1/2, y+radius*(5/6), arcade.color.BLACK, thick)
    arcade.draw_circle_filled(x, y+radius+(radius*.1966667), radius/4.5, arcade.color.BLUE_GRAY)
    arcade.draw_circle_outline(x, y+radius+(radius*.1966667), radius/4.5, arcade.color.BLACK, thick)
    arcade.finish_render()


def move(delta_time):
    global times
    global first
    global track
    times += 1
    for each in movers:
        thick = 3
        x = each[0]
        y = each[1]
        radius = each[2]
        if radius <= 20:
            thick = 2
        if times > 25 and times < 150:
            if first:
                time.sleep(15)
                first = False
            arcade.draw_circle_filled(x, y, radius, arcade.color.WHEAT)  # big circle body
            arcade.draw_circle_outline(x, y, radius, arcade.color.WHEAT, thick)  # outline
            arcade.draw_circle_filled(x, y, radius * (2 / 3), arcade.color.WHEAT)  # smaller circle in body
            arcade.draw_circle_outline(x, y, radius * (2 / 3), arcade.color.WHEAT, thick)  # outline
            arcade.draw_circle_filled(x, y, (radius * (2 / 3)) / 2, arcade.color.WHEAT)  # smallest circle in body
            arcade.draw_circle_outline(x, y, (radius * (2 / 3)) / 2, arcade.color.WHEAT, thick)  # outline
            arcade.draw_arc_filled(x, y + radius - (radius * .16666667), radius * 1.5, radius * 1.5, arcade.color.WHEAT,
                                   0, 180)
            arcade.draw_arc_outline(x, y + radius - (radius * .16666667), radius * 1.5, radius * 1.5,
                                    arcade.color.WHEAT, 0, 180, thick + 2)
            arcade.draw_line(x - radius * 1.5 / 2, y + radius * (5 / 6), x - radius * 1.5 * -1 / 2,
                             y + radius * (5 / 6), arcade.color.WHEAT, thick)
            arcade.draw_circle_filled(x, y + radius + (radius * .1966667), radius / 4.5, arcade.color.WHEAT)
            arcade.draw_circle_outline(x, y + radius + (radius * .1966667), radius / 4.5, arcade.color.WHEAT, thick)
            each[0] = random.randint(50, 550)
            each[1] = random.randint(50, 550)
            each[2] = radius
            draw_BB8(each[0], each[1], radius)
    print("times:", times)
    if times >= 150 and times <= 200:
        # arcade.play_sound(arcade.load_sound("alarm.mp3"))
        draw_BB8(random.randint(50, 550), random.randint(50, 550), random.randint(10, 60), True)
    elif times > 200 and times <= 320:
        track += 1
        if track == 20:
            print("track")
            arcade.stop_sound(arcade.load_sound("alarm.mp3"))
            arcade.play_sound(arcade.load_sound("alarm.mp3"))
            track = 0
        for i in range(25):
            draw_BB8(random.randint(50, 550), random.randint(50, 550), random.randint(10, 60), True)
    elif times > 320:
        arcade.stop_sound(arcade.load_sound("alarm.mp3"))
        for i in range(60):
            draw_BB8(random.randint(50, 550), random.randint(50, 550), random.randint(times-200, times-100), True)
            print("big")




# The main function where we set background color, start and finish rendering and run.
def main():
    arcade.open_window(600, 600, "BB8")
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()
    draw_BB8(100, 50, 50, True)
    draw_BB8(300, 300, 30, True)
    draw_BB8(500, 100, 20, True)
    draw_BB8(500, 400, 60, True)
    draw_BB8(120, 500, 15, True)
    if movers:
        arcade.schedule(move, 1/20)
    arcade.run()
# Calls the main function
if __name__=="__main__":
    main()
