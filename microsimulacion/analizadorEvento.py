import simpy


class AnalizadorEvento(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Recibiendo informacion  en tiempo %d' % self.env.now)
            duration = 1
            yield self.env.process(self.charge(duration))

            print('Buscando y eliminando duplicado %d' % self.env.now)
            duration = 5
            yield self.env.process(self.charge(duration))

            # deberian ser dos hilos uno apra el semantico y otro para el
            # analizador de mapa y ranking db
            print('Analizando semanticamente en tiempo %d' % self.env.now)
            duration = 3
            yield self.env.process(self.charge(duration))

            print('Categorizando tweett %d' % self.env.now)
            duration = 3
            yield self.env.process(self.charge(duration))


    def charge(self, duration):
        yield self.env.timeout(duration)


