from win10toast import ToastNotifier

TEXT = "Hello World!"

notifier = ToastNotifier()
notifier.show_toast(
    title='Title',
    msg=TEXT,
    duration=5,
    icon_path=None,
    threaded=False
)
