"""
Namn: Noah de Luna
KTH-mail: noahdl@kth.se
"""
from readbooks import max,min, result, measure_memory
import timeit

if __name__ == "__main__":
    k= 1000
    n=75000
    #Skriva ut topplistorna:
    print(result(k,n))
    """
    #Testa tiden:
    
    bintid = timeit.timeit(stmt = lambda: max(k,n), number = 100)
    print(f"Alternativ 1 där n = {n} och k = {k} tog", round(bintid, 4) , "sekunder")

    bintid = timeit.timeit(stmt = lambda: min(k,n), number = 100)
    print(f"Alternativ 2 där n = {n} och k = {k} tog", round(bintid, 4) , "sekunder")

    #Testa minnesåtgången:
    
    print("Max-heap:", measure_memory(max, k, n), "MB")
    print("Min-heap:", measure_memory(min, k, n), "MB")

    #Testa energianvändingen:

    """
    from codecarbon import OfflineEmissionsTracker
    rep = 100
    tracker = OfflineEmissionsTracker(
        project_name = "Booklist",
        country_iso_code="SWE",         # välj Sverige som land för beräkning av koldioxidkonsumption
        log_level="error",              # kör spåraren i "tyst" läge
        save_to_file=False              # spara inte resultatet som csv-fil
    )

    tracker.start_task()
    for i in range(rep):
        max(k,n)                               # spåraren tittar bara på det som händer mellan start_task och stop_task!
    co2_1 = tracker.stop_task()           # lagra resultatet i en variabel

    tracker.start_task()                # det går bra att spåra flera olika algoritmer i samma körning
    for i in range(rep):
        min(k,n) 
    co2_2 = tracker.stop_task()        # ...men kom ihåg att ändra variabelnamnet

    print(co2_1.emissions * 10000/rep , "gram CO2")        # multiplicera med 1000 för att skriva ut i g CO2 (istället för kg)
    print(co2_2.emissions * 10000/rep , "gram CO2")
