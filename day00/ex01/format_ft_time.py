import time

seconds = time.time()

result = f'{seconds:,.4f}'
print("Second since January 1, 1970:", result, "or%10.3e" % (seconds),
      "in scientific notation")

current_time = time.localtime()
time_string = time.strftime("%b %d %Y", current_time)

print(time_string)
