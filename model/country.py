from dataclasses import dataclass
@dataclass
class Country:
    state: int
    abbr: str
    id: int

    @classmethod
    def __hash__(self):
        return hash(self.abbr)
    @classmethod
    def __str__(self):
        return f"{state}"

    @classmethod
    def __eq__(self,el1, el2):
        return el1.abbr < el2.abbr