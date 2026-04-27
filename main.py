#1-misol
class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Yosh: {self.yosh}")


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet):
        super().__init__(ism, yosh)
        self.universitet = universitet

    def malumot(self):
        super().malumot()
        print(f"Universitet: {self.universitet}")


# Test
t = Talaba("Ali", 20, "TATU")
t.malumot()
