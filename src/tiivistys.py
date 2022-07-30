class Tiivistys:
    def __init__(self, sana="sana"):
        self.sana = sana

    def mika_on_sana(self):
        return self.sana

    def __str__(self):
        return f"{self.mika_on_sana()}"
