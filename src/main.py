from ProducerConsumer import *
import random
import time

def example_producer():
    time.sleep(random.uniform(0.1, 0.5))
    value = random.randint(1, 100)
    print(f"Produced: {value}")
    return value

def example_consumer(item):
    time.sleep(random.uniform(0.2, 0.6))
    result = item ** 2
    print(f"Consumed: {item}, Result: {result}")
    return result

if __name__ == "__main__":
    producer_consumer_system = ProducerConsumer(
        producer_func=example_producer,
        consumer_func=example_consumer,
        num_producers=2,
        num_consumers=4,
    )
    producer_consumer_system.start()
    results = producer_consumer_system.collect_results()
    print("Results:", results)