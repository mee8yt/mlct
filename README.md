# MLCT ✨
**MLCT** *(**M**ine**L**and **C**ode **T**ranslator)* (эм эл кэ тэ) - Мод, для установки письменного варианта блочного кода на сервере Mineland.

## Содержание 🗂️

Этот репозиторий только для компилятора

1. [Установка](#установка-)
2. [Синтаксис](#синтаксис-)
3. [Документация](#документация-)
4. [Примеры](#примеры-)
5. [Подсветка кода](#подсветка-кода-)

# Установка 🤙

1. Необходимо иметь Python версии не ниже 3.11.1 \(Установить можно [тут](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)\)
2. Откройте раздел [релизов](https://github.com/mee8yt/mlct-compiler/releases/latest ) и нажмите "Download ZIP"
3. Распакуйте архив
4. Запустите `Setup.py`

> [!IMPORTANT]
> Без Python вы банально не сможете скомпилировать ваш код
>[!NOTE]
> После установки не перемешайте папку с компилятором, не меняйте и не удаляйте исходные файлы компилятора
# Синтаксис 💻

> [!NOTE]
> Перед использованием `MLCT` следует знать его синтаксис.

Типы данных:
```js
123          // Числовое значение
"Текст"      // Текстовое значение
`Переменная` // Переменная / сложное значение
```

Если перед переменной поставить букву(ы), то переменная может превратиться в сложное значение:
```js
`Переменная`                    // Так и осталось
s`Сохранённая переменная`       // Переменная стала сохранённой
a`Массив`                       // Теперь это массив
as`Массив`                      // Массив тоже умеет сохраняться
l`Местоположение`               // Набор из пяти чисел, или местоположение
v`Значение`                     // Игровое значение, то есть яблочко
i`Предмет`                      // Любой предмет
potion`Зелье`                   // Эффект зелья
particle`Частица`               // Эффект частицы

"Текст"                         // Обычный текст
c"Текстовый компонент"          // Текстовый компонент
cls"Бесцветный текст"           // Символ & не заменится на цветной символ
```

Такая буква (буквы), делающая из одного значение другое называется "оболочка значения" (Value shell).

Однако любые значения надо заполнять с умом. Например, снос текста на новую строку:
```js
"Намеренный снос \
   строки"
```
Учитывайте, что на новой строке не будут учитываться все символы пропуска вплоть до твёрдых букв (табуляции, пробелы, и другие сносы строк).

Так-же стоит учитывать, что если не поставить обратый слеш на конце первой строки, то компилятор посчитает этот текст незавершённым:

```js
"Снос без
слеша" // -> LexerError: Токен STRING со значением "Снос без" не имеет конца
```

Из свободного текста ("слов" не обёрнутых в переменную или текст) и разных типов данных могут рисоваться базовые структуры кодинга. Это обозначения блоков кода и событий, обозначения поршней условий, различные вне-блочные стуктуры, которые упрощают работу напрямую с компилятором. Разберём всё по-порядку.

Установка переменных:
```js
var `test` = 0;
var s`%player% money` = 0;
```
Установка переменной таким образом называется вне-блочной конструкцией, позже поймёте почему

Вызов действий:
```js
player.send("Привет!");
```

Эта строка кода описывает "Действие игрока - Отправить сообщение"

Теперь разберём строение этой строки кода:

```js
   player.send("Привет!");
// ^^^^^^
// Блок

player.send("Привет!");
//    ^
//    Разделитель

player.send("Привет!");
//     ^^^^
//     Имя действия

player.send("Привет!");
//          ^^^^^^^^^
//          Аргументы

player.send("Привет!");
//                    ^
//                   Конец блока
```

> [!IMPORTANT]
>Каждый блок кода должен оканчиваться знаком ";" (точка с запятой)

То есть блочной конструкцией является это: `блок.вид(аргументы);`, а вне-блочная конструкция это: `операция цель: аргументы;` (например *var*)

На очереди заполнение аргументов блоков

Например возьмём действие "Отправить титул". У него есть аргументы "text1, text2, number1, number2, number3". Их можно указать разными способами:

*Позиционный:*
```js
player.title("Привет", "Это мой мир", 20, 20, 20);
```

*По имени:*
```js
player.title(text1="Привет", number1=0);
```
*Комбинированный:*
```js
player.title(text1="Привет", "Это мой мир");

//Позиционные аргументы устанавливаются на следующее неустановленное значение:
player.title(number2=5, "Привет", "Это мой мир"); // Тоже самое, что (text1="Привет", text2="Это мой мир", number2=5);
```

Аргументы бывают двух видов: значение и переключатель. Переключатели задаются числом, которое отражает количество нажатий по переключателю:
```js
player.send(["Вы прошли паркур", "Хотите ещё раз? /play"], 2); // Переключатель нажмётся 2 раза, и будет "разделение на строки".
```

Аргументы, которые отражают значение могут принимать сразу много значений, для этого используется "список значений". В квадратных скобках `[]` через запятую устанавливаются несколько значений для одного аргумента
```js
player.send(["Игрок лайкнул игру", "Хочешь так-же? /like"]);
```

У действий есть селекторы (когда нажимаешь по табличке ШИФТ + ПКМ):
```js
player.send<all>("&fИгрок &e%player%&f зашёл в игру!");
```
>[!WARNING]
>Селекторы можно ставить только *перед* круглыми скобками


Теперь научимся писать код, посмотрим на события и условия:
```js
PlayerEvent(join) {
   player.send<all>("&fИгрок &e%player%&f зашёл в игру!");
   ifPlayer.havePermissions() {
      player.setGamemode(3);
   }
   game.startLoop("random_item");
}

Loop(random_item, 100) {
   player.giveRandomItem<all>(i`diamond`, i`emeralnd`, i`stone`);
}
```

>[!WARNING]
>Для циклов, функций и событий, у которых имя содержит пробелы используются спец. символы ``
>
>Например, если функция или цикл называется "анти гм", то в строке Loop() или Function()
> имя пишется так: \`анти гм\`

У условий и выборок тоже есть селекторы, и не только:

```js
ifPlayer.nameEquals<not><selected>("Mee8YT") {
    select.player.ifPlayer.gamemodeEquals(2);
    player.setGamemode<selected>(1);
} 
```

>[!NOTE]
>Параметр `<not>` ставит стрелочку НЕ на условиях и выборке, и он также ставится перед круглыми скобками

>[!TIP]
>Для условий можно комбинировать селектор и инверсию условия, и не важно в каком порядке они были указаны

Для оптимизации и повышения читабельности кода можно использовать переменные среды (или **константы**).

Это переменные, которые доступны только для компилятора, и которые не требуют дополнительных блоков "Присв. Переменную":
```js
const message = "Очень длинный текст"; // Создаём константу

PlayerEvent(join) {
    player.send(@env(message));
} 
```

>[!IMPORTANT]
>Константу можно установить только вне линии кода

Константы могут хранить целый список значений::
```js
const items = [i`diamond`, i`emerald`];
```

Как вы уже увидели, константа может хранить целый список значений. Их можно использовать по разному:
```js
player.giveItems(@env(items));
player.giveItems([@env(items), i`stone`]);
```

Чтобы не мусорить в файле млкт кода можно хранить их в файле `environments.json`:
```json
{
  "message": {
    "token": "STRING",
    "shell": null,
    "value": "Очень длинный текст"
} 
```
*`code.txt`:*
```js
PlayerEvent(join) {
  player.send(@env(message));
}
```

Константы удобны тем, что они делают код читабельнее, а итоговый вариант траснлируемого кода не будет содержать лишние блоки кода.

**Модули** могут сделать код *ещё читабельнее*. Модулем именуется содержимое любого файла, которое будет скомпилировано в 1 сеанс компиляции. 

Проще говоря, можно разделять код на несколько файлов. Модули можно импортировать и использовать:

```js
// main.txt
import 'module.txt'; // Загружаем модуль

PlayerEvent(join) {}

// module.txt
Function() {}
```
> [!IMPORTANT]
>`import` доступен только вне линий кода. 

При импорте компилятор устанавливает код вместо импорта, и в последствии обрабатывает его.

В модули можно помещать код, и даже создавать константы. Константы, созданные в других модулях могут быть доступны и в других модулях, главное вовремя импортировать иодуль с константами.

Так-же для удобства модули можно импортировать в конце:

```js
import "module.txt" end; // Модуль вставится не вместо import, а якобы в самом конце

```


# Документация 📜
Более подробная информация по всем событиям, условиям и действиям кода.
   - [Активаторы](documentation/activators.md) 
     -  [Событие игрока](documentation/activators.md#событие-игрока---playereventevent--none--)
     -  [Событие мира](documentation/activators.md#событие-мира---worldeventevent--none--)
     -  [Циклы](documentation/activators.md#циклы---loopname-0--none--)
     -  [Функции](documentation/activators.md#функции---functionname--none--)
   - [Действия](documentation/actions.md)
     - [Действие игрока](documentation/actions.md#действие-игрока---playeractionargs-)
     - [Игровое действие](documentation/actions.md#игровое-действие---gameactionargs-)
     - [Установить переменную](documentation/actions.md#установить-переменную---varactionargs-)
     - [Работа с массивами](documentation/actions.md#работа-с-массивами---arrayactionargs-)
     - [Выбрать объект](documentation/actions.md#выбрать-объект---selectaction-)
   - [Условия](documentation/conditions.md)
     - [Если игрок](documentation/conditions.md#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](documentation/conditions.md#если-значение---ifvalueconditionargs--none--)
     - [Если существо](documentation/conditions.md#если-существо---ifentityconditionargs--none--)
     - [Если игра](documentation/conditions.md#если-игра---ifgameconditionargs--none--)
     - [Иначе](documentation/conditions.md#иначе---else--none--)
   - [Значения](documentation/values.md)
     - [Игровое значение](documentation/values.md#игровое-значение---vvalue-)
     - [Местоположение](documentation/values.md#местоположение---lx-y-z-y-p-)
     - [Предмет](documentation/values.md#предмет---imaterial-c-m-)
     - [Частица](documentation/values.md#частица---particlevariant-)
     - [Зелье](documentation/values.md#зелье---vid-d-f-)
   - [Прочее](documentation/other.md)
     - [Константы](documentation/other.md#константы-)
     - [Ошибки](documentation/other.md#ошибки-)
     - [Комментарии](documentation/other.md#комментарии-)
     - [Языковой модуль](documentation/other.md#языковой-модуль-)
# Примеры 📧

Векторное оружие:
```js
PlayerEvent(rightClick) {
   ifPlayer.holdingItem(i`golden_hoe`) {
      ifPlayer.itemHasDelay<not>(i`golden_hoe`) {
         ifVar.notEquals(`%player% vector.status`, 1) {
            player.setDelay(i`golden_hoe`, 10);
            var `%player% vector.status` = 1;
            var `%player% vector.speed` = 0;
            var `%player% vector.particle` = particle`CRIT`;
            var `%player% vector.final_pos` = v`targetBlockLocation`;
            var.setLocation(`%player% vector.pos`, v`location`, y_mode = 1, y = 0.6);
            game.callFunction("gun.vector");
            game.callFunction("gun.raycast");
         }
      }
   }
}

Function(`gun.vector`) {
      @comment("GUN / Create vector", 9, "gun.vector", 13, "Создаёт &3&l&nвектор&f из взгляда.");

      var `%player% vector.pos.ray_coefficient` = 1;
      var.getLocationValue(`%player% vector.pos.yaw`, `%player% vector.pos`, 3);
      var.getLocationValue(`%player% vector.pos.pitch`, `%player% vector.pos`, 4);
      var.radians(`%player% vector.pos.rad(yaw)`, `%player% vector.pos.yaw`);
      var.radians(`%player% vector.pos.rad(pitch)`, `%player% vector.pos.pitch`);
      var.sinus(`%player% vector.pos.sin(yaw)`, `%player% vector.pos.rad(yaw)`);
      var.sinus(`%player% vector.pos.sin(pitch)`, `%player% vector.pos.rad(pitch)`);
      var.cosinus(`%player% vector.pos.cosinus(yaw)`, `%player% vector.pos.rad(yaw)`);
      var.cosinus(`%player% vector.pos.cosinus(pitch)`, `%player% vector.pos.rad(pitch)`);

      var.multiply(`%player% vector.pos.vector_x`, -1, [`%player% vector.pos.sin(yaw)`, `%player% vector.pos.sin(yaw)`, `%player% vector.pos.cosinus(pitch)`, `%player% vector.pos.ray_coefficient`]);
      var.multiply(`%player% vector.pos.vector_y`, -1, [`%player% vector.pos.sin(pitch)`, `%player% vector.pos.ray_coefficient`]);
      var.multiply(`%player% vector.pos.vector_z`, `%player% vector.pos.cosinus(yaw)`, [`%player% vector.pos.cosinus(pitch)`, `%player% vector.pos.ray_coefficient`]);
}

Function(`gun.raycast`) {
   pass;
}

PlayerEvent(takeDamagePlayer) {
   pass;
}
```

# Подсветка кода 💡
тут гайд про вс код
