"""
Game Analytics Dashboard

Ce script analyse les données d'un jeu vidéo comprenant des joueurs,
 des sessions de jeu,
des modes de jeu et des réalisations (achievements).
Il utilise des compréhensions
de listes, dictionnaires et sets pour calculer :

- Les joueurs avec des scores élevés (>2000)
- Les scores doublés
- Les joueurs actifs (ayant joué plus de 25 sessions)
- Les catégories de score (high, medium, low)
- Les comptes de réalisations par joueur
- Les ensembles uniques de joueurs et de réalisations
- Les statistiques combinées telles que le joueur avec
le meilleur score et la moyenne des scores

Les annotations de type (`type hints`) sont utilisées pour
clarifier les types des variables.
"""


if __name__ == "__main__":
    data: list[dict[str, any]] = [{
        'players':
        {
            'alice':
            {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5
            },
            'bob':
            {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2
            },
            'charlie':
            {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7
            },
            'diana':
            {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4
            },
            'eve':
            {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7
            },
            'frank':
            {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1
            }
        },
        'sessions':
        [
            {
                'player': 'bob',
                'duration_minutes': 94,
                'score': 1831,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'bob',
                'duration_minutes': 32,
                'score': 1478,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 17,
                'score': 1570,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 98,
                'score': 1981,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 15,
                'score': 2361,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'eve',
                'duration_minutes': 29,
                'score': 2985,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 34,
                'score': 1285,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'alice',
                'duration_minutes': 53,
                'score': 1238,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 1555,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'frank',
                'duration_minutes': 92,
                'score': 2754,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 98,
                'score': 1102,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'diana',
                'duration_minutes': 39,
                'score': 2721,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 46,
                'score': 329,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 56,
                'score': 1196,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 117,
                'score': 1388,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'diana',
                'duration_minutes': 118,
                'score': 2733,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 22,
                'score': 1110,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'frank',
                'duration_minutes': 79,
                'score': 1854,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'charlie',
                'duration_minutes': 33,
                'score': 666,
                'mode': 'ranked',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 101,
                'score': 292,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 25,
                'score': 2887,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'diana',
                'duration_minutes': 53,
                'score': 2540,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'eve',
                'duration_minutes': 115,
                'score': 147,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'frank',
                'duration_minutes': 118,
                'score': 2299,
                'mode': 'competitive',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 42,
                'score': 1880,
                'mode': 'casual',
                'completed': False
            },
            {
                'player': 'alice',
                'duration_minutes': 97,
                'score': 1178,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 18,
                'score': 2661,
                'mode': 'competitive',
                'completed': True
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 761,
                'mode': 'ranked',
                'completed': True
            },
            {
                'player': 'eve',
                'duration_minutes': 46,
                'score': 2101,
                'mode': 'casual',
                'completed': True
            },
            {
                'player': 'charlie',
                'duration_minutes': 117,
                'score': 1359,
                'mode': 'casual',
                'completed': True
            }
        ],
        'game_modes':
        [
            'casual',
            'competitive',
            'ranked'
        ],
        'achievements':
        [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer'
        ]
    }
    ]
    hight_score: list[str] = []
    total_scores: list[int] = [
        player['total_score'] * 2
        for player in data[0]['players'].values()
    ]
    player_active: list[str] = []
    score_categorie: dict[str, int] = {
        'high': 0,
        'medium': 0,
        'low': 0
    }

    for player in data[0]['players'].values():
        score = player['total_score']
        if score > 5000:
            score_categorie['high'] += 1
        elif score >= 2000:
            score_categorie['medium'] += 1
        else:
            score_categorie['low'] += 1
    player_score: dict[str, int] = {
        name: player['total_score']
        for name, player in data[0]['players'].items()
    }
    player_achivement: dict[str, int] = {
        name: player['achievements_count']
        for name, player in data[0]['players'].items()
    }
    player_unique: set[str] = set((data[0]['players']))
    unique_achivement: set[str] = set((data[0]['achievements']))
    active_regions: set[str] = set()
    for name, player in data[0]['players'].items():
        if (player['total_score'] > 2000):
            hight_score.append(name)
        if (player['sessions_played'] > 25):
            player_active.append(name)
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000): ", hight_score)
    print("Scores doubled:", total_scores)
    print("Active players:", player_active)
    print()
    print("=== Dict Comprehension Examples ===")
    print("Player scores:", player_score)
    print("Score categories:", score_categorie)
    print("Achievement counts:", player_achivement)
    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", player_unique)
    print("Unique achievements:", unique_achivement)
    print()
    print("=== Combined Analysis ===")
    print("Total players:", len(data[0]['players']))
    print("Total unique achievements:", len(unique_achivement))
    print(f"Average score: {(sum(total_scores)/2)/len(total_scores):.2f}")
    name: str
    stats: dict[str, int]
    name, stats = max(
        data[0]['players'].items(),
        key=lambda item: item[1]['total_score'])
    print(f"Top performer: {name}", end=" ")
    print(f"({stats['total_score']} points,", end="")
    print(f"{stats['achievements_count']} achievements)")
