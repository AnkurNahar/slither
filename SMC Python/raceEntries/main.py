from race import Race
from entrant import Entrant

def main():
   
    race1 = Race("RACE 1", "10:00 AM May 12, 2021")
    race2 = Race("RACE 2", "11:00 AM May 12, 2021")
    race3 = Race("RACE 3", "12:00 PM May 12, 2021")

    race1.add_entrant(Entrant("Misty Spirit", "John Valazquez"))
    race1.add_entrant(Entrant("Frankly I'm Kidding", "Mike E. Smith"))

    race2.add_entrant(Entrant("Rage Against the Machine", "Russell Baze"))
    race2.add_entrant(Entrant("Night Runner", "Edgar Prado"))

    race3.add_entrant(Entrant("Secretariat", "Bill Shoemaker"))
    race3.add_entrant(Entrant("Man o' War", "David A. Gall"))
    race3.add_entrant(Entrant("Seabiscuit", "Angel Cordero Jr"))

    days_schedule = [race1, race2, race3]

    for race in days_schedule:
        race.print_race_entries()


if __name__ == "__main__":
    main()