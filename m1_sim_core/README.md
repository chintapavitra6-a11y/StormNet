# Module 1: Simulation and Mesh Messaging Core

**Owner:** Pavitra  
**Status:** In Progress (Foundation Module)

## Goal
Build the discrete-event simulation world that powers StormNet. Model hundreds of moving devices in disaster scenarios (cyclones, urban flooding) that connect when in radio range, manage battery life, buffer emergency messages, and forward packets using store-and-forward delay-tolerant networking (DTN).

## Core Responsibilities & Tasks
1. **Node Model**:
   - Device attributes: `id`, position `(x, y)`, transmission range $R$, battery level, message buffer, seen message set.
   - Buffer management: Priority queueing (urgent priority-1 SOS packets prioritized over routine status packets).
2. **Mobility Models**:
   - Random Walk / Random Waypoint.
   - Disaster-aware mobility (movement toward elevated ground and designated relief shelters).
3. **Disaster Engine & Scenarios**:
   - Simulating progressive cellular tower failures.
   - Flood zone expansion (nodes submerged/powered down).
   - Battery consumption: Transmission cost vs. reception cost vs. idle decay.
4. **Baseline Routing Protocols**:
   - **Epidemic Router**: Unconstrained flooding to all unseen neighbours (upper-bound benchmark).
   - **Spray-and-Wait Router**: Limited copy distribution ($L$ copies) to avoid congestion.
   - **Shortest-Path / Oracle Router**: Theoretical optimum for comparison.
5. **Metrics & Logging**:
   - Delivery ratio (%), average latency (s), replication overhead (copies per delivered message), battery depletion rate.
   - Export 3D connectivity log `(T, N, N)` (`data/conn_log.npy`) for Module 2.
6. **Physical Demo**:
   - Lightweight Python socket prototype (`asyncio` / UDP / TCP) demonstrating real packet passing between 2-3 laptops on an offline local Wi-Fi hotspot.
