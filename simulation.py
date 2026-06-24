def run_simulation(population, infected_start, days):
    S = [population - infected_start]
    I = [infected_start]
    R = [0]

    infection_rate = 0.3
    recovery_rate = 0.1
    
    immunity_days = 60        # NEW FEATURE ⭐
    immunity_loss_rate = 1 / immunity_days

    for day in range(days):
        # Normal infection
        new_infected = infection_rate * S[-1] * I[-1] / population
        
        # Recovery
        new_recovered = recovery_rate * I[-1]
        
        # Immunity loss (Recovered → Susceptible again)
        immunity_lost = immunity_loss_rate * R[-1]

        # Update values
        S.append(S[-1] - new_infected + immunity_lost)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered - immunity_lost)

    return S, I, R