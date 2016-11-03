import i3ipc
from decorator import contextmanager


@contextmanager
def i3_connection(block):
    i3 = i3ipc.Connection()
    yield block(i3)


def focus_window(id):
    with i3_connection() as i3:
        i3.command("[id='%s'] focus" % id)


i3 = i3ipc.Connection()
output = i3.get_tree()
workspace = i3.get_tree().find_focused().workspace()
windows = workspace.nodes
# to focus an window go for i3.command("[id='%s'] focus")
if len(windows) > 1:
    for window in windows:
        focus_window(window.id)

