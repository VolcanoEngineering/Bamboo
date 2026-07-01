# Bamboo Obfuscation & Proprietary Redlining Standard

This document establishes the official behavioral standard for identifying, stripping, and obfuscating proprietary execution math and sensitive system parameters before they are committed to open-source or public Bamboo modules.

---

## 1. Core Rule: Public Structure, Private Sauce

Downstream agents and human collaborators MUST partition repository elements into two distinct boundaries:
1.  **Public Structure (Core Bamboo):** High-level architectural patterns, documentation compliance checkers, context decay formulas, general memory tiering algorithms, and abstract project manifests.
2.  **Private Sauce (Proprietary Extensions):** Specific mathematical weights, live pricing models, API execution latencies, specific option strike rules, trading filters, and live database schemas.

---

## 2. Forbidden Data (Redline List)

The following parameters and configurations MUST NEVER be written, logged, or referenced in public-facing documentation:
*   **Capital & Balance Metrics:** Do not reference actual account values, cash allocations, or transaction sizes (e.g., replace "$1,000 cash balance" with "Balance Variable B").
*   **Asset Tickers:** Avoid referencing active portfolio symbols (e.g., substitute "TQQQ/SQQQ options swing strategy" with "Leveraged Index Strategy Node").
*   **Numerical Optimization Constants:** Do not publish fitted coefficients, covariance matrices, or standard deviations derived from live market data (e.g. replace standard deviations like `0.05 * 0.2625` with general scaling factor `\alpha_x`).
*   **API & Broker Signatures:** Strictly forbid staging specific Robinhood, yfinance, or IBKR request URLs, token endpoints, or client payload keys.

---

## 3. Abstract Replacements (Obfuscation Mapping)

When validating the performance or compiling case studies for public reports, use the following replacement mapping:

| Proprietary Parameter | Obfuscation Target |
| :--- | :--- |
| Active Equity Tickers (e.g. SPY, HOOD) | `Asset Alpha`, `Asset Beta` |
| Options Expirations and Strikes | `Option Strike K`, `Expiration T` |
| Volatility Regimes / Custom Signals | `Regime Alpha`, `Regime Beta` |
| Specific Leverage & Sizing Ratios | `Sizing Coefficient \omega` |
| Live Execution Logs | Abstracted Scenario Logs (e.g., "Scenario 1") |

---

## 4. Pre-Commit Validation

Before staging any commit to the public Bamboo repository:
1.  Verify that all equations are clearly labeled as **conceptual bounding models**.
2.  Check all markdown files and code updates to ensure no specific portfolio calculations or sensitive database parameters are present.
3.  Ensure that all references to testing metrics use sanitized, normalized values.

---

**Last Updated:** 2026-07-01-v0.0.1
