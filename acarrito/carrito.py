class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        carrito = self.session.get('carrito')

        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito
    
    def agregar_producto(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito [producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': (str(producto.precio)),
                'cantidad': 1,
                'imagen': producto.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value ['cantidad'] = value ['cantidad'] + 1
                    value ['precio'] = float(value ['precio']) + producto.precio
                    break

        self.guardar_carrito()  
    
    def guardar_carrito(self):
        self.session ['carrito'] = self.carrito
        self.session.modified = True

    def eliminar_prodcuto(self, producto):
        producto.id = str(producto.id)

        if producto.id in self.carrito:
            del self.carrito [producto.id]
            self.guardar_carrito()

    def restar_producto(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value ['cantidad'] = value ['cantidad'] - 1
                if value ['cantidad'] < 1:
                    self.eliminar_prodcuto (producto)
                
                value ['precio'] = float(value ['precio']) - producto.precio
                break
        
        self.guardar_carrito()

    def limipar_carrito(self):
        self.session ['carrito'] = {}
        self.session.modified = True