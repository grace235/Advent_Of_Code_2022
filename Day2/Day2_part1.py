with open('input.txt', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

def points_per_round(round_string):
    opponent_shape = map_input[round_string[0]]
    our_shape = map_input[round_string[2]]

    if opponent_shape == our_shape:
        return points_per_outcome['Draw'] + points_per_shape[our_shape]
    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        # loss for us
        return points_per_outcome['Lose'] + points_per_shape[our_shape]
    else:
        return points_per_outcome['Win'] + points_per_shape[our_shape]
    

sum([points_per_round(round_string) for round_string in rounds])
