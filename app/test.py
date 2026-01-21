from datetime import datetime, timedelta, timezone
expire = datetime.now() + timedelta(minutes=1)
expire2 = datetime.now()
print(expire)
print(expire2)