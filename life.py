import numpy as np

def count_neighbours(a):
    res = np.zeros(a.shape)
    b = np.copy(a)
    res += np.roll(b, (-1, -1), axis=(0, 1))
    res += np.roll(b, (0, -1), axis=(0, 1))
    res += np.roll(b, (1, -1), axis=(0, 1))
    res += np.roll(b, (-1, 0), axis=(0, 1))
    res += np.roll(b, (1, 0), axis=(0, 1))
    res += np.roll(b, (-1, 1), axis=(0, 1))
    res += np.roll(b, (0, 1), axis=(0, 1))
    res += np.roll(b, (1, 1), axis=(0, 1))
    return res

def iterate(a):
    nbs = count_neighbours(a)
    res = np.zeros(a.shape)
    res[(nbs==3)|((nbs==2)&(a==1))] = 1
    return res

def printable(a):
    res = np.empty(a.shape, dtype='<U1')
    res[a==1] = '*'
    res[a!=1] = ' '
    return res

def main():
    a = np.random.randint(0, 2, (10, 10))
    print(a)
    iters = '1'
    while iters != '0':
        print('==============================================================')
        a = iterate(a)
        print('\n'.join(map(''.join, printable(a).tolist())))
        iters = input()


if __name__ == '__main__':
    main()