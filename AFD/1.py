from AFD import AFD

if __name__ == "__main__":
    Q = ['q0', 'q1', 'q2', 'q3', 'T']
    Sigma = ['a', 'b']
    delta = {
        ('q0', 'a'): 'T', ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q1', ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3', ('q2', 'b'): 'T',
        ('q3', 'a'): 'T', ('q3', 'b'): 'T',
        ('T', 'a'): 'T', ('T', 'b'): 'T'
    }
    q0 = 'q0'
    F = ['q3']
    M = (Q, Sigma, delta, q0, F)
    
    while (True):
        cadeia = input("(:q para sair) Cadeia: ")
        
        if cadeia == ':q': break
        
        print(f"Resultado => {AFD(M, cadeia)}")
