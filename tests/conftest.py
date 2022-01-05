import pytest
from datetime import date
from project.user import User

@pytest.fixture(scope='function')
def app_user():
    user_details=User(first_name = 'Khalid', last_name = 'Agha', email = 'khalid_agha20@hotmail.com',\
                      password = 'uclmecheng', dob = date(2000, 12, 16))
    yield user_details