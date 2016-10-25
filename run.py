from microsimulacion.analizadorTweet import AnalizadorTweet
from microsimulacion.analizadorEvento import AnalizadorEvento
import simpy


RANDOM_SEED = 42               # custom ramdom seed to control de ramdomize
PROCESORS = 3     	           # number of procesors working at the same time
TIME_BT_TWEET = [5, 15]            # Create a tweet every [min, max] seconds
TIME_BT_EVENT = [10, 60]        # Create a message every [min, max] seconds
SIM_TIME = 100                  # Simulation time in seconds
CATASTROPHE = ['TERREMOTO', 'INCENDIO',
               'TSUNAMI', 'ACCIDENTE']  # kind of event
L1_CACHE_SIZE = 1024 * 32  # 32 KB
L2_CACHE_SIZE = 1024 * 32  # 32 KB
RAM_SIZE = 2048 ** 4       # 2 GB =  2048b^4


# event manager
env = simpy.Environment()

#number of processors
procesors = simpy.Resource(env, PROCESORS)


l1_cache = simpy.Container(env, L1_CACHE_SIZE, init=0)
l2_cache = simpy.Container(env, L2_CACHE_SIZE, init=0)
ram = simpy.Container(env, RAM_SIZE, init=0)

eventoPE = AnalizadorEvento(env, procesors)
tweetPE = AnalizadorTweet(env, procesors, eventoPE)
env.process(tweetPE.generator(env, procesors, TIME_BT_TWEET))
env.process(eventoPE.generator(env, procesors, TIME_BT_EVENT))


# corre durante n ciclos
env.run(until=SIM_TIME)