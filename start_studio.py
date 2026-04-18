"""
start_studio.py – called by the GitHub Actions workflow.

Required environment variables (set as GitHub repo secrets):
  LIGHTNING_USER_ID   – from lightning.ai → Avatar → Settings → Keys
  LIGHTNING_API_KEY   – from lightning.ai → Avatar → Settings → Keys

Required environment variables (set in the workflow):
  STUDIO_NAME         – name of the existing studio to start
  STUDIO_TEAMSPACE    – teamspace that owns the studio (e.g. "my-teamspace")
  STUDIO_MACHINE      – machine type: CPU, T4, L4, A10G, A100  (default: CPU)
"""

import os
import sys
from lightning_sdk import Machine, Studio

# ── resolve config from environment ──────────────────────────────────────────
studio_name = os.environ.get("STUDIO_NAME", "").strip()
teamspace   = os.environ.get("STUDIO_TEAMSPACE", "").strip() or None
machine_str = os.environ.get("STUDIO_MACHINE", "CPU").strip().upper()

if not studio_name:
    print("ERROR: STUDIO_NAME environment variable is not set.", file=sys.stderr)
    sys.exit(1)

machine_map = {
    "CPU":  Machine.CPU,
    "T4":   Machine.T4,
    "L4":   Machine.L4,
    "A100": Machine.A100,
}

machine = machine_map.get(machine_str)
if machine is None:
    print(
        f"ERROR: Unknown machine type '{machine_str}'. "
        f"Valid options: {', '.join(machine_map)}",
        file=sys.stderr,
    )
    sys.exit(1)

# ── connect to and start the studio ──────────────────────────────────────────
print(f"Studio  : {studio_name}")
print(f"Teamspace: {teamspace or '(personal)'}")
print(f"Machine : {machine_str}")
print()

studio = Studio(
    name=studio_name,
    teamspace=teamspace,
    create_ok=False,   # don't silently create a new studio if the name is wrong
)

studio.start(machine=machine)

print(f"Status  : {studio.status}")
print(f"Machine : {studio.machine}")
print()
print("Studio started successfully ✔")
