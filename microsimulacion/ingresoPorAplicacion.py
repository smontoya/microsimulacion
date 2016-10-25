import simpy


class ingresoPorAplicacion(object):
    def __init__(self, env, procesadores):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run(procesadores))

    def run(self, procesadores):
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


