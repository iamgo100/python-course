import cython as cy
from joblib import Parallel, delayed
import concurrent.futures as ftres
from functools import partial

def integrate(f, a: cy.double, b: cy.double, *, n_iter: cy.int=1000):
    h: cy.double
    x: cy.double
    s: cy.double
    h=(b-a)/n_iter
    x=a
    s=0
    while x<=b-h:
        s+=f(x)
        x+=h
    return round(h*s, 8)

def integrate_async(f, a: cy.double, b: cy.double, *, n_jobs: cy.int=2, n_iter: cy.int=1000):
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = Parallel(n_jobs=n_jobs, prefer="threads")(delayed(spawn(a + i * step, a + (i + 1) * step))(a=a, i=i, step=step) for i in range(n_jobs))
    return sum(f.result() for f in ftres.as_completed(fs))

def timer():
    from timeit import timeit
    res = timeit('integrate_async(atan, 0, pi / 2, n_jobs=2, n_iter=10**6)', number=100, setup="from __main__ import integrate_async; from math import atan, pi")
    print('1. ', res)
    res = timeit('integrate_async(atan, 0, pi / 2, n_jobs=4, n_iter=10**6)', number=100, setup="from __main__ import integrate_async; from math import atan, pi")
    print('2. ', res)
    res = timeit('integrate_async(atan, 0, pi / 2, n_jobs=6, n_iter=10**6)', number=100, setup="from __main__ import integrate_async; from math import atan, pi")
    print('3. ', res)

if __name__ == '__main__':
    timer()