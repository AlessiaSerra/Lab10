from dataclasses import dataclass
@dataclass
class Country:
    state: int
    abbr: str
    id: int

    def __hash__(self):
        return hash(self.abbr)

    def __str__(self):
        return f"{self.state}"


    def __eq__(self,el2):
        return self.abbr < el2.abbr
