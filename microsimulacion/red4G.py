import itertools
import random


class Red4G(object):
    def __init__(self, env, espacio_disponibles, trafico):
        self.env = env
        self.espacio_disponibles = espacio_disponibles
        self.trafico = trafico

    def addToQueue(self, name):
        print("entro ", name)
        print('%0.3f #%s Solicitando acceso 4G' % (self.env.now, name))
        duration = 0.01
        yield self.env.process(self.hold(duration))

        with self.espacio_disponibles.request() as req:
            start = self.env.now
            yield req

            print('{} {} Source eNB -> UE: Control de la medida'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} UE, Source eNB / Source eNB, Target eNB, MME, Serving Gateway -> Paquete de datos'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> UE: Asignación de UL'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} UE -> Source eNB: Informe de medición'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} HO Decision'.format(self.env.now, name))
            duration = 0.001 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> Target eNB: Solicitud de traspaso'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Target eNB -> Source eNB: Solicitud de traspaso ACK'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> UE: Asignación de DL'.format(self.env.now, name))
            duration = 0.04 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> UE: Reconfiguración de la conexión RRC'.format(self.env.now, name))
            duration = 0.04 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> Target eNB: Transmisor de status SN'.format(self.env.now, name))
            duration = 0.04 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> Target eNB: Reenvío de datos'.format(self.env.now, name))
            duration = 0.04 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> Target eNB: Reenvío de datos'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} UE, Source eNB, Target eNB -> Sincronización'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Target eNB, Source eNB, UE -> Asignación de UL + TA para UE'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} UE, Source eNB, Target eNB -> Reconfiguración de la conexión RRC completo'.format(self.env.now, name))
            duration = 0.001 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} UE, Source eNB, Target eNB -> Paquete de datos'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Target eNB, MME, Serving Gateway -> Paquete de datos'.format(self.env.now, name))
            duration = 0.03 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Target eNB -> MME: Solicitud de interruptor de URL'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} MME -> Serving Gateway: Solicitud de actualización del plano del usuario'.format(self.env.now, name))
            duration = 0.04 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Serving Gateway, MME, Target eNB, Source eNB -> Marcador final'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Serving Gateway, MME, Target eNB -> Paquete de datos'.format(self.env.now, name))
            duration = 0.03 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Source eNB -> Target eNB: Marcador final'.format(self.env.now, name))
            duration = 0.01 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Serving Gateway -> MME: Solicitud de actualización del plano del usuario'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} MME -> Target eNB: Solicitud de interruptor de URL ACK'.format(self.env.now, name))
            duration = 0.02 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} MME -> Target eNB: Solicitud de interruptor de URL ACK'.format(self.env.now, name))
            duration = 0.002 + self.trafico
            yield self.env.process(self.hold(duration))

            print('{} {} Target eNB -> Source eNB: Liberación de contexto de UE'.format(self.env.now, name))
            duration = 0.05 + self.trafico
            yield self.env.process(self.hold(duration))

    def hold(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_APP):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_APP))
            env.process(self.addToQueue('Ingreso 4g %d' % i))