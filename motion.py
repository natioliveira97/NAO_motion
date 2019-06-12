import walk
import stand
from action import session


######################################
#           Motion Variables         #
######################################

# In the motion module, we need to declare all the variables that can be changed by the competition code

X 			= 0.0 # Step size forward (negative to go backwards)
Y 			= 0.0 # Step size left (negative to go right)
Theta 		= 0.0 # Turning angle??
Frequency 	= 0.0 # Frequency of steps (min = 0.0 max = 1.0)

######################################
#          Motion Functions          #
######################################

def walk(session):
	walk.main(session, X, Y, Theta, Frequency)

def walk(session):
	stand.main(session)

