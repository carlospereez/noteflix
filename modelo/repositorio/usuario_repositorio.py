from typing import List

from modelo import Usuario
class UsuarioRepositorio:
    def crearUsuario(self, correo_electronico: str) -> None:
        ...

    def leerUsuario(self, correo_electronico: str) -> Usuario:
        ...

    def leerUsuarios(self) -> List[Usuario]:
        ...

    def actualizaUsuario(self, usuario: Usuario) -> None:
        ...