class FiniteStateMachine:
    def __init__(self, states, transitions, start_state, accepting_states):
        self.start_state = start_state
        self.states = states
        self.transitions = transitions
        self.current_state = start_state
        self.accepting_states = accepting_states
    
    def transition(self, symbol):
        if (self.current_state, symbol) not in self.transitions:
            return False
        self.current_state = self.transitions[(self.current_state, symbol)]
        return True
    
    def is_accepted(self):
        return self.current_state in self.accepting_states
    
    def reset(self):
        self.current_state = self.start_state

# Define a FSM
estados = ['q0']
transicoes = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q0',
}
estado_inicial = 'q0'
estados_aceitos = ['q0']
fsm = FiniteStateMachine(estados, transicoes, estado_inicial, estados_aceitos)

# Processa uma string
sequencias = [
    "",
    "010110",
    "010",
    "00100",
    "10000",
    "01011",
    "1011010",
]

for palavra in sequencias:
    print(palavra if palavra != "" else "(string vazia)", " => ", end="")
    for symbol in palavra:
        if not fsm.transition(symbol):
            print("String não aceita...")
            break
    print("String aceita!") if fsm.is_accepted() else print("String não aceita...")
    fsm.reset()
    