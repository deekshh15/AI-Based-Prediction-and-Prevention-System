from mdp_decision import choose_action
from hmm_model import detect_hidden_state
from simulation import run_simulation
from graphs import plot_graph
from ai_analysis import analyze_outbreak
from prevention import give_tips

def welcome():
    print("\n" + "="*50)
    print("🌍 AI EPIDEMIC PREDICTION SYSTEM")
    print("="*50)
    print("This system predicts how a disease spreads")
    print("and suggests smart AI prevention steps.\n")

def show_menu():
    print("\nSelect population type:")
    print("1️⃣  City")
    print("2️⃣  School / College")
    print("3️⃣  Family / Small Group")
    print("4️⃣  Custom Population")

def get_population(choice):
    if choice == "1":
        return 100000
    elif choice == "2":
        return 2000
    elif choice == "3":
        return 10
    elif choice == "4":
        return int(input("Enter total population: "))
    else:
        print("Invalid choice → Defaulting to Family 👨‍👩‍👧")
        return 10

while True:
    welcome()
    show_menu()

    choice = input("\n👉 Enter your choice (1-4): ")
    population = get_population(choice)

    print("\n--- Disease Setup ---")
    infected_start = int(input("🤒 People infected at start: "))
    days = int(input("📅 Days to simulate: "))

    print("\n⏳ Running AI Simulation...")
    S, I, R = run_simulation(population, infected_start, days)

    print("\n📊 Showing epidemic graphs...")
    plot_graph(S, I, R)

    print("\n🧠 AI OUTBREAK ANALYSIS")
    peak_day, peak_infected, risk = analyze_outbreak(I, population)

    print("\n🧬 HIDDEN OUTBREAK DETECTION (HMM)")
    state = detect_hidden_state(I, population)

    print("\n🎯 AI DECISION MAKING (MDP)")
    choose_action(state)

    print("\n🛡️ PREVENTION TIPS")
    give_tips(risk)

    again = input("\n🔁 Run another simulation? (yes/no): ")
    if again.lower() != "yes":
        print("\n💙 Thank you for using AI Epidemic Prediction System!")
        print("Stay Safe 🌸")
        break