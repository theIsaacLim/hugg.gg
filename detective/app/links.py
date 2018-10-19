urls = [{'num': 0}]


def add_newrl(message=None):
    """
    Function used for adding new hugs. Will return unique id that has to be used in the url
    :param message: Optional message, if blank will default to None
    :return:
    """
    global urls
    num = urls[-1]['num'] + 1  # Generates a unique id for hug access
    urls.append({'num': num,
                 'message': message})  # Adds this to the list of existing ids
    return num  # Returns the id


def get_existing_url(num):
    """
    Function used for getting existing hugs.
    :param num: Unique ID
    :return: Data related to the URL ie. optional message, anything else I need for future expansion
    """
    global urls
    url_data = next(item for item in urls if item["num"] == num)
    urls.remove(url_data)
    return url_data
