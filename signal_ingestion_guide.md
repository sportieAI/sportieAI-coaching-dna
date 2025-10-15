# 🧠 Signal Ingestion Guide

This guide explains how to ingest coaching, coordinator, and team-level signal data into SportieAI’s simulation engine.

---

## 📦 Artifact Overview

| File | Purpose |
|------|---------|
| `coaching_tree_matrix.json` | Head coach lineage, scheme, and signal tags |
| `coordinator_matrix.json` | OC/DC traits, scheme identity, and legacy echoes |
| `signal_tags.csv` | Definitions for all behavioral and schematic traits |
| `capsule_templates.json` | Commentary tied to coaching decisions and signal triggers |
| `team_history_signal.json` | Franchise-level legacy burdens and culture tags |

---

## 🔁 Ingestion Flow

1. **Load JSON/CSV files** using `signal_ingestion.py`
2. **Map signal tags** to coaches, coordinators, and teams
3. **Inject capsules** based on scenario + signal trigger
4. **Simulate matchups** using combined signal traits
5. **Generate commentary** using capsule templates and legacy echoes

---

## 🧠 Signal Tag Categories

| Category | Examples |
|----------|----------|
| Offensive Philosophy | `SpeedOverSize`, `QBAmplifier`, `MotionMaster` |
| Defensive Philosophy | `EraserLogic`, `TempoControl`, `DefenseOverride` |
| Behavioral Trait | `AggressionCollapse`, `PatternRepetitionRisk`, `TrustCollapse` |
| Franchise Trait | `LegacyBurden`, `BigBrotherCeiling`, `PeakCollapseRisk` |
| Emotional Trait | `BlinkRisk`, `ConfidenceScript`, `CultureMismatch` |

---

## 🧬 Capsule Injection

Capsules are triggered when:
- A coach or coordinator activates a signal tag
- A scenario matches a known capsule template
- A team’s legacy tag aligns with outcome

> Example:
> *“LaFleur’s conservative pivot triggered collapse. Red zone creativity suppressed. Legacy burden reinforced.”*

---

## 🪞 Matchup Simulation

To simulate a matchup:
1. Select two teams
2. Load head coach and coordinator signal tags
3. Overlay team legacy tags
4. Inject capsule commentary based on scenario triggers

> Example:
> *“McDaniel’s motion discipline distorted Spagnuolo’s pressure logic. QB amplifier neutralized. Tempo override confirmed.”*

---

## 🧠 Expansion Tips

- Add new coaches or coordinators to their respective matrices
- Define new signal tags in `signal_tags.csv`
- Create new capsule templates tied to real game moments
- Update team history signals as culture evolves

---

## 🤝 Contributor Notes

- Keep signal tags modular and reusable
- Use real-world coaching decisions to inspire capsules
- Maintain emotional and strategic clarity in legacy echoes

---

SportieAI doesn’t just simulate football—it simulates **why football happens**.  
This guide is your key to injecting cognition into every snap.

