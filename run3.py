from microsimulacion.analizadorTweet import AnalizadorTweet
from microsimulacion.analizadorEvento import AnalizadorEvento
from microsimulacion.ingresoPorAplicacion import IngresoPorAplicacion
from microsimulacion.eliminaDuplicado import DuplicacionInfo
from microsimulacion.procesaMapa import ProcesaMapa
from microsimulacion.rankingEventos import ProcesaRanking
from microsimulacion.procesador import ProcesadorResource
from functools import partial, wraps

import simpy


RANDOM_SEED = 42               # custom ramdom seed to control de ramdomize
PROCESORS = 8                  # number of core per processor at the same time
TIME_BT_TWEET = [1, 2]         # Create a tweet every [min, max] seconds
TIME_BT_EVENT = [15, 30]       # Create a message every [min, max] seconds
SIM_TIME = 100                 # Simulation time in seconds
CATASTROPHE = ['TERREMOTO', 'INCENDIO',
               'TSUNAMI', 'ACCIDENTE']  # kind of event

RAM_SIZE = 2048 ** 4       # 2 GB =  2048b^4


# event manager
env = simpy.Environment()

#number of processors
procesors = ProcesadorResource(env, PROCESORS)


ram = simpy.Container(env, RAM_SIZE, init=0)

eventoPE = AnalizadorEvento(env, procesors)
tweetPE = AnalizadorTweet(env, procesors, eventoPE)
appPE = IngresoPorAplicacion(env, procesors, eventoPE)


duplicadoPE = DuplicacionInfo(env, procesors)
mapaPE = ProcesaMapa(env, procesors)
rankingPE = ProcesaRanking(env, procesors)

env.process(tweetPE.generator(env, procesors, TIME_BT_TWEET))
env.process(appPE.generator(env, procesors, TIME_BT_EVENT))
# env.process(tweetPE.ProcessChecker(env, fuel_pump))




# corre durante n tiempo
env.run(until=SIM_TIME)

for data in procesors.data:
    print(data)
