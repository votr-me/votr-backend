from logging import Filter
from typing import List


class RedactApiKeyFilter(Filter):
    def __init__(self, api_keys: List[str], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_keys = api_keys

    def filter(self, record):
        for api_key in self.api_keys:
            if api_key in record.getMessage():
                record.msg = record.getMessage().replace(api_key, "*****")

                if record.args:
                    record.args = tuple(
                        arg.replace(api_key, "****") if isinstance(arg, str) else arg
                        for arg in record.args
                    )
        return True
