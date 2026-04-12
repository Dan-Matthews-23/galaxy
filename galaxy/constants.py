# constants.py

CIV_DATA = {
    1: {
        'name': 'The New United Nations',
        'income_mod': 1.0,
        'attack_mod': 1.0,
        'defence_mod': 1.5,
        'intelligence_mod': 1.0,
        'motto': 'United we stand',
        'leader_title': 'Secretary-General',
        'short_description': 'A true united democracy to serve all mankind. The New United Nations favours debate over brute force and boasts an impressive defensive boost over the other civilisations',
        'long_description': '',        
    },

    2: {
        'name': 'Future Corp',
        'income_mod': 1.5,
        'attack_mod': 1.0,
        'defence_mod': 1.0,
        'intelligence_mod': 1.0,
        'motto': 'Fortune favours the bold',
        'leader_title': 'Chief Executive',
        'short_description': 'Future Corp provides workers with homes, food and purpose, but only for those who work for it. Exploitation through efficiency delivers a considerable income boost over other civilisations',
        'long_description': '',
    },
 
    3: {
        'name': 'The State',
        'income_mod': 1.0,
        'attack_mod': 1.0,
        'defence_mod': 1.0,
        'intelligence_mod': 1.5,
        'motto': 'The State is sight. The State is Truth',
        'leader_title': 'Overseer',
        'short_description': 'We are watching. Remain vigilant. Report suspicion. The state will provide. This civilisation boasts a considerable intelligence boost over others',
        'long_description': '',
    },

    4: {
        'name': 'The Conclave',
        'income_mod': 1.0,
        'attack_mod': 1.5,
        'defence_mod': 1.0,
        'intelligence_mod': 1.0,
        'motto': 'You will serve',
        'leader_title': 'Emperor',
        'short_description': 'Diplomacy is for the weak. Conquest is the future. All must serve. Glory to the empire! This civilisation boasts a considerable attack boost over others',
        'long_description': '',
    },    
}

# constants.py

TROOP_DATA = {
    1: { # The New United Nations
        'attack_units': [
            {'level': 1, 'name': 'Peacekeeper Corps', 'cost': 150, 'power': 10},
            {'level': 2, 'name': 'Aegis Vanguard', 'cost': 400, 'power': 30}
        ],
        'defense_units': [
            {'level': 1, 'name': 'Guardian Garrison', 'cost': 100, 'power': 15}
        ]
    },
    2: { # Future Corp
        'attack_units': [
            {'level': 1, 'name': 'Asset Recovery Team', 'cost': 200, 'power': 12},
            {'level': 2, 'name': 'Hostile Takeover Division', 'cost': 500, 'power': 35}
        ],
        
    }
    2: { # The State
        'attack_units': [
            {'level': 1, 'name': 'Asset Recovery Team', 'cost': 200, 'power': 12},
            {'level': 2, 'name': 'Hostile Takeover Division', 'cost': 500, 'power': 35}
        ],        
    }
    2: { # The Conclave
        'attack_units': [
            {'level': 1, 'name': 'Asset Recovery Team', 'cost': 200, 'power': 12},
            {'level': 2, 'name': 'Hostile Takeover Division', 'cost': 500, 'power': 35}
        ],        
    }
}


























if __name__ == "__main__":
    print(f"{'ID':<4} | {'CIVILIZATION':<25} | {'INC':<5} | {'ATK':<5} | {'DEF':<5} | {'INT':<5}")
    print("-" * 65)

    for civ_id, data in CIV_DATA.items():
        # Extracting the modifiers with a default of 1.0 just in case
        inc = data.get('income_mod', 1.0)
        atk = data.get('attack_mod', 1.0)
        dfn = data.get('defence_mod', 1.0)
        itl = data.get('intelligence_mod', 1.0)
        name = data.get('name', 'Unknown')

        # Formatting the output into a clean table
        print(f"{civ_id:<4} | {name:<25} | {inc:<5} | {atk:<5} | {dfn:<5} | {itl:<5}")

    print("-" * 65)