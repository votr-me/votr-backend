import pandas as pd
import numpy as np
from typing import Callable, List, Any, Dict, Optional
from numba import njit


class SponsoredLegislation:
    """Legislation Analytics for sponsored legislation data."""

    def __init__(self, sponsored_legislation_response: dict) -> None:
        self._sponsored_legislation_response = sponsored_legislation_response
        self.sponsored_legislation_df = (
            self._create_sponsored_legislation_df()
        )  # Initialize immediately

    """"
    TODO:
    Metrics:
    1.) # of sponsored legislation by policy area --> should give options by congress adn policy area
    2.) # of Ammendments to bills
    """

    @property
    def sponsored_legislation_response(self) -> dict:
        """Direct access to the original sponsored legislation response."""
        return self._sponsored_legislation_response

    async def _create_sponsored_legislation_df(self) -> pd.DataFrame:
        df = pd.json_normalize(self._sponsored_legislation_response).replace(
            np.nan, None
        )
        df["introducedDate"] = pd.to_datetime(df["introducedDate"], errors="coerce")
        df["latestAction.actionDate"] = pd.to_datetime(
            df["latestAction.actionDate"], errors="coerce"
        )

        return df

    async def initialize(self):
        """Initialize the DataFrame from the response data."""
        self.sponsored_legislation_df = await self._create_sponsored_legislation_df()

    async def get_sponsored_legislation_by_congress(
        self, congress: int
    ) -> List[Dict[str, Any]]:
        """Get sponsored legislation by congress."""
        df = await self.sponsored_legislation_df
        result_df = df[df.congress == congress]
        return result_df.to_dict(orient="records")

    async def get_sponsored_legislation_by_policy_area(
        self, policy_area: str
    ) -> List[Dict[str, Any]]:
        """Get sponsored legislation by policy area."""
        df = await self.sponsored_legislation_df
        result_df = df[df.policy_area == policy_area]
        return result_df.to_dict(orient="records")

    async def filter_dataframe(self, dataframe: pd.DataFrame, **kwargs):
        """Filters the provided DataFrame based on keyword arguments with comparison operators.

        Args:
            dataframe: The Pandas DataFrame to filter.
            **kwargs: Filter conditions as keyword arguments (e.g., column_name__gt=value).

        Supported operators:
            * __eq: Equal to (default if no operator is provided)
            * __ne: Not equal to
            * __lt: Less than
            * __le: Less than or equal to
            * __gt: Greater than
            * __ge: Greater than or equal to
        """

        filtered_df = dataframe.copy()

        for filter_str, value in kwargs.items():
            # Split the filter string to extract the column name and operator
            col, operator = (filter_str.split("__") + ["eq"])[:2]

            # Handle list values
            if isinstance(value, list):
                if operator in ("eq", "ne"):
                    filtered_df = (
                        filtered_df[filtered_df[col].isin(value)]
                        if operator == "eq"
                        else filtered_df[~filtered_df[col].isin(value)]
                    )
                else:
                    raise ValueError(f"Invalid operator '{operator}' for list values")
            else:
                # Apply comparison based on operator
                if operator == "eq":
                    filtered_df = filtered_df[filtered_df[col] == value]
                elif operator == "ne":
                    filtered_df = filtered_df[filtered_df[col] != value]
                elif operator == "lt":
                    filtered_df = filtered_df[filtered_df[col] < value]
                elif operator == "le":
                    filtered_df = filtered_df[filtered_df[col] <= value]
                elif operator == "gt":
                    filtered_df = filtered_df[filtered_df[col] > value]
                elif operator == "ge":
                    filtered_df = filtered_df[filtered_df[col] >= value]
                else:
                    raise ValueError(f"Invalid operator '{operator}'")

        return filtered_df

    async def aggregate_data_frame(
        self,
        dataframe: pd.DataFrame,
        aggregate_by: List[str],
        agg_values: str,
        agg_func: Callable[..., Any],
        filter_conditions: Optional[Dict] = None,
        *args: Any,
        **kwargs: Any,
    ) -> List[Dict[str, Any]]:
        """Aggregate data frame based on specified aggregation function."""

        if filter_conditions:
            dataframe = await self.filter_dataframe(dataframe, **filter_conditions)

        results = dataframe.groupby(aggregate_by, as_index=False)[agg_values].agg(
            agg_func, *args, **kwargs
        )

        return results.to_dict(orient="records")
