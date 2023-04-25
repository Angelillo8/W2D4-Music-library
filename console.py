from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo

# artist1 = Artist("Peter Schmidt")
# artist_repo.save(artist1)
# artist2 = Artist("Jose Gonzalez")
# artist_repo.save(artist2)

# artist1 = artist_repo.select(1)
# artist2 = artist_repo.select(2)

# album1 = Album("Row, row, your boat", "heavy", artist1)
# album_repo.save(album1)
# album2 = Album("Gently down the stream", "rock", artist2)
# album_repo.save(album2)

# artista = artist_repo.select(3)
# artista.name = "Angel Gonzalez"
# artist_repo.update(artista)

# album_x = album_repo.select(3)
# print(album_x.title)

# resultados = album_repo.albums_by_artist(1)
# for resultado in resultados:
#     print(resultados[0].title)
