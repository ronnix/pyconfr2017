from api_meteo import APIMeteo


class Temps:

    def __init__(self):
        self.api_meteo = APIMeteo()

    def il_va_faire_chaud(self, ville):
        return self.api_meteo.temperature(ville) > 20
