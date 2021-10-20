import re
from collections import OrderedDict
od = OrderedDict()
S = raw_input().strip()
k = raw_input().strip()
i = 0
l = list()
if re.search(k,S) == None:
    print (-1,-1)
else :
    while i<len(S):
        m = re.search(k,S[i:])
        if m == None:
            break;
        else:
            p = i+m.start()
            n = (p,p+len(k)-1)
            od[i] = n
        i = i+1

    for p,s in enumerate(od.values()):
        if od.values()[p] != od.values()[p-1]:
            print s