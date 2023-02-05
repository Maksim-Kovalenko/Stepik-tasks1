class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            d = list(map(self.__render, func()))
            return d
        return wrapper

class RenderDigit:
    def __call__(self,item, *args, **kwargs):
        try:
            a = int(item)
            return a
        except:
            return None

@InputValues(render=RenderDigit())
def input_dg():
    a = input()
    return a.split()

res = input_dg()
print(res)