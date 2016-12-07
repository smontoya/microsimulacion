import itertools
import random
# TWEET_SIZE = 140 char * 4 (utf-8) = 560 bytes


class AnalizadorTweet(object):
    def __init__(self, env, processors, eventoPE):
        self.env = env
        self.processors = processors
        self.eventoPE = eventoPE
        self.data = []
        self.entrantes = 0
        self.salientes = 0

    def addToQueue(self, name):
        total = 0
        start = self.env.now
        self.entrantes += 1

        with self.processors.request() as req:
            print('%0.3f #%s Encolando tweet' % (self.env.now, name))
            duration = 0.05 + self.processors.getUsage() / 100
            yield self.env.process(self.hold(duration))
            # Request one of the procesors
            yield req

        with self.processors.request() as req:
            print('%0.3f #%s Analizando tweet' % (self.env.now, name))
            duration = 2 + self.processors.getUsage() / 100
            yield req
            yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            print('%0.3f #%s Tomando geo y fecha ' % (self.env.now, name))
            duration = 1 + self.processors.getUsage() / 100
            yield self.env.process(self.hold(duration))

        with self.processors.request() as req:
            print('%0.3f #%s Categorizando tweett' % (self.env.now, name))
            duration = 2 + self.processors.getUsage() / 100
            yield self.env.process(self.hold(duration))
            print('%0.3f #%s ANALISIS TWEET TERMINADO' % (self.env.now, name))
            # se entrega para que lo agarre la cola de eventos
            self.eventoPE.addToQueue("%s_%s" % (name, "EVENTO"))
        end = self.env.now
        total = end - start
        self.data.append([name, total])
        self.salientes += 1
        print('{} {} Duración Analizador de Twwet: {}'.format(self.env.now, name, total))

    def hold(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_TWEET):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_TWEET) /10)
            env.process(self.addToQueue('Tweet %d' % i))
