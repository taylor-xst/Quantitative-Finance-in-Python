min = 42
sec = 42
distance = 10.0
miles = distance / 1.61

secs = 42 * 60 + 42

speed = secs / miles

print int(speed / 60), int(speed % 60)

print "%.2f" %(miles / secs * 3600)