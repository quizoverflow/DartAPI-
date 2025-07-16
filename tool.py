import os

# decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

#decorator
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called")
        func
        print(f"{func.__name__} finished")
    return wrapper

#debuger
class Debuger():
    @staticmethod
    def printd(msg):
        print(f"[DBG] {msg}",flush=True)
    @staticmethod
    def printc(msg):
        os.system("cls")
        print(f"[DBG] {msg}",flush = True)

class LoadingDebugger(Debuger):
    def __init__(self,name,total):
        os.system("cls")
        super().printd(f"{name} 시작")
        self.name = name
        self.total = total
        self.progress = 0.0
    def print_progress(self,cnt,flush = False):
        if cnt / self.total >= self.progress:
            if flush:
                os.system("cls")
            super().printd(f"{self.name} 진행률 : {cnt}/{self.total}   ||  {cnt/self.total * 100}%")
            self.progress += 0.1
    def __del__(self):
            super().printd(f"{self.name} 완료")