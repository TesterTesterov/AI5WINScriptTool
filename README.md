# AI5WINScriptTool
## English
 Dual languaged (rus+eng) tool for decompiling and compiling scripts .mes from the visual novel's engine AI5WIN. Very incomplete list of games on this engine you can find [on vndb](https://vndb.org/r?q=&o=a&s=title&f=fwAI5WIN-). With it thou can fully edit all the code, not just strings. Thou can add message breaks and change scenarios without restrictions!
 Mes script files can be used not just in AI5WIN, but also in AI6WIN and Silky Engine. For assembling and disassembling mes script files of AI6WIN use [AI6WINScriptTool](https://github.com/TesterTesterov/AI6WINScriptTool), for mes of Silky Engine use [mesScriptAsseAndDisassembler](https://github.com/TesterTesterov/mesScriptAsseAndDisassembler).
 
 Also you may want to pack and unpack archives of AI5WIN. For it use [AI5WINArcTool](https://github.com/TesterTesterov/AI5WINArcTool).

Definations: "#0-" are "free bytes", "#1-" are commands (and "\[...]" are arguments below), "#2-" are labels.

**Supported versions** *(list may not include all existing versions)*:
- 0 - in oldest games (before 2000);
- 1 - in main chunk of games (2000-2003(5));
- 2 - in the oldest games (after 2003(5)).

## Русский
 Двуязычное (рус+англ) средство для декомпиляции и компиляции скриптов .mes движка визуальных новелл AI5WIN. С неполным списком игр на нём вы можете ознакомиться [на vndb](https://vndb.org/r?q=&o=a&s=title&f=fwAI5WIN-). С ним вы можете полностью редактирвоать код, а не только строки; по вашему повелению добавлять разрывы между сообщений и даже менять сценарии по своему замыслу!
  Скрипты с расширением "mes" используются не только в AI6WIN, но также и в AI6WIN с Silky Engine. Чтобы дизассемблировать и ассемблировать скрипты движков AI6WIN и Silky Engine, используйте иные средства -- [AI6WINScriptTool](https://github.com/TesterTesterov/AI6WINScriptTool) и [mesScriptAsseAndDisassembler](https://github.com/TesterTesterov/mesScriptAsseAndDisassembler) соответственно.
 
 Также вам может понадобиться распаковывать и паковать архивы движка AI5WIN. Для сего используйте средство [AI5WINArcTool](https://github.com/TesterTesterov/AI5WINArcTool).
  
 Определения: "#0-" есть "вольные байты", "#1-" есть команды (и под ними "\[...]" аргументы), "#2-" есть метки.
 
**Поддерживаемые версии** *(список может не включать все существующие версии)*:
- 0 - в старейших играх (до 2000);
- 1 - в основной массе игр (2000-2003(5));
- 2 - в старейших играх (после 2003(5)).

 # Usage / Использование
## English
![image](https://user-images.githubusercontent.com/66121918/147504688-df9a4c38-1302-4d67-9ba8-57450d611700.png)
1. Choose the mode, file or directory. In first mode you will work with one .mes - .txt pair, in second -- with all files in a pair of directories.
2. Enter a name of the .mes file in the top entry (do see, with extension) or the directory name. Thou can also enter relative or absolute path. You can also click on "..." to choose.
3. Enter a name of the .txt file (do see, with extension) or the directory name. Thou can also enter relative or absolute path. You can also click on "..." to choose.
4. Choose the script version.
5. To decompile push the button "Decompile".
6. To compile push the button "Compile".
7. Status will be displayed on the text area below.

## Русский
![image](https://user-images.githubusercontent.com/66121918/147504673-fe7689ee-131a-45a9-bf08-412775c9bd88.png)
1. Выберите режим: файл или директорию. В первом вы будете работать с парой .mes - .txt, во втором -- со всеми файлами в паре директорий.
2. Введите название файла .mes в верхней форме (заметьте, с расширением) или имя директории. Также можно вводить относительный или абсолютный до него путь. Также вы можете нажать на кнопку "...", чтобы выбрать.
3. Введите название файла .txt в нижней форме (заметьте, с расширением) или имя директории. Также можно вводить относительный или абсолютный до него путь. Также вы можете нажать на кнопку "...", чтобы выбрать.
4. Выберите версию скрипта.
5. Для декомпиляции нажмите на кнопку "Декомпилировать".
6. Для компиляции нажмите на кнопку "Компилировать".
7. Статус сих операций будет отображаться на текстовом поле ниже.

# Tested on / Протестировано на
## English

- [Koihime](https://vndb.org/v2347).
- [Shangrlia](https://vndb.org/v3182) ([Elf Classics](https://vndb.org/r5220)).
- [Shangrlia 2](https://vndb.org/v3183) ([Elf Classics](https://vndb.org/r5220)).
- [Kono Yo no Hate de Koi o Utau Shoujo YU-NO](https://vndb.org/v1377) ([Elf Classics](https://vndb.org/r5220)).
- [Shangrlia](https://vndb.org/v3182) ([Shangrlia Multipack](https://vndb.org/r6255)).
- [Shangrlia 2](https://vndb.org/v3183) ([Shangrlia Multipack](https://vndb.org/r6255)).

## Русский

- [Принцесса любви](https://vndb.org/v2347).
- [Шангри-ла](https://vndb.org/v3182) ([Классика от Elf](https://vndb.org/r5220)).
- [Шангри-ла 2](https://vndb.org/v3183) ([Классика от Elf](https://vndb.org/r5220)).
- [Ю-НО, девушка, что воспевает любовь на краю нашего света](https://vndb.org/v1377) ([Классика от Elf](https://vndb.org/r5220)).
- [Шангри-ла](https://vndb.org/v3182) ([Шангли-ла: Комплексный пакет](https://vndb.org/r6255)).
- [Шангри-ла 2](https://vndb.org/v3183) ([Шангли-ла: Комплексный пакет](https://vndb.org/r6255)).

# Some useful function / Некоторые полезные функции
## English
There is one nasty problem. One you can encouter almost every time you work on fantranslation of game on this engine. And this is... lack of breaks! Not only AI5WIN's messagebox can contain too few symbols, this engine itself cannot print too many at once. But my tool, unlike some shabby string replacers, allows you to edit code fully and therefore solve all problem with breaks. This section also contains some other functions you may find useful.
Do note, methods here may not work on some script version.



## Russian
Есть одна неприятная проблема, с коей чуть ли не каждый раз столкнуться можно, когда работаешь над фанатским переводом игры на данном движке. Что же за проблема, спросите вы? Ответ же... недостаток переносов! Более того, в AI5WIN не просто не влезают сообщения, данный движок просто не может выводить слишком много символов за раз. Но моё средство, в отличии от всяких потрёпанных редакторов строк, позволяет вам полностью редактировать код. А, значит, и решить проблемы с переносами. Кроме того, в данной секции описывается ряд других полезных функций.
Заметьте, указанные здесь методы могут не работать во всех версиях скриптов.

