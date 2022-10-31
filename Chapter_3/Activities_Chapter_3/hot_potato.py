""" 3.13. Queue Simulation: Hot Potato¶
Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/SimulationHotPotato.html
"""
from pythonds3.basic import Queue

class potato:
    def hot_potato(self, name_list:list[str], num:int):
        sim_queue:Queue = Queue()

        for name in name_list:
            sim_queue.enqueue(name)
        
        while sim_queue.size() > 1:
            for i in range(num):
                out_for = sim_queue.dequeue()
                sim_queue.enqueue(out_for)
                print(f"{out_for} was requeued")
            out_while = sim_queue.dequeue()
            print(f"{out_while} is out!")
            print("======")
        
        return sim_queue.dequeue()


if __name__ == "__main__":
    name_list:list[str] = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    num:int = 7

    output = potato().hot_potato(name_list=name_list, num=num)

    print(output)