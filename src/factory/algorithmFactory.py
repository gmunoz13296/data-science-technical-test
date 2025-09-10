class AlgorithmFactory:

    _dicc = {}
    
    def register(self, type, service):
        self._dicc[type] = service       

    
    def create(self, type):
        service = self._dicc[type]
        if not service:
            raise ValueError(f"Algorithm '{type}' not found")
        return service()

    def getAll(self):
         return list(map(lambda service: service(), self._dicc.values()))         
        