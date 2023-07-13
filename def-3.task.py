def func_no_result(data):
    s = str(data)
    up = s.upper()


func_no_result(123)
func_no_result(45)


def send_email(to, txt):
    # connect to server
    # create text to send
    # send email
    pass


send_email('duzh.maxim@gamil.com', 'Hello Maxim')
send_email('duzh.desnid@gamil.com', 'Hello Denis')


def func_with_result(data):
    s = str(data)
    up = s.upper()
    return up


res = func_with_result(123)
print(res)
res2 = func_with_result("test")
print(res2)


def sum_all(a, b, c):
    value = a + b + c
    return value


res = sum_all(1, 2, 3)
res2 = sum_all(4, 5, 0)
res3 = res + res2
print(res3)


def build_route(a, b):
    # посмотреть какими дорогами можно доехать
    # посмотреть какие дороги и как загружены
    # посчитать скорость
    # calculate time
    res = {
        'start': a,
        'point1': 'Дзержинск',
        'point2': 'Столбцы',
        'end': b,
    }
    return res


route = build_route('Minsk', 'Brest')
print(route)
route = build_route('Minsk', 'Baranovichi')
print(route)
