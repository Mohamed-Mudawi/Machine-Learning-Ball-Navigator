# Mohamed Mudawi
# File that contains function that will help the ball find its path to the goal

# Function that will slowly move the ball's degree to the correct degree needed to get to the goal, if the ball's off track
def back_on_track(ball_degree,degree_to_goal):
    
    # Making the ball slowly get back on course if the degree to the goal was changed
    if ball_degree != degree_to_goal:

        # If the ball's degree is 1 or 2 more or less than the degree needed to reach the goal, change the ball's degree to the goal
        if ((360+ball_degree)%360 == ((360+degree_to_goal)+ 1)%360) or ((360+ball_degree)%360 == ((360+degree_to_goal)- 1)%360) or ((360+ball_degree)%360 == ((360+degree_to_goal)+ 2)%360) or ((360+ball_degree)%360 == ((360+degree_to_goal)- 2)%360) or ((360+ball_degree)%360 == ((360+degree_to_goal)+ 3)%360) or ((360+ball_degree)%360 == ((360+degree_to_goal)- 3)%360):
            ball_degree = degree_to_goal
            return ball_degree

        # Seeing if it would be faster to turn left or right
        elif degree_to_goal < 180:
            if ball_degree in range(degree_to_goal,degree_to_goal + 181):
                ball_degree = (360 + (ball_degree - 1)) % 360
                return ball_degree
            else:
                ball_degree = (360 + (ball_degree + 1)) % 360
                return ball_degree
        else:
            if ball_degree in range(degree_to_goal - 180,degree_to_goal+1):
                ball_degree = (360 + (ball_degree + 1)) % 360
                return ball_degree
            else:
                ball_degree = (360 + (ball_degree - 1)) % 360
                return ball_degree
    else:
        return ball_degree



# Function that will reset the ball as if the program just began
def reset_ball(ball_object_name):
    ball_object_name.ball_center = [-200,200]
    return 0











    

