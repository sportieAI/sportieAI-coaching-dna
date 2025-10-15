import json
import csv

# Load coaching tree matrix
def load_coaching_tree(path="coaching_tree_matrix.json"):
    with open(path, "r") as f:
        return json.load(f)

# Load signal tags
def load_signal_tags(path="signal_tags.csv"):
    tags = {}
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags[row["tag"]] = {
                "description": row["description"],
                "category": row["category"]
            }
    return tags

# Load capsule templates
def load_capsules(path="capsule_templates.json"):
    with open(path, "r") as f:
        return json.load(f)

# Load team history signals
def load_team_history(path="team_history_signal.json"):
    with open(path, "r") as f:
        return json.load(f)

# Load coordinator matrix
def load_coordinators(path="coordinator_matrix.json"):
    with open(path, "r") as f:
        return json.load(f)

# Get signal tags for a coach
def get_coach_signals(coach_name, coaching_tree):
    for coach in coaching_tree:
        if coach["name"].lower() == coach_name.lower():
            return coach.get("signal_tags", [])
    return []

# Get capsule commentary by scenario
def get_capsule_by_scenario(scenario, capsules):
    return [c for c in capsules if c["scenario"].lower() == scenario.lower()]

# Get team legacy tags
def get_team_legacy(team_name, team_history):
    for team in team_history:
        if team["team"].lower() == team_name.lower():
            return team.get("legacy_tags", [])
    return []

# Get coordinator traits
def get_coordinator_traits(name, coordinators):
    for coord in coordinators:
        if coord["name"].lower() == name.lower():
            return coord.get("signal_tags", [])
    return []

# Example usage
if __name__ == "__main__":
    tree = load_coaching_tree()
    tags = load_signal_tags()
    capsules = load_capsules()
    history = load_team_history()
    coords = load_coordinators()

    print("Andy Reid Signal Tags:", get_coach_signals("Andy Reid", tree))
    print("Red Zone Capsules:", get_capsule_by_scenario("Red zone playcall", capsules))
    print("Ravens Legacy Tags:", get_team_legacy("Baltimore Ravens", history))
    print("Ben Johnson Traits:", get_coordinator_traits("Ben Johnson", coords))
