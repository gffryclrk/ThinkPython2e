# https://stackoverflow.com/questions/2882308/spawning-a-thread-in-python
# https://stackoverflow.com/questions/16534458/how-to-know-if-a-process-is-still-running-in-python

import threading
import time
from datetime import datetime
import five_letter_avoids

t = threading.Thread(target=five_letter_avoids.min_combs)
t.start()

while (t.is_alive()):
    time.sleep(180)
    now = datetime.now()
    print('I\'m alive! {}'.format(now))
