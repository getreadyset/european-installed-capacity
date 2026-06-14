# European Installed Generation Capacity by Fuel — ENTSO-E, cleaned Parquet

Year-by-year installed generation capacity (MW) by fuel type for every European bidding zone — the structural backdrop to every supply/merit-order analysis, cleaned from ENTSO-E into one Parquet.

This repo hosts a **free sample** (one showcase zone). The full all-EU dataset is sold separately.

> 👉 **Full dataset — all 28 EU zones, 2017-12-31→2026-01-01 (3,608 rows) — launching shortly. ⭐ Star/watch to get notified.**

## What's inside
- Installed capacity by fuel type, all ~38 EU zones, yearly 2018–2026
- Fuel codes decoded to names (Nuclear, Fossil Gas, Wind Offshore, …)
- One row per zone × fuel × year; flat + partitioned
- The denominator for capacity-factor and energy-transition analytics

## Schema
| column | type | description |
|---|---|---|
| `zone` | str | Bidding zone |
| `ts` | timestamp (UTC) | Year (period start) |
| `fuel` | str | Decoded production type |
| `capacity_mw` | float | Installed capacity, MW |
| `unit` | str | Unit |
| `res_min` | int | Native resolution in minutes (15/30/60) |

Full field docs: [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).

## Load it
```python
import pandas as pd
df = pd.read_parquet("european-installed-capacity_sample.parquet")
```
More loaders (DuckDB / Polars): [`load_example.py`](load_example.py).

## Quality
Every build passes an automated QC suite (schema, value integrity, time consistency, coverage).

## More from ReadySet — European energy data
Same source (ENTSO-E), same clean-Parquet treatment — all join on `zone` + `ts`:
- [European Day-Ahead Electricity Prices](https://github.com/GetReadySet/european-day-ahead-prices)
- [European Electricity Load / Demand](https://github.com/GetReadySet/european-electricity-load)
- [European Power Generation by Fuel Type](https://github.com/GetReadySet/european-generation-by-fuel)
- [European Power Plant Outages](https://github.com/GetReadySet/european-power-plant-outages)

## License & source
CC-BY-4.0 (attribute ENTSO-E). Source: ENTSO-E Transparency Platform.
Derived, cleaned redistribution. No personal data; GDPR N/A.
