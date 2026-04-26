
import time

class timer:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.elapsed = 0
        self.laps = []


    def toggle(self):
        if self.running:
            self.elapsed += time.time() - self.start_time
            self.running = False
        else:
            self.start_time = time.time()
            self.running = True


    def lap(self):
        self.laps.append(self.get_time())

    def get_time(self):
        total = self.elapsed
        if self.running:
            total += time.time() - self.start_time

        total = int(total)
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        return f"{h:02}:{m:02}:{s:02}"

