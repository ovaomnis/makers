import datetime


class Clock:
    def current_time(self) -> datetime.time:
        return datetime.datetime.now().time()


class Alarm:
    def ring(self):
        print('Zzz-Zzz-Zzz-Zzz')


class AlarmClock(Alarm, Clock):
    def set_alarm(self):
        self.ring()


ac = AlarmClock()
ac.set_alarm()
