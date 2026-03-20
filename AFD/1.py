from AFD import AFD

if __name__ == "__main__":
    Q = ['q0', 'q1', 'q2']
    Sigma = ['0', '1']
    delta = {('q0', '0'): 'q0', ('q0', '1'): 'q1', ('q1', '0'): 'q2', ('q1', '1'): 'q1', ('q2', '0'): 'q1', ('q2', '1'): 'q1'}
    q0 = 'q0'
    F = ['q1']
    M = (Q, Sigma, delta, q0, F)
    
    cadeia = '1'
    
    r = AFD(M, cadeia)
    print(f"Resultado: {r}")