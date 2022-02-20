from User import User

def test_user():
    """
        Logic Examples:
            - If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
            - If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
            - If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
            - If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank
            - If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
    """    
    user = User()
    print(user)
    user.inc_progress(-7)
    print(user)
    user.inc_progress(-5)
    print(user)