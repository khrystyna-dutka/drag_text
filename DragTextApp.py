import tkinter as tk

class DragTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Перетягування тексту")
        
        # Створення полотна
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()
        
        # Додавання тексту
        self.text_id = self.canvas.create_text(200, 200, text="Перетягни мене", font=("Arial", 16), fill="black")
        
        # Перемінна для збереження стану перетягування
        self.dragging = False
        
        # Прив'язка подій миші
        self.canvas.tag_bind(self.text_id, "<ButtonPress-1>", self.on_mouse_down)
        self.canvas.tag_bind(self.text_id, "<B1-Motion>", self.on_mouse_move)
        self.canvas.tag_bind(self.text_id, "<ButtonRelease-1>", self.on_mouse_up)
    
    def on_mouse_down(self, event):
        # Перетягування активується
        self.dragging = True
    
    def on_mouse_move(self, event):
        if self.dragging:
            # Оновлення позиції тексту
            self.canvas.coords(self.text_id, event.x, event.y)
    
    def on_mouse_up(self, event):
        # Перетягування завершується
        self.dragging = False

# Створення вікна і запуск додатку
if __name__ == "__main__":
    root = tk.Tk()
    app = DragTextApp(root)
    root.mainloop()
