def C(n, m):
    res = []

    def rec(i):
        if len(res) == m:
            yield res.copy()
            return

        while i < n:
            res.append(i)
            for res_t in rec(i + 1):
                yield res_t
            i += 1
            res.pop()

    for res in rec(0):
        yield res

        
def A(n, m):
    res = []
    taken = set()

    def rec(i):
        if len(res) == m:
            yield res.copy()
            return

        while i < n:
            if i not in taken:
                res.append(i)
                taken.add(i)
                for res_t in rec(0):
                    yield res_t
                res.pop()
                taken.remove(i)
            i += 1

    for res in rec(0):
        yield res


def P(n):
    res = []
    taken = set()

    def rec(i):
        if len(res) == n:
            yield res.copy()
            return

        while i < n:
            if i not in taken:
                res.append(i)
                taken.add(i)
                for res_t in rec(0):
                    yield res_t
                res.pop()
                taken.remove(i)
            i += 1

    for res in rec(0):
        yield res
