import threading

a = 0

def subthread():
    global a
    a = 10
    print(a)

def process():
    sub = threading.Thread(target=subthread)
    sub.start()
    sub.join()
    print(a)

process()