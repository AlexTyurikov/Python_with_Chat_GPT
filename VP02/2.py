
def compress_string(s):
    # Если строка пустая, возвращаем её сразу
    if not s:
        s = print('Введена пустая строка')    
        return s
       
    compressed = []
    count = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append(prev_char + str(count))
            prev_char = char
            count = 1
    
    # Не забываем добавить последний накопленный символ
    compressed.append(prev_char + str(count))
    
    # Преобразуем список в строку
    compressed_string = ''.join(compressed)
    
    # Если сжатая строка не короче оригинальной, возвращаем оригинальную строку
    return compressed_string if len(compressed_string) < len(s) else print('сжатая строка не короче оригинальной')

# Пример использования
input_string = input('введите строку: ')
output_string = compress_string(input_string)
print(output_string)  # Вывод: "a2b1c5a3"