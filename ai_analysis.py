def analyze_outbreak(infected_list, population):
    peak_infected = max(infected_list)
    peak_day = infected_list.index(peak_infected)

    percent = (peak_infected / population) * 100

    if percent > 40:
        risk = "HIGH"
    elif percent > 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print("\n----- AI OUTBREAK ANALYSIS -----")
    print("Peak infection day:", peak_day)
    print("Maximum infected:", int(peak_infected))
    print("Risk level:", risk)

    return peak_day, peak_infected, risk