import pandas as pd
import numpy as np
from typing import Callable, List, Any, Dict, Optional


class SponsoredLegislation:
    """Legislation Analytics for sponsored legislation data."""

    def __init__(self, sponsored_legislation_response: dict) -> None:
        self._sponsored_legislation_response = sponsored_legislation_response
        # self.sponsored_legislation_df = (
        #     self._create_sponsored_legislation_df()
        # )  # Initialize immediately

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

    async def initialize(self):
        """Initialize the DataFrame from the response data."""
        self._sponsored_legislation_df = await self._create_sponsored_legislation_df()

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
            query_str = " & ".join(
                [f"`{col}` == '{val}'" for col, val in filter_conditions.items()]
            )
            dataframe = dataframe.query(query_str)

        results = dataframe.groupby(aggregate_by, as_index=False)[agg_values].agg(
            agg_func, *args, **kwargs
        )

        return results.to_dict(orient="records")
