
class Furniture:
    def __init__(self, style):
        self.style = style

    def sit_on(self):
        raise NotImplementedError("This method should be overridden.")


class Chair(Furniture):
    def sit_on(self):
        print(f"Sitting on a {self.style} chair.")


class Sofa(Furniture):
    def sit_on(self):
        print(f"Sitting on a {self.style} sofa.")


class FurnitureFactory:
    @staticmethod
    def create_furniture(furniture_type, style):
        if furniture_type == "chair":
            return Chair(style)
        elif furniture_type == "sofa":
            return Sofa(style)
        else:
            raise ValueError("Unknown furniture type")


if __name__ == "__main__":
   
    modern_chair = FurnitureFactory.create_furniture("chair", "Modern")
    modern_chair.sit_on()

 
    victorian_sofa = FurnitureFactory.create_furniture("sofa", "Victorian")
    victorian_sofa.sit_on()
