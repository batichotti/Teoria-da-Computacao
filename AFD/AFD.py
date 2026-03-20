def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F