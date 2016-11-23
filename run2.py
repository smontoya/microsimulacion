from microsimulacion.analizadorTweet import AnalizadorTweet
from microsimulacion.analizadorEvento import AnalizadorEvento
from microsimulacion.ingresoPorAplicacion import IngresoPorAplicacion
from microsimulacion.eliminaDuplicado import DuplicacionInfo
from microsimulacion.procesaMapa import ProcesaMapa
from microsimulacion.rankingEventos import ProcesaRanking
from grafica.simulacion import IniciarGrafica
from microsimulacion.red4G import Red4G
import time

import simpy
import threading


def slow_proc(env):
    time.sleep(0.002)  # Heavy computation :-)
    yield env.timeout(1)


RANDOM_SEED = 42               # custom ramdom seed to control de ramdomize
PROCESORS = 3                  # number of procesors working at the same time
TIME_BT_TWEET = [5, 15]            # Create a tweet every [min, max] seconds
TIME_BT_EVENT = [10, 60]        # Create a message every [min, max] seconds
SIM_TIME = 100                  # Simulation time in seconds
CATASTROPHE = ['TERREMOTO', 'INCENDIO', 'TSUNAMI', 'ACCIDENTE']  # kind of event
L1_CACHE_SIZE = 1024 * 32  # 32 KB
L2_CACHE_SIZE = 1024 * 32  # 32 KB
RAM_SIZE = 2048 ** 4       # 2 GB =  2048b^4

USER_PER_ANTENA = 100
ANTENAS = 6


# event manager
env = simpy.rt.RealtimeEnvironment(factor=0.01)


#number of processors
# procesors = simpy.Resource(env, PROCESORS)
antena = simpy.Resource(env, USER_PER_ANTENA * ANTENAS)
red4G = Red4G(env, antena, USER_PER_ANTENA * ANTENAS)

env.process(slow_proc(env))
grafica = IniciarGrafica(red4G)
grafica.start()

# l1_cache = simpy.Container(env, L1_CACHE_SIZE, init=0)
# l2_cache = simpy.Container(env, L2_CACHE_SIZE, init=0)
# ram = simpy.Container(env, RAM_SIZE, init=0)

# eventoPE = AnalizadorEvento(env, procesors)
# tweetPE = AnalizadorTweet(env, procesors, eventoPE)
# appPE = IngresoPorAplicacion(env, procesors, eventoPE)

# duplicadoPE = DuplicacionInfo(env, procesors)
# mapaPE = ProcesaMapa(env, procesors)
# rankingPE = ProcesaRanking(env, procesors)

# env.process(appPE.generator(env, procesors, TIME_BT_EVENT))


# env.process(red4G.generator(env, antena, [1, 2]))
env.run(1000)
