"""Growth of a population
In a small town the population is p0 = 1000 at the beginning of a year.
The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
"""


def nb_year(p0: int, percent: float, aug: int, p: int):
    y = 0
    np = p0
    pc = percent / 100

    while np < p:
        np += int((np * pc) + aug)
        y += 1

    return y


def run_tests():
    print(nb_year(1000, 2.0, 50, 1214) == 15)
    print(nb_year(1500000, 2.5, 10000, 2000000) == 10)
    print(nb_year(1500000, 0.25, 1000, 2000000) == 94)


if __name__ == '__main__':
    run_tests()
