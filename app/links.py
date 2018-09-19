urls = [{'num':0}]

def generate_newrl():
    global urls
    return urls[-1]['num'] + 1


def add_newrl(message=None):
    global urls
    num = generate_newrl()
    urls.append({'num': num,
                 'message': message})
    return num


def get_existing_url(num):
    global urls
    url_data = next(item for item in urls if item["num"] == num)
    urls.remove(url_data)
    return url_data
