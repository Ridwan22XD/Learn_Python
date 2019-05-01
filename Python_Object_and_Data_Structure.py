
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
#formatting
print("***********formatting***********");
print("This is a string {}\".format(\"INSERT\") --> ","This is a string {}".format("INSERT"));
print("The {} {} {} \".format(\"fox\",\"brown\",\"quick\") --> ","The {} {} {} ".format("fox","brown","quick"));
print("The {2} {0} {1} \".format(\"fox\",\"brown\",\"quick\") --> ","The {2} {0} {1} ".format("fox","brown","quick"));
print("The {b} {q} {f} \".format(f=\"fox\",b=\"brown\",q=\"quick\") --> ","The {b} {q} {f} ".format(f="fox",b="brown",q="quick"));
print("\n\n");












