class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if hours <= Time.max_hours:
            self.hours = hours

        if minutes <= Time.max_minutes:
            self.minutes = minutes

        if seconds <= Time.max_seconds:
            self.seconds = seconds

    def format_time(self, number):
        if number < 10:
            return f"0{number}"
        return number

    def get_time(self):
        return f"{self.format_time(self.hours)}:{self.format_time(self.minutes)}:{self.format_time(self.seconds)}"


    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()



time = Time(23, 59, 59)
print(time.next_second())