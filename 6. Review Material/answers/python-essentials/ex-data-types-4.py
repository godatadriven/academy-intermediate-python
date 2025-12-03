name = name_of_sport.replace('HOCKEY', 'Shinty').title()
years = datetime.datetime.now().year - int(birth_year)

print(
    f"{name} has been around since {birth_year}. That's {years} years!"
)
