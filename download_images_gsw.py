import requests as req

months_range = range(1,13)
ftp = 'https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/'

menu = int(input('Selecione base para download:\n[1]YearlyClassification\n[2]Aggregated\n[3]MonthlyHistory\n[4]MonthlyRecurrence\n\033[93m[0]TODAS AS BASES\33[0m\nPadrão: TODAS AS BASES: '))
if menu == 0:
    tipos = ['yearlyClassification','aggregated', 'monthlyHistory','monthlyRecurrence']
elif menu == 1:
    tipos = ['yearlyClassification']
elif menu == 2:
    tipos = ['aggregated']
elif menu == 3:
    tipos = ['monthlyHistory']
elif menu == 4:
    tipos = ['monthlyRecurrence']
else:
    print('menu inválido, baixando todas as bases')
    tipos = ['yearlyClassification','aggregated', 'monthlyHistory','monthlyRecurrence']

ano_inicio = int(input('Informe o ANO Inicial que deseja fazer download, formatação em 4 dígitos [ex: 1999]: (caso queira baixar toda a série histórica (1984-2021), digite [0]:\n'))
if ano_inicio == 0:
    a = range(1984, 2023)
else:
    ano_fim = int(input('Digite ANO Final que deseja fazer download, formatação em 4 dígitos [ex: 2020]\n'))
    a = range(ano_inicio, ano_fim+1)

tipo_sec = []
img1 = '0000320000-0000520000.tif'
img2 = '0000320000-0000560000.tif'


for tipo in tipos:
    if tipo == 'monthlyRecurrence':
        for m in months_range:
            tipo_sec = ['has_observations', 'monthlyRecurrence']
            for tipo2 in tipo_sec:
                #exemplo: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/MonthlyRecurrence/VER4-0/tiles/has_observations1/
                consulta = f'{ftp}MonthlyRecurrence/LATEST/tiles/{tipo2}{m}/'
                url_img1 = consulta+img1
                url_img2 = consulta+img2
                print(url_img1)
                print(url_img2)
                url_img1 = consulta+img1
                url_img2 = consulta+img2

                download1 = req.get(url_img1, allow_redirects=True)
                open(f'{tipo}_{tipo2}_{img1}', 'wb').write(download1.content)
                download2 = req.get(url_img2, allow_redirects=True)
                open(f'{tipo}_{tipo2}_{img2}', 'wb').write(download2.content)

    else:
        for ano in a:
            if tipo == 'yearlyClassification':
                #exemplo: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/YearlyClassification/LATEST/tiles/yearlyClassification1984/yearlyClassification1984-0000000000-0000000000.tif
                consulta = f'{ftp}YearlyClassification/LATEST/tiles/{tipo}{ano}/{tipo}{ano}-'
            if tipo == 'aggregated':
                tipo_sec = ['change', 'extent', 'occurrence', 'recurrence', 'seasonality', 'transitions']
                for tipo2 in tipo_sec:
                    #exemplo: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/Aggregated/LATEST/extent/tiles/
                    consulta = f'{ftp}Aggregated/LATEST/{tipo2}/tiles/{tipo2}-'
            if tipo == 'monthlyHistory':
                #exemplo: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/
                for m in months_range:
                    consulta = f'{ftp}MonthlyHistory/LATEST/tiles/{ano}/{ano}_{m}/{ano}_{m}-'

            url_img1 = consulta+img1
            url_img2 = consulta+img2
            print(url_img1)https://jeodpp.jrc.ec.eur
            print(url_img2)
            if len(tipo_sec) == 0:
                download1 = req.get(url_img1, allow_redirects=True)
                open(f'{tipo}_{ano}_{img1}', 'wb').write(download1.content)
                download2 = req.get(url_img2, allow_redirects=True)
                open(f'{tipo}_{ano}_{img2}', 'wb').write(download2.content)

            else:
                download1 = req.get(url_img1, allow_redirects=True)
                open(f'{tipo}_{tipo2}_{ano}_{img1}', 'wb').write(download1.content)
                download2 = req.get(url_img2, allow_redirects=True)
                open(f'{tipo}_{tipo2}_{ano}_{img2}', 'wb').write(download2.content)

