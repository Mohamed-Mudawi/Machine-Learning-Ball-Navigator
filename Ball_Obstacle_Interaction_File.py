# Mohamed Mudawi
# File the controls whens the ball will reflect off an obstacle, and what new degree the ball will travel in

# Interaction function (moves one frame when function is called)
def ball_interaction(display_to_user, goal_borders, ball_object_name, ball_direction, ball_borders, up_bounce, down_bounce, right_bounce, left_bounce):

    # Display the ball if true, and if false don't display
    if display_to_user:
        ball_object_name.move_ball(ball_direction)
    else:
        ball_object_name.move_ball(ball_direction, False)


    for ball_border in ball_borders:

        # Checking if the ball touched the goal borders
        for goal_border in goal_borders:
            if (ball_border[0] >= goal_border[0]-1) and (ball_border[0] <= goal_border[0]+1) and (ball_border[1] >= goal_border[1]-1) and (ball_border[1] <= goal_border[1]+1):
                return [round(ball_direction),'goal',[]] # Returning information about which degree the ball bounced, the location it bounced in,
                                                         # and which obstacle orientation it bounced in. The program will unpack this information and work with it accordingly.
                                                         # In this case it touched the goal so not a lot of information is needed because the program ends when it hits the goal
                                                         
        # If the ball is going right and hits an obstacle, bounce left
        for obstacle_border_coors in left_bounce:
            if ball_border[1] in range(obstacle_border_coors[1][0],obstacle_border_coors[1][-1]+1):
                for obstacle_border in range(obstacle_border_coors[1][0],obstacle_border_coors[1][-1]+1):

                    # Calculating the new degree the ball will head in, based on what degree the ball was going in
                    if (ball_border[0] >= obstacle_border_coors[0]-1) and (ball_border[0] <= obstacle_border_coors[0]+1) and (ball_border[1] >= obstacle_border-1) and (ball_border[1] <= obstacle_border+1):
                        if (ball_direction >= 0) and (ball_direction < 90):
                            ball_direction = 180 - ball_direction
                        elif (ball_direction > 270) and (ball_direction < 360):
                            ball_direction = (360 - ball_direction) + 180
                        return [round(ball_direction),'left',obstacle_border_coors] 

        # If the ball is going left and hits an obstacle, bounce right
        for obstacle_border_coors in right_bounce:
            if ball_border[1] in range(obstacle_border_coors[1][0],obstacle_border_coors[1][-1]+1):
                for obstacle_border in range(obstacle_border_coors[1][0],obstacle_border_coors[1][-1]+1):
                    
                    # Calculating the new degree the ball will head in, based on what degree the ball was going in
                    if (ball_border[0] >= obstacle_border_coors[0]-1) and (ball_border[0] <= obstacle_border_coors[0]+1) and (ball_border[1] >= obstacle_border-1) and (ball_border[1] <= obstacle_border+1):
                        if (ball_direction > 90) and (ball_direction <= 180):
                            ball_direction = 180 - ball_direction
                        elif (ball_direction > 180) and (ball_direction < 270):
                            ball_direction = (360 - ball_direction)+180
                        return [round(ball_direction),'right',obstacle_border_coors]

        # If the ball is going down and hits an obstacle, bounce up
        for obstacle_border_coors in up_bounce:
            if ball_border[0] in range(obstacle_border_coors[0][0],obstacle_border_coors[0][-1]+1):
                for obstacle_border in range(obstacle_border_coors[0][0],obstacle_border_coors[0][-1]+1):
                    
                    # Calculating the new degree the ball will head in, based on what degree the ball was going in
                    if (ball_border[1] >= obstacle_border_coors[1]-1) and (ball_border[1] <= obstacle_border_coors[1]+1) and (ball_border[0] >= obstacle_border-1) and (ball_border[0] <= obstacle_border+1):
                        if (ball_direction > 180) and (ball_direction <= 270):
                            ball_direction = 360 - ball_direction
                        elif (ball_direction > 270) and (ball_direction < 360):
                            ball_direction = 360 - ball_direction
                        return [round(ball_direction),'up',obstacle_border_coors]
        
        # If the ball is going up and hits an obstacle, bounce down
        for obstacle_border_coors in down_bounce:
            if ball_border[0] in range(obstacle_border_coors[0][0],obstacle_border_coors[0][-1]+1):
                for obstacle_border in range(obstacle_border_coors[0][0],obstacle_border_coors[0][-1]+1):

                    # Calculating the new degree the ball will head in, based on what degree the ball was going in
                    if (ball_border[1] >= obstacle_border_coors[1]-1) and (ball_border[1] <= obstacle_border_coors[1]+1) and (ball_border[0] >= obstacle_border-1) and (ball_border[0] <= obstacle_border+1):
                        if (ball_direction > 0) and (ball_direction <= 90):
                            ball_direction = 360 - ball_direction
                        elif (ball_direction > 90) and (ball_direction < 180):
                            ball_direction = 360 - ball_direction
                        return [round(ball_direction),'down',obstacle_border_coors]
                    
    return [ball_direction,'no bounce',[]] # The ball hasn't hit anything, so the ball will keep traveling in the direction it was headed in
