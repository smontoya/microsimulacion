import itertools
import random


class AnalizadorEvento(object):
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors

    def addToQueue(self, name):

        print('#%s Recibiendo informacion  en tiempo %d' % (name, self.env.now))
        duration = 0.1
        yield self.env.process(self.charge(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('%s Recibiendo informacion  en tiempo %d' % (name,
                                                               self.env.now))
            duration = 1
            yield self.env.process(self.charge(duration))

            print('%s Buscando y eliminando duplicado %d' % (name,
                                                             self.env.now))
            duration = 5
            yield self.env.process(self.charge(duration))

            # deberian ser dos hilos uno apra el semantico y otro para el
            # analizador de mapa y ranking db
            print('%s Analizando semanticamente en tiempo %d' % (name,
                                                                 self.env.now))
            duration = 3
            yield self.env.process(self.charge(duration))

            print('%s RE-Categorizando %d' % (name, self.env.now))
            duration = 3
            yield self.env.process(self.charge(duration))


    def charge(self, duration):
        yield self.env.timeout(duration)


    def generator(self, env, processors, TIME_BT_EVENT):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_BT_EVENT))
            env.process(self.addToQueue('EVENT %d' % i))
