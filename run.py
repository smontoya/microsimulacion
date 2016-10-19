from microsimulacion.analizadorTweet import AnalizadorTweet
from microsimulacion.analizadorEvento import AnalizadorEvento
import simpy


env = simpy.Environment()

tweetPE = AnalizadorTweet(env)
# corre durante n ciclos
env.run(until=50)
