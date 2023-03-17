celcius = int(input("masukkan nilai celcius"))

fahrenheit = (9/5) * celcius + 32
print(f"nilai {celcius} C ke F adalah: {fahrenheit}")

rearmur = float(input("masukkan nilai rearmur"))

fahrenheit = (9/4) * rearmur + 32
print(f"nilai {rearmur} R ke F adalah: {fahrenheit}")

mata_uang = {
    'idr' : 1,
    'usd' : 0.000071,
    'sgd' : 0.000098,
    'eur' : 0.000061,
    'jpy' : 0.0079
}

uang = input("masukkan matauang (idr,usd,sgd,eur,jpy): ")
nominal = int(input("masukkan nilai uang :"))
print(mata_uang[uang]*nominal)

classroom ={ 
    'aslab' : {
    'aslab_01':{
    'nama' : 'mas_safri',
    'umur' : '21'
},
}
}



string = "ikan bakar gosong item pahit banget"
print(string[0:4]) # ikan
print(string[5:10]) # bakar
print(string[10:16]) # gosong
print(string[17:20]) # item
print(string[21:25]) # pahit
print(string[26:31]) # banget



