from handler.storage.mainObject import MainObject
from handler.storage.objsVariables.condition import Condition
from handler.storage.objsVariables.situation import Situation


class IfSituation(Situation):
    def record(self, condition: Condition) -> "IfSituation":
        pass
    def directRecord(self, condition: Condition, action_object: MainObject) -> "IfSituation":
        self.condition = condition
        self.action_object = action_object
        return self
    def run(self) -> None:
        if self.condition.check():
            print("condition become true")
            self.action_object.run()
            print("actions runed")
        else:
            print("condition not matched")