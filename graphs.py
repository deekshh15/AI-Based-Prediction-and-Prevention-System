import matplotlib.pyplot as plt

def plot_graph(S, I, R):
    plt.figure(figsize=(8,5))
    plt.plot(S, label="Healthy")
    plt.plot(I, label="Infected")
    plt.plot(R, label="Recovered")

    plt.title("Epidemic Spread Simulation")
    plt.xlabel("Days")
    plt.ylabel("Number of People")
    plt.legend()
    plt.show()

    print("\nGRAPH EXPLANATION:")
    print("Healthy line ↓ means people getting infected")
    print("Infected peak shows worst outbreak day")
    print("Recovered line ↑ shows people healing")