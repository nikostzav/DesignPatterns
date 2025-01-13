
class Legs:
    def count(self):
        raise NotImplementedError("Subclasses must implement the count method.")

class Upholstery:
    def material(self):
        raise NotImplementedError("Subclasses must implement the material method.")


class ModernLegs(Legs):
    def count(self):
        return 4

class ModernUpholstery(Upholstery):
    def material(self):
        return "leather"


class VictorianLegs(Legs):
    def count(self):
        return 4

class VictorianUpholstery(Upholstery):
    def material(self):
        return "velvet"


class FurniturePartsFactory:
    def create_legs(self):
        raise NotImplementedError("Subclasses must implement the create_legs method.")
    
    def create_upholstery(self):
        raise NotImplementedError("Subclasses must implement the create_upholstery method.")


class ModernFurniturePartsFactory(FurniturePartsFactory):
    def create_legs(self):
        return ModernLegs()
    
    def create_upholstery(self):
        return ModernUpholstery()


class VictorianFurniturePartsFactory(FurniturePartsFactory):
    def create_legs(self):
        return VictorianLegs()
    
    def create_upholstery(self):
        return VictorianUpholstery()


class FurnitureWithParts:
    def __init__(self, style, factory: FurniturePartsFactory):
        self.style = style
        self.legs = factory.create_legs()
        self.upholstery = factory.create_upholstery()

    def describe(self):
        print(f"This {self.style} furniture has {self.legs.count()} legs and {self.upholstery.material()} upholstery.")


if __name__ == "__main__":
    
    modern_factory = ModernFurniturePartsFactory()
    modern_furniture = FurnitureWithParts("Modern", modern_factory)
    modern_furniture.describe()

    
    victorian_factory = VictorianFurniturePartsFactory()
    victorian_furniture = FurnitureWithParts("Victorian", victorian_factory)
    victorian_furniture.describe()
