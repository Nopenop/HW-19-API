import psutil
import tools_config
class Tool:
    """Creates tool object to access information on server
    """
    def __init__(self) -> None:
        self.path = tools_config.Path().disk_path
    
    def get_mem(self) -> int:
        """returns the percentage of virtual memory in use"""
        memory = psutil.virtual_memory()
        return (memory.used/memory.total) * 100
    
    def get_cpu(self) -> int:
        """returns the percentage of the cpu is in use"""
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        total = 0
        used = 0
        for i, usage in enumerate(cpu_percent):
            total += 100
            used += usage
        return (used/total) * 100
    
    def get_disk(self) -> int:
        """returns the percentage of the disk is in use"""
        disk = psutil.disk_usage(self.path)
        return (disk.used/disk.total) * 100