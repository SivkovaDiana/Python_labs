def Map(func, iterable):
    """
    Summary:
     Функция-генератор, отображает одно множество значений на другое
    Args:
        func: Применяемая функция к каждому элементу множества
        iterable: Колекция

    Yields:
        Any: пропущенный через функцию очередной элемент последовательности
    """
    #Если последовательность итерируемая
    if (hasattr(iterable,"__iter__")):
        it = iter(iterable)
    #Иначе, если передан итератор
    elif (hasattr(iterable),"__next__"):
        it = iterable

    while True:
        try:
            yield func(next(it))
        except StopIteration:
            return

def Filter(func, iterable):
    """
    Summary:
        Функция-генератор отбрасывает элементы последовательности, которые не удовлетворяют
        некоторому условию, переданному в качестве первого параметра

    Args:
        func (Any): условие оставления элемента в последовательности - предикат
        iterable (Any): последовательность

    Yields:
        Any: Следующий элемент последовательности, удовлетворяющий условию
    """
    if (hasattr(iterable, "__iter__")):
        it = iter(iterable)
    elif (hasattr(iterable),"__next__"):
        it = iterable

    while True:
        try:
            value = next(it)
            while(not func(value)):
                value = next(it)
            yield value
        except StopIteration:
            return

def Reduce(iterable,start_value,binary_function):
    """
    Summary:
        Функция, которая аккумулирует все значения в последовательности

    Args:
        iterable (Any): Аккумулируемая последовательность
        start_value (Any): Начальное значение аккумулятора
        binary_function (Callable): Функция-аккумулятор.
                                        Первым параметром на вход ей отдается накопленное значение
                                        Вторым - Очередное значение колекции

    Returns:
        Any: Результат работы функции зваисит от входных параметров
    """
    result = start_value;

    for i in iterable:
        result = binary_function(result, i)

    return result

if __name__ == "__main__":
    ls = [1,2,3,4,5,6]
    res = Filter(lambda x: x%2==0, ls)
    r = Reduce(res,0,lambda x,y : x+y)
