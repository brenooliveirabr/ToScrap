#Atualizacao 2
import requests

for i in range(1,10):
    #Será extraído o HTML deste site
    url=f'https://quotes.toscrape.com/page/{i}/'
    
    #Imprime a pagina atual
    print(url)
    
    #Abre o site
    r=requests.get(url)

    #Se Status_Code = 200, está ok! Pode prosseguir
    #print(r.status_code)

    #Pega o HTML do site
    html=r.text

    #Padrao da frase
    frase_padrao_inicio=' <span class="text" itemprop="text">'
    frase_padrao_fim='</span>'

    #padrao do autor
    autor_padrao_inicio='<span>by <small class="author" itemprop="author">' 
    autor_padrao_fim='</small>'

    with open('./citacoes.txt','a',encoding='utf-8') as f:
        
        
    #Percorre linha por linha do HTML. De início o HTML é considerado como um Bloco inteiro.
        for line in html.split('\n'):
            
            #Verifica se tem o frase_padrao_inicio a ser procurado
            if  frase_padrao_inicio in line:
                #Remove os padrões da linha, assim como as chaves, ficando apenas com o texto
                line=line.replace(frase_padrao_inicio,'').replace(frase_padrao_fim,'').replace('“','').replace('”','')
                
                #Remove os espaços em branco da linha
                frase=line.strip()
            # print(line)
                    
            #Verifica se tem o autor_padrao_inicio a ser procurado
            if  autor_padrao_inicio in line:
                #Remove os padrões da linha, assim como as chaves, ficando apenas com o texto
                line=line.replace(autor_padrao_inicio,'').replace(autor_padrao_fim,'')#.replace('“','').replace('”','')
                
                #Remove os espaços em branco da linha
                autor=line.strip()
                
                
                
                
                f.write(frase + "\n" + "--" + autor+'\n'+'\n')