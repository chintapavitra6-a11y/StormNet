# StormNet: Disaster-Resilient Neighbourhood Network

> **A disaster-resilient neighbourhood mesh network built entirely in Python.**  
> Designed to maintain critical life-safety communications, emergency message routing, and local service delivery when cellular towers and the internet collapse during extreme weather events (cyclones, urban flooding).

---

## 1. Problem Statement

When extreme weather (e.g., cyclones or severe flooding) strikes coastal and urban regions:
1. **Telecom Infrastructure Collapse:** Cellular towers lose grid power or backhaul; home Wi-Fi routers shut down.
2. **The "Dead Zone" Dilemma:** Mobile devices retain battery power, but families cannot broadcast emergency SOS calls, and rescue personnel cannot map urgent needs.
3. **Flaws in Traditional Offline Mesh Apps:** Existing offline messaging applications rely on unconstrained **Epidemic Flooding** (every phone replicates every packet to every encountered device). This rapidly drains scarce battery reserves, clogs the narrow radio spectrum, treats life-critical medical emergencies identically to casual chatter, and ignores mobility patterns.
4. **Storage Duplication:** Neighbours independently cache duplicate non-essential content while missing crucial local relief maps, emergency shelter registries, and first-aid guides.

**StormNet solves this through intelligent mathematics and delay-tolerant networking (DTN):**
* **Priority-Aware Routing:** Critical SOS packets get preferential buffering and forwarding over routine telemetry.
* **Predictive Routing (DMD):** Dynamically forecasts link availability and contact patterns using Dynamic Mode Decomposition.
* **Decentralized Optimization (ADMM):** Solves forwarding and cache allocation problems distributively across devices without a central server.
* **Trust & Security:** Authenticates emergency broadcasts using digital signatures and detects rogue/black-hole nodes using statistical hypothesis tests.

---

## 2. Team Roster & Module Ownership

| Module | Focus Area | Owner | Key Technologies & Concepts |
| :--- | :--- | :--- | :--- |
| **Module 1** | **Simulation & Mesh Messaging Core** | **Pavitra** | `simpy`, `networkx`, discrete-event simulation, mobility, battery models, baseline routers (Epidemic, Spray-and-Wait), physical socket prototype |
| **Module 2** | **Predictive Routing & Optimisation** | **Daphna** | `numpy`, `scipy`, `pydmd`, `cvxpy`, Hankel matrices, Dynamic Mode Decomposition (DMD), Quadratic Programming (QP), consensus ADMM |
| **Module 3** | **Offline Content & Gateway Services** | **Harini** | `fastapi`, `uvicorn`, `zeroconf`, cooperative cache planning, P2P chunk sync, local media/emergency server, opportunistic gateway bridging |
| **Module 4** | **Security, Statistics, Dashboard & DevOps** | **Niharika** | `pynacl` (Ed25519), `scipy.stats` (binomial & Poisson tests), `streamlit`, REST API, Docker, GitHub Actions CI |

---

## 3. High-Level Architecture

```
                    ┌────────────────────────────────────────────────┐
                    │            MODULE 4: Rescue Dashboard          │
                    │      (Streamlit Map, Triage List, Health)      │
                    └───────────────────────▲────────────────────────┘
                                            │ State Telemetry (REST API)
    ┌───────────────────────────┬───────────┴───────────────┬───────────────────────────┐
    │                           │                           │                           │
┌───┴───────────────────────┐ ┌─┴─────────────────────────┐ ┌─────────────────────────┴───┐
│   MODULE 2: Intelligence  │ │  MODULE 4: Trust & Sec    │ │   MODULE 3: Local Content     │
│  - Hankel + DMD Forecast  │ │  - Ed25519 Sign/Verify    │ │  - Pre-storm Cache Planner    │
│  - QP / ADMM Optimization │ │  - Statistical Anomaly    │ │  - Zeroconf Peer-to-Peer Sync │
│  - Predictive Router      │ │    Detection (Black-Hole) │ │  - FastAPI Local Portal / TV  │
└───▲───────────────────────┘ └──▲────────────────────────┘ └─────────────────────────▲───┘
    │ Plugs into Router API      │ sign() / verify() hooks                             │
    └───────────────────────────┐│┌────────────────────────────────────────────────────┘
                                │││
                    ┌───────────┴┴▼──────────────────────────┐
                    │        MODULE 1: Simulation Core       │
                    │   - SimPy Discrete-Event World         │
                    │   - Node Mobility & Disaster Dynamics  │
                    │   - Store-and-Forward DTN Buffering    │
                    │   - Real-World Laptop Sockets (Demo)   │
                    └────────────────────────────────────────┘
```

---

## 4. Repository Structure

```text
StormNet/
├── README.md                 # Project guide and architecture documentation
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore configuration
│
├── common/                   # SHARED CONTRACTS (Changes require team agreement)
│   ├── __init__.py
│   ├── message.py            # Canonical Message dataclass (serialization, priority, signing)
│   └── router_api.py         # Abstract Router base class & EpidemicRouter baseline
│
├── m1_sim_core/              # MODULE 1: Simulation & Mesh Core (Owner: Pavitra)
│   ├── __init__.py
│   └── README.md
│
├── m2_predictive/            # MODULE 2: Predictive Routing & Optimisation (Owner: Daphna)
│   ├── __init__.py
│   └── README.md
│
├── m3_content/               # MODULE 3: Offline Content & Gateway (Owner: Harini)
│   ├── __init__.py
│   └── README.md
│
├── m4_security_dash/         # MODULE 4: Security, Dashboard & DevOps (Owner: Niharika)
│   ├── __init__.py
│   └── README.md
│
├── data/                     # Shared datasets and connectivity logs (conn_log.npy)
│   └── README.md
│
└── tests/                    # Unit and integration test suite
    ├── __init__.py
    └── test_common_message.py
```

---

## 5. Getting Started

### Prerequisites
* Python 3.10 or 3.11 installed.
* Git installed.

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chintapavitra6-a11y/StormNet.git
   cd StormNet
   ```

2. **Create and activate a virtual environment:**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the test suite:**
   ```bash
   pytest tests
   ```

---

## 6. Shared Contracts (Do Not Break)

To enable 4 developers to work in parallel without blocking one another, all modules adhere strictly to shared contracts defined in `common/`:

1. **`Message` (`common/message.py`)**:
   Standardized packet structure containing `id`, `kind` (`SOS`, `STATUS`, `ACK`), `priority` ($1$ highest to $5$ lowest), `lat`, `lon`, `created_at`, `ttl`, `sender`, `payload`, and `signature`.
2. **`Router` (`common/router_api.py`)**:
   Abstract base class exposing `select_next_hops(node, message, neighbours, now) -> List[Node]`. All routers (Epidemic, Spray-and-Wait, and Predictive Router) implement this identical interface.
3. **Connectivity Log (`data/conn_log.npy`)**:
   3D NumPy array of shape `(T, N, N)` recording active links over time steps $T$ across $N$ nodes. Produced by M1, consumed by M2.

---

## 7. Git Workflow for the Team

* **`main` Branch Protection:** The `main` branch must always remain functional. Never push untested code directly to `main`.
* **Feature Branches:** Each member creates and works on their own branch named by module:
  * Pavitra: `m1/...` (e.g., `git checkout -b m1/sim-engine`)
  * Daphna: `m2/...` (e.g., `git checkout -b m2/dmd-forecaster`)
  * Harini: `m3/...` (e.g., `git checkout -b m3/cache-planner`)
  * Niharika: `m4/...` (e.g., `git checkout -b m4/security-keys`)
* **Pull Requests (PR):** Open a PR on GitHub for feature reviews before merging into `main`.
* **Shared Code:** Any changes to `common/` must be discussed and agreed upon by all four members before merging.
