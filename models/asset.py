from pydantic import BaseModel, model_validator
from typing import Literal, Optional, List, Dict


class AssetTrackingConfig(BaseModel):
    """
    Configuration model for tracking an asset.

    This class defines the configuration for tracking assets such as stocks or metals.
    It validates the input to ensure that stock assets have a symbol and metal assets do not.

    Attributes:
        name (str): The name of the asset being tracked.
        type (Literal["stock", "metal"]): The type of the asset (either "stock" or "metal").
        threshold (float): The threshold value for triggering an alert.
        threshold_type (Literal["percent", "absolute"]): The type of threshold (percentage or absolute value).
        direction (Literal["increase", "decrease"]): The direction of the threshold (increase or decrease).
        symbol (Optional[str]): The stock symbol, required for stock assets and not allowed for metal assets.

    Methods:
        check_symbol_for_stock() -> 'AssetTrackingConfig':
            Validates that stock assets have a symbol and metal assets do not.
    """
    name: str
    type: Literal["stock", "metal"]
    threshold: float
    threshold_type: Literal["percent", "absolute"]
    direction: Literal["increase", "decrease"]
    symbol: Optional[str] = None

    @model_validator(mode="after")
    def check_symbol_for_stock(self) -> 'AssetTrackingConfig':
        """
        Validate the symbol field based on the asset type.

        Raises:
            ValueError: If the asset type is "stock" and no symbol is provided, or if the asset type
                        is "metal" and a symbol is provided.

        Returns:
            AssetTrackingConfig: The validated configuration object.
        """
        if self.type == "stock" and not self.symbol:
            raise ValueError("Symbol must be provided for stock assets.")
        elif self.type == "metal" and self.symbol:
            raise ValueError("Symbol must not be provided for metal assets.")
        return self


class AlertRule(BaseModel):
    """
    Model for defining alert rules for assets.

    This class defines the rules for triggering alerts based on asset thresholds.
    It validates the input to ensure that stock assets have a symbol and metal assets do not.

    Attributes:
        asset_name (str): The name of the asset the alert is associated with.
        asset_type (Literal["stock", "metal"]): The type of the asset (either "stock" or "metal").
        trigger_type (Literal["above", "below"]): The type of trigger (above or below the threshold).
        threshold (float): The threshold value for triggering the alert.
        active (bool): Whether the alert rule is active. Defaults to True.
        symbol (Optional[str]): The stock symbol, required for stock assets and not allowed for metal assets.

    Methods:
        check_symbol_for_stock() -> 'AlertRule':
            Validates that stock assets have a symbol and metal assets do not.
    """
    asset_name: str
    asset_type: Literal["stock", "metal"]
    trigger_type: Literal["above", "below"]
    threshold: float
    active: bool = True
    symbol: Optional[str] = None

    @model_validator(mode="after")
    def check_symbol_for_stock(self) -> 'AlertRule':
        """
        Validate the symbol field based on the asset type.

        Raises:
            ValueError: If the asset type is "stock" and no symbol is provided, or if the asset type
                        is "metal" and a symbol is provided.

        Returns:
            AlertRule: The validated alert rule object.
        """
        if self.asset_type == "stock" and not self.symbol:
            raise ValueError("Symbol must be provided for stock assets.")
        elif self.asset_type == "metal" and self.symbol:
            raise ValueError("Symbol must not be provided for metal assets.")
        return self



