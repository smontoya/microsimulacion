import itertools
import random
class ingresoPorAplicacion(object):
    def __init__(self, env, processors):
        self.env = env
        self.processors = processors
        
    def run(self,name, processors,CREATION_TIME_APP):
        contador_dato = 0
        while True:
            with procesadores as req:
                yield req
            contador_dato + 1
            print('Leyendo informacion  enviada por usuario %i en tiempo %d' % contador_dato % self.env.now)
            lecture_duration = 1
            yield self.env.process(self.charge(lecture_duration))

            print('Enviando datos ingresados a la BD en tiempo%d' % self.env.now)
            database_duration = 3
            yield self.env.process(self.charge(database_duration))

            print('Enviando mensaje de respuesta a usuario %d' % self.env.now)
            message_duration = 3
            yield self.env.process(self.charge(message_duration))


    def charge(self, duration):
        yield self.env.timeout(duration)


