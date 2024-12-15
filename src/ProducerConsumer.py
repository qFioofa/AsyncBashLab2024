import multiprocessing
from queue import Empty
from typing import Callable, Any, List

class ProducerConsumer:
    producer_func: Callable[[], Any]
    consumer_func: Callable[[Any], Any]
    num_producers: int
    num_consumers: int
    queue_size: int
    
    def __init__(
        self,
        producer_func: Callable[[], Any],
        consumer_func: Callable[[Any], Any],
        num_producers: int,
        num_consumers: int,
        queue_size: int = 100,
    ):
        self.queue_size = queue_size
        self.producer_func = producer_func
        self.consumer_func = consumer_func
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.queue = multiprocessing.Queue(maxsize=queue_size)
        self.result_queue = multiprocessing.Queue()
        self.stop_event = multiprocessing.Event()

    def producer_worker(self):
        while not self.stop_event.is_set():
            try:
                item = self.producer_func()
                if item is None:
                    break
                self.queue.put(item, block=True)
            except Exception as e:
                print(f"Producer an error: {e}")
                self.stop_event.set()
                break

    def consumer_worker(self):
        while not self.stop_event.is_set():
            try:
                item = self.queue.get(block=True, timeout=1)
                result = self.consumer_func(item)
                self.result_queue.put(result)
            except Empty:
                if self.stop_event.is_set():
                    break
            except Exception as e:
                print(f"Consumer encountered an error: {e}")
                self.stop_event.set()
                break

    def start(self):
        producers = [
            multiprocessing.Process(target=self.producer_worker)
            for _ in range(self.num_producers)
        ]
        consumers = [
            multiprocessing.Process(target=self.consumer_worker)
            for _ in range(self.num_consumers)
        ]

        for p in producers + consumers:
            p.start()

        for p in producers:
            p.join()

        self.stop_event.set()
        for c in consumers:
            c.join()

    def collect_results(self) -> List[Any]:
        results = []
        while not self.result_queue.empty():
            try:
                results.append(self.result_queue.get_nowait())
            except Empty:
                break
        return results
