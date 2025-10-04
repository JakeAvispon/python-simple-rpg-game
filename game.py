# ----- RPG GAME -----
# Juego sencillo utilazando POO en Python
#   Añadir funcionalidades extra

# CLASE PADRE
class Character:                                            # BUENA PRACTICA - PascalCase "Character" (Primer letra mayuscula)
    def __init__(self, name: str, health: int, attack: int, defense: int):     # BUENA PRACTICA - Type Hinting "name: str, health: int, attack: int, defense: int" (Definir tipo de dato)
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1                                                          # ««« 1
        self.experience = 0                                                     # ««« 1
        
    # CONSEJOS
    def __str__(self):
        return (f"--- Estado de {self.name} ---\n"
                f"Vida: {self.health}\n"
                f"Ataque: {self.attack}\n"
                f"Defensa: {self.defense}")

    def alive(self):
        return self.health > 0
    
    def do_damage(self, target):
        print(f"¡{self.name} ataca a {target.name}!")
        damage = max(0, self.attack - target.defense)              # CORRECCION - Previo (damage = self.attack - target.defense)
        if damage > 0:
            print(f"¡{target.name} recibe {damage} puntos de daño!")
            target.health -= damage
            if not target.alive():
                print(f"¡{target.name} ha sido derrotado!")
        else:
            print(f"¡El ataque de {self.name} no es efectivo contra {target.name}!")
            
            
# -- HERENCIA --
# CLASE HIJO
class Mage(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, mana: int):
        super().__init__(name, health, attack, defense)
        self.mana = mana
        
    # METODO unico para los magos
    def cast_fireball(self, target):
        mana_cost = 20
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            fireball_damage = 30                            # Daño magico, ignora defensa
            target.health -= fireball_damage
            print(f"¡{self.name} lanza una bola de fuego a {target.name} causando {fireball_damage} de daño!")
        else:
            print(f"¡{self.name} no tiene suficiente mana!")
            
    # POLIMORFISMO (sobreescribir un metodo)
    def __str__(self):
        base_stats = super().__str__()
        return base_stats + f"\nMana: {self.mana}"
            
class Warrior(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, fury: int):
        super().__init__(name, health, attack, defense)
        self.fury = fury
        
    def heavy_strike(self, target):
        fury_cost = 25
        if self.fury >= fury_cost:
            self.fury -= fury_cost
            
            base_damage = self.attack * 2
            actual_damage = max(0, base_damage - target.defense)
            
            target.health -= actual_damage
            print(f"¡{self.name} realiza un ataque pesado contra {target.name} causando {actual_damage} de daño!")
        else:
            print(f"¡{self.name} no tiene suficiente furia!")
            
    # POLIMORFISMO (sobreescribir un metodo)
    def __str__(self):
        base_stats = super().__str__()
        return base_stats + f"\nFuria: {self.fury}"
    
class Archer(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, arrows: int):
        super().__init__(name, health, attack, defense)
        self.arrows = arrows
        
    def shoot_arrow(self, target):
        arrow_cost = 1
        if self.arrows >= arrow_cost:
            self.arrows -= arrow_cost
            
            arrow_damage = self.do_damage(target)
            print(f"¡{self.name} dispara una flecha contra {target.name} causando {arrow_damage} de daño!")
        else:
            print(f"¡{self.name} no tiene flechas suficientes!")
            
    def __str__(self):
        base_stats = super().__str__()
        return base_stats + f"\nFlechas: {self.arrows}"
 
      
# -- DEMO JUEGO --  
if __name__ == "__main__": 
    # HERENCIA
    mage = Mage("Gandalf", 70, 10, 8, 100)
    chief_orc = Character("Jefe Orco", 90, 15, 10)
    warrior = Warrior("Borimir", 110, 16, 12, 50)
    orc = Character("Orco Explorador", 40, 8, 4)
    archer = Archer("Legolas", 90, 15, 10, 15)
    
    # POLIMORFISMO
    party = [mage, warrior, orc, archer]
    
    print("----- MI EQUIPO -----")
    for character in party:
        # Polimorfismo imprime el "__str__"
        print(f"{character}\n")