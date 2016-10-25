import simpy 

res = simpy.Resource(env, capacity=1)

def print_stats(res):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)

def user(res):
    print_stats(res)
    with res.request() as req:
        yield req
        print_stats(res)
    print_stats(res)

#procs = [env.process(user(res)), env.process(user(res))]
env.run()
