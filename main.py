import msoffcrypto
import io
import time
from itertools import product

def brute_force_word(file_path, min_length=1, max_length=5):
    with open(file_path, "rb") as f:
        office_file = msoffcrypto.OfficeFile(f)
        start_time = time.time()

        # Генерация всех возможных комбинаций от min_length до max_length
        total_attempts = sum(10**i for i in range(min_length, max_length + 1))  # Подсчет общего числа комбинаций
        attempt = 0  # Счетчик попыток

        for length in range(min_length, max_length + 1):
            for num_tuple in product("0123456789", repeat=length):
                password = "".join(num_tuple)
                attempt += 1
                print(f"Проверяю пароль: {password} ({attempt}/{total_attempts})")

                try:
                    office_file.load_key(password=password)
                    decrypted = io.BytesIO()
                    office_file.decrypt(decrypted)
                    elapsed_time = time.time() - start_time
                    print(f"\n✅ Пароль найден: {password}")
                    print(f"⏳ Время подбора: {elapsed_time:.2f} сек.")
                    return password
                except:
                    pass

        print("\n❌ Пароль не найден в заданном диапазоне.")
        return None

file_path = "protected.docx"  # Укажи путь к файлу
brute_force_word(file_path, min_length=1, max_length=5)
