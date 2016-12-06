import itertools
import random


class AnalizadorEvento(object):
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors

    def addToQueue(self, name):
        total = 0
        print('%0.3f #%s Recibiendo informacion.' % (self.env.now, name))
        duration = 0.05
        total = total + duration
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

        with self.processors.request() as req:
            # deberian ser dos hilos uno apra el semantico y otro para el
            # analizador de mapa y ranking db
            print('%0.3f %s Analizando semánticamente ' % (self.env.now, name))
            duration = 1
            total = total + duration
            yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            print('%0.3f %s Análsis de Categoria' % (self.env.now, name))
            duration = 0.5
            total = total + duration
            yield self.env.process(self.hold(duration))
            posibilidad_error = random.randint(1,50)

            while(posibilidad_error < 10):
                print('%0.3f %s Análsis de Categoria' % (self.env.now, name))
                duration = 0.5
                total = total + duration
                yield self.env.process(self.hold(duration))
                posibilidad_error = random.randint(1,100)

            print('%0.3f %s Agregando a BD' % (self.env.now, name))
            duration = 0.1
            total = total + duration
            yield self.env.process(self.hold(duration))

        print('{} {} Duración Analizador de Eventos: {}'.format(self.env.now, name, total))

    def hold(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_BT_EVENT):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_BT_EVENT))
            env.process(self.addToQueue('EVENT %d' % i))
