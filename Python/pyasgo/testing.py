import os.path

if __name__ == '__main__':
    target = "USER"
    val = os.environ(target)
    if not val:
        print("%s not set" % target)
    else:
        print("%s=%s" % (target, val))
