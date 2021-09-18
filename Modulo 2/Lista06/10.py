x = [input() for x in range(10)]
m = 0
m_index = 0
for i in range(0,10,2):
    if int(x[i]) > m:
        m = int(x[i])
        m_index = i
print(f"a maioe nota foi de {x[m_index+1]} com {x[m_index]} pontos")