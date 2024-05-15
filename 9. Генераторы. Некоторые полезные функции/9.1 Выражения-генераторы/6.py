cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

g = (cities[i % 6] for i in range(1_000_000))

print(*(next(g) for _ in range(20)))
