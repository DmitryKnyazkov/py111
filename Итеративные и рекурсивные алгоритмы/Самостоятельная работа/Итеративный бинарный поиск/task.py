from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    left_ = 0
    right_ = len(seq)-1

    for _ in range(len(seq)+1):
        seredina = left_ + (right_ - left_) // 2
        if not seq:
            raise ValueError("пустая коллекция")

        if seq[seredina] == value:
            if seredina != 0:

                while seq[seredina-1] == seq[seredina]:
                    seredina = seredina - 1
            return print(f"ваше число {value}, оно находится по {seredina} индексу")

        if seq[seredina] < value:
            left_ = seredina + 1

        if seq[seredina] > value:
            right_ = seredina - 1

        if len(seq) == 1 and seq[0] != value:
            break

    raise ValueError("Такого числа нет")


binary_search(68, [0,0,0,2,5,7,9,9,9,68])
      # TODO реализовать итеративный алгоритм бинарного поиска
