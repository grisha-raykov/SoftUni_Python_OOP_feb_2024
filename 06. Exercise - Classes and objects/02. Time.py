class Time:
    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        # if hours <= Time.max_hours and minutes <= Time.max_minutes and seconds <= Time.max_seconds: #I predict there might be a problem here
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self) -> str:
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self) -> None:
        self.seconds += 1
        self.update_valid_time()
        return self.get_time()

    def update_valid_time(self) -> None:
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

