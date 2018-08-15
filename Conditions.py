class Conditions:

    def __init__(self):
        self.Conditions = list()

    def check_cond(self,name):
        if len(self.Conditions):
            for cond in self.Conditions:
                if cond[0] == name:
                    return True
        return False

    def add_cond(self,name,title):
        if not self.check_cond(name):
            self.Conditions.append([name,title])

    def get_cond(self):
        return self.Conditions