import psutil


conversor_gigabyte = 1024**3

ram = psutil.virtual_memory()
ram_total = round(float(ram.total)/conversor_gigabyte,2)
ram_free = round(float((ram.free)/conversor_gigabyte),2)
ram_used = round(float((ram.used)/conversor_gigabyte),2)

cpu_core = psutil.cpu_count(logical=False)
cpu_core_logical = psutil.cpu_count()
cpu_percent_all = psutil.cpu_percent(interval= 0.1)



# for x in range(3):


disc = psutil.disk_usage("/")
disc_total = round(disc.total/conversor_gigabyte)
disc_used = round(disc.used/conversor_gigabyte)
disc_free = round(disc.free/conversor_gigabyte)
percent_used = disc.percent

sensor = psutil.sensors_temperatures()
disc_temp_atual = sensor["nvme"][0].current
cpu_temperature_atual = sensor["coretemp"][0].current


print(
    f"CPU:\n"
    f"  Cores: {cpu_core}\n"
    f"  Virtual Core: {cpu_core_logical}\n"
    f"  Percent Using: {percent_used}%\n"
    f"  Temperature:{cpu_temperature_atual}°C\n\n"
    f"RAM:\n"
    f"  Total: {ram_total}\n GiB"
    f"  Used: {ram_used}\n GiB"
    f"  Free: {ram_free}\n\n GiB"
    f"Disc:\n"
    f"  Total: {disc_total}\n GiB"
    f"  Used: {disc_used}\n GiB"
    f"  Free: {disc_free}\n GiB"
    f"  Temperature:{disc_temp_atual}°C\n\n"
)


