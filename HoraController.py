from model.Hora import HoraConverter

class HoraController:
    def __init__(self):
        self._hora_converter = HoraConverter()

    def validar_horas(self):
        if self._hora_converter.horas is None or self._hora_converter.horas < 0:
            raise ValueError("A quantidade de horas não pode ser negativa ou nula.")

    def converter_horas_para_minutos(self):
        self.validar_horas()
        return self._hora_converter.converter_horas_para_minutos()

    @property
    def hora_converter(self):
        return self._hora_converter

    @hora_converter.setter
    def hora_converter(self, valor):
        self._hora_converter = valor
