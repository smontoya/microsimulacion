import simpy 

class Procesador(object):
	def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())
        
	processors = simpy.Resource(self.env, capacity=4)