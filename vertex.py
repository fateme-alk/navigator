class Vertex:
    def __init__(self, name: str, coordinate: list):
        self.name = name
        self.lat = coordinate[0]
        self.long = coordinate[1]
     
    
    def __repr__(self):
        return f'{self.__class__.__name__} name {self.name} has coordinate: ({self.lat}, {self.long})'
    

