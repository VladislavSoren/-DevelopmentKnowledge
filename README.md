## Базовые знания по разработке

### Принципы качественной разработки
Источник: https://habr.com/ru/companies/itelma/articles/546372/


1. **YAGNI** (You Aren’t Gonna Need It / Вам это не понадобится)  
Если пишете код, то будьте уверены, что он вам понадобится. Не пишите код, если думаете, что он пригодится позже. 
Если код снова понадобятся – вы сможете воспользоваться git-репозиторием, чтобы воскресить его из мертвых.
---

2. **DRY** (Don’t Repeat Yourself / Не повторяйтесь)  
Идея вращается вокруг единого источника правды (single source of truth — SSOT).  
SSOT – это практика структурирования информационных моделей и схемы данных, 
которая подразумевает, что все фрагменты данных обрабатываются (или редактируются) только в одном месте.  
В большинстве случаев дублирование кода происходит из-за незнания системы.  
Прежде чем что-либо писать, проявите прагматизм: осмотритесь. Возможно, эта функция где-то реализована. 
Возможно, эта бизнес-логика существует в другом месте.  
Повторное использование кода – всегда разумное решение.
---

3. **KISS** (Keep It Simple, Stupid / Будь проще)  
Принцип гласит, что простые системы будут работать лучше и надежнее.  
Применительно к разработке ПО он значит следующее – не придумывайте к задаче более сложного решения, 
чем ей требуется.  
Иногда самое разумное решение оказывается и самым простым.   
Написание производительного, эффективного и простого кода – это прекрасно.
---

4. **Big Design Up Front** (Глобальное проектирование прежде всего)  
Прежде чем переходить к реализации, убедитесь, что все хорошо продумано.
Зачастую продумывание решений избавляло нас от проблем при разработке…  
Внесение изменений в спецификации занимало час или два. Если бы мы вносили эти изменения в код,  
на это уходили бы недели.  
Составив план, вы избавите себя от необходимости раз за разом начинать с нуля.
---

5. **SOLID**
- `Single-responsibility principle /Принцип единственной ответственности`  
Каждый объект, класс и метод должны отвечать только за что-то одно.  
Если ваш объект/класс/метод делает слишком много, вы получите спагетти-код.  
Еще один побочный эффект такого кода – проблемы с тестированием.  
Запутанный функционал тестировать сложно.

- `Open–closed principle / Принцип открытости-закрытости`  
Программные объекты должны быть открыты для расширения, но закрыты для модификации.  
Речь о том, что `НЕЛЬЗЯ` переопределять методы или классы, просто добавляя дополнительные функции  
по мере необходимости.  
Хороший способ решения этой проблемы – использование наследования.

- `Liskov substitution principle / Принцип подстановки Лисков`  
Этот принцип гласит, что объекты старших классов должны быть заменимы объектами подклассов,  
и приложение при такой замене должно работать так, как ожидается.
Наследующий класс должен дополнять, а не замещать поведение базового класса.

- `Interface segregation principle / Принцип разделения интерфейсов`  
Объекты не должны зависеть от интерфейсов, которые они не используют.
ПО должно разделяться на независимые части. Побочные эффекты необходимо сводить к минимуму,  
чтобы обеспечивать независимость.  
Убедитесь, что вы не заставляете объекты реализовывать методы, которые им никогда не понадобятся.

- `Dependency inversion principle / Принцип инверсии зависимостей`  
Этот принцип невозможно переоценить. Мы должны полагаться на абстракции, а не на конкретные реализации.  
Компоненты ПО должны иметь низкую связность и высокую согласованность.  
Заботиться нужно не о том, как что-то устроено, а о том, как оно работает.  
Простой пример – использование дат в JavaScript. Вы можете написать для них свой слой абстракции.  
Тогда если у вас сменится источник получения дат, вам нужно будет внести изменения в одном месте, а не в тысяче.
`Формулировка`:  
-- Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.  
-- Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.  
Объяснение: https://www.youtube.com/watch?v=ZS1klrs6g-4
---

6. **Avoid Premature Optimization** (Избегайте преждевременной оптимизации)  
Поймите правильно, предвидеть, что произойдет что-то плохое – это хорошо.  
Но прежде чем вы погрузитесь в детали реализации, убедитесь, что эти оптимизации действительно полезны.  
Очень простой пример – масштабирование. Вы не станете покупать 40 серверов из предположения,  
что ваше новое приложение станет очень популярным. Вы будете добавлять серверы по мере необходимости.
Преждевременная оптимизация может привести к задержкам в коде и, следовательно,  
увеличит затраты времени на вывод функций на рынок.  
Многие считают преждевременную оптимизацию корнем всех зол.
---

7. **Бритва Оккама** (ле́звие О́ккама)  
«Не следует множить сущее без необходимости» (либо «Не следует привлекать новые сущности  
без крайней на то необходимости».  
Не создавайте ненужных сущностей без необходимости. Будьте прагматичны — подумайте, нужны ли они,  
поскольку они могут в конечном итоге усложнить вашу кодовую базу.

### Абстрактные классы/методы
Источник: https://sky.pro/media/raznicza-mezhdu-abstraktnym-klassom-i-interfejsom-v-python/  
`Абстрактный класс` — это класс, который не может быть инстанциирован, то есть нельзя создать его экземпляр.  
Он представляет собой шаблон или чертеж для создания других классов.  
Абстрактный класс может содержать абстрактные методы (методы без реализации) и/или обычные методы.  
_Пример абстрактного класса:_  
```
from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    @abstractmethod
    def do_something(self):
        pass
```
В этом примере AbstractClassExample — это абстрактный класс, который содержит абстрактный метод do_something.   
Этот метод должен быть обязательно реализован в любом классе, который наследует AbstractClassExample

`Интерфейс`. В Python нет встроенной поддержки интерфейсов, как это есть, например, в Java.  
Однако концепцию интерфейса можно реализовать с помощью абстрактного класса,  
в котором все методы являются абстрактными.  
_Пример интерфейса:_  
```
from abc import ABC, abstractmethod
 
class InterfaceExample(ABC):
 
    @abstractmethod
    def method1(self):
        pass
 
    @abstractmethod
    def method2(self):
        pass
```
В этом примере `InterfaceExample` — это интерфейс, который содержит два абстрактных метода: `method1` и `method2`.  
Любой класс, который наследует `InterfaceExample`, должен реализовать оба этих метода.  
Важно понимать, что принципиальное отличие между абстрактным классом и интерфейсом заключается в том,  
что абстрактный класс может иметь как абстрактные, так и неабстрактные методы,  
тогда как интерфейс содержит только абстрактные методы.  
Следовательно, абстрактный класс можно использовать для создания общей функциональности для группы связанных классов,  
а интерфейс — для определения общего поведения группы классов, возможно, не связанных между собой.


































