class Logger:

    def __init__(self):
        self.mapping = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        flag = True
        if message in self.mapping:
            if self.mapping[message] <= timestamp:
                self.mapping[message] = timestamp+10
            else: 
                flag = False
        else: 
            self.mapping[message] = timestamp+10
        return flag
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)