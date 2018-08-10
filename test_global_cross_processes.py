import multiprocessing

a = 0

def subprocess():
    global a
    a = 10
    print(a)

def process():
    sub = multiprocessing.Process(target=subprocess)
    sub.start()
    sub.join()
    print(a)

process()