from time import perf_counter

def perf_timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

def convert_unit(size_in_bytes):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if size_in_bytes == 0:
        return "0 B"

    size_in_bytes = float(size_in_bytes)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    size_in_gb = size_in_mb / 1024
    if size_in_gb >= 1:
        return f"{round(size_in_gb, 2)} GB"  
    elif size_in_mb >= 1:
        return f"{round(size_in_mb, 2)} MB" 
    elif size_in_kb >= 1:
        return f"{round(size_in_kb, 2)} KB" 
    else:
        return f"{round(size_in_bytes, 2)} B" 

