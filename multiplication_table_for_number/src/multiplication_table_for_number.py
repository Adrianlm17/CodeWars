
def multi_table(number):
    res_forma = str()
    for i in range(1,11):
        resul = i * number
        res_forma += "{} * {} = {}\n".format(i,number,resul)
        res_fin = res_forma.strip('\n')
        
    return res_fin
