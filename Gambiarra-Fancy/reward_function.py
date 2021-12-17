import math
def reward_function(params):
    '''
    Reward function for AWS deeprace
    '''
    
    x = params['x']    
    
    y = params['y']    
    
    # heading
    heading = params['heading']    
    
    # float [0, 100]
    # Percentage of the track complete.
    progress = params['progress']
    
    # integer
    # Number of steps completed. One step is one (state, action, next state, reward tuple).
    steps = params['steps']
    
    # waypoints
    # List of (float, float)
    waypoints = params['waypoints']    
    
    # closest_waypoints
    # (integer, integer)
    # Euclidean distance from the center of the vehicle.
    closest_waypoints = params['closest_waypoints']    
    
    # A boolean flag to indicate if the vehicle is on-track or off-track. 
    all_wheels_on_track = params['all_wheels_on_track']    
        
    # float [-30, 30]
    # Steering angle, in degrees
    steering_angle = params['steering_angle']
    
    # boolean
    # A Boolean flag to indicate if the vehicle is on the left side to the track 
    # center (True) or on the right side (False).
    is_left_of_center = params['is_left_of_center']
    
    # float
    # Track width in meters.
    track_width = params['track_width']
    
    
    # float [0.0, 8.0]
    # The observed speed of the vehicle, in meters per second (m/s).
    speed = params['speed']    
    
    # float [0, ~track_width/2]
    # Distance from the center of the track, in unit meters.
    distance_from_center = params['distance_from_center']
    
    reward = 1e-4
    rewardLn = 1e-4
    
    normDistance = distance_from_center/track_width
    
    BEST_DISTANCE = 0.1
    OK_DISTANCE = 0.2 
    AVG_DISTANCE = 0.35	
    BAD_DISTANCE = 0.5
    
    strPos = "UNK"
       
    # Give reward based on progress & steps
    if (steps>=3):
        reward = 5.2 + 4*math.log(progress/steps)
        rewardLn = 5.2 + 4*math.log(progress/steps)
    
    # Adjust reward for position
    if (normDistance<=BEST_DISTANCE):
        reward += 0.8        
        
    elif(normDistance<=OK_DISTANCE):
        reward +=0.64       
    
    elif (normDistance<=AVG_DISTANCE):
        reward += 0.32

    elif (normDistance<=BAD_DISTANCE):
        reward += 0.16

    else:
        reward += 1e-4
        
    if (reward <= 0):
        reward = 1e-4        
    
    return float(reward)
