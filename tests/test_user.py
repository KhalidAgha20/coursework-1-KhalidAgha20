def test_if_full_name_is_given_properly(app_user):
    """
    GIVEN a user with first Name 'Khalid' and last name 'Agha' is registered
    WHEN the user logs in
    THEN the full name must be output as 'Khalid Agha'
    """
    name = app_user.create_full_name()
    assert name == 'Khalid Agha'


def test_correct_age_is_calculated(app_user):
    """
    GIVEN a user born on 16/12/2000 is registered
    WHEN the user logs in
    THEN the age must be calculated as 21
    """
    age = app_user.calculate_age()
    assert age == 21


def test_if_password_is_encrypted_when_hashed(app_user):
    """
    GIVEN a user is logging in
    WHEN the user inputs the correct password
    THEN the stored password is encrypted and thus different from the actual password string
    """
    status = app_user.hash_password('uclmecheng')
    assert status != 'uclmecheng'


def test_that_output_is_true_when_correct_password_is_typed(app_user):
    """
    GIVEN a registered user is logging in
    WHEN the user inputs the correct password
    THEN the identification status must be true
    """
    status = app_user.is_correct_password('uclmecheng')
    assert status == True

