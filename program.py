from foto import Foto
from error import DimensionError

def test_foto():
    try:
        foto = Foto(1000, 2000, 'foto1.jpg')
        print(f"Foto creada correctamente: {foto.ancho}x{foto.alto}")

        try:
            foto.ancho = 3000
        except DimensionError as e:
            print(f"Error al establecer el ancho: {e}")

        try:
            foto.alto = 0
        except DimensionError as e:
            print(f"Error al establecer el alto: {e}")

        try:
            foto.alto = 2600
        except DimensionError as e:
            print(f"Error al establecer el alto: {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    test_foto()
