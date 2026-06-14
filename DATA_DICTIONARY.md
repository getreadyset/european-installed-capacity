# Data Dictionary — European Installed Generation Capacity by Fuel — ENTSO-E, cleaned Parquet

| column | type | description |
|---|---|---|
| `zone` | str | Bidding zone |
| `ts` | timestamp (UTC) | Year (period start) |
| `fuel` | str | Decoded production type |
| `capacity_mw` | float | Installed capacity, MW |
| `unit` | str | Unit |
| `res_min` | int | Native resolution in minutes (15/30/60) |

*Source: ENTSO-E Transparency Platform. Times are UTC.*
