# by pwn爷爷
import angr

filename = raw_input("Input the filename:")
temp = input("Explore(1) or Run(2):")
token = int(temp)
p = angr.Project(filename)
st = p.factory.entry_state()
sm = p.factory.simgr(st)
if token == 1:
    path = input("Find address:")
    avo = input("Avoid address:")
    if avo == 0:
        sm.explore(find=path)
    else:
        sm.explore(find=path,avoid=avo)
    for pp in sm.found:
        print pp.posix.dumps(0)
    exit()
elif token == 2:
    sm.run()
    for pp in sm.deadended:
        print pp.posix.dumps(0)
    exit()