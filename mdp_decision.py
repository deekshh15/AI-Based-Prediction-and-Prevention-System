def choose_action(outbreak_state):

    print("\n----- MDP DECISION MAKER -----")

    states = ["LOW", "MEDIUM", "HIGH"]
    actions = ["Do Nothing", "Masks", "Vaccination", "Lockdown"]

    # Reward matrix (state vs action)
    # rows = states, columns = actions
    rewards = {
        "LOW":     [5, 10, 8, -5],
        "MEDIUM":  [0, 15, 20, 10],
        "HIGH":    [-10, 10, 25, 40]
    }

    state_rewards = rewards[outbreak_state]
    best_action_index = state_rewards.index(max(state_rewards))
    best_action = actions[best_action_index]

    print("Best action recommended by AI:", best_action)

    return best_action