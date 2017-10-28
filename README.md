### The machine search developed in python.  :snake:

## The application is about organization and retrieval of txt's documents. 
You can inject your documents on folder and the code retun yours results search in order.
![alt text](https://github.com/Phelipesilva/ORI/blob/master/image-rename/img1.png)

1. [Instalation.](#instalation)
2. [Edit for use.](#edit-for-use)
3. [How I Execute.](#execute)



### Instalation.

Before clone this repository, for use this code you have Let's first install python3, pip and flask.

How install python3 on Linux:

Ubuntu/Debian
```
sudo apt-get install python3
```

Arch
```
pacman -S install python3
```


How install pip3 on Linux:

Ubuntu/Debian
```
sudo apt-get install python3-pip
```

Arch
```
pacman -S install python3-pip
```

How install Flask on Linux:

Ubuntu/Debian
```
sudo pip3 install flask
```

Arch
```
sudo pip3 install flask
```


### Edit for use.

1. Add yours documents on folder ./docs.
  - your documents must are type of txt.

2. Rename yours document with n(number of document) starting n=1.
  - Ex: 1.txt;2.txt;(...);n.txt.
You can add n document's, but it will slow down.

3. Edit line on document .py in /ORI/Main.py.
  - QNT     = 10 (add your number of documents)   # Quantidade de Documentos

### Execute.

Open the terminal on folder.Write

```
python3 Main.py
```

Open your browser. Write on input.

```
127.0.0.1:5000
```

Write on input website and click in search.