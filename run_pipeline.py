import json
import csv
import random
from collections import Counter
import matplotlib.pyplot as plt

# === Loaders ===

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_csv(path):
    tags = {}
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags[row["tag"]] = {
                "description": row["description"],
                "category": row["category"]
            }
    return tags

# === Signal Density Visualization ===

def visualize_signal_density(coaching_tree):
    all_tags = []
    for coach in coaching_tree:
        all_tags.extend(coach.get("signal_tags", []))
    tag_counts = Counter(all_tags)

    tags = list(tag_counts.keys())
    counts = list(tag_counts.values())

    plt.figure(figsize=(12, 6))
    plt.bar(tags, counts, color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.title("Signal Tag Density Across Head Coaches")
    plt.xlabel("Signal Tag")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("signal_density_chart.png")
    print("✅ Signal density chart saved as signal_density_chart.png")

# === Capsule Feed Generator ===

def generate_capsule_feed(capsules, num=5):
    feed = random.sample(capsules, num)
    print("\n🧠 Weekly Capsule Feed:")
    for c in feed:
        print(f"- {c['capsule']} ({c['coach']} → {c['signal_trigger']})")

# === Main Pipeline ===

def run_pipeline():
    print("🚀 Running SportieAI Ingestion Pipeline...\n")

    # Load all artifacts
    coaching_tree = load_json("coaching_tree_matrix.json")
    coordinator_matrix = load_json("coordinator_matrix.json")
    signal_tags = load_csv("signal_tags.csv")
    capsule_templates = load_json("capsule_templates.json")
    team_history = load_json("team_history_signal.json")

    print("✅ Artifacts loaded successfully.")

    # Visualize signal tag density
    visualize_signal_density(coaching_tree)

    # Generate capsule feed
    generate_capsule_feed(capsule_templates)

    print("\n🏁 Pipeline complete. Ready for simulation or CI integration.")

# === Entry Point ===

if __name__ == "__main__":
    run_pipeline()
