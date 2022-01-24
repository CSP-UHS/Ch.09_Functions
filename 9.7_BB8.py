z
import arcade

# Opens a 600px by 600px window and puts BB8 in the title
arcade.open_window(600, 600, "BB8")
#light steel blue, orange, white, blue gray
# Function to draw BB8 robots
def draw_BB8(x,y, radius):
    arcade.draw_circle_filled(x,y,radius,arcade.color.WHITE)
    arcade.draw_circle_outline(x,y,radius,arcade.color.BLACK)

'''The main function where we set background color, start and finish rendering and run.'''
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
if __name__=="__main__":
    main()
