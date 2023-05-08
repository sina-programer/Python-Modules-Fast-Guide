import winsound

# Note: this module is only available in Windows OS

# Minimum=37
# Maximum=32767

for i in range(1, 5):
    # winsound.Beep(freq, duration)
    winsound.Beep(1000 * i, 200)
    winsound.Beep(1000 * i, 200 - (i*50))


# The sound when a window opens
winsound.MessageBeep()
