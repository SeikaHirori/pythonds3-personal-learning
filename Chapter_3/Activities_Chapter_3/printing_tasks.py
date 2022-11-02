""" 3.14. Queue Simulation: Printing Tasks¶
Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/SimulationPrintingTasks.html
"""

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


class PrintQueue:
    def __init__(self) -> None:
        pass