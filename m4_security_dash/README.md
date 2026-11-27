# Module 4: Security, Statistics, Dashboard and DevOps

**Owner:** Niharika  
**Depends On:** All modules (collects state telemetry; hooks into Module 1 message pipeline)

## Goal
Protect the integrity of emergency communications, identify malicious or malfunctioning nodes using statistical hypothesis tests, deliver an intuitive real-time rescue operations dashboard, and maintain CI/CD and deployment infrastructure.

## Core Responsibilities & Tasks
1. **Cryptographic Authentication**:
   - Ed25519 digital signature keypair generation and verification using `pynacl`.
   - Provide `sign(message)` and `verify(message)` hooks for Module 1.
2. **Statistical Anomaly & Attack Detectors**:
   - **Black-Hole Attack Detector**: Statistical binomial test (`scipy.stats.binomtest`) to detect and isolate nodes that absorb packets without forwarding them.
   - **SOS Spam Detector**: Poisson arrival rate hypothesis testing to detect compromised nodes spamming false alerts.
3. **Partition & Topology Analysis**:
   - Real-time connected components analysis using `networkx` to detect network splits.
4. **Rescue Dashboard**:
   - Streamlit application displaying real-time geographic map of nodes, priority-sorted triage lists, network health, and cache status.
5. **REST API & DevOps**:
   - FastAPI state ingestion endpoints for simulation and edge nodes.
   - Containerization via Docker & `docker-compose.yml`.
   - Continuous Integration via GitHub Actions (`.github/workflows/ci.yml`).
