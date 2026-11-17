#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIPHERGHOST v4.0 - Advanced Autonomous Terminal Breach & Cryptographic Vault Simulation
Under [ [bold] Khalid Bin Walid [/bold] Tools]
"""

import hashlib
import os
import random
import string
import sys
import time
from dataclasses import dataclass
from typing import List, Tuple

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
except ImportError:
    print("[!] Missing dependency: 'rich'. Install it with: pip install -r requirements.txt")
    sys.exit(1)

console = Console()

BANNER = r"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝██║  ███╗███████║██║   ██║███████╗   ██║   
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══██║██║   ██║╚════██║   ██║   
╚██████╗██║██║     ██║  ██║███████╗██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
"""

BRAND_SUB = "Under [Khalid Bin Walid Tools]"


@dataclass
class Contract:
    operation: str
    target: str
    ip_address: str
    objective: str
    time_limit: int
    ports: List[Tuple[str, int, str, bool]]
    firewalls: List[str]
    vault_code: str
    loot_files: List[Tuple[str, str]]


CONTRACTS: List[Contract] = [
    Contract(
        operation="VAULT-7",
        target="NEXORA-CORP [Zürich, Switzerland]",
        ip_address="203.0.113.42",
        objective="open the vault",
        time_limit=60,
        ports=[
            ("web-gateway", 443, "FILTERED", False),
            ("mail-relay", 25, "CLOSED", False),
            ("vpn-endpoint", 1194, "HARDENED", False),
            ("legacy-admin", 8443, "OPEN", True),
        ],
        firewalls=["packet filter", "intrusion detection", "behavior analysis"],
        vault_code="X9K4V2",
        loot_files=[
            ("project_chimera_keys.pem", "4.2 KB"),
            ("offshore_ledger_2026.enc", "18.7 MB"),
            ("vault7_root_token.jwt", "1.1 KB"),
        ],
    ),
    Contract(
        operation="BLACKSITE-09",
        target="AETHER-DYNAMICS [Tokyo, Japan]",
        ip_address="198.51.100.88",
        objective="extract neural core dump",
        time_limit=55,
        ports=[
            ("edge-proxy", 8080, "FILTERED", False),
            ("ssh-bastion", 22, "HARDENED", False),
            ("telemetry-bus", 9092, "FILTERED", False),
            ("diag-bridge", 6443, "OPEN", True),
        ],
        firewalls=["deep packet inspection", "heuristic sandbox", "zero-trust enclave"],
        vault_code="Q7M2Z8",
        loot_files=[
            ("synapse_weights_v4.bin", "142.0 MB"),
            ("blackbox_audit_log.db", "9.4 MB"),
            ("admin_override_cert.p12", "3.8 KB"),
        ],
    ),
    Contract(
        operation="GHOST-PROTOCOL",
        target="SYNTHESIS-BANK [London, United Kingdom]",
        ip_address="192.0.2.199",
        objective="bypass swift cold-storage",
        time_limit=50,
        ports=[
            ("swift-gw", 443, "HARDENED", False),
            ("hsm-cluster", 5000, "FILTERED", False),
            ("ntp-sync", 123, "CLOSED", False),
            ("backup-daemon", 31337, "OPEN", True),
        ],
        firewalls=["stateful packet filter", "ai anomaly engine", "quantum key gate"],
        vault_code="R4T8N1",
        loot_files=[
            ("cold_wallet_shards.dat", "64.0 KB"),
            ("clearinghouse_master.key", "2.0 KB"),
            ("ghost_audit_wipe.sh", "1.5 KB"),
        ],
    ),
    Contract(
        operation="ARCTIC-SHIELD",
        target="KRONOS-BIOTECH [Reykjavik, Iceland]",
        ip_address="198.51.100.210",
        objective="extract pathogen genome sequence",
        time_limit=55,
        ports=[
            ("bio-portal", 443, "FILTERED", False),
            ("hpc-cluster", 22, "HARDENED", False),
            ("cryo-bus", 8888, "CLOSED", False),
            ("lab-relay", 8080, "OPEN", True),
        ],
        firewalls=["deep packet inspection", "bio-metric gate", "ai heuristic sentinel"],
        vault_code="K9P2X5",
        loot_files=[
            ("pathogen_strain_alpha.seq", "84.2 MB"),
            ("cryo_facility_blueprints.pdf", "32.1 MB"),
            ("director_access_token.pfx", "4.5 KB"),
        ],
    ),
    Contract(
        operation="NEON-GRID",
        target="SHANGHAI-QUANTUM-LAB [Shanghai, China]",
        ip_address="203.0.113.155",
        objective="intercept qubit encryption matrix",
        time_limit=45,
        ports=[
            ("quantum-bus", 8443, "FILTERED", False),
            ("ssh-enclave", 22, "HARDENED", False),
            ("laser-telemetry", 9000, "CLOSED", False),
            ("debug-port", 9999, "OPEN", True),
        ],
        firewalls=["quantum key distributor", "stateful inspection", "zero-trust mesh"],
        vault_code="Q8W3R9",
        loot_files=[
            ("qubit_state_matrix.dat", "210.5 MB"),
            ("quantum_encryption_keys.key", "1.2 KB"),
            ("shanghai_lab_audit.db", "14.8 MB"),
        ],
    ),
    Contract(
        operation="CYBER-TITAN",
        target="VALKYRIE-DEFENSE [Stockholm, Sweden]",
        ip_address="198.51.100.12",
        objective="exfiltrate hypersonic telemetry",
        time_limit=50,
        ports=[
            ("radar-gw", 443, "FILTERED", False),
            ("bastion-ssh", 22, "HARDENED", False),
            ("telemetry-bus", 5005, "CLOSED", False),
            ("debug-core", 7777, "OPEN", True),
        ],
        firewalls=["mil-spec packet inspection", "anomaly IDS", "airlock sentinel"],
        vault_code="V4L7K9",
        loot_files=[
            ("hypersonic_guidance_v2.enc", "78.4 MB"),
            ("valkyrie_net_topology.json", "5.1 MB"),
            ("root_auth_cert.pem", "2.1 KB"),
        ],
    ),
    Contract(
        operation="RED-OCTOBER",
        target="MOSCOW-ENERGETICS [Moscow, Russia]",
        ip_address="203.0.113.88",
        objective="bypass scada power grid controls",
        time_limit=55,
        ports=[
            ("scada-portal", 443, "FILTERED", False),
            ("modbus-tcp", 502, "HARDENED", False),
            ("telemetry-feed", 2404, "CLOSED", False),
            ("plc-console", 8081, "OPEN", True),
        ],
        firewalls=["deep packet scada filter", "behavioral tripwire", "isolation gate"],
        vault_code="R3D0CT",
        loot_files=[
            ("power_grid_substations.db", "45.0 MB"),
            ("scada_master_keys.bin", "12.4 KB"),
            ("override_protocols.pdf", "8.9 MB"),
        ],
    ),
    Contract(
        operation="SUN-STRIKE",
        target="HELIOS-SOLAR-ARRAY [Cairo, Egypt]",
        ip_address="192.0.2.77",
        objective="override satellite uplink frequency",
        time_limit=50,
        ports=[
            ("sat-link", 443, "FILTERED", False),
            ("teleport-ssh", 22, "HARDENED", False),
            ("rf-sensor", 8888, "CLOSED", False),
            ("ground-control", 9001, "OPEN", True),
        ],
        firewalls=["rf spectrum analyzer", "stateful firewall", "zero-trust gateway"],
        vault_code="H3L10S",
        loot_files=[
            ("orbital_ephemeris_data.bin", "34.2 MB"),
            ("uplink_cryptokeys.pem", "3.1 KB"),
            ("helios_command_log.db", "15.6 MB"),
        ],
    ),
    Contract(
        operation="PACIFIC-DAWN",
        target="SYDNEY-FINANCIAL-HUB [Sydney, Australia]",
        ip_address="198.51.100.140",
        objective="extract forex algorithmic weights",
        time_limit=45,
        ports=[
            ("fin-gw", 443, "FILTERED", False),
            ("swift-bastion", 22, "HARDENED", False),
            ("ledger-bus", 8443, "CLOSED", False),
            ("quant-daemon", 6555, "OPEN", True),
        ],
        firewalls=["ai fraud detector", "packet filter", "quantum cryptography lock"],
        vault_code="P4C1F1",
        loot_files=[
            ("forex_arbitrage_engine.py", "18.2 MB"),
            ("sydney_vault_ledger.enc", "92.0 MB"),
            ("clearing_token.jwt", "1.4 KB"),
        ],
    ),
    Contract(
        operation="OMEGA-SAHARA",
        target="ATLAS-MINING-CORP [Johannesburg, South Africa]",
        ip_address="203.0.113.210",
        objective="intercept rare-earth supply ledger",
        time_limit=50,
        ports=[
            ("erp-portal", 443, "FILTERED", False),
            ("db-bastion", 22, "HARDENED", False),
            ("logistics-bus", 8080, "CLOSED", False),
            ("remote-diag", 9990, "OPEN", True),
        ],
        firewalls=["heuristic anomaly engine", "packet inspector", "perimeter guard"],
        vault_code="5AHARA",
        loot_files=[
            ("mineral_reserves_2026.db", "28.5 MB"),
            ("atlas_global_contracts.enc", "14.1 MB"),
            ("executive_passkey.pfx", "3.2 KB"),
        ],
    ),
    Contract(
        operation="NEO-TOKYO",
        target="ZEPHYR-ROBOTICS [Kyoto, Japan]",
        ip_address="198.51.100.55",
        objective="download humanoid neural firmware",
        time_limit=50,
        ports=[
            ("robo-gw", 443, "FILTERED", False),
            ("ai-core", 22, "HARDENED", False),
            ("telemetry", 9090, "CLOSED", False),
            ("firmware-api", 8088, "OPEN", True),
        ],
        firewalls=["neural IDS", "stateful packet filter", "deep sandbox"],
        vault_code="T0KY09",
        loot_files=[
            ("bipedal_kinematics_v9.bin", "310.4 MB"),
            ("zephyr_neural_weights.enc", "85.2 MB"),
            ("board_auth_token.pem", "2.0 KB"),
        ],
    ),
    Contract(
        operation="SILICON-VALLEY",
        target="QUANTUM-PULSE [San Francisco, USA]",
        ip_address="192.0.2.221",
        objective="extract neural LLM architecture weights",
        time_limit=55,
        ports=[
            ("ai-gateway", 443, "FILTERED", False),
            ("ssh-bastion", 22, "HARDENED", False),
            ("cluster-bus", 6379, "CLOSED", False),
            ("dev-endpoint", 8000, "OPEN", True),
        ],
        firewalls=["zero-trust mesh", "deep packet inspection", "behavior analyzer"],
        vault_code="PUL5E7",
        loot_files=[
            ("trillion_param_weights.safetensors", "450.0 MB"),
            ("training_corpus_index.db", "112.5 MB"),
            ("founder_access_key.p12", "4.0 KB"),
        ],
    ),
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def select_contract() -> Contract:
    """Displays contract selection with 12 global targets and a Custom Contract option."""
    clear_screen()
    console.print(f"[bold bright_green]{BANNER}[/bold bright_green]")
    console.print(f"[dim]{BRAND_SUB}[/dim]\n")
    console.print("[bold yellow]AVAILABLE GLOBAL CONTRACTS & TARGETS:[/bold yellow]\n")

    for i, c in enumerate(CONTRACTS, start=1):
        console.print(f"  [bold bright_green][{i:2d}][/bold bright_green] {c.operation:<16} -> [cyan]{c.target}[/cyan] ([white]{c.objective}[/white])")
    
    console.print(f"  [bold bright_magenta][13][/bold bright_magenta] CUSTOM CONTRACT     -> [cyan]Configure Custom Target & IP via Terminal Input[/cyan]")

    choice = console.input(f"\n[bold bright_green]Select contract [1-{len(CONTRACTS) + 1}]: [/bold bright_green]").strip()

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(CONTRACTS):
            return CONTRACTS[idx - 1]
        elif idx == len(CONTRACTS) + 1:
            return build_custom_contract()

    return CONTRACTS[0]


def build_custom_contract() -> Contract:
    """Interactively prompts the operator for essential parameters to build a custom target contract."""
    clear_screen()
    console.print(f"[bold bright_green]{BANNER}[/bold bright_green]")
    console.print("[bold yellow]=== CUSTOM TARGET CONTRACT BUILDER ===[/bold yellow]\n")
    console.print("[dim]Provide target details for your custom operation mission parameters:[/dim]\n")

    op_name = console.input("[bold cyan]Operation Code Name [e.g., PHANTOM-X]: [/bold cyan]").strip().upper()
    if not op_name:
        op_name = "CUSTOM-OP-01"

    target_org = console.input("[bold cyan]Target Organization & Location]: [/bold cyan]").strip()
    if not target_org:
        target_org = "CUSTOM-TARGET [Global]"

    ip_addr = console.input("[bold cyan]Target IP Address [e.g., 10.0.42.1 or 192.168.1.10]: [/bold cyan]").strip()
    if not ip_addr:
        ip_addr = "192.0.2.88"

    obj_desc = console.input("[bold cyan]Mission Objective [e.g., exfiltrate core database]: [/bold cyan]").strip()
    if not obj_desc:
        obj_desc = "breach encrypted enclave"

    time_str = console.input("[bold cyan]Time Limit in Seconds [default=60]: [/bold cyan]").strip()
    time_limit = int(time_str) if time_str.isdigit() else 60

    vault_code = "".join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=6))

    custom_ports = [
        ("web-edge", 443, "FILTERED", False),
        ("ssh-portal", 22, "HARDENED", False),
        ("telemetry", 9090, "CLOSED", False),
        ("admin-rpc", 8443, "OPEN", True),
    ]

    custom_firewalls = ["stateful packet inspection", "ai behavioral sentinel", "zero-trust enclave"]

    custom_loot = [
        ("custom_target_master_key.pem", "5.4 KB"),
        ("decrypted_payload_archive.enc", "42.1 MB"),
        ("operator_access_token.jwt", "1.2 KB"),
    ]

    console.print(f"\n[bold bright_green][✓] Custom Contract '{op_name}' successfully compiled for {target_org}![/bold bright_green]")
    time.sleep(1.2)

    return Contract(
        operation=op_name,
        target=target_org,
        ip_address=ip_addr,
        objective=obj_desc,
        time_limit=time_limit,
        ports=custom_ports,
        firewalls=custom_firewalls,
        vault_code=vault_code,
        loot_files=custom_loot,
    )


def render_hud(operation: str, trace: int, access: int, time_left: float):
    trace = max(0, min(100, int(trace)))
    access = max(0, min(100, int(access)))

    bar_width = 24
    trace_filled = int((trace / 100) * bar_width)
    access_filled = int((access / 100) * bar_width)

    trace_color = "bright_green" if trace < 40 else ("yellow" if trace < 75 else "bold red")
    trace_bar = f"[{trace_color}]{'█' * trace_filled}[/{trace_color}][dim]{'░' * (bar_width - trace_filled)}[/dim]"
    access_bar = f"[bright_cyan]{'█' * access_filled}[/bright_cyan][dim]{'░' * (bar_width - access_filled)}[/dim]"

    hud = Text.from_markup(
        f"[bold white]CIPHERGHOST - OPERATION {operation} ({BRAND_SUB})[/bold white]   "
        f"[dim]T-{max(0, int(time_left)):02d}s[/dim]\n"
        f"[bold white]TRACE[/bold white]  {trace_bar}  [{trace_color}]{trace:>2}%[/{trace_color}]   "
        f"[bold white]ACCESS[/bold white] {access_bar}  [bright_cyan]{access:>3}%[/bright_cyan]\n"
        f"[dim]{'─' * 78}[/dim]"
    )
    console.print(hud)


def random_hex_line() -> str:
    addr = random.randint(0x0000, 0xFFFF)
    bytes_str = " ".join(f"{random.randint(0, 255):02X}" for _ in range(16))
    return f"0x{addr:04X}  {bytes_str}"


def build_gorgeous_block_grid(unlocked_count: int, total_blocks: int = 256, cols: int = 32) -> Text:
    """Renders a gorgeous animated 256-block cyberpunk encryption matrix."""
    glyphs = "0123456789ABCDEF#$%&@*+=?▲■◆"
    grid = Text()
    for i in range(total_blocks):
        if i > 0 and i % cols == 0:
            grid.append("\n")
        ch = random.choice(glyphs)
        if i < unlocked_count:
            grid.append(f" {ch} ", style="bold bright_cyan on blue")
        elif i == unlocked_count and unlocked_count < total_blocks:
            grid.append(f" {ch} ", style="bold black on bright_yellow")
        else:
            grid.append(f" {ch} ", style="bold white on dark_red")
    return grid


def show_briefing(contract: Contract) -> str:
    clear_screen()
    console.print(f"[bold bright_green]{BANNER}[/bold bright_green]")
    console.print(f"[dim]{BRAND_SUB}[/dim]\n")

    minutes = contract.time_limit // 60
    seconds = contract.time_limit % 60
    briefing_text = (
        f"[bold yellow]INCOMING CONTRACT BRIEFING[/bold yellow]\n"
        f"[dim]OPERATION[/dim]   [bold white]{contract.operation}[/bold white]\n"
        f"[dim]TARGET[/dim]      [bold cyan]{contract.target}[/bold cyan]\n"
        f"[dim]OBJECTIVE[/dim]   [white]{contract.objective}[/white]\n"
        f"[dim]TIME LIMIT[/dim]  [bold white]{minutes:02d}:{seconds:02d}[/bold white]\n"
        f"[dim]RISK LEVEL[/dim]  [bold red]trace reaches 100% -> mission failed[/bold red]"
    )
    console.print(Panel(briefing_text, border_style="bright_green", box=box.ROUNDED, width=78))
    console.print("\n[dim]Instructions: Press [bold white]Enter[/bold white] or type [bold bright_green]breach[/bold bright_green] to start autonomous protocol | [bold cyan]select[/bold cyan] to choose contract[/dim]")

    while True:
        cmd = console.input("[bold bright_green]$ [/bold bright_green]").strip().lower()
        if cmd in ("", "breach", "start", "auto", "run"):
            return "auto"
        elif cmd == "select":
            return "select"
        elif cmd in ("exit", "quit"):
            sys.exit(0)
        else:
            return "auto"


def run_mission(contract: Contract):
    trace = 0
    access = 5
    start_time = time.time()
    deadline = start_time + contract.time_limit

    def time_remaining() -> float:
        return max(0.0, deadline - time.time())

    # Phase 1: Recon & Fingerprinting
    clear_screen()
    render_hud(contract.operation, trace, access, time_remaining())
    domain = contract.target.split()[0].lower()
    console.print(f"[dim][T-39][/dim] [bold cyan]OPS[/bold cyan] target acquired: [bold white]{domain}[/bold white]")
    time.sleep(0.35)

    access = 12
    clear_screen()
    render_hud(contract.operation, trace, access, time_remaining())
    console.print(f"[dim][T-39][/dim] [bold cyan]OPS[/bold cyan] target acquired: [bold white]{domain}[/bold white]")
    console.print(f"[dim][T-39][/dim] [bold cyan]NET[/bold cyan] resolving host -> [bold white]{contract.ip_address}[/bold white]")
    console.print("[bright_green]✓[/bright_green] Mapping global perimeter", end="")
    sys.stdout.flush()
    time.sleep(0.4)
    print("\r\033[K", end="")
    console.print("[bright_green]✓[/bright_green] Mapping global perimeter                    [bold bright_green][MAPPED][/bold bright_green]")
    console.print("[bright_green]✓[/bright_green] Fingerprinting service enclaves", end="")
    sys.stdout.flush()
    time.sleep(0.4)
    print("\r\033[K", end="")
    console.print("[bright_green]✓[/bright_green] Fingerprinting service enclaves              [bold bright_green][DONE][/bold bright_green]")

    access = 24
    for service, port, state, is_weak in contract.ports:
        time.sleep(0.18)
        if is_weak:
            console.print(f"  [bold bright_green]● {service:<15} :{port:<5} {state}[/bold bright_green]")
            console.print(f"  [bold bright_green]➜ EXPLOITABLE PIVOT FOUND: {service} :{port}[/bold bright_green]")
        else:
            color = "yellow" if state in ("FILTERED", "HARDENED") else "dim"
            console.print(f"  [dim]●[/dim] {service:<15} :{port:<5} [{color}]{state}[/{color}]")

    time.sleep(0.4)

    # Phase 2: 3-Layer Firewall Traversal
    for idx, fw_name in enumerate(contract.firewalls, start=1):
        if time_remaining() <= 0 or trace >= 100:
            break

        if idx == 2:
            trace += 6

        clear_screen()
        render_hud(contract.operation, trace, access, time_remaining())
        console.print(
            f"[bold white on blue] FIREWALL LAYER {idx} : {fw_name.upper()} [/bold white on blue]"
        )

        for step in range(12):
            if time_remaining() <= 0:
                break
            line = random_hex_line()
            if idx == 2 and step == 8:
                trace += 5
                console.print(f"[bright_cyan]{line}[/bright_cyan]   [bold white on red] ⚡ IDS TRACE TRIGGERED & MITIGATED ! [/bold white on red]")
            else:
                style = "bright_cyan" if step % 3 != 0 else "cyan"
                console.print(f"[{style}]{line}[/{style}]")

            if idx >= 2 and step % 4 == 0:
                trace += 1
            time.sleep(0.04)

        access = min(65, access + 14)
        console.print(f"[bold bright_green][ LAYER {idx} AUTONOMOUSLY BYPASSED ][/bold bright_green]")
        time.sleep(0.35)

    if trace >= 100 or time_remaining() <= 0:
        mission_failed("ACTIVE IDS TRACE LOCKED ORIGIN IP" if trace >= 100 else "ATTACK WINDOW EXPIRED")
        return

    # Phase 3: Autonomous Vault 256-Block Encryption Matrix Breaker
    code = contract.vault_code
    unlocked_chars = 0
    total_chars = len(code)

    while unlocked_chars < total_chars:
        if time_remaining() <= 0 or trace >= 100:
            break

        unlocked_blocks = int((unlocked_chars / total_chars) * 256)
        access = 65 + int((unlocked_chars / total_chars) * 35)

        clear_screen()
        render_hud(contract.operation, trace, access, time_remaining())

        for _ in range(6):
            console.print(f"[cyan]{random_hex_line()}[/cyan]")

        console.print(f"\n[bold yellow]● {contract.operation} - AUTONOMOUS 256-BLOCK DECRYPTION ENGINE[/bold yellow]")
        console.print("[dim]Status: [bold bright_green]AI Neural Bruteforce & Quantum Relay Active (Zero Human Input Required)[/bold bright_green][/dim]")
        console.print(build_gorgeous_block_grid(unlocked_blocks))

        masked = []
        for i in range(total_chars):
            if i < unlocked_chars:
                masked.append(f"[bold black on bright_green] {code[i]} [/bold black on bright_green]")
            elif i == unlocked_chars:
                spin_ch = random.choice(string.ascii_uppercase + string.digits)
                masked.append(f"[bold black on bright_yellow] {spin_ch} [/bold black on bright_yellow]")
            else:
                masked.append(f"[dim][ {random.choice(string.ascii_uppercase + string.digits)} ][/dim]")
        console.print(f"\n[bold white]VAULT KEYSPACE:[/bold white]  {' '.join(masked)}")

        # Autonomous self-solving ticker
        time.sleep(0.55)
        unlocked_chars += 1
        trace = max(8, trace + random.randint(2, 6) - 3)

    if trace >= 100 or time_remaining() <= 0:
        mission_failed("COUNTER-INTRUSION TRACE REACHED 100%" if trace >= 100 else "TIME LIMIT EXCEEDED")
        return

    # Phase 4: Final Vault Breach & Exfiltration Summary
    clear_screen()
    render_hud(contract.operation, trace, 100, time_remaining())
    console.print(f"\n[bold yellow]● {contract.operation} - AUTONOMOUS 256-BLOCK DECRYPTION ENGINE[/bold yellow]")
    console.print("[bold bright_green]VAULT DECRYPTION COMPLETE - ROOT ACCESS GRANTED[/bold bright_green]")
    console.print(build_gorgeous_block_grid(256))

    revealed_pw = " ".join(f"[bold black on bright_green] {c} [/bold black on bright_green]" for c in code)
    console.print(f"\n[bold white]VAULT MASTER KEY:[/bold white] {revealed_pw}")
    console.print("[bold black on bright_green]  ✔ VAULT UNLOCKED - ALL SECRETS EXFILTRATED SUCCESSFULLY  [/bold black on bright_green]\n")

    console.print("[bold cyan]EXFILTRATED PAYLOAD ARTIFACTS:[/bold cyan]")
    for fname, fsize in contract.loot_files:
        sha = hashlib.sha256(f"{contract.operation}:{fname}".encode()).hexdigest()[:16]
        time.sleep(0.25)
        console.print(f"  [bright_green]✔[/bright_green] {fname:<30} [dim]({fsize})[/dim]  [cyan]sha256:{sha}...[/cyan]")

    elapsed = round(time.time() - start_time, 2)
    console.print(
        Panel(
            f"[bold bright_green]MISSION ACCOMPLISHED[/bold bright_green]  [dim]|[/dim]  [cyan]{BRAND_SUB}[/cyan]\n"
            f"Target: [white]{contract.target}[/white]  |  Final Trace: [yellow]{trace}%[/yellow]  |  Time: [cyan]{elapsed}s[/cyan]",
            border_style="bright_green",
            width=78,
        )
    )


def mission_failed(reason: str):
    console.print(f"\n[bold white on red] MISSION FAILED: {reason} [/bold white on red]")
    console.print(f"[dim]Connection terminated by watchdog. {BRAND_SUB}[/dim]\n")


def main():
    while True:
        contract = select_contract()
        cmd = show_briefing(contract)
        if cmd == "select":
            continue

        run_mission(contract)

        again = console.input("\n[dim]Press [bold white]Enter[/bold white] to return to contract selection, or type [bold white]quit[/bold white]: [/dim]").strip().lower()
        if again in ("quit", "exit", "q"):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n[!] Session aborted. {BRAND_SUB}")
        sys.exit(0)