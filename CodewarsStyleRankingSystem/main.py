import logging
from tests.test_user import test_user
from User import User

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    test_user()
    
    user = User()
    user.inc_progress(1)
    print(user.rank)