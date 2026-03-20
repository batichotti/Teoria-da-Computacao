from AFD import AFD

if __name__ == "__main__":
    Q = 0
    Sigma = 0
    delta = 0
    q0 = 0
    F = 0
    M = (Q, Sigma, delta, q0, F)
    
    while (True):
        cadeia = input("(:q para sair) Cadeia: ")
        
        if cadeia == ':q': break
        
        print(f"Resultado => {AFD(M, cadeia)}")
