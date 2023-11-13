data =input('digite uma data no formato da dd/mm/aaaa: ')
dia,mes,ano=data.split('/')
if ano <0:
    print('ano invalido!')
else:
    if mes<1 or mes >12:
        print('mes invalido!')
    elif mes in[1,3,5,7]