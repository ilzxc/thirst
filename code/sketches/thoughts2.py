from time import localtime, clock

def prefix():
    t = localtime()
    return "{0}{1}{2}{3}{4:.4f}".format(t.tm_mon, t.tm_mday,
                                        t.tm_hour, t.tm_min,
                                        t.tm_sec + clock())
