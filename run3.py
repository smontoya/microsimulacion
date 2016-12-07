from microsimulacion.analizadorTweet import AnalizadorTweet
from microsimulacion.analizadorEvento import AnalizadorEvento
from microsimulacion.ingresoPorAplicacion import IngresoPorAplicacion
from microsimulacion.eliminaDuplicado import DuplicacionInfo
from microsimulacion.procesaMapa import ProcesaMapa
from microsimulacion.rankingEventos import ProcesaRanking
from microsimulacion.procesador import ProcesadorResource
from microsimulacion.antenaResource import AntenaResource
from microsimulacion.red4G import Red4G
from functools import partial, wraps
import simpy


RANDOM_SEED = 643              # custom ramdom seed to control de ramdomize
PROCESORS = 8                  # number of core per processor at the same time
TIME_BT_TWEET = [1, 3]         # Create a tweet every [min, max] seconds
TIME_BT_EVENT = [3, 9]       # Create a message every [min, max] seconds
SIM_TIME = 1000                # Simulation time in seconds
CATASTROPHE = ['TERREMOTO', 'INCENDIO',
               'TSUNAMI', 'ACCIDENTE']  # kind of event

USER_PER_ANTENA = 100
ANTENAS = 6 * USER_PER_ANTENA

RAM_SIZE = 2048 ** 4       # 2 GB =  2048b^4


# event manager
env = simpy.Environment()

#number of processors
procesors = ProcesadorResource(env, PROCESORS)
antenas_processors = AntenaResource(env, ANTENAS)


ram = simpy.Container(env, RAM_SIZE, init=0)

eventoPE = AnalizadorEvento(env, procesors)
tweetPE = AnalizadorTweet(env, procesors, eventoPE)
appPE = IngresoPorAplicacion(env, procesors, eventoPE)
red4G = Red4G(env, antenas_processors, eventoPE)

duplicadoPE = DuplicacionInfo(env, procesors)
mapaPE = ProcesaMapa(env, procesors)
rankingPE = ProcesaRanking(env, procesors)

env.process(tweetPE.generator(env, procesors, TIME_BT_TWEET))
env.process(eventoPE.generator(env, procesors, TIME_BT_EVENT))
env.process(red4G.generator(env, antenas_processors, TIME_BT_EVENT))
# env.process(tweetPE.ProcessChecker(env, fuel_pump))


# corre durante n tiempo
env.run(until=SIM_TIME)

def crear_registro(nombre, listado):
    fileData = open(str(nombre+".txt"), "w")
    for data in listado:
        datastr = "%s|%s\n" %(str(data[0]), str(data[1]))
        fileData.write(datastr)
    fileData.close()


crear_registro("tiempo_pe_tweet", tweetPE.data)
crear_registro("uso_procesadores", procesors.data)
crear_registro("troutput_tweet", [[tweetPE.entrantes, tweetPE.salientes]])

crear_registro("tiempo_pe_app", eventoPE.data)
crear_registro("troutput_ingreso_x_app", [[eventoPE.entrantes, eventoPE.salientes]])

crear_registro("tiempo_conexion_antenas", red4G.data)
crear_registro("uso_antenas", antenas_processors.data)
crear_registro("troutput_antenas", [[red4G.entrantes, red4G.salientes]])
