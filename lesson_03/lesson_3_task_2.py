from smartphone import Smartphone

catalog = [Smartphone("Iphone", 11, "+79521234567"),
           Smartphone("Iphone", 15, "+79255486958"),
           Smartphone("Samsung", "Galaxy s10", "+79112563485"),
           Smartphone("Xiaomi", "Redmi 12C", "+79778569254"),
           Smartphone("Nokia", "Lumia 640", "+79854752635")]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
    