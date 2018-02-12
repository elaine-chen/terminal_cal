import sched
from datetime import datetime, timedelta
import time

class Notifier():
    def __init__(self):
        self.scheduler = sched.scheduler(datetime.now, Notifier.time_delay)
        self.event_tracker = {}
        self.scheduler.run()

    def add(self, n):
        prev = self.event_tracker.get(n.id)
        if prev != None:
            self.scheduler.cancel(prev)
        event = self.scheduler.enterabs(n.notify_at,
            0,
            Notifier.notify,
            (n.event_msg,)
            )
        self.event_tracker[n.id] = (event, n.start_time)

    def has_notification(self, notification):
        prev = self.event_tracker.get(notification.id)
        return prev != None and prev[1] == notification.start_time

    @staticmethod
    def notify(*args):
        for arg in args:
            print(arg)
            print("\a")

    @staticmethod
    def time_delay(delta):
        if delta == 0:
            return
        time.sleep(delta.seconds)


class Notification():
    def __init__(self, event_id, start_time, alert_before, msg):
        self.start_time = start_time
        self.notify_at = start_time - alert_before
        self.event_msg = msg
        self.id = event_id
