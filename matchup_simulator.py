# Matchup Simulator
import sportieai

def simulate_matchup(team_a, team_b, year):
    a_capsule = sportieai.load_capsule(team_a, year)
    b_capsule = sportieai.load_capsule(team_b, year)

    signal_diff = sportieai.compare_signals(a_capsule, b_capsule)
    emotional_echo = sportieai.echo_resonance(team_a, team_b, year)

    result = sportieai.run_simulation(signal_diff, emotional_echo)
    return result

# Example
if __name__ == "__main__":
    outcome = simulate_matchup("KC", "BUF", 2022)
    print("Simulation Result:", outcome)
