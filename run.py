from microsimulacion.analizadorTweet import AnalizadorTweet
from microsimulacion.analizadorEvento import AnalizadorEvento
import simpy


RANDOM_SEED = 42
PROCESORS = 1     						# number of procesors
TIME_TWEET = [1, 5]        		# Create a tweet every [min, max] seconds
MESSAGE_PER_SECOND = [10, 60]			# Create a message every [min, max] seconds
SIM_TIME = 100          				# Simulation time in seconds
CATASTROPHE = ['TERREMOTO', 'INCENDIO', 'TSUNAMI', 'ACCIDENTE'] #kind of event



env = simpy.Environment()

procesors = simpy.Resource(env,PROCESORS)

cores = simpy.Container(env, 4, init=4)

tweetPE = AnalizadorTweet(env,procesors)
env.process(tweetPE.generator(env, procesors, TIME_TWEET))


# corre durante n ciclos
env.run(until=SIM_TIME)