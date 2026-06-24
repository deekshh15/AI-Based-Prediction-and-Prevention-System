import numpy as np

def detect_hidden_state(infected_list, population):

    print("\n----- HMM OUTBREAK DETECTOR -----")

    # Hidden states
    states = ["LOW", "MEDIUM", "HIGH"]

    # Start probabilities
    start_prob = np.array([0.6, 0.3, 0.1])

    # Transition probabilities
    transition_prob = np.array([
        [0.7, 0.2, 0.1],  # LOW → LOW/MED/HIGH
        [0.2, 0.6, 0.2],  # MED → LOW/MED/HIGH
        [0.1, 0.3, 0.6]   # HIGH → LOW/MED/HIGH
    ])

    # Convert infected numbers into observations
    observations = []
    for i in infected_list:
        percent = (i / population) * 100
        if percent < 10:
            observations.append(0)   # low cases
        elif percent < 30:
            observations.append(1)   # medium cases
        else:
            observations.append(2)   # high cases

    # Viterbi Algorithm (HMM core)
    V = np.zeros((len(states), len(observations)))
    V[:,0] = start_prob

    for t in range(1, len(observations)):
        for s in range(len(states)):
            prob = V[:,t-1] * transition_prob[:,s]
            V[s,t] = np.max(prob)

    final_state_index = np.argmax(V[:,-1])
    final_state = states[final_state_index]

    print("Hidden outbreak stage detected:", final_state)
    return final_state