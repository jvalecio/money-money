import numpy as np

def interest(args):
    ans = np.zeros((args.n,))
    ans[0] = args.c

    for i in range(1,args.n):
        it = (ans[i-1])*(1+args.j) + args.r
        ans[i] = np.round(it,2)

    return ans