# Mohamed Mudawi
# File that creates and moves the ball using Turtle module
import turtle
import time
my_screen = turtle.Screen()
my_screen.setup(500,500) # 500 by 500 pixels screen
my_screen.tracer(0) # Screen instantly updates


# Ball Class
class Ball(turtle.Turtle):

    def __init__(self,ball_center):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.pu()
        self.ball_center = list(ball_center)
        
        # Creating an abstract border of the ball around the center of the ball
        self.ball_borders = []
        self.ball_borders.append([round(self.ball_center[0]+10), round(self.ball_center[1])])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)-(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((3**0.5)/2))), round(self.ball_center[1]+ (10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((2**0.5)/2))), round(self.ball_center[1]+(10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(1/2))), round(self.ball_center[1]+(10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]), round(self.ball_center[1]+10)])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(1/2))), round(self.ball_center[1]+(10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((2**0.5)/2))), round(self.ball_center[1]+(10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((3**0.5)/2))), round(self.ball_center[1]+(10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)-(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]-10),round(self.ball_center[1])])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)-(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((3**0.5)/2))), round(self.ball_center[1]+(-10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((2**0.5)/2))), round(self.ball_center[1]+(-10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(1/2))), round(self.ball_center[1]+(-10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]),round(self.ball_center[1]-10)])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(1/2))), round(self.ball_center[1]+(-10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((2**0.5)/2))), round(self.ball_center[1]+(-10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((3**0.5)/2))), round(self.ball_center[1]+(-10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)-(2**0.5))/4)))])
    
    def update_ball_borders(self): # Method that creates new abstract ball borders if the center of the ball has been changed
        self.ball_borders = []
        self.ball_borders.append([round(self.ball_center[0]+10), round(self.ball_center[1])])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)-(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((3**0.5)/2))), round(self.ball_center[1]+ (10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((2**0.5)/2))), round(self.ball_center[1]+(10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(1/2))), round(self.ball_center[1]+(10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]), round(self.ball_center[1]+10)])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(1/2))), round(self.ball_center[1]+(10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((2**0.5)/2))), round(self.ball_center[1]+(10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((3**0.5)/2))), round(self.ball_center[1]+(10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(10*(((6**0.5)-(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]-10),round(self.ball_center[1])])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)-(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((3**0.5)/2))), round(self.ball_center[1]+(-10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*((2**0.5)/2))), round(self.ball_center[1]+(-10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(1/2))), round(self.ball_center[1]+(-10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(-10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]),round(self.ball_center[1]-10)])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)-(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)+(2**0.5))/4)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(1/2))), round(self.ball_center[1]+(-10*((3**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((2**0.5)/2))), round(self.ball_center[1]+(-10*((2**0.5)/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*((3**0.5)/2))), round(self.ball_center[1]+(-10*(1/2)))])
        self.ball_borders.append([round(self.ball_center[0]+(10*(((6**0.5)+(2**0.5))/4))), round(self.ball_center[1]+(-10*(((6**0.5)-(2**0.5))/4)))])
        

    def draw_ball(self): # Method that draws the current position of the ball for the user to see
        self.clear()
        self.pu()
        self.goto(self.ball_center[0],self.ball_center[1])
        self.setheading(270)
        self.fd(10)
        self.setheading(0)
        self.fillcolor((0,0,0))
        self.begin_fill()
        self.pd()
        self.circle(10)
        self.end_fill()
        my_screen.update()

    # Method that alters the ball center with the direction provided, updates the borders, and displays it for the user (moves one frame when it's called)
    def move_ball(self, direction_of_movement, display_to_user = True): 
        self.pu()
        self.goto(self.ball_center[0],self.ball_center[1])
        self.setheading(direction_of_movement)
        self.fd(1)
        self.ball_center = list(self.position())
        self.update_ball_borders()
        if display_to_user:
            self.draw_ball()

    # Method that returns the degree needed to travel in a straight path to the goal
    def degree_to_goal(self, goal_center):
        self.pu()
        self.goto(self.ball_center[0],self.ball_center[1])
        return self.towards(goal_center[0],goal_center[1])
        
        
        



if __name__ == '__main__': # Example of ball moving
    ball_object = Ball((1,2))
    for _ in range(200):
        time.sleep(0.01)
        ball_object.move_ball(45)


