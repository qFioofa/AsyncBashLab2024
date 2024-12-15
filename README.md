# ProducerConsumer Class

Класс ProducerConsumer реализует шаблон producer-consumer, используя модуль multiprocessing Python.
Он позволяет создавать несколько процессов-производителей и потребителей, которые могут взаимодействовать через очередь.

## Features

- Поддержка нескольких производителей и потребителей.
- Настраиваемый размер очереди для обмена данными.
- Обрабатывает исключения как в процессах-производителях, так и в процессах-потребителях.
- Собирает результаты из процессов-потребителей.

## Installation

Чтобы использовать класс ProducerConsumer, следует определить функции producer и consumer.
- producer должн возвращать данные для обработки
- сonsumer должн принимать эти данные и выполнять требуемую обработку.

## Usage

### Initialization

Версия Python - 3.x. 
Вы можете скопировать определение класса непосредственно в свой проект или сохранить его в виде файла модуля (например, producer_consumer.py).

### Methods

- __init__(producer_func, consumer_func, num_producers, num_consumers, queue_size): Создает объект класса для реализации шаблона producer-consumer

- producer_worker(): Обрабатывает правильную заботу всех producer

- consumer_worker(): Обрабатывает правильную заботу всех consumer

- start(): Запускает процесс 

- collect_results() -> List[Any]: Собирает результаты из очереди результатов после завершения обработки

### Example

Пример, демонстрирующий использование класса ProducerConsumer:

```python
import random
import time

def producer_func(item):
    # Создает число в диапозоне от 1 до 100
    # Шанс 10%, что выведит None
    if random.random() < 0.9:
        return random.randint(1, 100)
    return None

def consumer_func(item):
    # Обработка предмета
    # Пример: возведение в квадрат
    return item * item

if __name__ == "__main__":
    pc = ProducerConsumer(
        producer_func=producer_func,
        consumer_func=consumer_func,
        num_producers=4,
        num_consumers=2,
        queue_size=10,
    )

    pc.start()
    results = pc.collect_results()

    print("Results collected:", results)

```

## Notes

- Учитывайте возможные блокировки при создании и обработки элементов, особенно если может потребоваться много времени.

- Можете настроить queue_size в зависимости от потребностей вашего приложения.
