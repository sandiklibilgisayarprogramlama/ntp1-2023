class Araba:

    def __init__(self, marka, model, beygir_gucu, yakit_tipi):
        self.marka = marka
        self.model = model
        self.beygir_gucu = beygir_gucu
        self.yakit_tipi = yakit_tipi

    def model_yazdir(self):
        print(self.model)

    def marka_dondur(self):
        return self.marka
