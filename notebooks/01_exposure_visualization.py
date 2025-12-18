import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
prices = pd.read_csv("../data/raw/commodity_prices.csv")
positions = pd.read_csv("../data/raw/positions.csv")

# 2. Merge price & position data
df = positions.merge(
    prices,
    on=["date", "commodity"],
    how="left"
)

# 3. Calculate exposure
df["exposure"] = df["position_size"] * df["price"]

# 4. Aggregate by commodity
exposure_by_commodity = (
    df.groupby("commodity")["exposure"]
    .sum()
    .reset_index()
)

# 5. Plot
plt.figure()
plt.bar(
    exposure_by_commodity["commodity"],
    exposure_by_commodity["exposure"]
)
plt.title("Commodity Exposure Overview")
plt.xlabel("Commodity")
plt.ylabel("Total Exposure")
plt.tight_layout()
plt.show()




# Scenario: 5% price drop
df["scenario_pnl"] = df["exposure"] * (-0.05)

scenario_result = (
    df.groupby("commodity")["scenario_pnl"]
    .sum()
    .reset_index()
)

plt.figure()
plt.bar(
    scenario_result["commodity"],
    scenario_result["scenario_pnl"]
)
plt.title("Scenario PnL: 5% Price Drop")
plt.xlabel("Commodity")
plt.ylabel("PnL")
plt.tight_layout()
plt.show()
