""" 3.14. Queue Simulation: Printing Tasks¶
Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/SimulationPrintingTasks.html
"""
import random
from pythonds3.basic.queue import Queue
class Printer:
    def __init__(self, ppm) -> None:
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    
    def busy(self):
        return self.current_task is not None
    
    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task:
    def __init__(self, time) -> None:
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    
    def get_stamp(self):
        return self.timestamp
    
    def get_pages(self):
        return self.pages
    
    def wait_time(self, current_time):
        return current_time - self.timestamp


class PrintQueue:
    
    def simulation(self, num_seconds, pages_per_minute) -> None:
        lab_printer:Printer = Printer(pages_per_minute)
        print_queue:Queue = Queue()
        waiting_times = []

        for current_second in range(num_seconds):
            if self.new_print_task():
                
    
    def new_print_task(self) -> bool:
        num = random.randrange(1,181)
        return num == 180

if __name__ == "__main__":
    for i in range(10):
        PrintQueue().simulation(3600, 5)
