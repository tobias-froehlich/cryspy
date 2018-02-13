import numpy as np
from cryspy import numbers as nb


floatlist = []
hashlist = []

ufloatlist = []
ufloathashlist = []
maxufloathash = -1

delta = nb.delta


def floathash(number):
   return floathash_new(number)

def floathash_old(number):
    global floatlist
    global hashlist
    for i in range(len(floatlist)):
        if np.abs(number - floatlist[i]) < delta:
            return hashlist[i]
    h = hash(number)
    if len(floatlist) == 0:
        floatlist = [number]
        hashlist = [h]
    elif floatlist[0] > number:
        floatlist = [number] + floatlist
        hashlist = [h] + hashlist
    elif floatlist[-1] < number:
        floatlist = floatlist + [number]
        hashlist = hashlist + [h]
    else:
        for i in range(len(floatlist) - 1):
            if floatlist[i] < number < floatlist[i+1]:
                floatlist = floatlist[0:i+1] + [number] + floatlist[i+1:]
                hashlist = hashlist[0:i+1] + [h] + hashlist[i+1:] 
    return h

def floathash_new(number):
    global floatlist
    global hashlist
    n = len(floatlist)
    if n == 0:
        h = hash(number)
        floatlist = [number]
        hashlist = [h]
        return h
    imin = 0
    imax = n-1
    def search(imin, imax):
        global floatlist
        global hashlist
        imid = (imin + imax)//2
        if abs(floatlist[imid] - number) < delta:
            return hashlist[imid]
        else:
            if imin == imax:
                h = hash(number)
                if floatlist[imid] < number:
                    floatlist[imid+1:imid+1] = [number]
                    hashlist[imid+1:imid+1] = [h]
                else:
                    floatlist[imid:imid] = [number]
                    hashlist[imid:imid] = [h]
                return h
            else:
                if floatlist[imid] < number:
                    return search(imid+1, imax)
                else:
                    return search(imin, imid)
    return search(imin, imax)

def ufloathash_new(number):
    global ufloatlist
    global ufloathashlist
    global maxufloathash
    number = nb.Mixed(number)
    n = len(ufloatlist)
    if n == 0:
        h = 1
        ufloatlist = [number]
        ufloathashlist = [h]
        maxufloathash = h
        return h
    imin = 0
    imax = n-1
    def search(imin, imax):
        global ufloatlist
        global ufloathashlist
        global maxufloathash
        n = len(ufloatlist)
        imid = (imin + imax)//2
        if abs(ufloatlist[imid].value.n - number.value.n) < delta :
            i = imid
            while (abs(ufloatlist[i].value.n - number.value.n) < delta) and i >= 0:
                if ufloatlist[i] == number:
                    return ufloathashlist[i]
                i -= 1
            i = imid
            while (i < n) and (abs(ufloatlist[i].value.n - number.value.n) < delta):
                if ufloatlist[i] == number:
                    return ufloathashlist[i]
                i += 1
            h = maxufloathash + 1
            maxufloathash = h
            ufloatlist[i:i] = [number]
            ufloathashlist[i:i] = [h]
            return h
        else:

            if imin == imax:
                h = maxufloathash + 1
                maxufloathash = h
                if ufloatlist[imid].value.n < number.value.n:
                    ufloatlist[imid+1:imid+1] = [number]
                    ufloathashlist[imid+1:imid+1] = [h]
                else:
                    ufloatlist[imid:imid] = [number]
                    ufloathashlist[imid:imid] = [h]
                return h
            else:
                if ufloatlist[imid].value.n < number.value.n:
                    return search(imid+1, imax)
                else:
                    return search(imin, imid)
    return search(imin, imax)




def ufloathash(number):
    return ufloathash_new(number)

def ufloathash_old(number):
    global ufloatlist
    global ufloathashlist
    for i in range(len(ufloatlist)):
        if nb.uapprox(ufloatlist[i], number):
            return ufloathashlist[i]
    h = len(ufloatlist)
    ufloatlist.append(number)
    ufloathashlist.append(h)
    return h

