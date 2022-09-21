#Procura os 250 filmes mais bem avaliados no site IMDB

import requests
from bs4 import BeautifulSoup

with open('IMDB.csv','w') as f:

    #f.write(filme_nome + ',' + filme_lancamento + ',' + filme_classificacao +'\n' )
    f.write('Nome' + ',' + 'Lancamento' + ',' + 'Classificacao' + ',' + 'Duração' + '\n')
        
    #Será extraído o HTML deste site
    url='https://www.imdb.com/chart/top/'

    #Abre o site
    pagina1=requests.get(url)

    #Se Status_Code = 200, está ok! Pode prosseguir
    print(pagina1.status_code)

    #Pega o HTML do site
    html=pagina1.text

    #Cria Objeto Soup com o código HTML
    pagina1_soup=BeautifulSoup(html,'html.parser')    

    #Procura o primeiro TBody
    pagina1_tbody=pagina1_soup.find('tbody',{'class':'lister-list'})

    #Procura todos os 'trs' DENTRO do primeiro tbody
    pagina1_trs=pagina1_tbody.findAll('tr')

    #Percorre cada 'tr' encontrado DENTRO de 'trs'
    for pagina1_tr in pagina1_trs:


        #para cada tr encontrado, localize 'td' e a sua classe "titleColumn"
        pagina1_td = pagina1_tr.find('td',{'class':'titleColumn'})

        #Encontra o Id de cada filme
        pagina1_Filme_id = pagina1_td.a['href']

        # Localize o filme pelo seu Nome('a') e ano('span') 
        filme_nome=pagina1_td.a.string
        filme_ano =pagina1_td.span.string 

        #String para cada link do filme
        filmes_links = f'https://www.imdb.com{pagina1_Filme_id}'
        #filmes_links='https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=DEBEVVQCSAY77R7T611J&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

        print(filmes_links)

        #Faz conexão com a url dos detalhes do filme: Lançamento, duração!!
        pagina2=requests.get(filmes_links)

        #Cria o objeto_soup
        pagina2_soup = BeautifulSoup(pagina2.text,'html.parser')

        #Encontra a TAG onde está todos os detalhes no link aberto
        pagina2_ul = pagina2_soup.find('ul',{'class':'ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt'})

        #Encontra todos os lis dentro da TAG ANTERIORMENTE encontrada
        pagina2_lis=pagina2_ul.findAll('li',{'class':'ipc-inline-list__item'})
        


        #Este contador será utilizado no for
        contador=0
    
        #Percorre todos os lis
        for li in pagina2_lis:

            if contador ==0:
                filme_ano=li.a.string

            if contador==1:
                filme_classificacao = li.a.string
                
            
            if contador==2:

                # A TAG da duração vem neste formato: 
                # <li class="ipc-inline-list__item" role="presentation">2<!-- -->h<!-- --> <!-- -->22<!-- -->m</li>
                
                duracao_removedor1='<li class="ipc-inline-list__item" role="presentation">'
                duracao_removedor2='<!-- -->'
                duracao_removedor3='</li>'

                filme_duracao=str(li)
                filme_duracao=filme_duracao.replace(duracao_removedor1,'').replace(duracao_removedor2,'').replace(duracao_removedor3,'')
                # print(filme_duracao)
                
            
            contador+=1

    
        print(filme_nome + ',' + filme_ano + ',' + filme_classificacao + ',' + filme_duracao + '\n')
        f.write(filme_nome + ',' + filme_ano + ',' + filme_classificacao + ',' + filme_duracao + '\n')    
    
    print('\n' + 'Fim')

     
      
      
   
   
      
   
  

    