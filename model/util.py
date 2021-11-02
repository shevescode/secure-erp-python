import random
import string


def generate_id():
    """         number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"
    """
    list = []
    allowed_special_chars = ["_", "+", "-", "!"]
    for i in range(4):
        list.append(chr(random.randint(97, 122)))
    for i in range(2):
        list.append(chr(random.randint(65, 90)))
    for i in range(2):
        list.append(random.randint(0,9))
    for i in range(2):
        list.append(random.choice(allowed_special_chars))
    random.shuffle(list)
    new_id = ""
    for i in list:
        new_id += str(i)
    # 'T!uq6-b4Yq' było w return przed edycja funkcji
    return new_id
