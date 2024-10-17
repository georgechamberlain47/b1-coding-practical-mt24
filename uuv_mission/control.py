#Define constants to be used in controller
Kp = 0.08
Kd = 0.7

def PDcontroller(currentpos, previouspos, references, t):
    e_tcurrent = references[t]-currentpos #Calculate the current error signal
    if t > 0:
        #Provided we are not on the first data entry, calculate the previous error signal
        e_tprevious = references[t-1]-previouspos
        #Return the control action to be sent to the submarine as given
        return (Kp * e_tcurrent) + Kd * (e_tcurrent-e_tprevious)
    else:
        #If we are on the first data entry, the previous error makes no sense to calculate and is just 0
        #Therefore return the appropriate controla action to be sent to the submarine
        return (Kp * e_tcurrent) + Kd *(e_tcurrent)
 