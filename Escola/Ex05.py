class musica:
        musicas = []
        def __init__(self, nome_musica, autor, tempo):
        
            self.nome_musica = nome_musica
            self.autor = autor
            self.tempo= tempo
            da_p_ouvir = True
            musica.musicas.append(self)
        def __str__(self):
            return  f"nome da musica: {self.nome_musica} autor: {self.autor} Tempo: {self.tempo} "
        
        @classmethod
        def listar_musicas():
            for musica in musica.musicas:
                 print(f"nome_musica".ljust(25) | "autor".ljust(25) | "tempo".ljust(25))
                 print('-' * 68)
                for musica in cls.musicas:
                      
musica1 = musica("chove chuva","fancisco","3.2 minutos")
print(musica1)

