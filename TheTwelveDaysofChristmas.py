__doc__ = """
## Return the lyrics of the song The Twelve Days of Christmas:

On the First day of Christmas
My true love sent to me
A partridge in a pear tree.

On the Second day of Christmas
My true love sent to me
Two turtle doves, and
A partridge in a pear tree.

...

[
"On the Twelfth day of Christmas",
"My true love sent to me",
"Twelve drummers drumming,",
"Eleven pipers piping,",
"Ten lords a-leaping,",
"Nine ladies dancing,",
"Eight maids a-milking,",
"Seven swans a-swimming,",
"Six geese a-laying,",
"Five gold rings,",
"Four calling birds,",
"Three French hens,",
"Two turtle doves, and",
"A partridge in a pear tree.",
]

## Your code can be maximum 510 characters long. Oh, and no imports, please!
"""


def gg(i):
    return [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth',
        'Sixth',
        'Seventh',
        'Eight',
        'Ninth',
        'Tenth',
        'Eleventh',
        'Twelfth',
    ][i]


def lg(i):
    return ["Twelve drummers drumming,",
            "Eleven pipers piping,",
            "Ten lords a-leaping,",
            "Nine ladies dancing,",
            "Eight maids a-milking,",
            "Seven swans a-swimming,",
            "Six geese a-laying,",
            "Five gold rings,",
            "Four calling birds,",
            "Three French hens,",
            "Two turtle doves, and",
            "A partridge in a pear tree."
            ][::-1][:i + 1][::-1]


ds = [
    'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eight',
    'Ninth', 'Tenth', 'Eleventh', 'Twelfth',
]

ls = ["Twelve drummers drumming,",
      "Eleven pipers piping,",
      "Ten lords a-leaping,",
      "Nine ladies dancing,",
      "Eight maids a-milking,",
      "Seven swans a-swimming,",
      "Six geese a-laying,",
      "Five gold rings,",
      "Four calling birds,",
      "Three French hens,",
      "Two turtle doves, and",
      "A partridge in a pear tree."]
gd = lambda i: [f"On the {ds[i]} day of Christmas", 'My true love sent to me']
gl = lambda i: ls[::-1][:i + 1][::-1]


def f():
    return "\n".join(["\n".join(gd(i) + gl(i) + ['']) for i in range(12)])


if __name__ == '__main__':
    print(f())

"""
    for i in range(len(days)):
        string = "\n".join([f"On the {days[i]} day of Christmas", 'My true love sent to me'] + lines[:i + 1])
        print(f'{string}')
        print()
"""


class EventParser:
    def __init__(self):
        self._parser = {
            'telegram1': self._parse_telegram1
        }

    def parse_event(self, event):
        parser = self._parser[event['telegram_name']]
        return parser(event)

    @staticmethod
    def _parse_telegram1(event):
        return event
