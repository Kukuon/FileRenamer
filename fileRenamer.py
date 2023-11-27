import os
from unidecode import unidecode

def transliterate_to_english(text):
    # Транслитерация и удаление нелатинских символов
    return unidecode(text)

def process_directory(directory):
    # Обработка всех файлов и поддиректорий в указанной директории
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            original_path = os.path.join(root, name)

            # Проверка наличия русских символов в названии файла или директории
            if any(char.isalpha() and ord(char) > 127 for char in name):
                new_name = transliterate_to_english(name)

                # Создание нового пути с транслитерированным именем
                new_path = os.path.join(root, new_name)

                # Переименование файла или директории
                os.rename(original_path, new_path)
                print(f'Renamed: {original_path} -> {new_path}')

if __name__ == "__main__":
    target_directory = input("Введите путь к целевой директории: ")

    if os.path.exists(target_directory):
        process_directory(target_directory)
        print("Процесс завершен.")
    else:
        print("Указанной директории не существует.")
