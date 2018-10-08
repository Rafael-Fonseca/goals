'''****************************************************************************
**      Neste arquivo estão todas as regras de negócio do projeto Goals      **
****************************************************************************'''


class Goal:

    def __init__(self, name, final_date, category):
        self._name = name
        self._final_date = final_date
        self._category = category

    def remove_goal(self):
        del self


def register(username, password, email):
    """
    :param username: String
    :param password: String
    :param email: String
    :return: False if username already exist and True otherwise
    """

    with open("usersDB.txt", "a+") as db:
        """
        Dictionary comprehension: For each line of the file,
        update the dictionary current_users according,
        the unpanck of variables [username, password, email] in line.split()
        
        FAILED DICT COMP
        current_users = {username: [password, email] for line in content
                         for username, password, email in line.split()}
        """
        current_users = {}
        for line in db.readlines():
            _username, _password, _email = line.split()
            current_users.update({_username: [_password, _email]})

        try:
            current_users[username]
            db.close()
            return False
        except KeyError:
            db = open("usersDB.txt", "a+")
            new_user = username + " " + password + " " + email + "\n"
            db.write(new_user)
            db.close()
            return True


def validate_login(username, password):
    """
    :param username: String
    :param password: String
    :return: True if credentials are correct, False otherwise
    """

    with open("usersDB.txt", "r") as db:
        """
        equals comment in function register(username, password,email):
        """
        current_users = {}
        for line in db.readlines():
            _username, _password, _email = line.split()
            current_users.update({_username: [_password, _email]})

        try:
            return password == current_users[username][0]  # wrong password
        except KeyError:
            return False  # Unknown username

