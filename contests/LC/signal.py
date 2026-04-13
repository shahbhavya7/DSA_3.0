class Solution:
    def trafficSignal(self, timer: int) -> str:
        if (timer == 0):
            return "green"
        elif (timer == 30):
            return "yellow"
        elif (30 < timer <= 90):
            return "red"
        else:
            return "Invalid"