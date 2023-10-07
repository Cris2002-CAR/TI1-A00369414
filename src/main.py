from model.automata import StoryAutomaton
from ui.interface import get_user_choice

def main():
    automaton = StoryAutomaton()
    automaton.add_states_and_symbols(["inicio", "opcion1"], ["explorar", "hablar"])
    automaton.set_start_state("inicio")
    automaton.add_transition("inicio", "explorar", "opcion1")
    
    print("Bienvenido a 'La Maldición del Reloj de Arena'")
    name = input("Por favor, introduce tu nombre: ")
    
    while True:
        choice = get_user_choice("¿Qué deseas hacer?", ["Explorar las ruinas", "Hablar con Dr. Mora", "Usar el reloj de arena"])
        if choice == 0 and automaton.is_accepted(["explorar"]):
            print("Encuentras un antiguo altar...")
           
        elif choice == 1:
            print("Dr. Mora: 'Debemos tener cuidado con el reloj, Luna.'")
        elif choice == 2:
            print("El reloj de arena te envuelve en una brillante luz...")
        replay = input("¿Quieres intentarlo de nuevo? (s/n): ")
        if replay.lower() != 's':
            break

if __name__ == "__main__":
    main()

