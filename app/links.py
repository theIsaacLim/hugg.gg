urls = [{'num': 0}, {'num': 1, 'message': 'seriiiii'}, {'num': 2, 'message': 'Thank you :3 '}, {'num': 3, 'message': 'Nice'}, {'num': 4, 'message': ''}, {'num': 5, 'message': 'A hug'}]



def generate_newrl():
    global urls
    return urls[-1]['num'] + 1


def add_newrl(message=None):
    global urls
    num = generate_newrl()
    urls.append({'num': num,
                 'message': message})
    print(urls)
    return num


def get_existing_url(num):
    global urls
    url_data = next(item for item in urls if item["num"] == num)
    print(urls)
    urls.remove(url_data)
    print(urls)
    return url_data
