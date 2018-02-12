import threading
from datetime import datetime, timedelta
import time

class Notifier():
    def __init__(self):
        self.event_tracker = {}

    def cancel_all(self):
        for v in self.event_tracker.values():
            v[0].cancel()

    def add(self, n):
        prev = self.event_tracker.get(n.id)
        if prev != None:
            prev[0].cancel()
        countdown = n.notify_at - datetime.now()
        t = threading.Timer(countdown.total_seconds(), Notifier.notify, args=[n.event_msg])
        t.start()
        self.event_tracker[n.id] = (t, n.notify_at)

    def has_notification(self, notification):
        prev = self.event_tracker.get(notification.id)
        return prev != None and prev[1] == notification.notify_at

    @staticmethod
    def notify(*args):
        for arg in args:
            print(arg)
            print("\a")

class Notification():
    def __init__(self, event_id, start_time, alert_before, msg):
        self.start_time = start_time
        self.notify_at = start_time - alert_before
        self.event_msg = msg
        self.id = event_id
