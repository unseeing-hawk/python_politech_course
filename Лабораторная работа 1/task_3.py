list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players_count = len(list_players)
half_index = players_count//2

print(list_players[:half_index])
print(list_players[half_index:])
