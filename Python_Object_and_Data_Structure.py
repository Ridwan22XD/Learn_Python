
                                #Python Numbers
print("\t\t\t\tPython Number");
a=10
b=5

#modulo
c=a%b;

#pangkat
d=a**b;

#tambah,kurang, bagi, kali
e=1*3+2/2;
f=1*(3+2)/2;
print(a," modulo ", b, ":", c);
print(a," pangkat ", b, ":", d);
print("1*3+2/2: ",e);
print("1*(3+2)/2: ",f);
print("\n\n");




                                #Introduction String
print("\t\t\t\tIntroduction String");
a = 'hello world'
b = 'hello \'world'
c = "hello world"
d = "hello 'world'"
e = "hello \"world\""

print("menggunakan titik satu: ",a);
print("menggunakan titik satu dan satu: ",b);
print("menggunakan titik satu dua: ",c);
print("menggunakan titik satu dua dan satu: ",d);
print("menggunakan titik satu dua dan dua: ",e);
print("panjang string a: ",len(a));
print("\n\n");




                        #Indexing And Slicing With String
print("\t\t\tIndexing And Slicing With String");
#indexing
print("***********indexing***********");
a="abcdefg"
print("a = abcdefg");
print("index ke-2: ",a[1]); # dalam komputer indeks dimulai dari 0
print("index ke-5: ",a[4]); # dalam komputer indeks dimulai dari 0

#slicing
print("***********slicing***********");
a="abcdefg"
print("a = abcdefg");
print("slicing index 2 sampai terakhir --> [2:]: ",a[2:]);
print("slicing index 3 sebelum terakhir sampai terakhir --> [-3:]: ",a[-3:]);
print("slicing index 0 sampai terakhir dengan lompatan 2 --> [::2]: ",a[::2]);
print("slicing index 1 sampai terakhir dengan lompatan 3 --> [1::3]: ",a[1::3]);
print("\n\n");




                            #String Properties and Methods
print("\t\t\tString Properties and Methods");
#String Properti
print("***********String Properti***********");
a="abcdefg "
print("a = abcdefg ");
print("Cetak a sebanyak 3 kali --> a*3: ",a*3);

#Methods
print("***********Method 1***********");
a="abcdefg "
print("a = abcdefg ");
print("Huruf balok a --> a.upper(): ",a.upper());
print("Cetak a --> a: ",a);
print("***********Method 2***********");
x="apa saja mau kamu"
print("x = apa saja mau kamu");
print("mengganti spasi dengan koma pada x --> x.split(): ",x.split());
print("mengganti huruf a dengan koma pada x --> x.split(\"x\"): ",x.split("a"));
print("\n\n");





                        #Print Formatting with String
print("\t\t\tPrint Formatting with String");
#formatting string
print("***********Formatting String***********");
print(">>1<<");
print("This is a string {}\".format(\"INSERT\") --> ","This is a string {}".format("INSERT"));
print(">>2<<");
print("The {} {} {} \".format(\"fox\",\"brown\",\"quick\") --> ","The {} {} {} ".format("fox","brown","quick"));
print(">>3<<");
fo="fox";
b="brown";
q="quick";
print("fo=fox \nb=brown \nq=quick");
print("f\"The {fo} {b} {q} \" --> ",f"The {fo} {b} {q} ");
print(">>4<<");
print("The {2} {0} {1} \".format(\"fox\",\"brown\",\"quick\") --> ","The {2} {0} {1} ".format("fox","brown","quick"));
print(">>5<<");
print("The {b} {q} {f} \".format(f=\"fox\",b=\"brown\",q=\"quick\") --> ","The {b} {q} {f} ".format(f="fox",b="brown",q="quick"));
#formatting float
print("***********formatting Float***********");
result = 314.8920887;
print("result = 314.8920887");
print(">>1<<");
print("The result was {}\".format(result) -->","The result was {}".format(result));
print(">>2<<");
print("f\"The result was: {result}\" --> ",f"The result was: {result}");
print(">>3<<");
print("f\"The result was: {result:1.3f}\" --> ",f"The result was: {result:1.3f}");5
print("\n\n");




                                    #List In Python

print("\t\t\tList In Python");
print("List itu muntable --> Dapat diubah")
#Indexing
print("\n***********Indexing***********");
sample=["a","b","c"]
print("sample=(\"a\",\"b\",\"c\")");
print("sample index ke 1 --> sample[1] : ",sample[1]);
print("sample index ke 2 sampai 3 --> sample[2::3] : ",sample[2::3]);
#Combine 2 List
print("\n***********Combine 2 List***********");
sample1=["a","b","c"]
sample2=["1","2","3"]
print("sample1=(\"a\",\"b\",\"c\")");
print("sample2=(\"1\",\"2\",\"3\")");
print("gabungan sample 1 dan 2 --> sample1+sample2: ",sample1+sample2);
#Replace List
print("\n***********Replace List***********");
sample1=["a","b","c"]
sample[1] ="q"
print("sample=(\"a\",\"b\",\"c\")");
print("ganti nilai sample index ke-1 --> sample1[1] = \"q\" : ");
#Adding Member List
print("\n***********Adding Member List***********");
sample=["a","b","c"]
print("sample=(\"a\",\"b\",\"c\")");
sample.append("d")
print("Menambah anggota list sample --> sample.append(\"d\"): ",sample);
#Delete Or Move Member List
print("\n***********Delete Or Move Member List***********");
print(">>Delete<<");
sample=["a","b","c"]
sample.pop(-1)
print("sample=(\"a\",\"b\",\"c\")");
print("menghapus index ke-(-1) sample --> sample.pop(-1): ",sample);
sample=["a","b","c"]
sample.pop(-2)
print("sample=(\"a\",\"b\",\"c\")");
print("menghapus index ke-(-2) sample --> sample.pop(-2): ",sample);
print(">>Move<<");
sample=["a","b","c"]
pindah = sample.pop(-1)
print("sample=(\"a\",\"b\",\"c\")");
print("memindah index ke-(-1) sample ke pindah --> pindah = sample.pop(-1): ",pindah);
sample=["a","b","c"]
pindah = sample.pop(-2)
print("sample=(\"a\",\"b\",\"c\")");
print("memindah index ke-(-2) sample ke pindah --> pindah = sample.pop(-2): ",pindah);
#Sort Or Reverse Member List
print("\n***********Sort Or Reverse Member List***********");
print(">>Sort<<");
sample=["c","a","b"]
sample.sort()
print("sample=(\"c\",\"a\",\"b\")");
print("Mengurutkan sample --> sample.sort(): ",sample);
sample=[4,7,2]
sample.sort()
print("sample=(4,7,2)");
print("Mengurutkan sample --> sample.sort(): ",sample);
print(">>Reverse<<");
sample=["d","g","a"]
sample.reverse()
print("sample=(\"d\",\"g\",\"a\")");
print("Mengurutkan terbalik sample --> sample.reverse(): ",sample);
sample=[4,7,2,3]
sample.reverse()
print("sample=(4,7,2,3)");
print("Mengurutkan terbalik sample --> sample.reverse(): ",sample);

print("\n\n");




                                   #Dictionary In Python

print("\t\t\tDictionary In Python");
#Contents
print("\n***********Contents***********");
dictionary={"a":1,"Me":2,2.3:3,2.4:[1,2,3,4]}
print("dictionary = ",dictionary);
#Mutable
print("\n***********Mutable***********");
print("dictionary = ",dictionary);
dictionary["a"] = "new"
print("dictionary --> dictionary[\"a\"] = \"new\" = ",dictionary);
#Nested Object
print("\n***********Nested Object***********");
print("dictionary = ",dictionary);
print("dictionary queue 4 index ke-2 --> dictionary[2.4][2] = ",dictionary[2.4][2]);
#Only Call Keys Or Values
print("\n***********Only Call Key Or Value***********");
print("dictionary = ",dictionary);
print("key dictionary --> dictionary.keys() = ",dictionary.keys());
print("value dictionary --> dictionary.values() = ",dictionary.values());
#Combination Dictionary and Method (.upper)
print("\n***********Combination Dictionary and Method (.upper)***********");
print("dictionary = ",dictionary)
print("dictionary value queue 1 --> dictionary[\"a\"].upper() = ",dictionary["a"].upper())
print("dictionary = ",dictionary)
print("Menampung nilai key \"a\" yang sudah di upper")
dictionary["a"] = dictionary["a"].upper()
print("dictionary --> dictionary[\"a\"] = dictionary[\"a\"].upper() = ",dictionary)
print("\n\n");





                    #Tuples With Python
#Similiar with List
#Immuntable -> usefull for konstan variable
Tuples=("a","b","c","a","e","a","g")
print("Tuples : ",Tuples)
#Method
print("***********Method 1 (count)***********")
print("count alphabet \"a\" : ",Tuples.count('a'))
print("***********Method 2 (index)***********")
print("Position alphabet \"e\" in index : ",Tuples.index("e"))
