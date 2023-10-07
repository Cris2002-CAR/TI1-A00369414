from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol

class StoryAutomaton:

    def __init__(self):
        self.dfa = DeterministicFiniteAutomaton()

    def add_states_and_symbols(self, states, symbols):
        for state in states:
            self.dfa.add_state(State(state))
        for symbol in symbols:
            self.dfa.add_input_symbol(Symbol(symbol))
            
    def set_start_state(self, state):
        self.dfa.add_start_state(State(state))
        
    def set_final_state(self, state):
        self.dfa.add_final_state(State(state))

    def add_transition(self, src, symbol, dest):
        self.dfa.add_transition(State(src), Symbol(symbol), State(dest))

    def is_accepted(self, string):
        return self.dfa.accepts(string)
