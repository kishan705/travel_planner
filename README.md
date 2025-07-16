
# Offline Travel Planner

## Overview
Enter **any** world city names.  
This tool:
1. **Validates** against a free `worldcities.csv` dataset.  
2. Builds a complete graph weighted by **great‑circle distances**.  
3. Finds the **shortest‑distance path** (Dijkstra).  
4. Plots the route on an **interactive map**.

## Setup

1. **Clone** this folder.
2. **Download** [`worldcities.csv`](https://simplemaps.com/data/world-cities) (free) into `data/`.
3. Create & activate a virtual env:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
4. Install deps:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run**:
   ```bash
   python main.py
   ```

## Features
- Works offline for city lookup and distance computation.
- Supports 120,000+ global cities.
- Uses **haversine formula** for realistic distances.
- Generates an **interactive map** (HTML) using Folium.

## Requirements
- Python 3.8+
- pandas
- networkx
- folium
