power2n = [None]*10000
power2n[0] = 0
power2n[1] = 1

def power2n_d(n):
    if n < 0:
        if not power2n[n] is None: 
            return power2n[n]
        power2n[n] = power2n_d(n - 1) + power2n_d(n - 2)
        return power2n[n]

print('power2n(40)=', power2n_d(40))