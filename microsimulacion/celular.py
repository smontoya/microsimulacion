class Celuar(object):
    # estados
    # 0 sin señal
    # 1 con señal, sin conexion
    # 2 conectado 4g

    def __init__(self):
        self.x, self.y = (0, 0)
        self.estado = 0
        self.antena_actual = None
    
    def enviar_mensaje(self):
        if self.estado == 2:

    def set_antenas_disponibles(self, antenas):


    def generator(self, env, TIME_MSG):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_MSG))
            env.process(self.enviar_mensaje('M%d' % i))
