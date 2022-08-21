__doc__ = """
"When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said"

In this kata, No algorithms, only funny ;-)

Description:
"All the people hurry up! We need to take a picture. The tallest standing in the middle, and then left and right descending...All the people, hand in hand..."

Give you an array legs. It recorded the length of the legs of all the people(we assume that their upper body is the same height), please follow the above rules to arrange these people, and then complete and return the photo:

legs = [1,2,3]
After arrange --> [2,3,1]

The photo should be:
             + +   
   + +      +o o+  
  +o o+    +  u  +      + +     
 +  u  +    + ~ +      +o o+  
  + ~ +       |       +  u  + 
    |       +-o-+      + ~ +  
  +-o-+    /| o |\       |    
_/| o |\__/ +-o-+ \    +-o-+  
  +-o-+      | |   \__/| o |\_
   | |       | |       +-o-+  
   I I       I I        I I   
 
 
 
legs = [1,1,1,2,3]
After arrange --> [1,2,3,1,1]

The photo should be:
                       + +   
             + +      +o o+  
   + +      +o o+    +  u  +      + +      + +     
  +o o+    +  u  +    + ~ +      +o o+    +o o+  
 +  u  +    + ~ +       |       +  u  +  +  u  + 
  + ~ +       |       +-o-+      + ~ +    + ~ +  
    |       +-o-+    /| o |\       |        |    
  +-o-+    /| o |\__/ +-o-+ \    +-o-+    +-o-+  
_/| o |\__/ +-o-+      | |   \__/| o |\__/| o |\_
  +-o-+      | |       | |       +-o-+    +-o-+  
   I I       I I       I I        I I      I I   

Note:
- The length of array legs always be a positive odd integer, all elements are positive integers.
- The order is tallest in the middle, then left, then right, then left, then right..
- If necessary, please add some spaces on both sides.
- Please pay attention to "hand in hand". You can assume that their arms are retractable ;-)
"""


from typing import List


class Person:
    def __init__(self, legs: int):
        self.body = self.create_body(legs)
        self.legs = [legs]
        self.has_arms = False

    @property
    def height(self):
        return len(self.body)

    @property
    def arm_start(self):
        return self.height - 5

    def __str__(self) -> str:
        self.add_ws_side()
        return "\n".join(self.body)

    def __repr__(self) -> str:
        return "Person(legs=%s, height=%s)" % (self.legs, self.height)

    def add_ws_top(self, ws: int):
        for _ in range(ws):
            self.body.insert(0, " " * len(self.body[0]))

    def add_ws_side(self):
        max_len = max(len(p) for p in self.body)
        min_len = min(len(p) for p in self.body)
        delta = (max_len - min_len) / 2
        ws = " " * int(delta)
        self.body = [ws + p + ws if len(p) != max_len else p for p in self.body]

    @staticmethod
    def create_body(legs: int):
        body_parts = [" + + ", "+o o+", "+ ~ +", "  |  ", "+-o-+", "| o |", "+-o-+"]

        for _ in range(legs - 1):
            body_parts.append(" | | ")

        body_parts.append(" I I ")

        return body_parts

    def __len__(self):
        return len(self.body)

    def add_arms(self, other=None):
        if not self.has_arms:
            self.body[-self.arm_start] = "_/" + self.body[-self.arm_start] + "\\_"
            self.add_ws_side()
            self.has_arms = True
        return self

    def merge(self, other):
        # Add arms

        self.add_arms(other)
        other.add_arms(self)

        # Add whitespace to top
        delta = abs(len(self) - len(other))

        if delta != 0:
            if len(self) > len(other):
                other.add_ws_top(delta)
            else:
                self.add_ws_top(delta)

        # Construct new body by merging self and other person
        new_body = []

        for elem in zip(self.body, other.body):
            new_body.append(" ".join(elem))

        # Append legs of other to self
        self.legs = self.legs + other.legs

        # Update self.body
        self.body = new_body

        return self


def arrange_by_height(legs: List[int]):
    legs.sort(reverse=True)
    ret = []

    for i in range(len(legs)):
        if i % 2 == 0:
            ret.append(legs[i])
        else:
            ret.insert(0, legs[i])

    return ret


def merge_people(l: List[Person]):
    if len(l) == 1:
        return "\n".join(l[0].body)

    p1 = l.pop(0)
    p2 = l.pop(0)

    l.insert(0, p1.merge(p2))

    return merge_people(l)


def pattern(legs: List[int]):
    # Arrange people according to height
    arranged_people = arrange_by_height(legs)

    # Make people
    people = [Person(i) for i in arranged_people]

    # Merge people
    return merge_people(people)


if __name__ == "__main__":
    print("-" * 50)
    print(pattern([1, 2, 3]))
    print("-" * 50)
    print(pattern([1, 1, 1, 2, 3]))
    print("-" * 50)
