from collections import Counter


class Card:
    def __init__(self, sign):
        SCORES = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }

        v, s = sign[:-1], sign[-1]

        self.value = v
        self.score = SCORES[v]
        self.suit = s

    def __repr__(self):
        return f"{self.value}{self.suit}"

    def __str__(self):
        return f"{self.value}{self.suit}"


def get_longest_consecutive(all_cards):
    consecutives = []

    for v in all_cards:
        for l in consecutives:
            if v.score == l[-1].score - 1:
                l.append(v)
                break
        else:
            consecutives.append([v])

    consecutives.sort(key=lambda l: len(l), reverse=True)
    longest_consecutive = consecutives[0]
    longest_consecutive.sort(key=lambda c: c.score, reverse=True)
    return longest_consecutive


def hand(hole_cards, community_cards):
    hand = [Card(c) for c in hole_cards]
    cards = [Card(c) for c in community_cards]
    all_cards = hand + cards
    all_cards.sort(key=lambda c: c.score, reverse=True)

    suit_count = Counter([c.suit for c in all_cards]).most_common()
    value_count = Counter([c.value for c in all_cards]).most_common()
    longest_consecutive = get_longest_consecutive(all_cards)

    if suit_count[0][1] >= 5:
        most_common_suit = suit_count[0][0]
        flush_cards = [c for c in all_cards if c.suit == most_common_suit]
        flush_cards.sort(key=lambda c: c.score, reverse=True)
        longest_consecutive = get_longest_consecutive(flush_cards)
        if len(longest_consecutive) >= 5:
            print("straight flush")
            result = [c.value for c in longest_consecutive[:5]]
            return "straight-flush", result
    if value_count[0][1] >= 4:
        print("four of a kind")
        most_common_value = value_count[0][0]
        other_cards = [c for c in all_cards if c.value != most_common_value]
        other_cards.sort(key=lambda c: c.score, reverse=True)
        result = [most_common_value] + [c.value for c in other_cards[:1]]
        return "four-of-a-kind", result
    if value_count[0][1] == 3 and value_count[1][1] == 2:
        print("full house")
        most_common_value = value_count[0][0]
        second_most_common_value = value_count[1][0]
        result = [most_common_value, second_most_common_value]
        return "full house", result
    if suit_count[0][1] >= 5:
        print("flush")
        most_common_suit = suit_count[0][0]
        flush_cards = [c for c in all_cards if c.suit == most_common_suit]
        flush_cards.sort(key=lambda c: c.score, reverse=True)
        result = [c.value for c in flush_cards[:5]]
        return "flush", result
    if len(longest_consecutive) >= 5:
        print("straight")
        result = [c.value for c in longest_consecutive[:5]]
        return "straight", result
    if value_count[0][1] == 3:
        print("three-of-a-kind")
        most_common_value = value_count[0][0]
        other_cards = [c for c in all_cards if c.value != most_common_value]
        other_cards.sort(key=lambda c: c.score, reverse=True)
        result = [most_common_value] + [c.value for c in other_cards[:2]]
        return "three-of-a-kind", result
    if value_count[0][1] == 2 and value_count[1][1] == 2:
        print("two pair")
        most_common_value = value_count[0][0]
        second_most_common_value = value_count[1][0]
        other_cards = [
            c
            for c in all_cards
            if c.value != most_common_value and c.value != second_most_common_value
        ]
        other_cards.sort(key=lambda c: c.score, reverse=True)
        result = [most_common_value, second_most_common_value] + [
            c.value for c in other_cards[:1]
        ]
        return "two pair", result
    if value_count[0][1] == 2:
        print("pair")
        most_common_value = value_count[0][0]
        other_cards = [c for c in all_cards if c.value != most_common_value]
        other_cards.sort(key=lambda c: c.score, reverse=True)
        result = [most_common_value] + [c.value for c in other_cards[:3]]
        return "pair", result

    return "nothing", [c.value for c in all_cards[:5]]


class test:
    @staticmethod
    def assert_equals(a, b):
        a1, a2 = a
        b1, b2 = b
        assert a1 == b1, f"({a1}, {a2}) != ({b1}, {b2})"
        assert a2 == b2, f"({a1}, {a2}) != ({b1}, {b2})"

        print(f"({a1}, {a2}) == ({b1}, {b2})")


if __name__ == "__main__":
    print("======== nothing ========")
    test.assert_equals(
        hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
        ("nothing", ["A", "K", "Q", "J", "9"]),
    )
    print("======== pair ========")
    test.assert_equals(
        hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
        ("pair", ["Q", "K", "J", "9"]),
    )
    print("======== two pair ========")
    test.assert_equals(
        hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]),
        ("two pair", ["K", "J", "9"]),
    )
    print("======== three of a kind ========")
    test.assert_equals(
        hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]),
        ("three-of-a-kind", ["Q", "J", "9"]),
    )
    print("======== straight ========")
    test.assert_equals(
        hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]),
        ("straight", ["K", "Q", "J", "10", "9"]),
    )
    print("======== flush ========")
    test.assert_equals(
        hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]),
        ("flush", ["Q", "J", "10", "5", "3"]),
    )
    print("======== full house ========")
    test.assert_equals(
        hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]),
        ("full house", ["A", "K"]),
    )
    print("======== four of a kind ========")
    test.assert_equals(
        hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]),
        ("four-of-a-kind", ["2", "3"]),
    )
    print("======== straight flush ========")
    test.assert_equals(
        hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]),
        ("straight-flush", ["J", "10", "9", "8", "7"]),
    )
