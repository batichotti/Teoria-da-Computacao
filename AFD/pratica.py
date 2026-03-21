from AFD import AFD

if __name__ == "__main__":
    Q = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
    Sigma = ['a', 'b']
    delta = {
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q2',
        ('q1', 'a'): 'q0', ('q1', 'b'): 'q3',
        ('q2', 'a'): 'q3', ('q2', 'b'): 'q4',
        ('q3', 'a'): 'q2', ('q3', 'b'): 'q5',
        ('q4', 'a'): 'q5', ('q4', 'b'): 'q0',
        ('q5', 'a'): 'q4', ('q5', 'b'): 'q1'
    }
    q0 = 'q0'
    F = ['q1']
    M = (Q, Sigma, delta, q0, F)
    
    while (True):
        print("(Digite ':q' para sair) ")
        cadeia = input("Cadeia: ")
        
        if cadeia == ':q': break
        
        print(f"Resultado => {AFD(M, cadeia)}")
