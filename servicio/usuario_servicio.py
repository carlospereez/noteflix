from modelo import Usuario, Media
class UsuarioServicio:
    @classmethod
    def alta_usuario(cls, correo_electronico: str) -> None:
        ...

    @classmethod
    def ver_media(cls, usuario: Usuario, media: Media) -> None:
        ...

