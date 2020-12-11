def cube(x): return pow(x, 3)


def fibonacci(n):
    lis = [0, 1]
    for i in range(2, n):
        lis.append(lis[i - 2] + lis[i - 1])
    return(lis[0:n])


if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
