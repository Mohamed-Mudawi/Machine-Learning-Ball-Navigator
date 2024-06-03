# Mohamed Mudawi
# File that uses combines all files to create a program that allows the user to create obstacles, and the ball to find its path through these obstacles
from Ball_File import my_screen
from Ball_File import turtle
import Ball_File
import User_Creates_Obstacles_File
import Ball_Obstacle_Interaction_File
import Machine_Learning_Functions_File
import time

# Creating a ball, but not moving it yet, just to show the user where the ball will start
ball_1 = Ball_File.Ball([-200,200])
ball_1.draw_ball()

# Letting the user create obstacles
obstacle_object = User_Creates_Obstacles_File.Obstacle_Creation()
obstacle_object.listen_to_user_input()

# Ending the drawing process if the user presses backspace, and using a while loop to animate the ball and allow the ball to learn to avoid obstacles
def user_end_drawing():
    obstacle_object.hideturtle()
    my_screen.listen()
    my_screen.onkeypress(None,'Up')
    my_screen.onkeypress(None,'Down')
    my_screen.onkeypress(None,'Left')
    my_screen.onkeypress(None,'Right')
    my_screen.onkeypress(None,'space')
    my_screen.onkeypress(None,'BackSpace')
    obstacle_object.pu()
    print('Drawing over')
    my_screen.update()

    # Speed of the animation
    speed = 0.001
            
    # This variable will give information about the current ball degree, what obstacle it hit, and the position that the ball hit
    # It starts off facing the direction of the goal and assumes it hasn't hit any obstacle
    ball_1_degree = [315,'no bounce',[]] 
    
    frame = 0 # Variable which will be used to tell how many frames have passed so far since the start of the while loop

    # Function that first lets the ball bounce a little to show the user, and then resets the balls, frames, and degree
    def reset_ball(ball_1_degree):
        for _ in range (200):
            time.sleep(speed)
            ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
        frame = Machine_Learning_Functions_File.reset_ball(ball_1)
        return 315,frame

    # Lists which will tell when the ball has to turn
    points_to_turn_right_avoiding_up = []
    points_to_turn_right_avoiding_down = []
    points_to_turn_left_avoiding_up = []
    points_to_turn_left_avoiding_down = []
    points_to_turn_up_avoiding_right = []
    points_to_turn_up_avoiding_left = []
    points_to_turn_down_avoiding_right = []
    points_to_turn_down_avoiding_left = []

    # Lists which will tell the location of where the ball has hit an obstacle,
    # so that if the ball has hit the same location twice it will go in a different direction so it doesn't go in an endless loop
    location_of_right_avoiding_up = []
    location_of_right_avoiding_down = []
    location_of_left_avoiding_up = []
    location_of_left_avoiding_down = []
    location_of_up_avoiding_right = []
    location_of_up_avoiding_left = []
    location_of_down_avoiding_right = []
    location_of_down_avoiding_left = []


    # While loop which will animate the ball and complete a frame each iteration
    while True:
        time.sleep(speed)



        # If the ball hit an obstacle that sent it going up, avoid it next time the ball resetst
        if ball_1_degree[1] == 'up':
            if ball_1_degree[0] <= 90: # If the ball was going more right than left, then avoid the obstacle by going a little right
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels right and dont add a new point, and if not then add a new point
                    if points_to_turn_right_avoiding_up[-1][0]+points_to_turn_right_avoiding_up[-1][1] + 45 > frame: 
                        points_to_turn_right_avoiding_up[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go right and make it go left, and if not then go right
                    if ball_1_degree[2] in location_of_right_avoiding_up:
                        points_to_turn_left_avoiding_up.append([frame - 20, 0])
                        location_of_left_avoiding_up.append(ball_1_degree[2])
                    else:
                        points_to_turn_right_avoiding_up.append([frame - 20, 0])
                        location_of_right_avoiding_up.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)
                
            else: # If the ball was going more left than right, then avoid the obstacle by going a little left
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels left and dont add a new point, and if not then add a new point
                    if points_to_turn_left_avoiding_up[-1][0]+points_to_turn_left_avoiding_up[-1][1] + 45 > frame:
                        points_to_turn_left_avoiding_up[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go left and make it go right, and if not then go left
                    if ball_1_degree[2] in location_of_left_avoiding_up:
                        points_to_turn_right_avoiding_up.append([frame - 20, 0])
                        location_of_right_avoiding_up.append(ball_1_degree[2])
                    else:
                        points_to_turn_left_avoiding_up.append([frame - 20, 0])
                        location_of_left_avoiding_up.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)
        


        # If the ball hit an obstacle that sent it going down, avoid it next time the ball resets
        if ball_1_degree[1] == 'down':
            if ball_1_degree[0] >= 270: # If the ball was going more right than left, then avoid the obstacle by going a little right
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels right and dont add a new point, and if not then add a new point
                    if points_to_turn_right_avoiding_down[-1][0]+points_to_turn_right_avoiding_down[-1][1] + 45 > frame:
                        points_to_turn_right_avoiding_down[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go right and make it go left, and if not then go right
                    if ball_1_degree[2] in location_of_right_avoiding_down:
                        points_to_turn_left_avoiding_down.append([frame - 20, 0])
                        location_of_left_avoiding_down.append(ball_1_degree[2])
                    else:
                        points_to_turn_right_avoiding_down.append([frame - 20, 0])
                        location_of_right_avoiding_down.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)
            else: # If the ball was going more left than right, then avoid the obstacle by going a little left
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels left and dont add a new point, and if not then add a new point
                    if points_to_turn_left_avoiding_down[-1][0]+points_to_turn_left_avoiding_down[-1][1] + 45 > frame:
                        points_to_turn_left_avoiding_down[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go left and make it go right, and if not then go left
                    if ball_1_degree[2] in location_of_left_avoiding_down:
                        points_to_turn_right_avoiding_down.append([frame - 20, 0])
                        location_of_right_avoiding_down.append(ball_1_degree[2])
                    else:
                        points_to_turn_left_avoiding_down.append([frame - 20, 0])
                        location_of_left_avoiding_down.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)



        # If the ball hit an obstacle that sent it going left, avoid it next time the ball resets
        if ball_1_degree[1] == 'left':
            if ball_1_degree[0] >= 180:
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels down and dont add a new point, and if not then add a new point
                    if points_to_turn_down_avoiding_left[-1][0]+points_to_turn_down_avoiding_left[-1][1] + 45 > frame:
                        points_to_turn_down_avoiding_left[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go down and make it go up, and if not then go down
                    if ball_1_degree[2] in location_of_down_avoiding_left:
                        points_to_turn_up_avoiding_left.append([frame - 20, 0])
                        location_of_up_avoiding_left.append(ball_1_degree[2])
                    else:
                        points_to_turn_down_avoiding_left.append([frame - 20, 0])
                        location_of_down_avoiding_left.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)
            else:
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels up and dont add a new point, and if not then add a new point
                    if points_to_turn_up_avoiding_left[-1][0]+points_to_turn_up_avoiding_left[-1][1] + 45 > frame:
                        points_to_turn_up_avoiding_left[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go up and make it go down, and if not then go up
                    if ball_1_degree[2] in location_of_up_avoiding_left:
                        points_to_turn_down_avoiding_left.append([frame - 20, 0])
                        location_of_down_avoiding_left.append(ball_1_degree[2])
                    else:
                        points_to_turn_up_avoiding_left.append([frame - 20, 0])
                        location_of_up_avoiding_left.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)


        # If the ball hit an obstacle that sent it going right, avoid it next time the ball resets
        if ball_1_degree[1] == 'right':
            if ball_1_degree[0] >= 90:
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels down and dont add a new point, and if not then add a new point
                    if points_to_turn_down_avoiding_right[-1][0]+points_to_turn_down_avoiding_right[-1][1] + 45 > frame:
                        points_to_turn_down_avoiding_right[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go down and make it go up, and if not then go down
                    if ball_1_degree[2] in location_of_down_avoiding_right:
                        points_to_turn_up_avoiding_right.append([frame - 20, 0])
                        location_of_up_avoiding_right.append(ball_1_degree[2])
                    else:
                        points_to_turn_down_avoiding_right.append([frame - 20, 0])
                        location_of_down_avoiding_right.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)
            else:
                try:
                    # Seeing if the ball bounced a few frames before, and if it has then move a few pixels up and dont add a new point, and if not then add a new point
                    if points_to_turn_up_avoiding_right[-1][0]+points_to_turn_up_avoiding_right[-1][1] + 45 > frame: 
                        points_to_turn_up_avoiding_right[-1][1] += 30
                    else:
                        raise Exception
                except:
                    # Checking to see if the ball has hit that position before, and if it has don't make it go up and make it go down, and if not then go up
                    if ball_1_degree[2] in location_of_up_avoiding_right:
                        points_to_turn_down_avoiding_right.append([frame - 20, 0])
                        location_of_down_avoiding_right.append(ball_1_degree[2])
                    else:
                        points_to_turn_up_avoiding_right.append([frame - 20, 0])
                        location_of_up_avoiding_right.append(ball_1_degree[2])
                # Resetting the ball, it's degree, and frame
                ball_1_degree[0],frame = reset_ball(ball_1_degree)



        # Ending the program if the goal was found
        if ball_1_degree[1] == 'goal':
            print('Goal found')
            return
           

        
        # Moving the ball one frame, and recording if the ball hit an obstacle      
        ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
        
          
            
        # Making the ball turn to the degree needed to get the goal if it was changed, and seeing if the ball is on track
        ball_1_degree[0] = Machine_Learning_Functions_File.back_on_track(ball_1_degree[0],round(ball_1.degree_to_goal(obstacle_object.goal_center)))



        # Creating a temporary copy of the lists to alter them in for loops
        temporary_right_avoiding_up = points_to_turn_right_avoiding_up[:]
        temporary_down_avoiding_left = points_to_turn_down_avoiding_left[:]

        # If the ball is going right and hits a wall that sends it going left, instead of going right and then down, go right and then up to avoid the wall.
        # And if the ball is going down and hits a wall, go left instead of going right
        for down_turn in temporary_down_avoiding_left[::-1]:
            for right_turn in temporary_right_avoiding_up[::-1]:
                if (right_turn[0] < down_turn[0]) and (right_turn[0]+31 > down_turn[0]) and (right_turn[1] == 0):
                    points_to_turn_down_avoiding_left.remove(down_turn)
                    points_to_turn_up_avoiding_left.append(down_turn)
                    break
                elif (right_turn[1] > 0) and (right_turn[0]+right_turn[1] < down_turn[0]) and (right_turn[0]+right_turn[1]+20 > down_turn[0]):
                    points_to_turn_down_avoiding_left.remove(down_turn)
                    points_to_turn_up_avoiding_left.append(down_turn)
                    break
                elif (right_turn[1] > 0) and (right_turn[0]+right_turn[1]-20 < down_turn[0]) and (right_turn[0]+right_turn[1] > down_turn[0]):
                    points_to_turn_right_avoiding_up.remove(right_turn)
                    right_turn = [right_turn[0],right_turn[1] - ((right_turn[0]+right_turn[1])-(down_turn[0]-1))]
                    points_to_turn_right_avoiding_up.append(right_turn)
                    points_to_turn_down_avoiding_left.remove(down_turn)
                    points_to_turn_up_avoiding_left.append(down_turn)
                    break
                    
                if (down_turn[0] < right_turn[0]) and (down_turn[0]+31 > right_turn[0]) and (down_turn[1] == 0):
                    points_to_turn_right_avoiding_up.remove(right_turn)
                    points_to_turn_left_avoiding_up.append(right_turn)
                    break
                elif (down_turn[1] > 0) and (down_turn[0]+down_turn[1] < right_turn[0]) and (down_turn[0]+down_turn[1]+20 > right_turn[0]):
                    points_to_turn_right_avoiding_up.remove(right_turn)
                    points_to_turn_left_avoiding_up.append(right_turn)
                    break
                elif (down_turn[1] > 0) and (down_turn[0]+down_turn[1]-20 < right_turn[0]) and (down_turn[0]+down_turn[1] > right_turn[0]):
                    points_to_turn_down_avoiding_left.remove(down_turn)
                    down_turn = [down_turn[0],down_turn[1] - ((down_turn[0]+down_turn[1])-(right_turn[0]-1))]
                    points_to_turn_down_avoiding_left.append(down_turn)
                    points_to_turn_right_avoiding_up.remove(right_turn)
                    points_to_turn_left_avoiding_up.append(right_turn)
                    break
            break

                    

        # Creating a temporary copy of the lists to alter them in for loops
        temporary_right_avoiding_down = points_to_turn_right_avoiding_down[:]
        temporary_up_avoiding_left = points_to_turn_up_avoiding_left[:]

        # If the ball is going right and hits a wall that sends it going left, instead of going left and then up, go left and then down to avoid the wall.
        # And if the ball is going up and hits a wall, go left instead of going right
        for up_turn in temporary_up_avoiding_left[::-1]:
            for right_turn in temporary_right_avoiding_down[::-1]:
                if (up_turn[0] < right_turn[0]) and (up_turn[0]+31 > right_turn[0]) and (up_turn[1] == 0):
                    points_to_turn_right_avoiding_down.remove(right_turn)
                    points_to_turn_left_avoiding_down.append(right_turn)
                    break
                elif (up_turn[1] > 0) and (up_turn[0]+up_turn[1] < right_turn[0]) and (up_turn[0]+up_turn[1]+20 > right_turn[0]):
                    points_to_turn_right_avoiding_down.remove(right_turn)
                    points_to_turn_left_avoiding_down.append(right_turn)
                    break
                elif (up_turn[1] > 0) and (up_turn[0]+up_turn[1]-20 < right_turn[0]) and (up_turn[0]+up_turn[1] > right_turn[0]):
                    points_to_turn_up_avoiding_left.remove(up_turn)
                    up_turn = [up_turn[0],up_turn[1] - ((up_turn[0]+up_turn[1])-(right_turn[0]-1))]
                    points_to_turn_up_avoiding_left.append(up_turn)
                    points_to_turn_right_avoiding_down.remove(right_turn)
                    points_to_turn_left_avoiding_down.append(right_turn)
                    break

                if (right_turn[0] < up_turn[0]) and (right_turn[0]+31 > up_turn[0]) and (right_turn[1] == 0):
                    points_to_turn_up_avoiding_left.remove(up_turn)
                    points_to_turn_down_avoiding_left.append(up_turn)
                    break
                elif (right_turn[1] > 0) and (right_turn[0]+right_turn[1] < up_turn[0]) and (right_turn[0]+right_turn[1]+20 > up_turn[0]):
                    points_to_turn_up_avoiding_left.remove(up_turn)
                    points_to_turn_down_avoiding_left.append(up_turn)
                    break
                elif (right_turn[1] > 0) and (right_turn[0]+right_turn[1]-20 < up_turn[0]) and (right_turn[0]+right_turn[1] > up_turn[0]):
                    points_to_turn_right_avoiding_up.remove(right_turn)
                    right_turn = [right_turn[0],right_turn[1] - ((right_turn[0]+right_turn[1])-(up_turn[0]-1))]
                    points_to_turn_right_avoiding_up.append(right_turn)
                    points_to_turn_up_avoiding_left.remove(up_turn)
                    points_to_turn_down_avoiding_left.append(up_turn)
                    break
            break



        # Creating a temporary copy of the lists to alter them in for loops
        temporary_left_avoiding_down = points_to_turn_left_avoiding_down[:]
        temporary_up_avoiding_right = points_to_turn_up_avoiding_right[:]

        # If the ball is going left and hits a wall that sends it going right, instead of going left and then up, go left and then down to avoid the wall.
        # And if the ball is going up and hits a wall, go right instead of going left
        for up_turn in temporary_up_avoiding_right[::-1]:
            for left_turn in temporary_left_avoiding_down[::-1]:
                if (left_turn[0] < up_turn[0]) and (left_turn[0]+31 > up_turn[0]) and (left_turn[1] == 0):
                    points_to_turn_up_avoiding_right.remove(up_turn)
                    points_to_turn_down_avoiding_right.append(up_turn)
                    break
                elif (left_turn[1] > 0) and (left_turn[0]+left_turn[1] < up_turn[0]) and (left_turn[0]+left_turn[1]+20 > up_turn[0]):
                    points_to_turn_up_avoiding_right.remove(up_turn)
                    points_to_turn_down_avoiding_right.append(up_turn)
                    break
                elif (left_turn[1] > 0) and (left_turn[0]+left_turn[1]-20 < up_turn[0]) and (left_turn[0]+left_turn[1] > up_turn[0]):
                    points_to_turn_left_avoiding_down.remove(left_turn)
                    left_turn = [left_turn[0],left_turn[1] - ((left_turn[0]+left_turn[1])-(up_turn[0]-1))]
                    points_to_turn_left_avoiding_down.append(left_turn)
                    points_to_turn_up_avoiding_right.remove(up_turn)
                    points_to_turn_down_avoiding_right.append(up_turn)
                    break
                
                if (up_turn[0] < left_turn[0]) and (up_turn[0]+31 > left_turn[0]) and (up_turn[1] == 0):
                    points_to_turn_left_avoiding_down.remove(left_turn)
                    points_to_turn_right_avoiding_down.append(left_turn)
                    break
                elif (up_turn[1] > 0) and (up_turn[0]+up_turn[1] < left_turn[0]) and (up_turn[0]+up_turn[1]+20 > left_turn[0]):
                    points_to_turn_left_avoiding_down.remove(left_turn)
                    points_to_turn_right_avoiding_down.append(left_turn)
                    break
                elif (up_turn[1] > 0) and (up_turn[0]+up_turn[1]-20 < left_turn[0]) and (up_turn[0]+up_turn[1] > left_turn[0]):
                    points_to_turn_up_avoiding_right.remove(up_turn)
                    up_turn = [up_turn[0],up_turn[1] - ((up_turn[0]+up_turn[1])-(left_turn[0]-1))]
                    points_to_turn_up_avoiding_right.append(up_turn)
                    points_to_turn_left_avoiding_down.remove(left_turn)
                    points_to_turn_right_avoiding_down.append(left_turn)
                    break
            break



        # Creating a temporary copy of the lists to alter them in for loops
        temporary_left_avoiding_up = points_to_turn_left_avoiding_up[:]
        temporary_down_avoiding_right = points_to_turn_down_avoiding_right[:]

        # If the ball is going left and hits a wall that sends it going right, instead of going left and then down, go left and then up to avoid the wall.
        # And if the ball is going down and hits a wall, go right instead of going left
        for down_turn in temporary_down_avoiding_right[::-1]:
            for left_turn in temporary_left_avoiding_up[::-1]:
                if (down_turn[0] < left_turn[0]) and (down_turn[0]+31 > left_turn[0]) and (down_turn[1] == 0):
                    points_to_turn_left_avoiding_up.remove(left_turn)
                    points_to_turn_right_avoiding_up.append(left_turn)
                    break
                elif (down_turn[1] > 0) and (down_turn[0]+down_turn[1] < left_turn[0]) and (down_turn[0]+down_turn[1]+20 > left_turn[0]):
                    points_to_turn_left_avoiding_up.remove(left_turn)
                    points_to_turn_right_avoiding_up.append(left_turn)
                    break
                elif (down_turn[1] > 0) and (down_turn[0]+down_turn[1]-20 < left_turn[0]) and (down_turn[0]+down_turn[1] > left_turn[0]):
                    points_to_turn_down_avoiding_right.remove(down_turn)
                    down_turn = [down_turn[0],down_turn[1] - ((down_turn[0]+down_turn[1])-(left_turn[0]-1))]
                    points_to_turn_down_avoiding_right.append(down_turn)
                    points_to_turn_left_avoiding_up.remove(left_turn)
                    points_to_turn_right_avoiding_up.append(left_turn)
                    break
                
                if (left_turn[0] < down_turn[0]) and (left_turn[0]+31 > down_turn[0]) and (left_turn[1] == 0):
                    points_to_turn_down_avoiding_right.remove(down_turn)
                    points_to_turn_up_avoiding_right.append(down_turn)
                    break
                elif (left_turn[1] > 0) and (left_turn[0]+left_turn[1] < down_turn[0]) and (left_turn[0]+left_turn[1]+20 > down_turn[0]):
                    points_to_turn_down_avoiding_right.remove(down_turn)
                    points_to_turn_up_avoiding_right.append(down_turn)
                    break
                elif (left_turn[1] > 0) and (left_turn[0]+left_turn[1]-20 < down_turn[0]) and (left_turn[0]+left_turn[1] > down_turn[0]):
                    points_to_turn_left_avoiding_up.remove(left_turn)
                    left_turn = [left_turn[0],left_turn[1] - ((left_turn[0]+left_turn[1])-(down_turn[0]-1))]
                    points_to_turn_left_avoiding_up.append(left_turn)
                    points_to_turn_down_avoiding_right.remove(down_turn)
                    points_to_turn_up_avoiding_right.append(down_turn)
                    break
                
                    
        
                
        
        # Avoiding obstacles by going in a certain direction if the ball hits a certain frame
        
        for point in points_to_turn_right_avoiding_up:
            if frame == point[0]:
                ball_1_degree[0] = 0
                for _ in range(point[1]): # Moving the ball more to the right since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
                    
        for point in points_to_turn_right_avoiding_down:
            if frame == point[0]:
                ball_1_degree[0] = 0
                for _ in range(point[1]): # Moving the ball more to the right since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
                    
        for point in points_to_turn_left_avoiding_up:
            if frame == point[0]:
                ball_1_degree[0] = 180
                for _ in range(point[1]): # Moving the ball more to the left since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
                    
        for point in points_to_turn_left_avoiding_down:
            if frame == point[0]:
                ball_1_degree[0] = 180
                for _ in range(point[1]): # Moving the ball more to the left since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
                ball_1_degree[0] = 125
                    
        for point in points_to_turn_up_avoiding_left:
            if frame == point[0]:
                ball_1_degree[0] = 90
                for _ in range(point[1]): # Moving the ball more to the up since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1

                    
        for point in points_to_turn_up_avoiding_right:
            if frame == point[0]:
                ball_1_degree[0] = 90
                for _ in range(point[1]): # Moving the ball more to the up since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
                ball_1_degree[0] = 145
                    
        for point in points_to_turn_down_avoiding_left:
            if frame == point[0]:
                ball_1_degree[0] = 270
                for _ in range(point[1]): # Moving the ball more to the down since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
                    
        for point in points_to_turn_down_avoiding_right:
            if frame == point[0]:
                ball_1_degree[0] = 270
                for _ in range(point[1]): # Moving the ball more to the down since the previous bounce didn't allow the ball to go past the obstacle
                    time.sleep(speed)
                    ball_1_degree = Ball_Obstacle_Interaction_File.ball_interaction(True, obstacle_object.goal_borders, ball_1, ball_1_degree[0], ball_1.ball_borders, obstacle_object.up_bounce_obstacles, obstacle_object.down_bounce_obstacles, obstacle_object.right_bounce_obstacles, obstacle_object.left_bounce_obstacles)
                    frame += 1
        
        frame += 1



        
        
# Listening for when the users clicks backspace
my_screen.listen()
my_screen.onkeypress(user_end_drawing, 'BackSpace')




    







