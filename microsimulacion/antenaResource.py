import simpy


class AntenaResource(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
        self.procesos_actuales = 0

    def request(self, *args, **kwargs):
        self.procesos_actuales += 1
        if self.procesos_actuales > 600:
            self.procesos_actuales -= 1
        self.data.append((self._env.now, self.procesos_actuales))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        self.procesos_actuales -= 1
        return super().release(*args, **kwargs)
