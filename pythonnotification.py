import time
from plyer import notification
if __name__=="__main__":
    notification.notify(
        title="Please drink water",
        message="You must drink 7-8 liters of water daily.",
        timeout=5
        )
time.sleep(6)
