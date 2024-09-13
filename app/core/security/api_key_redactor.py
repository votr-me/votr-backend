from logging import Filter


class RedactApiKeyFilter(Filter):
    def __init__(self, api_keys):
        super().__init__()
        self.api_keys = api_keys

    def filter(self, record):
        message = record.getMessage()

        # Check if the message is None or not a string before proceeding
        if not isinstance(message, str):
            return True  # Allow the log to proceed if the message is not a string (e.g., None or another type)

        # Replace any occurrence of API keys with "[REDACTED]"
        for api_key in self.api_keys:
            if api_key and api_key in message:
                record.msg = message.replace(api_key, "[REDACTED]")

        return True  # Always return True to allow the record to be logged
