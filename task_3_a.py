import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1

# Читання тексту з файлу "стаття 1"
def read_file(filename):
    with open(filename, 'r', encoding='windows-1251') as file:
        return file.read()

# Тестові файли
text1 = read_file('стаття 1.txt')

# Підрядки для пошуку
existing_substring = "прийняття рішення можна розбити"  # Існуючий підрядок стаття 1
non_existing_substring = "вигаданий підрядок"  # Вигаданий підрядок

# Вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    index = algorithm(text, pattern)
    end_time = timeit.default_timer()
    return index, end_time - start_time

# Функція для пошуку та виведення результату
def search_and_print(algorithm, text, pattern):
    index, exec_time = measure_time(algorithm, text, pattern)
    if index != -1:
        print(f"Знайдений рядок за індексом {index}, час виконання: {exec_time:.6f} секунд")
    else:
        print(f"Рядок не знайдено, час виконання: {exec_time:.6f} секунд")

# Результати для статті 1
print("Стаття 1 (існуючий підрядок):")
print("Пошук Боєра-Мура:")
search_and_print(boyer_moore, text1, existing_substring)
print("Пошук Кнута-Морріса-Пратта:")
search_and_print(kmp_search, text1, existing_substring)
print("Пошук Рабіна-Карпа:")
search_and_print(rabin_karp, text1, existing_substring)

print("Стаття 1 (вигаданий підрядок):")
print("Пошук Боєра-Мура:")
search_and_print(boyer_moore, text1, non_existing_substring)
print("Пошук Кнута-Морріса-Пратта:")
search_and_print(kmp_search, text1, non_existing_substring)
print("Пошук Рабіна-Карпа:")
search_and_print(rabin_karp, text1, non_existing_substring)
