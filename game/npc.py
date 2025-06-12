# game/npc.py

import random
import copy

from typing import List, Dict, Optional
from datetime import datetime, timedelta
from uuid import uuid4
from dataclasses import dataclass, field


@dataclass
class Rumor:
    id: str
    source: str                 # NPC who is spreading the rumor
    subject: str                # NPC the rumor is about
    event: str                  # e.g.,'sighting','hearsay', 'flavor'
    location: str               # Where the event took place
    time: datetime              # e.g., 'night', 'morning'
    text: str
    certainty: float             # How confident the speaker is
    # origin: str
    is_true: Optional[bool] = None  # For debugging / tracking

@dataclass
class NPCMemory:
    name: str
    seen_events: List[Rumor] = field(default_factory=list)
    heard_rumors: List[Rumor] = field(default_factory=list)
    beliefs: Dict[str, bool] = field(default_factory=dict)  # e.g. {"Marla is suspicious": True}
    is_vampire: bool = False

def generate_random_time():
    # Simulate a time between 6 AM and 2 AM
    hour = random.choice(list(range(6, 24)) + list(range(0, 3)))
    minute = random.choice([0, 15, 30, 45])
    return datetime(2025, 6, 10, hour, minute)

def generate_rumor(NPCS: List[str], LOCATIONS: List[str],
                   FLAVOR_TEMPLATES: List[str], SUSPICIOUS_TEMPLATES: List[str]) -> Rumor:
    subject = random.choice(NPCS)
    source = random.choice([npc for npc in NPCS if npc != subject])
    time = generate_random_time()
    location = random.choice(LOCATIONS)
    other = random.choice([npc for npc in NPCS if npc != subject and npc != source])
    template = random.choice(SUSPICIOUS_TEMPLATES + FLAVOR_TEMPLATES)
    time_str = time.strftime("%H:%M")
    text = template.format(subject=subject, location=location, time_str=time_str, other=other)

    return Rumor(
        id=str(uuid4()),
        source=source,
        subject=subject,
        event="flavor" if "looked tired" in text else "sighting",
        location=location,
        time=time,
        text=text,
        certainty=random.uniform(0.4, 1.0),
        is_true=None
    )
# def mutate_rumor(original_rumor, hearing_npc):
#     rumor = copy.deepcopy(original_rumor)
#     mutation_event = random.choices(
#         ["detail", "exaggerate", "simplify", "redirect", "none"],
#         weights=[0.3, 0.2, 0.2, 0.1, 0.2]
#     )[0]
#     print(mutation_event)
#
#     if mutation_event == "detail":
#         # Mutate location or time slightly
#         possible_locations = [l for l in LOCATIONS if l != rumor.location]
#         rumor.location = random.choice(possible_locations) if random.random() < 0.5 else rumor.location
#         rumor.time = rumor.time + timedelta(minutes=random.randint(-15, 15))
#         rumor.certainty *= 0.9  # Decrease certainty slightly
#
#     elif mutation_event == "exaggerate":
#         if "saw" in rumor.text:
#             rumor.text = rumor.text.replace("saw", "caught a glimpse of")
#         elif "heard" in rumor.text:
#             rumor.text = rumor.text.replace("heard", "heard loud screams near")
#         elif "looked tired" in rumor.text:
#             rumor.text = rumor.text.replace("looked tired", "collapsed")
#         rumor.certainty *= 0.95
#
#     elif mutation_event == "simplify":
#         rumor.text = f"Something strange happened near the {rumor.location} around {rumor.time.strftime('%H:%M')}."
#         rumor.subject = None
#         rumor.certainty *= 0.8
#
#     elif mutation_event == "redirect":
#         possible_subjects = [n for n in NPCS if n != rumor.subject]
#         rumor.subject = random.choice(possible_subjects)
#         rumor.text = rumor.text.replace(original_rumor.subject, rumor.subject)
#         rumor.certainty *= 0.6  # Becomes less trustworthy
#
#     # 'none' = no change
#     rumor.source = hearing_npc
#     rumor.id = str(uuid4())  # Treat as a new rumor now
#     return rumor
#
# def npc_share_rumors(sharer, listener, npc_memories):
#     shared = []
#     for rumor in npc_memories[sharer].seen_events + npc_memories[sharer].heard_rumors:
#         if random.random() < 0.7:  # 70% chance to share
#             mutated = mutate_rumor(rumor, listener)
#             npc_memories[listener].heard_rumors.append(mutated)
#             shared.append(mutated)
#     return shared
