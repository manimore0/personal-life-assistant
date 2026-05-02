# 🏗 Architecture — Personal Life Assistant

This document explains how the system is structured and how data flows through the application.

---

## 🔄 High-Level Flow

```text
CLI (main.py)
     ↓
Command Router
     ↓
Rule-based logic (fast path)
     ↓ (if needed)
AI Parser (fallback)
     ↓
SQLite Database (data layer)
     ↓
Recurring Engine
     ↓
Filter + Summary Layer