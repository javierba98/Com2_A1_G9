import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  # Hereda de gr.sync_block
    def __init__(self):  # Constructor sin argumentos adicionales
        gr.sync_block.__init__(
            self,
            name='e_Acum',  # Nombre que aparecerá en GRC
            in_sig=[np.float32],  # Señal de entrada
            out_sig=[np.float32]  # Señal de salida
        )
        self.accumulated = 0  # Inicializa el acumulador

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y = output_items[0]  # Señal de salida acumulada
        
        self.accumulated += np.cumsum(x)  # Acumula la señal de entrada
        y[:] = self.accumulated  # Asigna el valor acumulado a la salida
        
        return len(y)
