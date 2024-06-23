import pandas as pd
import numpy as np
from typing import Callable, List, Any

class SponsoredLegislation:
    """Legislation Analytics for sponsored legislation data."""
    def __init__(self, sponsored_legislation_response: dict):
        self.clean_sponsored_legislation_response = sponsored_legislation_response
        self.sponsored_legislation_df = None

    """"
    TODO:
    Metrics:
    1.) # of sponsored legislation by policy area --> should give options by congress adn policy area
    2.) # of Ammendments to bills
    """
    async def _create_sponsored_legislation_df(self) -> pd.DataFrame:
        df = pd.json_normalize(self.sponsored_legislation_respons).replace(np.NaN, None)
        df['introducedDate'] = pd.to_datetime(df['introducedDate'], errors='coerce')
        df['latestAction.actionDate'] = pd.to_datetime(df['latestAction.actionDate'], errors='coerce')

        return df
    
    async def initialize(self):
        """Initialize the DataFrame from the response data."""
        self.sponsored_legislation_df = await self._create_sponsored_legislation_df()

    async def _get_sponsored_legislation_by_congress(self, congress: int) -> pd.DataFrame:
        return self.sponsored_legislation_df[self.sponsored_legislation_df.congress == congress]
    
    async def _get_sponsored_legislation_by_policy_area(self, policy_area: str) -> pd.DataFrame:
        return self.sponsored_legislation_df[self.sponsored_legislation_df.policy_area == policy_area]
    
    async def _aggregate_data_frame(
        self,
        dataframe:pd.DataFrame, 
        aggregate_by: str, 
        agg_values:List, 
        agg_func:Callable[..., Any], 
        *args, 
        **kwargs
    ):
        _df = dataframe.groupby(aggregate_by, as_index=False)
        results = _df[agg_values].agg(agg_func, *args, **kwargs)
        return results
        
        