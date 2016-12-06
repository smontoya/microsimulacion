import itertools
import random


class DuplicacionInfo():
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors

    def addToQueue(self, name):
        total = 0
        print('{} {} Encolando info'.format(self.env.now, name))
        duration = 0.05
        total = total + duration
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            probabilidad = random.randint(1, 20)
            # Request one of the procesors
            yield req

            print('{} {} Analizando info'.format(self.env.now, name))
            duration = 1
            total = total + duration
            yield self.env.process(self.hold(duration))
            
            if probabilidad > 10:
                print('{} {} Eliminando info '.format(self.env.now, name))
                duration = 0.3
                yield self.env.process(self.hold(duration))
            else:
                print('{} {} Info no duplicada '.format(self.env.now, name))
                duration = 0.1
                yield self.env.process(self.hold(duration))
            total = total + duration

            print('{} {} ANALISIS INFO TERMINADA'.format(self.env.now, name))

        print('{} {} Duración Eliminacion de Duplicados: {}'.format(self.env.now, name, total))

    def hold(self, duration):
        yield self.env.timeout(duration)