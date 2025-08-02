class Race:

    def __init__(self, race_name, race_time):
        self.race_name = race_name
        self.race_time = race_time
        self.entrants = [] 

    def add_entrant(self, entrant):
        self.entrants.append(entrant)

    def print_race_entries(self):
        print(f"{self.race_name}: {self.race_time}\n")
        
        for entrant in self.entrants:
            print(f"  Horse: {entrant.horse_name}")
            print(f"  Jockey: {entrant.jockey_name}\n")