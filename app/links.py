from time import time
urls = [{'num': 0,
         'date': time()+30.0}]


def generate_newrl():
    global urls
    for num in urls:
        if num != urls.index(num):
            print("a")
            return urls.index(num)
    print("b")
    return urls[-1] + 1


def add_newrl(message=None):
    global urls
    num = generate_newrl()
    urls.append({'num': num,
                 'date': time()+86400,
                 'message': message})
    return num


def get_existing_url(num):
    global urls
    url_data = next(item for item in urls if item["num"] == num)
    urls = urls.remove(url_data)
    return url_data
