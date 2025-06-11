# Knowledge chains (acyclic directed graph):
    # GoindAroundTheWorld -> Got80Days -> ItsABet

import random
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from uuid import uuid4

@dataclass
class Rumor:
    source: str                 # NPC who is spreading the rumor
    subject: str                # NPC the rumor is about
    event: str                  # e.g.,'sighting','hearsay', 'flavor'
    location: str               # Where the event took place
    time: str              # e.g., 'night', 'morning'
    certainty: float             # How confident the speaker is
    origin: str
    is_true: Optional[bool] = None  # For debugging / tracking

@dataclass
class NPC:
    name: str
    beliefs: List[Rumor] = field(default_factory=list)

    def spread_rumor(self, known_rumor: Rumor) -> Optional[Rumor]:
        # Mutate the rumor slightly
        new_certainty = max(0.3, min(1.0, known_rumor.certainty + random.uniform(-0.2, 0.2)))
        mutation_templates = [
            f"{known_rumor.source} told me {known_rumor.subject} was seen at the {known_rumor.location} around {known_rumor.time}.",
            f"Someone said {known_rumor.subject} was acting weird near the {known_rumor.location} at {known_rumor.time}.",
            f"I think {known_rumor.subject} was sneaking around {known_rumor.location} at {known_rumor.time}.",
            f"Rumor has it {known_rumor.subject} did something shady at {known_rumor.location}.",
        ]
        mutation_text = random.choice(mutation_templates)
        mutated_rumor = Rumor(
            source=self.name,
            subject=known_rumor.subject,
            event=mutation_text,
            location=known_rumor.location,
            time=known_rumor.time,
            certainty=new_certainty,
            origin=known_rumor.origin
        )
        self.beliefs.append(mutated_rumor)
        return mutated_rumor

    def respond_to_interrogation(self):
        if not self.beliefs:
            return f"{self.name}: I don't really know anything..."
        dialogue = []
        for belief in self.beliefs:
            dialogue.append(f"{self.name}: {belief.event} (certainty: {belief.certainty:.2f})")
        return "\n".join(dialogue)

# @dataclass
# class NPCMemory:
#     name: str
#     seen_events: List[Rumor] = field(default_factory=list)
#     heard_rumors: List[Rumor] = field(default_factory=list)
#     beliefs: Dict[str, bool] = field(default_factory=dict)  # e.g. {"Marla is suspicious": True}
#     is_vampire: bool = False
#
# @dataclass
# class VampireState:
#     last_fed: Optional[datetime] = None
#     recent_actions: List[str] = field(default_factory=list)

# NPCS = ["Cassandra", "Mildred", "Mr Whiskers", "Randy Hawthorne", "Michael"]
# LOCATIONS = ["cafe", "kitchen", "storage room", "attic", "cellar", "back alley", "park"]
#
# FLAVOR_TEMPLATES = [
#     "{subject} looked tired around {time_str}. Probably just didn’t sleep well.",
#     "Did you hear? {subject} was playing loud music in the {location} around {time_str}!",
#     "{subject} and {other} had a strange talk in the {location} around {time_str}."
# ]
#
# SUSPICIOUS_TEMPLATES = [
#     "I saw {subject} sneaking around the {location} at {time_str}. Kinda shady.",
#     "You know, {subject} hasn’t been the same since that weird thing in the {location}.",
#     "{subject} was muttering to themselves in the {location}. At {time_str}. Creepy."
# ]
#
# def generate_random_time():
#     # Simulate a time between 6 AM and 2 AM
#     hour = random.choice(list(range(6, 24)) + list(range(0, 3)))
#     minute = random.choice([0, 15, 30, 45])
#     return datetime(2025, 6, 10, hour, minute)

# def generate_rumor():
#     subject = random.choice(NPCS)
#     source = random.choice([npc for npc in NPCS if npc != subject])
#     time = generate_random_time()
#     location = random.choice(LOCATIONS)
#     other = random.choice([npc for npc in NPCS if npc != subject and npc != source])
#     template = random.choice(SUSPICIOUS_TEMPLATES + FLAVOR_TEMPLATES)
#     time_str = time.strftime("%H:%M")
#     text = template.format(subject=subject, location=location, time_str=time_str, other=other)
#
#     return Rumor(
#         id=str(uuid4()),
#         source=source,
#         subject=subject,
#         type="flavor" if "looked tired" in text else "sighting",
#         location=location,
#         time=time,
#         text=text,
#         strength=random.uniform(0.4, 1.0),
#         is_true=None  # For now, since these are pre-warmup, we can leave as unknown
#     )
#
# def simulate_vampire_action(vampire_name, npc_memories, current_time):
#     action = random.choice(["feed", "sneak"])
#     location = random.choice(LOCATIONS)
#     target = random.choice([n for n in NPCS if n != vampire_name])
#
#     print(action)
#
#     if action == "feed":
#         text = f"I heard a scream near the {location} around {current_time.strftime('%H:%M')}!"
#         rumor = Rumor(
#             id=str(uuid4()),
#             source="Unknown",
#             subject=target,
#             type="sighting",
#             location=location,
#             time=current_time,
#             text=text,
#             strength=1.0,
#             is_true=True
#         )
#         npc_memories[target].seen_events.append(rumor)
#         return [rumor]
#
#     elif action == "sneak":
#         text = f"I saw {vampire_name} creeping into the {location} around {current_time.strftime('%H:%M')}."
#         rumor = Rumor(
#             id=str(uuid4()),
#             source=random.choice([n for n in NPCS if n != vampire_name]),
#             subject=vampire_name,
#             type="sighting",
#             location=location,
#             time=current_time,
#             text=text,
#             strength=0.9,
#             is_true=True
#         )
#         npc_memories[rumor.source].seen_events.append(rumor)
#         return [rumor]
#
#     # elif action == "charm":
#         # No obvious rumor, but maybe target later contradicts themselves
#         # return []  # Will affect belief later
#
# npc_memories = {name: NPCMemory(name=name) for name in NPCS}
#
# vampire_name = random.choice(NPCS)
#
# for name, mem in npc_memories.items():
#     mem.is_vampire = (name == vampire_name)
#     if mem.is_vampire:
#         print(f"[DEBUG] {name} is the vampire.")
#
# # Generate warmup rumors
# rumor_pool = []
# for _ in range(20):
#     rumor = generate_rumor()
#     rumor_pool.append(rumor)
#     npc_memories[rumor.source].seen_events.append(rumor)
#
# warmup_time = generate_random_time()
# vampire_rumors = simulate_vampire_action(vampire_name, npc_memories, warmup_time)
# rumor_pool.extend(vampire_rumors or [])
#
# # Pretty print them
from rich.console import Console
# from rich.table import Table
from rich.text import Text
from rich.panel import Panel

#
# def print_rumors_sorted(rumors):
#     console = Console()
#     table = Table(title="Rumor Warmup Pool")
#     table.add_column("Source", style="cyan")
#     table.add_column("Time", style="green")
#     table.add_column("Rumor", style="white")
#     table.add_column("Strength", style="magenta")
#
#     sorted_rumors = sorted(rumors, key=lambda r: (r.source, r.time))
#
#     for r in sorted_rumors:
#         table.add_row(
#             r.source, 
#             r.time.strftime("%D %H:%M"),
#             r.text, 
#             f"{r.strength:.2f}"
#             )
#
#     console.print(table)
#
# print_rumors_sorted(rumor_pool)

# Create NPCs
npc_names = ["Felix", "Dana", "Harold", "Marla"]
npc_dict: Dict[str, NPC] = {name: NPC(name) for name in npc_names}

# Define real event (monster/vampire action)
real_event = Rumor(
    source="Felix",
    subject="Marla",
    event="saw Marla over a body in the alley",
    location="Back Alley",
    time="21:30",
    certainty=0.95,
    origin="Felix"
)
npc_dict["Felix"].beliefs.append(real_event)

# Spread rumors through the network
rumor_chain = [real_event]
current_rumor = real_event
spread_order = ["Dana", "Harold"]

for name in spread_order:
    npc = npc_dict[name]
    new_rumor = npc.spread_rumor(current_rumor)
    if new_rumor:
        rumor_chain.append(new_rumor)
        current_rumor = new_rumor

# Simulate interrogation
interrogation_results = {}
for npc in npc_dict.values():
    interrogation_results[npc.name] = npc.respond_to_interrogation()

interrogation_results["rumor_chain"] = [f"{r.source} -> {r.event}" for r in rumor_chain]

def display_interrogation_results_rich(results):
    console = Console()
    console.rule("[bold red]🕵️ INTERROGATION RESULTS")

    for name in ["Felix", "Dana", "Harold", "Marla"]:
        text = Text(f"{name}: ", style="bold cyan")
        text.append(results[name], style="white")
        console.print(Panel(text, title=name, subtitle="Belief or Memory", style="green"))

    chain = "\n".join(f"• [yellow]{link}[/yellow]" for link in results["rumor_chain"])
    console.print(Panel(chain, title="Rumor Chain", style="magenta"))
    console.rule()

display_interrogation_results_rich(interrogation_results)
