from progress.bar import Bar
import time


bar = Bar('Loading', fill = '▓' , max=100)
for i in range(100):
    # Do some work
    time.sleep(0.2) #sec = 1%
    bar.next()
bar.finish()

