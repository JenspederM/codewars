def get_pins(observed):
    """
    He noted the PIN 1357, but he also said, it is possible that each of
    the digits he saw could actually be another adjacent digit (horizontally or
    vertically, but not diagonally). E.g. instead of the 1 it could also be the
    2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

    He also mentioned, he knows this kind of locks. You can enter an unlimited
    amount of wrong PINs, they never finally lock the system or sound the alarm.
    That's why we can try out all possible (*) variations.

    * possible in sense of: the observed PIN itself and all variations
    considering the adjacent digits

    Can you help us to find all those variations? It would be nice to have a
    function, that returns an array (or a list in Java and C#) of all variations
    for an observed PIN with a length of 1 to 8 digits. We could name the
    function getPINs (get_pins in python, GetPINs in C#). But please note
    that all PINs, the observed one and also the results, must be strings,
    because of potentially leading '0's. We already prepared some test cases
    for you.

    Detective, we are counting on you!

    For C# user: Do not use Mono. Mono is too slower when run your code.
    :param observed: Pin
    :return: list of possible pins
    :example: test.describe('example tests')
    expectations = [('8', ['5','7','8','9','0']),
                    ('11',["11", "22", "44", "12", "21", "14", "41", "24",
                    "42"]),
                    ('369', ["339","366","399","658","636","258","268","669",
                    "668","266","369","398","256","296","259","368","638","396",
                    "238","356","659","639","666","359","336","299","338","696",
                    "269","358","656","698","699","298","236","239"])]

    for tup in expectations:
      test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])
    """
    keypad = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9'],
              ['None', '0', 'None']]
    res = []
    for i in range(3):
        for j in range(3):
            d = keypad[i][j]
            if d in observed:
                l = j - 1
                r = j + 1
                u = i - 1
                d = j + 1
