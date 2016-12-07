import simpy
import math


class ProcesadorResource(simpy.Resource):
    def __init__(self, env, capacity, *args, **kwargs):
        capacity = capacity / 2
        super().__init__(env, capacity, *args, **kwargs)
        
        self.data = []
        self.procesando = 0

    def request(self, *args, **kwargs):
        self.procesando = self.capacity*2 if self.procesando >= self.capacity*2 else self.procesando + 1
        self.data.append((self._env.now, int(math.fabs(self.procesando))))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        self.procesando -= 1
        return super().release(*args, **kwargs)

    def getUsage(self):
        return math.fabs(self.procesando)