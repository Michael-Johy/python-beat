import psutil

cpu_times = psutil.cpu_times()

print(cpu_times)

disk_partitions = psutil.disk_partitions()
print(disk_partitions)


