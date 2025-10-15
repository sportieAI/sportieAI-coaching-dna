import matplotlib.pyplot as plt
from collections import Counter
import json

def load_coaching_tree(path="coaching_tree_matrix.json"):
    with open(path, "r") as f:
        return json.load(f)

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
    plt.show()

if __name__ == "__main__":
    tree = load_coaching_tree()
    visualize_signal_density(tree)

