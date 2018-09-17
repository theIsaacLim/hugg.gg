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


def add_newrl():
    num = generate_newrl()
