# Atlassian Rovo + NeMo RL: The Intelligent Incident Bridge 🛠️🧠🤖

This project provides a **demo-ready showcase** of how Atlassian Rovo and NVIDIA NeMo RL work together to handle critical enterprise incidents.

## 🚀 Live Demo Simulation
I have created a user-facing dashboard to visualize this scenario:
- **File:** `demo.html`
- **How to view:** Open `demo.html` in any browser to see the Rovo + NeMo orchestration in action.

## 🏦 Scenario: "Code Red" Mortgage API Failure
When a P1 incident hits, speed is everything—but accuracy and compliance are mandatory.

### 1. Knowledge Synthesis (Rovo)
Rovo instantly bridges **Jira**, **Confluence**, and **Bitbucket** to identify the root cause:
- Correlates a specific Bitbucket deployment with a Jira spike.
- Pulls the exact recovery playbook from Confluence.
- Summarizes the last 10 messages in the Slack war room.

### 2. Regulatory Guardrails (NeMo RL)
Before the update is sent to stakeholders, a **NeMo RL-aligned model** (PPO/RLHF) rewrites the summary:
- **Filters Risk:** Removes unauthorized guarantees (e.g., "fixed in 5 mins").
- **Ensures Tone:** Adjusts language to meet SEC/FINRA financial compliance standards.
- **Safety Judge:** Uses a Reward Model to audit the final text for regulatory safety.

## 🛠️ Components
- `demo.html`: The user-facing dashboard showing the "proactive agent" in action.
- `nemo_rl_integration/`: Python scripts for compliance auditing and aligned text generation.
- `agents/`: Custom Rovo Agent definitions.

---
*Bridging Knowledge with Safety.*
