
import curses
import time

class Timer:
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


def draw_timer(stdscr, y, timer, title):
    stdscr.addstr(y, 2, title, curses.A_BOLD)
    stdscr.addstr(y + 1, 4, f"Time: {timer.get_time()}")
    stdscr.addstr(y + 2, 4, f"Status: {'Running' if timer.running else 'Stopped'}")

    stdscr.addstr(y + 3, 4, "Laps:")
    for i, lap in enumerate(timer.laps[-5:], 1):
        stdscr.addstr(y + 3 + i, 6, f"{i}. {lap}")


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    timer1 = Timer()
    timer2 = Timer()

    while True:
        stdscr.clear()

        draw_timer(stdscr, 1, timer1, "Timer 1")
        draw_timer(stdscr, 12, timer2, "Timer 2")

        stdscr.addstr(22, 2, "Controls:", curses.A_BOLD)
        stdscr.addstr(23, 4, "1: Start/Stop Timer 1")
        stdscr.addstr(24, 4, "2: Lap Timer 1")
        stdscr.addstr(25, 4, "8: Start/Stop Timer 2")
        stdscr.addstr(26, 4, "9: Lap Timer 2")
        stdscr.addstr(27, 4, "q: Quit")

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            timer1.toggle()
        elif key == ord('2'):
            timer1.lap()
        elif key == ord('8'):
            timer2.toggle()
        elif key == ord('9'):
            timer2.lap()
        elif key == ord('q'):
            break

        time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(main)

