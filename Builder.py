from abc import ABC, abstractmethod

# Product Class
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer Specifications:\nCPU: {self.cpu}\nRAM: {self.ram}\nStorage: {self.storage}\nGPU: {self.gpu}"

# Abstract Builder
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self): pass

    @abstractmethod
    def set_ram(self): pass

    @abstractmethod
    def set_storage(self): pass

    @abstractmethod
    def set_gpu(self): pass

    @abstractmethod
    def get_computer(self): pass

# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel i9"
    
    def set_ram(self):
        self.computer.ram = "32GB"
    
    def set_storage(self):
        self.computer.storage = "1TB SSD"
    
    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 3080"
    
    def get_computer(self):
        return self.computer

# Director Class
class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def build_computer(self):
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_gpu()
        return self.builder.get_computer()

# Client Code
if __name__ == "__main__":
    gaming_builder = GamingComputerBuilder()
    director = Director(gaming_builder)

    gaming_computer = director.build_computer()
    print("Gaming Computer Built:")
    print(gaming_computer)
