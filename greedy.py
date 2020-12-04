# -*- coding: utf-8 -*-
from timeit import timeit
from classes.team import Team

def create_team(names, aptitudes, matches, binary, ids):
    team = []
    for i in range(len(names)):
        team.append(Team(names[i], aptitudes[i], matches[i], binary[i], ids[i]))
    return team

def greedy(players, max_matches, keyfunction):
    players_copy = sorted(players, key=keyfunction, reverse=True)

    result = []
    total_aptitudes = 0
    total_matches = 0

    for i in range(len(players)):
        if (total_matches + players_copy[i].get_match() <= max_matches):
            if (len(result) < 5):
                players_copy[i].binary = 1
                result.append(players_copy[i])
                total_aptitudes = total_aptitudes + players_copy[i].get_aptitude()
                total_matches = total_matches + players_copy[i].get_match()
            else:
                result.append(players_copy[i])
    return result, total_matches, total_aptitudes

def exec_one():
    players = ['Lucio', 'Mauro', 'Filho', 'Luan', 'Podeisso', 'Arnaldo', 'Ronaldo', 'Neymar', 'Theus', 'Fenomeno']
    aptitudes = [3, 5, 6, 9, 4, 3, 3, 7, 5, 8]
    matches = [2, 4, 2, 8, 2, 4, 3, 6, 1, 7]
    binary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    item_list = create_team(players, aptitudes, matches, binary, ids)
    max_matches = 20

    team_list, total_matches, total_aptitudes = greedy(item_list, max_matches, Team.ratio)

    order_list = []
    binary_list = []

    for i in range(len(team_list)):
        row = {
            "ids": team_list[i].ids,
            "nome": team_list[i].name,
            "aptidao": team_list[i].aptitude,
            "partidas": team_list[i].match,
            "binario": team_list[i].binary,
        }
        order_list.append(row)

    def get_id(obj):
        return obj['ids']

    order_list.sort(key=get_id)
    for row in order_list:
        binary_list.append(row['binario'])

    print(f'Resultados do exercicio 1:\n\n'
        f'Lista Binaria: {binary_list}\n'
        f'Total de aptidao: {total_aptitudes}\n'
        f'Total de partidas: {total_matches}')

# Contador de execução
exec_one_time = timeit(lambda: exec_one(), number=1)

print(f'\nTempo de execucao do exercicio 1: {round(exec_one_time, 10)}s')
