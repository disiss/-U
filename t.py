import ctypes

lib_name = ctypes.cdll.LoadLibrary("C:/PythonUgliffier/libsum.dll")
res_int = lib_name.add_int(4,5)
print(res_int)