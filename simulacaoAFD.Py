def afd(Q, alfab, fTrans, q0, F, cadeia):
    qA = q0
    for i in cadeia:
        qA = tabela[(qA, i)]
    return qA in F

tabela = {('q0','0'): 'q0',('q0','1'): 'q1',('q1','0'): 'q2',('q1','1'): 'q1',('q2','0'): 'q1',('q2','1'): 'q1'}

Q = ['q0','q1','q2']
F = ['q1']
alfab = ['0','1']

aux = afd(Q, alfab, tabela, 'q0', F, '001010100')

if aux:
    print('Cadeia Aceita')
else:
    print('Cadeia Nao Aceita')