# Module 3: Offline Content, Local Services and Gateway

**Owner:** Harini  
**Depends On:** Module 2 (Maths package: DMD & ADMM) and Module 1 (Node environment)

## Goal
Enable disaster-hit neighbourhoods to access critical emergency information (shelter locations, maps, first-aid protocols, news bulletins) and educational/morale media without internet connectivity through coordinated pre-storm caching, local peer-to-peer sync, and dynamic gateway bridging.

## Core Responsibilities & Tasks
1. **Emergency Content Catalogue**:
   - Structured registry of essential resources classified by priority (Priority 1: Life safety & maps, Priority 2: Government alerts & news, Priority 3: Morale / educational video).
2. **Cooperative Pre-Storm Cache Planning**:
   - Formulate cooperative storage allocation (knapsack / QP relaxed formulation).
   - Ensure the neighbourhood avoids storing 50 identical copies of the same article while missing emergency medical guides.
3. **Peer-to-Peer Sync**:
   - Local device discovery using `zeroconf` (mDNS) over local Wi-Fi hotspots.
   - P2P chunk exchange to sync missing files between neighbours.
4. **Local HTTP / Media Server**:
   - FastAPI server serving local emergency portals and media to phones, laptops, and Smart TVs without internet.
5. **Opportunistic Gateway**:
   - Detect when an edge node acquires intermittent cellular or satellite connectivity, compress outbound SOS queues, and fetch fresh updates for the neighbourhood.
