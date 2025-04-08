from models.asset import AssetTrackingConfig, AlertRule
from pydantic import ValidationError

# The following test case is expected to pass because the symbol is provided for a stock asset.
print("\033[1m\n--- Valid Metal Config ---\033[0m")
metal = AssetTrackingConfig(
    name="Gold",
    type="metal",
    threshold=2.5,
    threshold_type="percent",
    direction="decrease"
)
print(metal)

# The following test case is expected to pass because the symbol is provided for a stock asset.
print("\033[1m\n--- Valid Stock Config ---\033[0m")
stock = AssetTrackingConfig(
    name="TCS",
    type="stock",
    threshold=100,
    threshold_type="absolute",
    direction="increase",
    symbol="TCS.NS"
)
print(stock)

# The following test case is expected to fail because the symbol is missing for a stock asset.
print("\033[1m\n--- Invalid Stock (Missing Symbol) ---\033[0m")
try:
    bad_stock = AssetTrackingConfig(
        name="Apple",
        type="stock",
        threshold=5,
        threshold_type="percent",
        direction="decrease"
        # Missing symbol
    )
except ValidationError as e:
    print("Validation Error:", e)

# The following test case is expected to fail because the symbol is provided for a metal asset.
print("\033[1m\n--- Invalid Metal (Symbol Provided) ---\033[0m")
try:
    bad_metal = AlertRule(
        asset_name="Silver",
        asset_type="metal",
        trigger_type="above",
        threshold=10,
        active=True,
        symbol="Ag"  # Symbol provided for metal
    )
except ValidationError as e:
    print("Validation Error:", e)

# The following test case is expected to pass because the symbol is provided for a stock asset.
print("\033[1m\n--- Valid Metal Alert Rule ---\033[0m")
valid_metal_alert = AlertRule(
    asset_name="Silver",
    asset_type="metal",
    trigger_type="above",
    threshold=10,
    active=True
)
print(valid_metal_alert)

# The following test case is expected to pass because the symbol is provided for a stock asset.
print("\033[1m\n--- Valid Stock Alert Rule ---\033[0m")
valid_stock_alert = AlertRule(
    asset_name="Apple",
    asset_type="stock",
    trigger_type="below",
    threshold=150,
    active=True,
    symbol="AAPL"
)
print(valid_stock_alert)

# The following test case is expected to fail because the symbol is missing for a stock asset.
print("\n--- Invalid Stock Alert Rule (Missing Symbol) ---      ")
try:
    invalid_stock_alert = AlertRule(
        asset_name="Tesla",
        asset_type="stock",
        trigger_type="above",
        threshold=200,
        active=True
        # Missing symbol
    )
except ValidationError as e:
    print("Validation Error:", e)
