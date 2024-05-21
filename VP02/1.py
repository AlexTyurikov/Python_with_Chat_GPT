def count_numbers_with_digit_3(limit):
    count = 0
    for number in range(1, limit + 1):
        if '3' in str(number):
            count += 1
    return count

# Устанавливаем предел до 2024
limit = 2024
result = count_numbers_with_digit_3(limit)
print(f"Количество натуральных чисел от 1 до {limit}, содержащих хотя бы одну цифру 3: {result}")
