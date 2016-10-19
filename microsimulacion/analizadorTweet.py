RED = '\033[95m'
NORMAL = '\033[0m'


class AnalizadorTweet(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def run(self):
        while True:

            print('Recibiendo tweet en tiempo %d' % self.env.now)
            duration = 1
            yield self.env.process(self.charge(duration))

            print('Analizando tweet %d' % self.env.now)
            duration = 5
            yield self.env.process(self.charge(duration))

            print('Tomando geo y fecha en tiempo %d' % self.env.now)
            duration = 3
            yield self.env.process(self.charge(duration))

            print('Categorizando tweett %d' % self.env.now)
            duration = 3
            yield self.env.process(self.charge(duration))


    def charge(self, duration):
        yield self.env.timeout(duration)
