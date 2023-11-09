import time

class ObjChecker:

    def __init__(self,wait_sec=1,timeout=120) -> None:
        self.timeout=timeout
        self.timer = 0
        self.wait_sec = wait_sec
        self.isTimeOut = False

    def isTimeUP(self,timer):
        if timer >= self.timeout:
            self.isTimeOut = True
            self.set_timer()
            return True
        else:
            return False

    def set_timer(self):
        self.timer = 0

    def wait_for_Checking(self,check):
        time.sleep(self.wait_sec)
        self.timer += self.wait_sec
        if not self.object_checker(check) and not self.isTimeUP(self.timer):
            return False
        return True

    def object_checker(self,obj):
        if obj != None:
            return True
        else:
            return False

    def wait_Action(self,action):
        checker = action()
        isFinished = self.wait_for_Checking(checker)
        if not isFinished:
            self.wait_Action(action)
        else:
            self.set_timer()
            return checker

    """ Check if time is up """
    def checkTime(self):
        return self.isTimeOut

if __name__ == "__main__":
    print("Object Checker")