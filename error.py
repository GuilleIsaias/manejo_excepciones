class DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo) -> None:
        super().__init__(mensaje, dimension, maximo)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else: 
            ret = f'{self.mensaje}.'
            if self.dimension != None:
                ret += f' Dimension ingresada {self.dimension}'
            if self.maximo != None:
                ret += f' Valor maximo permitido: {self.maximo}'
            return ret

        

        
