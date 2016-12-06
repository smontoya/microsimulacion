import itertools
import random

class ProcesaMapa(object):
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors

    def addToQueue(self, name):
        total = 0
        print('%0.3f #%s Cola de Ingreso a Mapa de Calor' % (self.env.now, name))
        duration = 0.05
        total = total + duration
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('%0.3f #%s Recibe de Coordenadas del evento' % (self.env.now, name))
            duration = 0.05
            total = total + duration
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Acceso a BD del Mapa' % (self.env.now, name))
            duration = 0.05
            total = total + duration
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Selección de tabla afectada' % (self.env.now, name))
            duration = 0.1
            total = total + duration
            yield self.env.process(self.hold(duration))

            posibilidad_error = random.randint(1,100)
            print('%0.3f #%s Ejecución de la consulta' % (self.env.now, name))
            duration = 0.1
            total = total + duration
            yield self.env.process(self.hold(duration))

            while(posibilidad_error < 10) :
	            print('Error en ejecución de consulta')
	            print('%0.3f #%s Nueva ejecución de la consulta' % (self.env.now, name))
	            duration = 0.1
	            total = total + duration
	            yield self.env.process(self.hold(duration))
	            posibilidad_error = random.randint(1,100)

            print('%0.3f #%s Actualizacion de base datos' % (self.env.now, name))
            duration = 0.1
            total = total + duration
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Generación de mapa actualizado' % (self.env.now, name))
            duration = 1.5
            total = total + duration
            yield self.env.process(self.hold(duration))

        print('{} {} Duración procesar mapa: {}'.format(self.env.now, name, total))

    def hold(self, duration):
        yield self.env.timeout(duration)