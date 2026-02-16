# Rovo Connector Configuration Strategy

To enable the "Code Red" scenario, Atlassian Rovo must be connected to the following enterprise data silos:

## 1. Primary Atlassian Stack
- **Jira Cloud:** Provides the incident stream and bug tracking.
- **Confluence Cloud:** Provides the "Source of Truth" for playbooks and requirements.
- **Bitbucket:** Provides the deployment context (commit messages + build status).

## 2. External SaaS Connectors
- **Slack:** Enable the Slack connector for Rovo to ingest "War Room" channel history.
- **Google Drive / SharePoint:** Connect to access PDF compliance checklists and legacy spreadsheets.
- **GitHub:** (Optional) If the team uses GitHub for source code, Rovo uses this to identify who changed the lines of code associated with a regression.

## 3. Knowledge Access Controls
Rovo respects existing permissions. For this scenario, the "Incident Responder" agent must have read access to:
- The `FIRE` project in Jira.
- The `Engineering` space in Confluence.
- Relevant private Slack channels via the Rovo Bot invite.
