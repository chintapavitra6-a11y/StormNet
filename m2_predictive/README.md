# Module 2: Predictive Routing and Distributed Optimisation

**Owner:** Daphna  
**Depends On:** Module 1 (Connectivity logs & `Router` interface)

## Goal
Implement the intelligent decision layer for StormNet. Instead of brute-force flooding, use linear dynamical systems theory and mathematical optimization to predict network topology changes and forward emergency packets along high-probability routes under tight battery and copy constraints.

## Core Responsibilities & Tasks
1. **Dynamic Mode Decomposition (DMD)**:
   - Construct time-delay Hankel matrices from link-up/link-down and contact histories.
   - Implement DMD via SVD: $X_2 \approx A X_1$.
   - Forecast future link availability and contact probabilities.
   - Benchmark forecast RMSE against Last-Value and Moving-Average baselines.
2. **Quadratic Programming (QP) Forwarding**:
   - Maximize priority-weighted delivery probability subject to node battery budgets and packet copy limits using `cvxpy`.
3. **Distributed ADMM (Alternating Direction Method of Multipliers)**:
   - Formulate consensus ADMM so nodes solve localized subproblems and agree on forwarding decisions without a centralized server.
4. **PredictiveRouter Implementation**:
   - Implement `common.router_api.Router` so Module 1 can run simulations with the predictive router in a single line.
