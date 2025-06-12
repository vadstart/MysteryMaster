from typing import Dict

from gui.gui import GameApp
from game.npc import generate_rumor, NPC

FLAVOR_TEMPLATES = [
    "{subject} looked tired around {time_str}. Probably just didn’t sleep well.",
    "Did you hear? {subject} was playing loud music in the {location} around {time_str}!",
    "{subject} and {other} had a strange talk in the {location} around {time_str}."
]

SUSPICIOUS_TEMPLATES = [
    "I saw {subject} sneaking around the {location} at {time_str}. Kinda shady.",
    "You know, {subject} hasn’t been the same since that weird thing in the {location}.",
    "{subject} was muttering to themselves in the {location}. At {time_str}. Creepy."
]

# Create NPCs
npc_list = []
npc_list.append(NPC("Cassandra", "🦊"))
npc_list.append(NPC("Mr Whiskers", "🐈"))
npc_list.append(NPC("Mildred", "🔮"))

if __name__ == "__main__":
    GameApp().run()

# Define real event (monster/vampire action)
# real_event = Rumor(
#     source="Felix",
#     subject="Marla",
#     event="saw Marla over a body in the alley",
#     location="Back Alley",
#     time="21:30",
#     certainty=0.95,
#     origin="Felix"
# )
# npc_list["Felix"].beliefs.append(real_event)
#
# # Spread rumors through the network
# rumor_chain = [real_event]
# current_rumor = real_event
# spread_order = ["Dana", "Harold"]
#
# for name in spread_order:
#     npc = npc_list[name]
#     new_rumor = npc.spread_rumor(current_rumor)
#     if new_rumor:
#         rumor_chain.append(new_rumor)
#         current_rumor = new_rumor


# Generate warmup rumors
# rumor_pool = []
# for _ in range(10):
#     rumor = generate_rumor(npc_list, FLAVOR_TEMPLATES, SUSPICIOUS_TEMPLATES)
#     rumor_pool.append(rumor)
    # npc_list[rumor.source].seen_events.append(rumor)

# print(rumor_pool[0])
# mutatedRumor = mutate_rumor(rumor_pool[0], random.choice(NPCS))
# print (mutatedRumor)
# mutatedRumor = mutate_rumor(mutatedRumor, random.choice(NPCS))
# print (mutatedRumor)
# mutatedRumor = mutate_rumor(mutatedRumor, random.choice(NPCS))
# print (mutatedRumor)

# # Simulate interrogation
# interrogation_results = {}
# for npc in npc_list.values():
#     interrogation_results[npc.name] = npc.respond_to_interrogation()
#
# interrogation_results["rumor_chain"] = [f"{r.source} -> {r.event}" for r in rumor_chain]
#
# def display_interrogation_results_rich(results):
#     console = Console()
#     console.rule("[bold red]🕵️ INTERROGATION RESULTS")
#
#     for name in ["Felix", "Dana", "Harold", "Marla"]:
#         text = Text(f"{name}: ", style="bold cyan")
#         text.append(results[name], style="white")
#         console.print(Panel(text, title=name, subtitle="Belief or Memory", style="green"))
#
#     chain = "\n".join(f"• [yellow]{link}[/yellow]" for link in results["rumor_chain"])
#     console.print(Panel(chain, title="Rumor Chain", style="magenta"))
#     console.rule()
#
# display_interrogation_results_rich(interrogation_results)
