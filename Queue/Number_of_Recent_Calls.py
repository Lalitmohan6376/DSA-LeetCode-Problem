
class RecentCounter:

    def __init__(self):
        self.q = []
        

    def ping(self, t: int):
        self.q.append(t)

        while len(self.q) > 0 and self.q[0] < t - 3000:
            self.q.pop(0)
        return len(self.q)

obj = RecentCounter()
param_1 = obj.ping(1)
param_1 = obj.ping(100)
param_1 = obj.ping(3001)
param_1 = obj.ping(3002)
