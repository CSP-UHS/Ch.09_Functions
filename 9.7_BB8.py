import arcade
arcade.open_window(600, 600, "BB8")
def draw_BB8(x,y, radius):
    arcade.draw_circle_outline(x,y,radius,arcade.color.BLACK,radius*2.05)
    arcade.draw_circle_filled(x,y,radius,arcade.color.WHITE)
    arcade.draw_circle_outline(x,y,radius/1.5,arcade.color.BLACK,radius)
    arcade.draw_circle_filled(x,y,radius/1.6,arcade.color.ORANGE)
    arcade.draw_circle_filled(x,y,radius/3,arcade.color.BLACK)
    arcade.draw_circle_filled(x,y,radius/3.4,arcade.color.LIGHT_STEEL_BLUE)
    arcade.draw_arc_filled(x,y+radius/1.15,radius*1.2,radius*1.25,arcade.color.BLACK,0,180,)
    arcade.draw_arc_filled(x,y+radius/1.1,radius*1.1,radius*1.1,arcade.color.WHITE,0,180)
    arcade.draw_circle_filled(x,y+radius*1.15,radius/5,arcade.color.BLACK)
    arcade.draw_circle_filled(x,y+radius*1.15,radius/5.5,arcade.color.BABY_BLUE)

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
if __name__=="__main__":
    main()
