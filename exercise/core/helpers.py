

def next_id_with_postfix(last_id, postfix):
    """
    Generate next id from module with postfix
    :param last_id:integer last full id
    :param postfix:integer ONE or TWO digit integer. postfix which whould add to next id
    :return: integer next id
    """
    return (int(last_id / 100) + 1) * 100 + postfix
