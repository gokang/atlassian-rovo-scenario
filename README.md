# Strategic Knowledge Bridge: Atlassian Rovo + NeMo RL 🛠️🧠🤖

This project showcases a realistic enterprise scenario where **Atlassian Rovo**'s cross-team synthesis is powered and guarded by **NeMo RL** (Reinforcement Learning).

## 🏦 Scenario: High-Stakes Compliance & Incident Response
In regulated industries (FinTech, Healthcare), an AI agent cannot just be "helpful"—it must be **Safe** and **Compliant**. 

We demonstrate a "Code Red" incident where Rovo identifies the technical debt, but a **NeMo RL-aligned policy** ensures the communication doesn't violate SEC/FINRA regulations or internal risk policies.

## 🌟 Integrated Features

### 1. Rovo Agent Orchestration
Custom agents for Jira, Confluence, and Slack that bridge data silos instantly.

### 2. NeMo RL Guardrails
Using the training pipelines defined in our [NeMo RL Enterprise](https://github.com/gokang/nemo-rl-enterprise) project:
- **Reward Modeling:** Scoring agent responses for "Regulatory Safety."
- **PPO Alignment:** Tuning the Rovo Agent's personality to avoid high-risk "guarantee" language.

## 🛠️ Components
- `agents/`: Rovo agent definitions, including the **RL-Aligned Compliance Auditor**.
- `prompts/`: Multi-hop prompts designed for RL-tuned models.
- `knowledge_base/`: Connector strategies for enterprise data.

---
*Bridging Knowledge with Safety.*
