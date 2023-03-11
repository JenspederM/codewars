class Duration:
    def __init__(self, seconds):
        self.seconds = seconds
        self.minutes = 0
        self.hours = 0
        self.days = 0
        self.years = 0
        self._calculate()

    def _calculate(self):
        self.years = self.seconds // 31536000
        self.seconds %= 31536000
        self.days = self.seconds // 86400
        self.seconds %= 86400
        self.hours = self.seconds // 3600
        self.seconds %= 3600
        self.minutes = self.seconds // 60
        self.seconds %= 60

    def __str__(self):
        components = []

        if self.years:
            components.append(f"{self.years} year{'s' if self.years > 1 else ''}")
        if self.days:
            components.append(f"{self.days} day{'s' if self.days > 1 else ''}")
        if self.hours:
            components.append(f"{self.hours} hour{'s' if self.hours > 1 else ''}")
        if self.minutes:
            components.append(f"{self.minutes} minute{'s' if self.minutes > 1 else ''}")
        if self.seconds:
            components.append(f"{self.seconds} second{'s' if self.seconds > 1 else ''}")

        if len(components) == 1:
            return components[0]
        elif len(components) == 2:
            return f"{components[0]} and {components[1]}"
        elif len(components) > 2:
            return ", ".join(components[:-1]) + f" and {components[-1]}"


def format_duration(seconds):
    if seconds == 0:
        return "now"

    return str(Duration(seconds))


class test:
    @staticmethod
    def assert_equals(a, b):
        assert a == b, f"{a} != {b}"
        print(f"{a} == {b}")


if __name__ == "__main__":
    test.assert_equals(format_duration(1), "1 second")
    test.assert_equals(format_duration(62), "1 minute and 2 seconds")
    test.assert_equals(format_duration(120), "2 minutes")
    test.assert_equals(format_duration(3600), "1 hour")
    test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
