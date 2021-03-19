# Servel
Es una herramienta que provee metodos para procesar los PDF del Padron Electoral de Chile, y dejarlo como CSV

Desde aqui
<img src="https://raw.githubusercontent.com/DiegoIdeas/Servel/main/Raw.PNG" style="float: left; margin-right: 10px;" />
hasta 
<img src="https://raw.githubusercontent.com/DiegoIdeas/Servel/main/Cleaned.PNG" style="float: left; margin-right: 10px;" />
y finalmente a CSV

### Disclaimer

Este proyecto pretende mostrar los problemas en la privacidad de datos. En particular, el fácil acceso de los datos entregados por Servel, los cuales se enmarcan dentro de la ley 18.556 sobre inscripciones electorales y servicio electoral. El uso que ud. haga de esta información es bajo su exclusiva responsabilidad. La ley impide que se haga cualquier uso comercial de estos datos. Por lo tanto, si desea venderlos, está cometiendo un delito. El código se entrega "as is", no hay soporte, y no hay cobro por descargar esto.

### Historia

Por cada elección, candidatura, el servicio electoral, publica en la red una serie de PDFs, que contiene la nomina
de personas, seccionado en comunas.
Este año como novedad incluye los pueblos indigenas

| NOMBRE                              | C.IDENTIDAD  | SEXO  | DOMICILIO ELECTORAL | CIRCUNSCRIPCIÓN | MESA | PUEBLO INDÍGENA |
|-------------------------------------|--------------|-------|---------------------|-----------------|------|-----------------|
| paterno materno primero segundo     | 11.111.111-9 | VARON | LOS PANTALONES #345 | ARICA           | 33V  | AIMARA          |
| paternox maternox primerox segundox | 5.555.555-7  | MUJER | LOS VESTIDOS #777   | PTA ARENAS      | 5    |                 |


### Barreras

Files = estan repartidos en archivos, con distintos numeros de pagina, y comunas.

Block = tiene una encryptacion, que impide su lectura directa.

Watermark = tiene un molesto sello de agua, que a la hora del parse afecta a los datos.

Formats = cada año, separan los inahabilitados, los del extranjero, y obviamente los habilitados, al tener mas o menos campos hacen diferente su procesamiento

### Dependencias Externas

QPDF, herramienta con la que se liberan las restricciones de lectura
JAVA JRE, modulo necesario, para procesar los PDF 

Para Ubuntu

> sudo apt install qpdf

> sudo apt install default-jre

Para Windows

colocar [qpdf.exe](https://github.com/qpdf/qpdf/releases) `qpdf-10.3.1-bin-mingw64.zip` y sus dependencias en el directorio raiz del proyecto
e instalar java jre 8 o la mas actual 

### Notas Importantes

1. Archivo de configuracion de rutas config.py
2. un modo de prueba que debera ser desactivado con test_mode = 0 dentro de config.py
3. Para windows powershell es necesario activar `execution-policy unrestricted` o una politica un poco menos permisiva
4. El proceso tras iteraciones ocupa como 20GB, la base de datos resultante es de 2 GB
5. Se realizaron mejoras como el separar nombres en paterno, materno, primero, segundo
6. La ejecucion esta diseñada para hacerse en paralelo, por tantos core como sea posible, llama librerias que ocuparan toda la memoria y el procesador, las del borrado de la marca de agua y la del parseo sobretodo.



### Instalación

Requerimiento oficial python3.7

1.  *Crear Ambiente Virtual*<br/>
    Detectar el python<br/>
    `python -V` o `python3 -V` o `python3.X -V` reemplazando la X por la version que se tenga instalada con el comando en que resulte se vera la version completa de python.<br/>
    > ***python\<version\> -V***
        
    Crear ambiente virtual (Mantener la versión en mente)
    Cambiar nombre_corto por ejemplo componente, el git ignora los directorios con la estructura venv_<nombre_corto><br/>
    `pyvenv` quedo deprecada a partir de python 3.6 en adelante [Referencia](https://docs.python.org/es/3/library/venv.html).
    > ***python\<version\> -m venv venv_\<nombrecorto\>***

2.  *Activar Ambiente Virtual*<br/>
    Posicionarse un directorio arriba de venv_<nombre_corto> en el directorio actual al hacer un `ls` debe estar venv_<nombre_corto> con esto aparecerá (venv_<nombre_corto>) en el principio de su terminal indicando así que el ambiente virtual fue activado<br/>
    
    <br/>linux<br/>
    
    > ***source venv_\<nombre_corto\>/bin/activate***<br/> 
    
    <br/>windows<br/>
    
    > ***venv_\<nombre_corto\>/Scripts/activate.ps1***<br/>
    
    > ***python -m ensurepip***
 
3.  *Upgradear pip*<br/>
    Repetir este paso hasta que pip sea 21.0 o superior en sistemas antiguos parte en 9 con el primer pgrade llega 20 y del 20 se salta al 21.
    
    <br/>linux<br/>
    
    > ***pip install --upgrade pip***<br/>
    
    <br/>windows<br/>
    
    > ***python -m pip install --upgrade pip***<br/>

4.  *Instalar requerimientos*<br/>
    
    > ***pip install -r requirements.txt***<br/>
     
5.  *Ejecutar codigo, para ver opciones disponibles*<br/>
    Desde ahora python se llama sin indicar version para el ambiente virtual
    
    > ***python toolkit.py -h***

6.  *opciones de ejecucion*<br/>

    download = descarga de PDFS ( ojo con test_mode = 1 ) limitara la cantidad de archivos<br/>
    
    unlock = libera los pdfs<br/>
    
    clear = remueve marca de agua<br/>
    
    parse = transforma los PDF en CSV<br/>
    
    y hay muchas más... ver toolkit para más modos<br/> 
    
    > ***python toolkit.py -a download***
    
<img src="https://raw.githubusercontent.com/DiegoIdeas/Servel/main/poc.PNG" style="float: left; margin-right: 10px;" />
