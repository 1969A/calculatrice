import tkinter as tk

# Couleurs inspirées du thème sombre de Windows
BG_COLOR = "#202020"
BTN_BG = "#333333"
BTN_FG = "#ffffff"
BTN_ACTIVE = "#454545"
EQUALS_BG = "#f7630c"
EQUALS_ACTIVE = "#d15206"

class Calculatrice:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("320x480")
        self.root.config(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.expression = "0"

        # Affichage (Écran)
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            root, textvariable=self.display_var, anchor="e",
            bg=BG_COLOR, fg="#ffffff", font=("Segoe UI", 32), padx=20
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(30, 20))

        # Disposition des boutons identique à l'image
        boutons = [
            ('CE', 1, 0), ('C', 1, 1), ('⌫', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), (',', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in boutons:
            # Bouton égal avec une couleur orange distinctive
            if text == '=':
                bg = EQUALS_BG
                active_bg = EQUALS_ACTIVE
            else:
                bg = BTN_BG
                active_bg = BTN_ACTIVE

            btn = tk.Button(
                root, text=text, bg=bg, fg=BTN_FG, 
                activebackground=active_bg, activeforeground=BTN_FG,
                bd=0, font=("Segoe UI", 14),
                command=lambda t=text: self.clic_bouton(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Configuration des poids des lignes et colonnes pour l'ajustement
        root.rowconfigure(0, weight=2)
        for i in range(1, 6):
            root.rowconfigure(i, weight=1)
        for j in range(4):
            root.columnconfigure(j, weight=1)

    def clic_bouton(self, char):
        if char in ('C', 'CE'):
            self.expression = "0"
        elif char == '⌫':
            if len(self.expression) > 1:
                self.expression = self.expression[:-1]
            else:
                self.expression = "0"
        elif char == '=':
            try:
                # Remplacement pour que Python comprenne les symboles mathématiques
                expr_python = self.expression.replace('×', '*').replace('÷', '/').replace(',', '.')
                resultat = str(eval(expr_python))
                
                # Suppression du .0 inutile pour les nombres entiers
                if resultat.endswith('.0'):
                    resultat = resultat[:-2]
                
                self.expression = resultat.replace('.', ',')
            except Exception:
                self.expression = "Erreur"
        elif char == '+/-':
            if self.expression.startswith('-'):
                self.expression = self.expression[1:]
            elif self.expression != "0":
                self.expression = '-' + self.expression
        else:
            if self.expression == "0" and char != ',':
                self.expression = char
            elif char == ',' and ',' in self.expression:
                return
            else:
                self.expression += char

        self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculatrice(root)
    root.mainloop()