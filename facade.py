class SubsystemA:
    def operation_a(self):
        return "Operação A do Subsistema A"

class SubsystemB:
    def operation_b(self):
        return "Operação B do Subsistema B!"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        results = []
        results.append(self._subsystem_a.operation_a())
        results.append(self._subsystem_b.operation_b())
        return "\n".join(results)

if __name__ == "__main__":
    facade = Facade()
    print(facade.operation())
