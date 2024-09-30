from abc import ABC,abstractmethod

class Empleado_A35(ABC):
    def __init__(self,RFC,apellidos,nombres):
        self.RFC=RFC
        self.apellidos=apellidos
        self.nombres=nombres

        
    @abstractmethod
    def ingresos(self):
        pass
    @abstractmethod
    def bonificacion(self):
        pass
    @abstractmethod
    def descuento(self):
        pass
    def sueldo_neto(self):
        return self.ingresos() + self.bonificacion() - self.descuento()
    def mostrar_informacion(self):
        print(f"RFC: {self.RFC}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Nombres: {self.nombres}")

        print(f"Ingresos: ${self.ingresos():.2f}")
        print(f"Bonificación: ${self.bonificacion():.2f}")
        print(f"Descuento: ${self.descuento():.2f}")
        print(f"Sueldo Neto: ${self.sueldo_neto():.2f}")


class EmpleadoVendedor_A35(Empleado_A35):
    def __init__(self, RFC, apellidos, nombres, montovendido, tasacomision):
        super().__init__(RFC, apellidos, nombres)
        self.montovendido= montovendido
        self.tasacomision =tasacomision
    def ingresos(self):
        return self.montovendido* self.tasacomision
    def bonificacion(self):
        if self.montovendido <1000:
            return 0
        elif 1000 <= self.montovendido<= 5000:
            return self.ingresos()* 0.05
        else:
            return self.ingresos()* 0.10
    def descuento(self):
        if self.ingresos()< 1000:
            return self.ingresos()* 0.11
        else:
            return self.ingresos()* 0.15
        
class EmpleadoPermanente_A35(Empleado_A35):
    def __init__(self,RFC,apellidos,nombres,sueldobase,numerosegurosocial):
        super().__init__(RFC,apellidos,nombres)
        self.sueldobase = sueldobase
        self.numerosegurosocial = numerosegurosocial
    def ingresos(self):
        return self.sueldobase
    def bonificacion(self):
        return 0
    def descuento(self):
        return self.sueldobase * 0.11
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Seguro Social: {self.numerosegurosocial}")

def main():
    empleado1 = EmpleadoVendedor_A35("ROCA0507", "Roldan Correa", "Alexis", 4000, 0.03)
    empleado2 = EmpleadoPermanente_A35("AGDJTIC", "Alberto de la Teja", "Julio", 5000, "JT24805")
    empleados = [empleado1, empleado2]

    for empleado in empleados:
        empleado.mostrar_informacion()
        print()

if __name__ == "__main__":
    main()
