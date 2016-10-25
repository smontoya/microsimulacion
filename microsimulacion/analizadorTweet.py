import itertools
import random
# TWEET_SIZE = 140 char * 4 (utf-8) = 560 bytes


class AnalizadorTweet(object):
    def __init__(self, env, processors, eventoPE):
        self.env = env
        self.processors = processors
        self.eventoPE = eventoPE


    def addToQueue(self, name):

        print('#%s Encolando tweet en tiempo %d' % (name, self.env.now))
        duration = 0.1
        yield self.env.process(self.charge(duration))

        with self.processors.request() as req:
            start = self.env.now
            # Request one of the procesors
            yield req

            print('#%s Analizando tweet %d' % (name, self.env.now))
            duration = 4
            yield self.env.process(self.charge(duration))

            print('#%s Tomando geo y fecha en tiempo %d' % (name,
                                                            self.env.now))
            duration = 2
            yield self.env.process(self.charge(duration))

            print('#%s Categorizando tweett %d' % (name, self.env.now))
            duration = 3
            yield self.env.process(self.charge(duration))
            print('#%s ANALIZADO Completamente %s %d' % (name, '='*10,
                                                         self.env.now))
            self.eventoPE.addToQueue("%s - %s" % (name, "EVENTO"))






    def charge(self, duration):
        yield self.env.timeout(duration)

    def generator(self, env, processors, TIME_TWEET):
        for i in itertools.count():
            yield env.timeout(random.randint(*TIME_TWEET))
            env.process(self.addToQueue('Tweet %d' % i))




