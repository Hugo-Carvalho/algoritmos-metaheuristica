from timeit import timeit
from classes.team import TeamBest

def create_team(names, aptitudes, matches, binary):
    team = []
    for i in range(len(names)):
        team.append(TeamBest(names[i], aptitudes[i], matches[i], binary[i]))
    return team

def neighborhood(names, aptitudes, matches, binarys):
    pos = []
    neighbors = []

    for j in range(5):
        aux_binary = binarys.copy()
        sum_aptitudes = 0
        sum_matches = 0
        
        for i in range(10):
            if aux_binary[i] == 0 and i not in pos:
                aux_binary[i] = 1
                pos.append(i)
                break

        for i in range(10):
            if aux_binary[i] == 1 and i not in pos:
                aux_binary[i] = 0
                pos.append(i)
                break

        for i in range(10):
            if aux_binary[i] == 1:
                sum_aptitudes += aptitudes[i]
                sum_matches += matches[i]

        neighbors.append({
        "time": create_team(names, aptitudes, matches, aux_binary),
        "aptidao": sum_aptitudes,
        "partidas": sum_matches,
    })

    return neighbors       

def best_improvements(best_team, players, aptitudes, matches, max_matches, binarys):
    neighbors = neighborhood(players, aptitudes, matches, binarys)

    sum_aptitudes = 0
    sum_matches = 0
    for i in range(10):
        if best_team[i].binary == 1:
            sum_aptitudes += best_team[i].aptitude
            sum_matches += best_team[i].match

    for neighbor in neighbors:
        if sum_aptitudes < neighbor['aptidao'] and neighbor['partidas'] <= max_matches:
            best_team = neighbor['time']
            sum_aptitudes = neighbor['aptidao']
            sum_matches = neighbor['partidas']
    
    return best_team

def exec_one():    
    players = ['Lucio', 'Mauro', 'Filho', 'Luan', 'Podeisso', 'Arnaldo', 'Ronaldo', 'Neymar', 'Theus', 'Fenomeno']
    aptitudes = [3, 5, 6, 9, 4, 3, 3, 7, 5, 8]
    matches = [2, 4, 2, 8, 2, 4, 3, 6, 1, 7]
    binarys = [0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
    max_matches = 20

    first_team = create_team(players, aptitudes, matches, binarys)

    best_team = None
    while True:
        best_team = best_improvements(first_team, players, aptitudes, matches, max_matches, binarys)

        str_best_team_binarys = ''
        for team in best_team:
            str_best_team_binarys = str_best_team_binarys + str(team.binary)

        if str(str_best_team_binarys) == str(''.join([str(binary) for binary in binarys])):
            break
        
        best_team_binarys = []
        for t in best_team:
            best_team_binarys.append(t.binary)

        binarys = best_team_binarys
        first_team = best_team
        
    best_team_binarys = []
    sum_aptitudes = 0
    sum_matches = 0
    for t in best_team:
        best_team_binarys.append(t.binary)
        if t.binary == 1:
            sum_aptitudes += t.aptitude
            sum_matches += t.match

    print(f'Resultados do exercicio 2:\n\n'
        f'Lista Binaria: {best_team_binarys}\n'
        f'Total de aptidao: {sum_aptitudes}\n'
        f'Total de partidas: {sum_matches}')

# Contador de execução
exec_one_time = timeit(lambda: exec_one(), number=1)

print(f'\nTempo de execucao do exercicio 2: {round(exec_one_time, 10)}s')