def solution(n):
    def f(n):
        if n == 1:
            return [0]
        else:
            a = f(n-1)
            for i in range(len(a)-1, -1, -1):
                if a[i]:
                    a.append(0)
                else:
                    a.append(1)
            a.insert(len(a)//2, 0)
            return a
    return f(n)