import itertools
import random
class IngresoPorAplicacion(object):
    def __init__(self, env, processors, eventoPE):
        self.env = env
        self.processors = processors
        self.eventoPE = eventoPE

    def addToQueue(self, name):

        print('%0.3f #%s Encolando ingreso por App' % (self.env.now, name))
        duration = 0.05
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('%0.3f #%s ANALISIS DE INGRESO POR APP TERMINADO' % (self.env.now, name))

            # se entrega para que lo agarre la cola de eventos
            self.eventoPE.addToQueue("%s_%s" % (name, "EVENTO"))

    def hold(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_APP):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_APP))
            env.process(self.addToQueue('ingreso por aplicación %d' % i))