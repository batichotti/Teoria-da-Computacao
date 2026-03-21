from AFD import AFD

if __name__ == "__main__":
    Q = ['q0', 'q1', 'q2', 'q3', 'T']
    Sigma = ['a', 'b']
    delta = {
        ('q0', 'a'):'q1', ('q0', 'b'): 'q2',
        ('q1', 'a'):'q0', ('q1', 'b'): 'q3',
        ('q2', 'a'):'T', ('q2', 'b'): 'q3',
        ('q3', 'a'):'T', ('q3', 'b'): 'q2',
        ('T', 'a'):'T', ('T', 'b'): 'T',
    }
    q0 = 'q0'
    F = ['q0', 'q3']
    M = (Q, Sigma, delta, q0, F)
    
    while (True):
        print("(Digite ':q' para sair) ")
        cadeia = input("Cadeia: ")
        
        if cadeia == ':q': break
        
        print(f"Resultado => {AFD(M, cadeia)}")
