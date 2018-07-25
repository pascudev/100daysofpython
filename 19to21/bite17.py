import itertools

friends = 'Bob Dante Julian Martin'.split()
team_members = 2
order_of_teams = True

def friends_teams(friend_list, team_size, order):
    if order == False:
        get_all_teams = itertools.permutations(friend_list, team_size)
        return get_all_teams
    else:
        get_all_teams = itertools.product(friend_list, repeat=team_size)
        return get_all_teams


test = friends_teams(friends, team_members, order_of_teams)


print(list(test))
