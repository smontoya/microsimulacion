import itertools
import random

class ProcesaRanking(object):
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors

    def addToQueue(self, name):

        print('%0.3f #%s Cola de Ingreso a Ranking de Eventos' % (self.env.now, name))
        duration = 0.05
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('%0.3f #%s Acceso a BD del Eventos' % (self.env.now, name))
            duration = 0.05
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Selección de tabla de Eventos' % (self.env.now, name))
            duration = 0.1
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Realiza consulta de conteo por categoría' % (self.env.now, name))
            duration = 0.05
            yield self.env.process(self.hold(duration))


            print('%0.3f #%s Nueva ejecución de la consulta de conteo por categoría' % (self.env.now, name))
            duration = 0.1
            yield self.env.process(self.hold(duration))
            posibilidad_error = random.randint(1,100)

            while(posibilidad_error<10) :
       
	            print('Error en ejecución de consulta')
	            print('%0.3f #%s Nueva ejecución de la consulta de conteo por categoría' % (self.env.now, name))
	            duration = 0.1
	            yield self.env.process(self.hold(duration))
	            posibilidad_error = random.randint(1,100)


            print('%0.3f #%s Generación de ranking actualizado' % (self.env.now, name))
            duration = 1.5
            yield self.env.process(self.hold(duration))


            # se entrega para que lo agarre la cola de eventos
            self.eventoPE.addToQueue("%s_%s" % (name, "ACTUALIZA MAPA DE CALOR"))

    def hold(self, duration):
        yield self.env.timeout(duration)