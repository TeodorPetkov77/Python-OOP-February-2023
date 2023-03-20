from abc import ABC, abstractmethod


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(AbstractWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(AbstractWorker):
    def work(self):
        print("I work very hard!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), '`worker` must be of type {}'.format(AbstractWorker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
worker = SuperWorker()
try:
    manager.set_worker(worker)
    manager.manage()
except AssertionError:
    print(f"manager fails to support {worker.__class__.__name__}....")


# _____________________________ BEFORE CODE _____________________________
# from abc import ABC, abstractmethod
#
#
# class AWorker(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
#
# class Worker(AWorker):
#     def work(self):
#         print("I'm working!!")
#
#
# class SuperWorker(AWorker):
#     def work(self):
#         print("I work very hard!!!")
#
#
# # this is not an inherited class on purpose for testing:
# class LazyWorker:
#     def work(self):
#         print("I am lazy!!!")
#
#
# class Manager:
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, AWorker), '`worker` must be of type {}'.format(AWorker)
#         self.worker = worker
#
#     def manage(self):
#         if self.worker is not None:
#             self.worker.work()
#
#
# worker = Worker()
# manager = Manager()
# manager.set_worker(worker)
# manager.manage()
# worker = LazyWorker()
# try:
#     manager.set_worker(worker)
#     manager.manage()
# except AssertionError:
#     print(f"manager fails to support {worker.__class__.__name__}....")
