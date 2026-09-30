\# 🚨 DiskAlert



\### Server Disk Space / Inode Spike Monitor with Telegram Bot



DiskAlert is a proactive disk-space and inode monitoring prototype designed to detect storage exhaustion before it causes server failures.



Instead of waiting until a filesystem reaches 98–100% usage, DiskAlert analyzes storage consumption trends and predicts when the disk could become full.



\---



\## 🎯 Problem



Linux servers can become unavailable when:



\- Disk partitions reach 100% capacity

\- Runaway application logs consume storage

\- Core dumps fill the filesystem

\- Docker/container data grows unexpectedly

\- Millions of small files exhaust available inodes

\- Traditional threshold alerts detect the problem too late



DiskAlert focuses on detecting these conditions earlier and providing actionable incident information through Telegram.



\---



\## 💡 Solution



DiskAlert combines:



1\. \*\*Disk Usage Monitoring\*\*

2\. \*\*Storage Consumption Prediction\*\*

3\. \*\*Inode Saturation Detection\*\*

4\. \*\*Top Directory Analysis\*\*

5\. \*\*Large Log File Analysis\*\*

6\. \*\*Telegram Incident Alerts\*\*

7\. \*\*Interactive Telegram Buttons\*\*



The prototype demonstrates a proactive monitoring workflow where storage trends can trigger an alert before complete exhaustion.



\---



\## 🏗️ Architecture



```text

&#x20;             ┌─────────────────────┐

&#x20;             │     DiskAlert       │

&#x20;             │      Monitor        │

&#x20;             └──────────┬──────────┘

&#x20;                        │

&#x20;             ┌──────────▼──────────┐

&#x20;             │ Storage Monitoring  │

&#x20;             │                     │

&#x20;             │ Disk Usage          │

&#x20;             │ Inode Usage         │

&#x20;             │ Consumption Slope   │

&#x20;             └──────────┬──────────┘

&#x20;                        │

&#x20;             ┌──────────▼──────────┐

&#x20;             │ Prediction Engine   │

&#x20;             │                     │

&#x20;             │ Usage Rate          │

&#x20;             │ Time Until Full     │

&#x20;             └──────────┬──────────┘

&#x20;                        │

&#x20;                   Alert Condition

&#x20;                        │

&#x20;             ┌──────────▼──────────┐

&#x20;             │  Incident Analysis  │

&#x20;             │                     │

&#x20;             │ Top Directories     │

&#x20;             │ Large Log Files     │

&#x20;             │ Inode Saturation    │

&#x20;             └──────────┬──────────┘

&#x20;                        │

&#x20;             ┌──────────▼──────────┐

&#x20;             │   Telegram Bot      │

&#x20;             │                     │

&#x20;             │ 🔍 Scan Again       │

&#x20;             │ 🧹 Safe Cleanup     │

&#x20;             │ 📄 Log Analysis     │

&#x20;             └─────────────────────┘

