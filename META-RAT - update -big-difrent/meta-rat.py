from module import main_handeler
import os
import platform
os_kind = platform.uname()
if "Windows" in os_kind:
    os.system("Title META RAT")
else:
    pass
while True:
    main_handeler.main_run()