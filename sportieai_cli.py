# SportieAI CLI
import argparse
from sportieai import simulate_matchup, echo_library, load_team_history

parser = argparse.ArgumentParser(description="SportieAI Cognitive Cockpit")
parser.add_argument("--team", type=str, help="Team abbreviation (e.g., KC)")
parser.add_argument("--opponent", type=str, help="Opponent abbreviation")
parser.add_argument("--year", type=int, help="Season year")
parser.add_argument("--echo", action="store_true", help="Trigger legacy echo")
parser.add_argument("--history", action="store_true", help="Print team signal history")

args = parser.parse_args()

if args.history:
    print(load_team_history(args.team))
elif args.echo:
    print(echo_library(args.team, args.year))
else:
    result = simulate_matchup(args.team, args.opponent, args.year)
    print("Matchup Simulation:", result)
