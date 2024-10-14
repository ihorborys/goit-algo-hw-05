def binary_search(arr, target):
    """
    Функція для бінарного пошуку елемента в відсортованому масиві з поверненням кількості ітерацій
    та найменшого елемента, більшого або рівного target.

    Parameters:
    arr (list): Відсортований масив для пошуку.
    target: Елемент, який шукаємо.

    Returns:
    tuple: Кортеж з двох елементів:
           - Кількість ітерацій
           - Найменший елемент, більший або рівний заданому значенню (upper bound)
    """
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None  # Найменший елемент, більший або рівний target

    while left <= right:
        iterations += 1  # Лічимо кількість ітерацій
        mid = (left + right) // 2  # Знаходимо середину масиву

        print(f"left: {left},\t right: {right},\t mid: {mid},\t target: {target},\t arr_mid: {arr[mid]}")

        if arr[mid] == target:
            upper_bound = arr[mid]  # Якщо знайдено елемент, це і є наш upper bound
            return iterations, upper_bound
        elif arr[mid] < target:
            left = mid + 1  # Якщо елемент менший за target, зміщуємо ліву межу
        else:
            upper_bound = arr[mid]  # Якщо елемент більший за target, зберігаємо його як upper bound
            right = mid - 1  # Зміщуємо праву межу

    # Якщо елемент не знайдено, повертаємо кількість ітерацій та upper bound (якщо знайдений)
    return iterations, upper_bound

# Приклад використання
array = [2.3, 5.1, 8.2, 12.5, 16.8, 23.4, 38.7, 56.1, 72.5, 91.9]
target = 29.5
result = binary_search(array, target)

if result[1] is not None:
    print(f"Пошук завершено за {result[0]} ітерацій. Найменший елемент >= {target} є {result[1]}")
else:
    print(f"Пошук завершено за {result[0]} ітерацій. Елемент, що більший або рівний {target}, не знайдено.")

print(result)