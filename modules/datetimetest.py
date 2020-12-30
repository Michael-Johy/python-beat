from datetime import datetime

now = datetime.now()
print(now)

print('type = ', type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)

ts = dt.timestamp();
print('timestamp', ts)

dt1 = datetime.fromtimestamp(ts)