# Mohamed Mudawi
# File that allows the user to create obstacles on the screen, and documents their borders so that ball interacts with them properly
from Ball_File import my_screen
from Ball_File import turtle

# Obstacle class
class Obstacle_Creation(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pu()
        self.goto(-200,0)
        self.setheading(0)
        self.pd()
        self.pen_up_or_down = 'Down'
        print('Up arrow to go forward\nLeft/right arrows to turn\nSpacebar to lift your pen\nBack arrow to stop drawing')
        
        # Lists that will document the postions of the obstacles, and how the ball will react when it comes in contact with them
        # If the ball touches right_bounce_obstacles, the ball will bounce right, if it touches left_bounce_obstacles it will go left, etc.
        self.right_bounce_obstacles = []
        self.left_bounce_obstacles = []
        self.up_bounce_obstacles = []
        self.down_bounce_obstacles = []
        my_screen.update()

        # Adding obstacle positions to the ends of the screen so the ball doesn't go off the screen
        self.right_bounce_obstacles.append([-250,[-250,250]])
        self.left_bounce_obstacles.append([250,[-250,250]])
        self.up_bounce_obstacles.append([[-250,250],-250])
        self.down_bounce_obstacles.append([[-250,250],250])
            

        # Creating a goal on the screen for the ball to reach
        self.goal_borders = []
        self.pu()
        self.goto(220,-220)
        self.goal_center = [220,-220]
        self.setheading(0)
        self.fd(10)
        self.setheading(270)
        self.fd(10)
        self.setheading(90)
        self.fillcolor((0,1,0))
        self.begin_fill()
        for _ in range(4):
            for _ in range(10):
                self.fd(1)
                self.goal_borders.append([round(self.position()[0]),round(self.position()[1])])
            self.left(90)
        self.end_fill()
        self.pd()
        self.pu()
        self.goto(-200,0)
        self.setheading(0)
        self.pd()
        self.fillcolor((0,0,0))

    # Methods that moves the pen forward 10 pixels up, down, left or right and creates and documents a small abstract "shell"
    # around the drawing so the ball may bounce in the correct direction when it encounters an obstacle
    def user_up(self):
        self.setheading(90)
        if self.pen_up_or_down == 'Down':
            self.down_bounce_obstacles.append([[round(self.position()[0]),round(self.position()[0])],round(self.position()[1]-1)])
            original_position = [round(self.position()[0]),round(self.position()[1])]
            self.fd(10)
            current_position = [round(self.position()[0]),round(self.position()[1])]
            self.up_bounce_obstacles.append([[round(self.position()[0]),round(self.position()[0])],round(self.position()[1])+1])
            self.left_bounce_obstacles.append([current_position[0]-1,[original_position[1],current_position[1]]])
            self.right_bounce_obstacles.append([current_position[0]+1,[original_position[1],current_position[1]]])
        else:
            self.fd(10)
        my_screen.update()
    def user_down(self):
        self.setheading(270)
        if self.pen_up_or_down == 'Down':
            self.up_bounce_obstacles.append([[round(self.position()[0]),round(self.position()[0])],round(self.position()[1])+1])
            original_position = [round(self.position()[0]),round(self.position()[1])]
            self.fd(10)
            current_position = [round(self.position()[0]),round(self.position()[1])]
            self.down_bounce_obstacles.append([[round(self.position()[0]),round(self.position()[0])],round(self.position()[1])-1])
            self.left_bounce_obstacles.append([current_position[0]-1,[current_position[1],original_position[1]]])
            self.right_bounce_obstacles.append([current_position[0]+1,[current_position[1],original_position[1]]])
        else:
            self.fd(10)
        my_screen.update()
    def user_left(self):
        self.setheading(180)
        if self.pen_up_or_down == 'Down':
            self.right_bounce_obstacles.append([round(self.position()[0])+1,[round(self.position()[1]),round(self.position()[1])]])
            original_position = [round(self.position()[0]),round(self.position()[1])]
            self.fd(10)
            current_position = [round(self.position()[0]),round(self.position()[1])]
            self.left_bounce_obstacles.append([round(self.position()[0])-1,[round(self.position()[1]),round(self.position()[1])]])
            self.up_bounce_obstacles.append([[current_position[0],original_position[0]],current_position[1]+1])
            self.down_bounce_obstacles.append([[current_position[0],original_position[0]],current_position[1]-1])
        else:
            self.fd(10)
        my_screen.update()
    def user_right(self):
        self.setheading(0)
        if self.pen_up_or_down == 'Down':
            self.left_bounce_obstacles.append([round(self.position()[0])-1,[round(self.position()[1]),round(self.position()[1])]])
            original_position = [round(self.position()[0]),round(self.position()[1])]
            self.fd(10)
            current_position = [round(self.position()[0]),round(self.position()[1])]
            self.right_bounce_obstacles.append([round(self.position()[0])+1,[round(self.position()[1]),round(self.position()[1])]])
            self.up_bounce_obstacles.append([[original_position[0],current_position[0]],current_position[1]+1])
            self.down_bounce_obstacles.append([[original_position[0],current_position[0]],current_position[1]-1])
        else:
            self.fd(10)
        my_screen.update()
                
    def user_pen_lift(self): # Method that lifts the pen up if it's down, and down if it's up
        if self.pen_up_or_down == 'Down':
            self.pu()
            self.pen_up_or_down = 'Up'
            my_screen.update()
        else:
            self.pd()
            self.pen_up_or_down = 'Down'
            my_screen.update()

    def listen_to_user_input(self):  # Method that will listen to the input of the user, and execute corresponding methods when key is pressed to allow the user to draw obstacles properly
        my_screen.listen()
        my_screen.onkeypress(self.user_up,'Up')
        my_screen.onkeypress(self.user_down,'Down')
        my_screen.onkeypress(self.user_left,'Left')
        my_screen.onkeypress(self.user_right,'Right')
        my_screen.onkeypress(self.user_pen_lift,'space')



if __name__ == '__main__': # Example of allowing the user to create obstacles
    obstacle_object = Obstacle_Creation()
    obstacle_object.listen_to_user_input()
        
        
    


