import streamlit as st 

target = st.text_input('colocar a sequencia alvo com 30 bp')
complemento = st.selectbox('Choose one:', options = ["5' -> 3'", "3' -> 5'"])
if target is not None:
    if complemento == "5' -> 3'":
      a = []
      b = []
      c= []
      target = target.upper()
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

      a_reverso = []
      b_reverso = []
      c_reverso = []
      #fazendo  dicionario pra criar o reverso complementar
      complemento = [('A', 'T'), ('T', 'A'),
                      ('C', 'G'), ('G', 'C')]

      reverso = dict(complemento)
      for i in a:
          a_reverso.append(reverso[i])
      a_reverso.reverse()
      a_reverso = "".join(a_reverso)

      for i in b:
          b_reverso.append(reverso[i])
      b_reverso.reverse()
      b_reverso = "".join(b_reverso)
      
      for i in c:
          c_reverso.append(reverso[i])
      c_reverso.reverse()
      c_reverso = "".join(c_reverso)
      #CRIANDO m1 E m2 EM FORMATO DE STRING 

      m1 = a + b + c_reverso + b_reverso + a_reverso
      m2 = c_reverso + a + b + c + b_reverso
      
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
      st.write("C", c)
      st.write("Creverso:", c_reverso)  
    elif complemento == "3' -> 5'":
        a = []
        b = []
        c= []
        target = target.upper()
        z = list(target)  
        lista_arg = reversed(z)
        
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
        
        a_reverso = []
        b_reverso = []
        c_reverso = []
        #fazendo  dicionario pra criar o reverso complementar
        complemento = [('A', 'T'), ('T', 'A'),
                      ('C', 'G'), ('G', 'C')]
        
        reverso = dict(complemento)
        for i in a:
          a_reverso.append(reverso[i])
        a_reverso.reverse()
        a_reverso = "".join(a_reverso)
        
        for i in b:
          b_reverso.append(reverso[i])
        b_reverso.reverse()
        b_reverso = "".join(b_reverso)
        
        for i in c:
          c_reverso.append(reverso[i])
        c_reverso.reverse()
        c_reverso = "".join(c_reverso)
        #CRIANDO m1 E m2 EM FORMATO DE STRING 
        
        m1 = a + b + c_reverso + b_reverso + a_reverso
        m2 = c_reverso + a + b + c + b_reverso
        
        alvo = []
        #O ALVO DEVERIA TER 22 BASES ENTÃO RETIREI AS OITO ULTIMAS MAS PRECISA DAS TRINTA PRA FAZER O M1 E M2 
        
        for num, i in enumerate(z):
            if num in range(0,22,1):
                  alvo.append(i)
        alvo = "".join(alvo)
          
        lista_arg = "".join(lista_arg)
        
        st.write("M1 5' 3':", m1)
        st.write("M2 5' 3':\n", m2)
        st.write("Alvo 5' 3':\n", alvo)
        st.write("C", c)
        st.write("Creverso:", c_reverso)  
