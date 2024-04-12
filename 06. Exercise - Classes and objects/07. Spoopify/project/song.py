class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = float
        self.single = single
    def get_info(self) -> str:
        return f'{self.name} - {self.length}'