class musica:
        def __init__(self, nome_musica, autor, tempo):
        
            self.nome_musica = nome_musica
            self.autor = autor
            self.tempo= tempo
            da_p_ouvir = True
        def __str__(self):
            return  f"nome da musica: {self.nome_musica} autor: {self.autor} Tempo: {self.tempo} "
    
musica1 = musica("chove chuva","fancisco","3.2 minutos")
print(musica1)

