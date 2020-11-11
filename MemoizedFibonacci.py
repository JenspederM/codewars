def memoize():
    cache = {}

    def memoized_fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            if n in [0, 1]:
                return n
            else:
                result = memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)
                cache[n] = result
                return result

    return memoized_fibonacci
