from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol
from pyformlang.cfg import CFG
from random import choice

class Story:
    def __init__(self):
        self._init_dfa()
        self.current_state = self.start

    def _init_dfa(self):
        self.dfa = DeterministicFiniteAutomaton()

        self.start = State("start")
        self.found_relic = State("found_relic")
        self.used_relic = State("used_relic")
        self.end = State("end")

        find_relic = Symbol("find_relic")
        use_relic = Symbol("use_relic")
        end_story = Symbol("end_story")

        self.dfa.add_transition(self.start, find_relic, self.found_relic)
        self.dfa.add_transition(self.found_relic, use_relic, self.used_relic)
        self.dfa.add_transition(self.used_relic, end_story, self.end)

    def proceed(self, choice):
        symbol = Symbol(choice)
        if self.dfa.accepts_input([symbol]):
            self.current_state = self.dfa.get_next_state(self.current_state, symbol)
            return True
        return False

    def get_dialogues(self):
        dialogues = {
            self.start: self._generate_dialogue("Luna: ¡Dr. Mora! Mira lo que encontré."),
            self.found_relic: self._generate_dialogue("Dr. Mora: ¡Cuidado! Eso es el reloj de arena maldito."),
            self.used_relic: self._generate_dialogue("Luna: El tiempo... todo se siente diferente."),
            self.end: self._generate_dialogue("Sombra: Has jugado con el destino. Ahora paga el precio.")
        }
        return dialogues.get(self.current_state, [])

    def _generate_dialogue(self, base_dialogue):
        cfg = CFG.from_text("""
            S -> '{base_dialogue}' RESPONSE
            RESPONSE -> '. ¿Qué deberíamos hacer ahora?'
                     | '. Esto es increíble.'
                     | '. Necesitamos proceder con cautela.'
        """.format(base_dialogue=base_dialogue))
        return ''.join(choice(cfg.generate()))

