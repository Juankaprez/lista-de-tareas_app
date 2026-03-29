import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("420x520")
        self.root.configure(bg="#1e1e2f")

        self.servicio = TareaServicio()

        # Título
        titulo = tk.Label(root, text="📝 Lista de Tareas",
                          font=("Arial", 16, "bold"),
                          bg="#1e1e2f", fg="white")
        titulo.pack(pady=10)

        # Entrada
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Lista
        self.lista = tk.Listbox(root, width=40, height=12,
                                font=("Arial", 11),
                                bg="#2c2c3e",
                                fg="white",
                                selectbackground="#6c63ff",
                                activestyle="none")
        self.lista.pack(pady=10)
        self.lista.bind("<Double-1>", self.completar_tarea_evento)

        # Botones
        frame_botones = tk.Frame(root, bg="#1e1e2f")
        frame_botones.pack(pady=10)

        btn_add = tk.Button(frame_botones, text="➕ Añadir",
                           bg="#4CAF50", fg="white", width=12,
                           command=self.agregar_tarea)
        btn_add.grid(row=0, column=0, padx=5)

        btn_done = tk.Button(frame_botones, text="✔ Completar",
                            bg="#2196F3", fg="white", width=12,
                            command=self.completar_tarea)
        btn_done.grid(row=0, column=1, padx=5)

        btn_delete = tk.Button(frame_botones, text="🗑 Eliminar",
                              bg="#f44336", fg="white", width=12,
                              command=self.eliminar_tarea)
        btn_delete.grid(row=0, column=2, padx=5)

    # EVENTOS
    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    # FUNCIONES
    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea")

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.servicio.completar_tarea(index)
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.servicio.eliminar_tarea(index)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            self.lista.insert(tk.END, texto)

            if tarea.completado:
                # Pintar en gris
                self.lista.itemconfig(tk.END, fg="gray")
                self.lista.delete(tk.END)
                self.lista.insert(tk.END, texto + " ✔")
                self.lista.itemconfig(tk.END, fg="gray")