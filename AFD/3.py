from AFD import AFD

if __name__ == "__main__":
    Q = ['q0', 'q1', 'q2']
    Sigma = ['a', 'b']
    delta = {
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2', ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q1', ('q2', 'b'): 'q1'
    }
    q0 = 'q0'
    F = ['q0', 'q2']
    M = (Q, Sigma, delta, q0, F)
    
    while (True):
        print("(:q para sair) ")
        cadeia = input("Cadeia: ")
        
        if cadeia == ':q': break
        
        print(f"Resultado => {AFD(M, cadeia)}")
