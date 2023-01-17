#!/usr/bin/env python


import pandas as pd


def clean_up(a_string):
    return a_string.lower().replace(' ', '_').replace('ª', '')


def load_data(csv_file_name, csv_separator):
    data = pd.read_csv(csv_file_name, sep=csv_separator)
    final_data = data[['fase', 'team_1', 'team_2', 'score_1', 'score_2']].dropna()
    final_data['score_1'] = final_data['score_1'].astype(int)
    final_data['score_2'] = final_data['score_2'].astype(int)
    final_data['fase'] = final_data['fase'].apply(clean_up)
    return final_data


def parse_games(full_data):
    all_games = []
    for _, row in full_data.iterrows():
        team_1 = row['team_1']
        team_2 = row['team_2']
        score_1 = row['score_1']
        score_2 = row['score_2']
        fase = row['fase']
        all_games.append({'fase': fase, team_1: score_1, team_2: score_2})
    return all_games


def get_team_names(full_data):
    """
    Return team's names
    :return: set
    """
    names = set()
    for _, row in full_data.iterrows():
        names.add(row['team_1'])
        names.add(row['team_2'])
    return sorted(names)


def main():
    print("Parsing data")
    data = load_data('basket/data/basket_2021-2022.csv', ';')
    games = parse_games(data)
    print(games)
    teams = get_team_names(data)
    print(teams)


if __name__ == "__main__":
    main()
