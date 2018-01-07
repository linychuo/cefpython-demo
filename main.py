#encoding=utf-8
from cefpython3 import cefpython as cef
import platform
import sys, os

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook
    cef.Initialize(settings = {
        'context_menu': {
            'enabled': False
        }
    })
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    cef.CreateBrowserSync(url=os.path.join(cur_dir, "resources", "index.html"),
                          window_title="你好，cefpython")
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    print("[hello_world.py] CEF Python {ver}".format(ver=cef.__version__))
    print("[hello_world.py] Python {ver} {arch}".format(
          ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"


if __name__ == '__main__':
    main()