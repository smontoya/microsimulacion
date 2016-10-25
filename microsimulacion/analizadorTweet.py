import itertools
import random
class AnalizadorTweet(object):
    def __init__(self, env, processors):
        self.env = env
        # Start the run process everytime an instance is created.
        self.processors = processors
    def run(self,name, processors,TIME_TWEET):
        print('#%s Recibiendo tweet en tiempo %d' % (name, self.env.now))
        duration = 1
        yield self.env.process(self.charge(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('#%s Analizando tweet %d' % (name, self.env.now))
            duration = 5
            yield self.env.process(self.charge(duration))

            print('#%s Tomando geo y fecha en tiempo %d' % (name, self.env.now))
            duration = 3
            yield self.env.process(self.charge(duration))

            print('#%s Categorizando tweett %d' % (name, self.env.now))
            duration = 3
            yield self.env.process(self.charge(duration))
            print('#%s ANALIZADO %d' % (name, self.env.now))



    def charge(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_TWEET):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_TWEET))
            env.process(self.run('Tweet %d' % i, env, processors))



