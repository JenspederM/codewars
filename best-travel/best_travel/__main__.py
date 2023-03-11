class test:
    @classmethod
    def assert_equals(cls, a, b):
        assert a == b, f"{a} != {b}"
        print(f"{a} == {b}")


from itertools import combinations


def choose_best_sum(t, k, ls):
    # your code
    if len(ls) < k:
        return None

    combs = combinations(ls, k)
    sums = [sum(comb) for comb in combs if sum(comb) <= t]
    if sums:
        return max(sums)

    return None


if __name__ == "__main__":
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    test.assert_equals(choose_best_sum(230, 4, xs), 230)
    test.assert_equals(choose_best_sum(430, 5, xs), 430)
    test.assert_equals(choose_best_sum(430, 8, xs), None)
