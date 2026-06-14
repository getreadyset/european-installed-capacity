"""Load examples for European Installed Generation Capacity by Fuel — ENTSO-E, cleaned Parquet."""
import pandas as pd

# everything in one file
df = pd.read_parquet("european-installed-capacity_all.parquet")
print(df.shape, df.zone.unique()[:10])

# one zone, fast, without loading the rest (DuckDB)
# import duckdb
# duckdb.sql("SELECT * FROM 'data/zone=FR/**/*.parquet'").df()

# polars
# import polars as pl
# pl.read_parquet("european-installed-capacity_all.parquet")
