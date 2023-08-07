
import unittest
import threading
import time
 
class TimeLimitExceededError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
class BusTourTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answer = None
        
    def test_case_01_safe_bridge(self):
        self.assertEqual(
          crash_check(
            1,
            [763]),
          'No crash'
        )
    
    def test_case_02(self):
        self.assertEqual(
          crash_check(
            3,
            [763, 245, 113]),
          'Crash 2'
        )
    
    def test_case_03_exact_bus_height(self):
        self.assertEqual(
          crash_check(
            1,
            [437]),
          'Crash 1'
        )
    
    def test_case_04_close_height(self):
        self.assertEqual(
          crash_check(
            1,
            [438]),
          'No crash'
        )
    
    def test_case_05_aganist_sum_func(self):
        self.assertEqual(
          crash_check(
            3,
            [245, 763, 113]),
          'Crash 1'
        )
    
    def thread_func(self):
        n = 1000000000
        r = crash_check(
            n,
            range(0, n))
        self.answer = r
 
    def test_case_06_check_efficiency(self):
        thr = threading.Thread(target=self.thread_func, daemon=True)
        thr.start()
        time.sleep(1)
        r = self.answer
        if r is None:
            raise TimeLimitExceededError('Чувак, попробуй уложиться в секунду!')
        self.assertEqual(
          r, 'Crash 1'
        )
 
def crash_check(n, h):
    """Функция от Gdez."""
    m = sum([h[i] < 437 for i in range(n)])
    return 'Crash ' + str(m) if m else 'No crash'
 
unittest.main()