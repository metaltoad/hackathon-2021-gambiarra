import math
def reward_function(params):
    '''
    Reward function
    Gambiarra-Fancy AWS deeprace model training.
    '''
    
    # float [0, 100]
    # Percentage of the track complete.
    progress = params['progress']
    
    # integer
    # Number of steps completed. One step is one (state, action, next state, reward tuple).
    steps = params['steps']
    
    # float
    # Track width in meters.
    track_width = params['track_width']    
    
    # float [0, ~track_width/2]
    # Distance from the center of the track, in unit meters.
    distance_from_center = params['distance_from_center']
    
    # Starting reward (VERY LOW)
    reward = 1e-4
    
    normDistance = distance_from_center/track_width
    
    BEST_DISTANCE = 0.1
    OK_DISTANCE = 0.2 
    AVG_DISTANCE = 0.35	
    BAD_DISTANCE = 0.5
       
    # Give reward based on progress & steps
    if (steps>=3):
        reward = 5.2 + 4*math.log(progress/steps)
    
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