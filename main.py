"""
Namn: Noah de Luna
KTH-mail: noahdl@kth.se
"""
from readbooks import max,min, result, measure_memory
import timeit

if __name__ == "__main__":
    k= 10
    #Skriva ut topplistorna:
    #result(k)
    
    #Testa tiden:
    """
    bintid = timeit.timeit(stmt = lambda: max(k), number = 100)
    print(f"Alternativ 1 där n = 75000 och k = {k} tog", round(bintid, 4) , "sekunder")

    bintid = timeit.timeit(stmt = lambda: min(k), number = 100)
    print(f"Alternativ 2 där n = 75000 och k = {k} tog", round(bintid, 4) , "sekunder")
"""
    #Testa minnesåtgången:
    """
    print("Max-heap:", measure_memory(max, k), "MB")
    print("Min-heap:", measure_memory(min, k), "MB")
"""
    #Testa energianvändingen:
    repetitions = 1
    from codecarbon import OfflineEmissionsTracker

    tracker = OfflineEmissionsTracker(
        project_name = "Booklist",
        country_iso_code="SWE",         # välj Sverige som land för beräkning av koldioxidkonsumption
        log_level="error",              # kör spåraren i "tyst" läge
        save_to_file=False              # spara inte resultatet som csv-fil
    )

    tracker.start_task()
    for j in range(repetitions):
        max(k)                               # spåraren tittar bara på det som händer mellan start_task och stop_task!
    co2_1 = tracker.stop_task()           # lagra resultatet i en variabel

    tracker.start_task()                # det går bra att spåra flera olika algoritmer i samma körning
    for j in range(repetitions):
            min(k) 
    co2_2 = tracker.stop_task()        # ...men kom ihåg att ändra variabelnamnet

    print(co2_1.emissions * 1000 / repetitions, "gram CO2")        # multiplicera med 1000 för att skriva ut i g CO2 (istället för kg)
    print(co2_2.emissions * 1000 / repetitions, "gram CO2")