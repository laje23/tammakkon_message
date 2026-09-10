from domain.interfaces import IReadMedia

class ReadMedia(IReadMedia):
    
    def read(self, storge_name: str) -> bytes:
        with open(storge_name , 'rb') as file:
            return file.read()