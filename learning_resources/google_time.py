import datetime
## Converts Google Time
def date_from_webkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601, 1, 1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return epoch_start + delta

# Example usage
webkit_time = 13359058434576089  # Replace with your timestamp
print(date_from_webkit(webkit_time))
