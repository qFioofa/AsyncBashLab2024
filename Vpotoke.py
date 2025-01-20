import os
import queue
import threading
from PIL import Image

# Папка с изображениями
input_folder = 'input_images'
# Папка для сохранения обработанных изображений
output_folder = 'output_images'

# Очередь для передачи путей к изображениям
image_queue = queue.Queue()


def producer():
    """Функция производителя: извлекает пути к изображениям из папки."""
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            image_queue.put(image_path)
            print(f'Производитель: добавлен путь к изображению {image_path}')

    # Добавляем сигнал завершения для каждого потребителя
    for _ in range(num_consumers):
        image_queue.put(None)


def consumer(consumer_id):
    """Функция потребителя: обрабатывает изображения и сохраняет их в выходной папке."""
    while True:
        image_path = image_queue.get()
        if image_path is None:
            break  # Завершение работы потребителя
        try:
            print(f'Потребитель {consumer_id}: обрабатывает {image_path}')
            # Открываем изображение
            img = Image.open(image_path)
            # Преобразуем в градации серого
            gray_img = img.convert('L')
            # Сохраняем изображение в выходной папке
            output_path = os.path.join(output_folder, os.path.basename(image_path))
            gray_img.save(output_path)
            print(f'Потребитель {consumer_id}: сохранено {output_path}')
        except Exception as e:
            print(f'Ошибка при обработке {image_path}: {e}')
        finally:
            image_queue.task_done()


# Количество потребителей
num_consumers = 16

# Создаем выходную папку, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Запускаем поток производителя
producer_thread = threading.Thread(target=producer)
producer_thread.start()

# Запускаем потоки потребителей
consumers = []
for i in range(num_consumers):
    consumer_thread = threading.Thread(target=consumer, args=(i,))
    consumer_thread.start()
    consumers.append(consumer_thread)

# Ожидаем завершения работы производителя
producer_thread.join()

# Ожидаем завершения работы всех потребителей
image_queue.join()
for _ in range(num_consumers):
    image_queue.put(None)  # Добавляем сигнал завершения для каждого потребителя
for consumer_thread in consumers:
    consumer_thread.join()

print('Обработка изображений завершена.')
