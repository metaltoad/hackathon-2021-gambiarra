import math
def reward_function(params):
    '''
    Reward function for AWS deeprace
    '''
    
    # Read input parameters. Copy from the InputParamater.py        

    reward = 1e-4
    rewardLn = 1e-4
    
    normDistance = distance_from_center/track_width
    
    BEST_DISTANCE = 0.1
    OK_DISTANCE = 0.2 
    AVG_DISTANCE = 0.35	
    BAD_DISTANCE = 0.5  # The rest is impossible to save, we call its IMM
    
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