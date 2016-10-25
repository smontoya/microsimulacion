import itertools
import random
# TWEET_SIZE = 140 char * 4 (utf-8) = 560 bytes


class AnalizadorTweet(object):
    def __init__(self, env, processors, eventoPE):
        self.env = env
        self.processors = processors
        self.eventoPE = eventoPE

    def addToQueue(self, name):

        print('%0.3f #%s Encolando tweet' % (self.env.now, name))
        duration = 0.05
        yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('%0.3f #%s Analizando tweet' % (self.env.now, name))
            duration = 2
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Tomando geo y fecha ' % (self.env.now, name))
            duration = 0.5
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s Categorizando tweett' % (self.env.now, name))
            duration = 2
            yield self.env.process(self.hold(duration))

            print('%0.3f #%s ANALISIS TERMINADO' % (self.env.now, name))

            # se entrega para que lo agarre la cola de eventos
            self.eventoPE.addToQueue("%s_%s" % (name, "EVENTO"))

    def hold(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_TWEET):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_TWEET))
            env.process(self.addToQueue('Tweet %d' % i))