from stopwatchpy import Stopwatch

class CountingStopwatch(Stopwatch):
     def __init__(self):
          #allow base class to do its initialization of the inherited 
          # instance variables
          super().__init__()
          #sets number of starts to zero
          self._count = 0

     def start(self):
          # count the start message unless the watch is already running
          if not self._running:
               self._count += 1
          # let base class do its start code
          super().start()
     def reset(self):
          #let base class reset the inherited instance variables
          super().reset()

          #reset the new instance variable that the base class method doesnt know about
          self._count = 0

     def count(self):
          return self._count