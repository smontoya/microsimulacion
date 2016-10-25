import itertools
import random


class DuplicacionInfo():
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors

    def addToQueue(self, name):

        print('{} {} Encolando info'.format(self.env.now, name))
        duration = 0.05
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            probabilidad = random.randint(1, 20)
            # Request one of the procesors
            yield req

            print('{} {} Analizando info'.format(self.env.now, name))
            duration = 1
            yield self.env.process(self.hold(duration))
            
            if probabilidad > 10:
                print('{} {} Eliminando info '.format(self.env.now, name))
                duration = 0.3
                yield self.env.process(self.hold(duration))
            else:
                print('{} {} Info no duplicada '.format(self.env.now, name))
                duration = 0.1
                yield self.env.process(self.hold(duration))

            print('{} {} ANALISIS INFO TERMINADA'.format(self.env.now, name))

    def hold(self, duration):
        yield self.env.timeout(duration)