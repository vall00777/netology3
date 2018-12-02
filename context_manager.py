from time import time

class Test:
     def __enter__(self):
          self.time = time()
          print('Начало: {0}'.format(self.time))
          return self
     def __exit__(self, exc_type, exc_value, exc_tb):
          now_time = time() - self.time
          print('Конец: {0}'.format(time()))
          print('Код проработал: {0}'.format(now_time))

with Test():
     for i in range(1, 1000000000): pass


              
