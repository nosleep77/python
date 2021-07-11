class Time:
    # previous method definitions here...

    def after(self, other):
        if self.hours > other.hours:
            return True
        if self.hours < other.hours:
            return False


time1 = Time()
time2 = Time()

time1.hours = 3
time2.hours = 7

print(time1.after(time2))

