class HoraConverter:
    def __init__(self):
        self._horas = None  # Inicializa as horas como None

    # Método para converter horas em minutos
    def converter_horas_para_minutos(self):
        if self._horas is not None:
            return self._horas * 60
        else:
            return None

    # Getter para horas
    @property
    def horas(self):
        return self._horas

    # Setter para horas
    @horas.setter
    def horas(self, value):
        if value < 0:
            raise ValueError("A quantidade de horas não pode ser negativa.")
        self._horas = value
