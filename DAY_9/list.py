travel_log = {
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_no": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_no": 5
    },
}

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = times_visited
    new_country["total_no"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
