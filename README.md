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


## 🏗️ Architecture

```text
┌─────────────────────────────┐
│         DiskAlert           │
│          Monitor            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Storage Monitoring      │
│                             │
│ • Disk Usage                │
│ • Inode Usage               │
│ • Consumption Trends        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Prediction Engine      │
│                             │
│ • Consumption Rate          │
│ • Time Until Full           │
│ • Exhaustion Alert          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Incident Analysis       │
│                             │
│ • Top Disk Consumers        │
│ • Inode Saturation          │
│ • Large Log Files           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Telegram Bot          │
│                             │
│ 🔍 Scan Again               │
│ 🧹 Safe Cleanup             │
│ 📄 Log Analysis             │
└─────────────────────────────┘

