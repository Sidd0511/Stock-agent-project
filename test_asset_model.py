from models.asset import AssetTrackingConfig
from pydantic import ValidationError

print("\n--- Valid Metal Config ---")
metal = AssetTrackingConfig(
    name="Gold",
    type="metal",
    threshold=2.5,
    threshold_type="percent",
    direction="decrease"
)
print(metal)

print("\n--- Valid Stock Config ---")
stock = AssetTrackingConfig(
    name="TCS",
    type="stock",
    threshold=100,
    threshold_type="absolute",
    direction="increase",
    symbol="TCS.NS"
)
print(stock)

print("\n--- Invalid Stock (Missing Symbol) ---")
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