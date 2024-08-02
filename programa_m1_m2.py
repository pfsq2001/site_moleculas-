import streamlit as st 

target = st.text_input('colocar a sequencia alvo com 30 bp')
if target is not None:
    
    a = []
    b = []
    c= []
    lista_arg = list(target)
    for num, i in enumerate(lista_arg):
        if num in range(0,7,1):
            a.append(i)
        elif num in range(7, 15, 1):
            b.append(i)
        else: 
            c.append(i)
    a = "".join(a)
    b = "".join(b)
    c = "".join(c)

    a_reverso = a[::-1]
    b_reverso = b[::-1]
    c_reverso = c[::-1]
    #CRIANDO m1 E m2 EM FORMATO DE STRING 

    m1 = a + b + c + b_reverso + c_reverso
    m2 = b_reverso + c + b + a + c_reverso

    alvo = []
    #O ALVO DEVERIA TER 22 BASES ENTÃO RETIREI AS OITO ULTIMAS MAS PRECISA DAS TRINTA PRA FAZER O M1 E M2 

   for num, i in enumerate(lista_arg):
        if num in range(0,22,1):
            alvo.append(i)
    alvo = "".join(alvo)
        
    lista_arg = "".join(lista_arg)
     
    st.write("M1 5' 3':", m1)
    st.write("M2 5' 3':\n", m2)
    st.write("Alvo 5' 3':\n", alvo)
        
