from time import perf_counter

class Stopwatch:
     """
     initializes stopwatch objects that programmers can use to time
     the execution time of portions of a program.
     """
     def __init__(self):
          """makes a new stopwatch ready for timing."""
          self.reset()
     
     def start(self):
          """
          starts the stopwatch unless it is already running.
          this method does not affect any time that we have already 
          accumulated on the timer.
          """
          if not self._running:
               self._start_time = perf_counter() - self._elapsed
               self._running = True   #clock now running
     
     def stop(self):
          """
          stops the stop watch unless it is not running.
          updates the accumulated elapsed time
          """
          if self._running:
               self._elapsed = perf_counter() - self._start_time
               self._running = False    # stopwatch stopped
     
     def reset(self):
          """resets stopwatch to zero"""
          self._start_time = self._elapsed = 0
          self._running = False
     
     def elapsed(self):
          """reveals the stopwatch running time since it was last reset."""
          if not self._running:
               return self._elapsed
          else:
               return perf_counter() - self._start_time
     

