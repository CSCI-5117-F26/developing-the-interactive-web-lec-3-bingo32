from halo import Halo
import time
spinner = Halo(text='Loading', spinner='dots')


spinner.start()

# Run time consuming work here
# You can also change properties for spinner as and when you want
time.sleep(60)
spinner.stop()