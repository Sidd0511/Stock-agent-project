from typing import List
from models.context import AssetContext

DIRECTION_INCREASE = "increase"
DIRECTION_DECREASE = "decrease"

def check_thresholds(contexts: List[AssetContext]) -> List[AssetContext]:
    
    for asset in assets:
        change = asset.current_price - asset.reference_price

        if asset.threshold_type == "percent":
            evaluate_threshold(asset, change, is_percent=True)
        elif asset.threshold_type == "absolute":
            evaluate_threshold(asset, change, is_percent=False)

    return contexts

def evaluate_threshold(asset: AssetContext, change: float, is_percent: bool):

    if is_percent:
        raw_value = (change/asset.reference_price)*100
        formatted_value = f"{abs{raw_value}:.2f}%"
    else:
        raw_value = change
        formatted_value = f"{abs(raw_value):.2f}"

    if asset.direction == DIRECTION_INCREASE and raw_value >= asset.threshold:
        asset.triggered = True
        asset.notes = f"Alert: Price increased by {formatted_value} which exceeds the threshold of {asset.threshold}."

    elif asset.direction == DIRECTION_DECREASE and raw_value <= -asset.threshold:
        asset.triggered = True
        asset.notes = f"Alert: Price decreased by {formatted_value} which exceeds the threshold of {asset.threshold}."
    else:
        asset.triggered = False
        asset.notes = f"No significant change."
