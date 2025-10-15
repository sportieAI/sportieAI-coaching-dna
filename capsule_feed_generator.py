import json
import random

def load_capsules(path="capsule_templates.json"):
    with open(path, "r") as f:
        return json.load(f)

def generate_weekly_feed(capsules, num=5):
    return random.sample(capsules, num)

if __name__ == "__main__":
    capsules = load_capsules()
    feed = generate_weekly_feed(capsules)
    print("🧠 Weekly Capsule Feed:\n")
    for c in feed:
        print(f"- {c['capsule']} ({c['coach']} → {c['signal_trigger']})")
