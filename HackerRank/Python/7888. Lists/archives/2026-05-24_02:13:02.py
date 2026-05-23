if __name__ == '__main__':
    N = int(input())
    
    lista = []
    
    for _ in range (N):
        linha = input().split()
        comando = linha[0]
        
        if  (comando == 'insert'):
            position = int(linha[1])
            value = int(linha[2])
            lista.insert(position, value)
            
        elif (comando == 'print'):
            print(lista)
            
        elif (comando == 'remove'):
            value = int(linha[1])
            lista.remove(value)
        
        elif (comando == 'append'):
            value = int(linha[1])
            lista.append(value)
            
        elif (comando == 'sort'):
            lista.sort()
            
        elif (comando == 'pop'):
            lista.pop()
            
        elif (comando == 'reverse'):
            lista.reverse()

    
