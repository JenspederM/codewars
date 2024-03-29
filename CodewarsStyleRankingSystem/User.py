import logging

log = logging.getLogger(__name__)

class User:
    """Class defining a User.
    
    Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

    Business Rules:
        - A user starts at rank -8 and can progress all the way to 8.
        - There is no 0 (zero) rank. The next rank after -1 is 1.
        - Users will complete activities. These activities also have ranks.
        - Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
        - The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
        - A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
        - Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression).
        - A user cannot progress beyond rank 8.
        - The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.
    
    The progress is scored like so:

        - Completing an activity that is ranked the same as that of the user's will be worth 3 points
        - Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
        - Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
        - Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.
    
    Logic Examples:
        - If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
        - If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
        - If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
        - If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank
        - If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
    """

    _available_ranks = [i for i in range(-8, 9) if i != 0]
    _rank_max = max(_available_ranks)
    _rank_len = len(_available_ranks) - 1


    def __init__(self, verbose=False) -> None:
        self.xp = 0
        self.verbose = verbose
        self.debug_print(None, None)

    @property
    def progress(self):
        if self.rank == self._rank_max:
            return 0

        return self.xp % 100
    
    @property
    def rank(self):
        new_rank = self._available_ranks[min(self.xp // 100, self._rank_len)]
        if new_rank < self._rank_max:
            return new_rank
        else:
            return self._rank_max
    
    def __repr__(self):
        return f"User(rank={self.rank}, progress={self.progress})"
    
    def debug_print(self, delta, increment):
        log.debug("{}, {}, {}".format(self, delta, increment))
    
    def assert_input(self, activity_rank: int) -> None:
        msg = "The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8."
        assert self.rank >= -8 and self.rank <= 8 and self.rank != 0, msg
        assert activity_rank >= -8 and activity_rank <= 8 and activity_rank != 0, msg


    def get_increment(self, activity_rank: int) -> int:
        delta = abs(self.rank - activity_rank)

        if (0 > self.rank and 0 < activity_rank) or (0 < self.rank and 0 > activity_rank):
            delta -= 1

        if activity_rank <= self.rank:
            if delta == 0:
                return 3
            elif delta == 1:
                return 1
            else:
                return 0
        else:
            return 10 * delta * delta
            
    
    def inc_progress(self, activity_rank: int = 0):
        self.assert_input(activity_rank=activity_rank)
        increment = self.get_increment(activity_rank)
        self.xp += increment
            
