import random
from loguru import logger

logger.add("logs/log.log", level="DEBUG", rotation="50 KB", retention="1 week")
logger.add("logs/log_war.log", level="WARNING", rotation="50 KB", retention="1 week")
logger.info("Приложение запущено")


def choice_sort(data: list[int | float]):
    n = len(data)
    logger.info(f"сортировка {choice_sort.__name__} начала работу с {data}, длина списка {n}")
    for a in range(n - 1):
        logger.debug(f"начался {a + 1} проход цикла, элемент: {data[a]}, индекс: {a}")
        min_num = data[a]
        min_idx = a
        for b in range(a + 1, n):
            if data[b] < min_num:
                min_num = data[b]
                min_idx = b
        logger.debug(f"минимальное число на текущем проходе {min_num}, индекс: {min_idx}")
        if min_idx != a:
            memory = data[a]
            data[a] = data[min_idx]
            data[min_idx] = memory
            logger.debug(f"по индексу {a} теперь {data[a]}, а по индексу {min_idx} теперь {data[min_idx]}")
    logger.success(f"список отсортирован: {data}")
    return data


def bingo_sort(data: list[int | float]):
    logger.info("Запуск сортировки bingo_sort")
    logger.debug(f"Исходные данные: {data}")
    max_idx = len(data) - 1
    next_value = data[max_idx]
    for i in range(max_idx - 1, -1, -1):
        if data[i] > next_value:
            next_value = data[i]
    logger.debug(f"Найдено начальное максимальное значение: {next_value}")
    while max_idx and data[max_idx] == next_value:
        max_idx -= 1
    logger.debug(f"Начальный max_idx скорректирован до: {max_idx}")
    while max_idx:
        value = next_value
        next_value = data[max_idx]
        logger.debug(f"Новый проход: прошлое максимальное value={value}, следующий next_value={next_value}")
        for x in range(max_idx - 1, -1, -1):
            if data[x] == value:
                logger.debug(f"Обмен элементов {data[x]} и {data[max_idx]} (индексы {x}, {max_idx})")
                data[x], data[max_idx] = data[max_idx], data[x]
                max_idx -= 1
                logger.debug(f"Массив после обмена: {data}")
            elif data[x] > next_value:
                next_value = data[x]
        logger.debug(f"Следующее значение для итерации: {next_value}")
        while max_idx and data[max_idx] == next_value:
            max_idx -= 1
        logger.debug(f"max_idx скорректирован до: {max_idx}")
    logger.info("Сортировка bingo_sort завершена")
    logger.success(f"Отсортированные данные: {data}")
    return data


def pancake_sort(data: list[int | float]):
    logger.info("Запуск сортировки pancake_sort")
    logger.debug(f"Исходные данные: {data}")
    if len(data) > 1:
        for size in range(len(data), 1, -1):
            max_idx = max(range(size), key=data.__getitem__)
            logger.debug(
                f"Текущий размер={size}, индекс максимума={max_idx}, значение={data[max_idx]}"
            )
            if max_idx + 1 != size:
                if max_idx != 0:
                    logger.debug(f"Переворот первых {max_idx + 1} элементов")
                    data[:max_idx + 1] = reversed(data[:max_idx + 1])
                    logger.debug(f"После первого переворота: {data}")
                logger.debug(f"Переворот первых {size} элементов")
                data[:size] = reversed(data[:size])
                logger.debug(f"После второго переворота: {data}")
    logger.info("Сортировка pancake_sort завершена")
    logger.success(f"Отсортированные данные: {data}")
    return data


def insert_sort(data: list[int | float]):
    n = len(data)
    logger.info(f"{insert_sort.__name__} запущена | данные: {data} | длина: {n}")
    for i in range(1, n):
        logger.debug(f"Итерация i={i}, текущее состояние: {data}")

        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                logger.debug(
                    f"swap: data[{j}]={data[j]} < data[{j - 1}]={data[j - 1]} → меняем"
                )
                data[j], data[j - 1] = data[j - 1], data[j]
                logger.debug(f"после swap: {data}")
            else:
                logger.debug(f"break на j={j}, порядок соблюдён")
                break

    logger.info(f"{insert_sort.__name__} завершена | результат: {data}")
    return data


def binary_insert_sort(data: list[int | float]):
    n = len(data)
    logger.info(f"{binary_insert_sort.__name__} запущена | данные: {data} | длина: {n}")
    for i in range(1, n):
        key = data[i]
        low, high = 0, i - 1
        logger.debug(f"Итерация i={i}, key={key}")
        while low <= high:
            mid = (low + high) // 2
            logger.debug(f"binary search: low={low}, high={high}, mid={mid}")
            if key < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        logger.info(f"позиция для вставки: {low}")
        for j in range(i, low, -1):
            data[j] = data[j - 1]
            logger.debug(f"сдвиг: data[{j}] = data[{j - 1}] → {data}")
        data[low] = key
        logger.debug(f"вставка key={key} на позицию {low} → {data}")
    logger.success(f"{binary_insert_sort.__name__} завершена | результат: {data}")
    return data


def bubble_sort(data: list[int | float]):
    n = len(data)
    logger.info(f"{bubble_sort.__name__} запущена | данные: {data} | длина: {n}")
    for i in range(0, n - 1):
        logger.info(f"Проход i={i}, текущее состояние: {data}")
        for j in range(0, n - 1 - i):
            if data[j] > data[j + 1]:
                logger.debug(
                    f"swap: data[{j}]={data[j]} > data[{j + 1}]={data[j + 1]} → меняем"
                )
                data[j], data[j + 1] = data[j + 1], data[j]
                logger.debug(f"после swap: {data}")
    logger.success(f"{bubble_sort.__name__} завершена | результат: {data}")
    return data


def merge_list(data1: list[int | float], data2: list[int | float]):
    data = []
    n = len(data1)
    m = len(data2)
    i = 0
    j = 0
    while i < n and j < m:
        if data1[i] <= data2[j]:
            data.append(data1[i])
            i += 1
        else:
            data.append(data2[j])
            j += 1
    data += data1[i:] + data2[j:]
    return data


def split_merge_sort(data: list[int | float]):
    n = len(data) // 2
    data1, data2 = data[:n], data[n:]
    if len(data1) > 1:
        data1 = split_merge_sort(data1)
    if len(data2) > 1:
        data2 = split_merge_sort(data2)
    return merge_list(data1, data2)


def quick_sort(data: list[int | float]):
    if len(data) > 1:
        x = data[random.randint(0, len(data) - 1)]
        low = [u for u in data if u < x]
        equal = [u for u in data if u == x]
        big = [u for u in data if u > x]
        data = quick_sort(low) + equal + quick_sort(big)
    return data


dataset = [541, 934, 661, -868, 709, -277, 142, 493, 286, 733, -229, 79]
dataset2 = [8, 7, 87, 87, 87, 87, 87, 85, 64, 534, 78, 87, 87, 87]
# sort1 = choice_sort(dataset.copy())
# print(sort1)
# sort2 = bingo_sort(dataset2.copy())
# print(sort2)
# sort3 = pancake_sort(dataset2.copy())
# print(sort3)
# sort4 = insert_sort(dataset.copy())
# print(sort4)
sort5 = binary_insert_sort(dataset.copy())
print(sort5)
sort6 = bubble_sort(dataset2.copy())
print(sort6)
# sort7 = split_merge_sort(dataset.copy())
# print(sort7)
# sort8 = quick_sort(dataset.copy())
# print(sort8)
