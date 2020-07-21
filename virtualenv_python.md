##### Виртуальное окружение python
Для начала глобально установим python3.7. Запоминать нет смысла, делаем по инструкции:

https://pyneng.github.io/docs/python-3-7/

Зачем виртуальные окружения:
- версия python уникальна в пределах окружения;
- библиотеки и зависимости каждого отдельного проекта будут уникальны в пределах виртуального окружения;
- pip также уникален для виртуального окружения, а, соответственно, и все пакеты, установленные через pip

Способы для Ubuntu 19.04:

1. Virtualenv + virtualenvwrapper

Эти инструменты входят в стандартную библиотеку Python (PyPi) и доступны для установки через pip. Можно пользоваться только virtualenv, а можно добавить обертку к virtualenv (virtualenvwrapper). Этот способ актуален для любой версии python.
Устанавливаем virtualenv:

`pip install virtualenv`
 
Для создания виртуального окружения используем:

`virtualenv pyneng-py3-1`

Для создания виртуального окружения с python3 используем:

`virtualenv -p /usr/bin/python3 pyneng-py3-1`
 
*pyneng-py3-1/bin/* – содержит скрипты для активации/деактивации окружения, интерпретатор Python, используемый в рамках данного окружения, менеджер pip и ещё несколько инструментов, обеспечивающих работу с пакетами Python.

*pyneng-py3-1/include/ *и *pyneng-py3-1/lib/ *– каталоги, содержащие библиотеки. Новые пакеты будут установлены в каталог *pyneng-py3-1/lib/pythonX.X/site-packages/*.

Запускаем окружение:

`source pyneng-py3-1/bin/activate`

Проверяем, что pip и python работают в контейнере, а также версию python:
```
which pip
which python
python -V
```

Выключаем виртуальное окружение:

`deactivate
`

В работе мы точно не будем ограничены одним виртуальным окружением, поэтому нам нужен инструмент для удобного управления окружениями:

`pip install virtualenvwrapper`

Ищем virtualenvwrapper.sh:

```
which virtualenvwrapper.sh
/usr/local/bin/virtualenvwrapper.sh
```

Теперь создадим директорию для будущих проектов:

`mkdir virtenvs`

Сделаем, чтобы bash-скрипт virtualenvwrapper запускался при старте системы с определенными параметрами:
```
sudo nano ~/.bashrc
## where to store our virtual envs
export WORKON_HOME=$HOME/virtenvs
# where projects will reside
export PROJECT_HOME=$HOME/Projects-Active
# where is the virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh
```
Рестартуем bash:

`exec bash`

или 

`source ~/.bashrc`

Теперь создаем виртуальные окружения и сразу указываем нужную нам версию python:
для python3:

`mkvirtualenvwrapper -p /usr/bin/python3 pyneng-py3-1`

или

`mkvirtualenv -p /usr/local/bin/python3.7 pyneng-py3-1`

для python2:

`mkvirtualenv pyneng-py2-1`

Проверяем:

`workon`

Видим весь список наших окружений. Находятся они в директории virtenvs.
Переключаемся между окржениями:

`workon pyneng-py3-1`

Проверяем версии прежним способом:
```
which pip
which python
python -V
```

Выход из окружения осуществляется прежним методом:

`deactivate`

В пределах окружения используется только одна версия python, поэтому нет необходимости каждый раз указывать версию при обращении к python. Пишем просто python.

Удаляются окружения с помощью:

`rmvirtualenv pyneng-py3-1`

В окружении можно установить ipython, это нестандартный интерпретатор python. Просто удобнее.

2. pyvenv (venv)

Работает только с 3 python, но прост в использовании:
Не входит в PyPi, поэтому инсталим так:

`sudo apt install python3-venv`

Создаем виртуальное окружение:

`/usr/bin/python3 -m venv pyneng-py3-1`

Запускаем виртуальное окружение:

`source pyneng-py3-1/bin/activate`

Выключаем:

`deactivate`

Полезные ссылки:
- [из самого курса](https://pyneng.readthedocs.io/ru/latest/book/01_intro/virtualenv.html)
- [pyvenv](https://ti-tech.ru/useful/virtual-environment-python3-ubuntu/)
- [virtualenv linux + windows](https://devpractice.ru/python-lesson-17-virtual-envs/)
- [virtualenv linux](https://djbook.ru/examples/85/)
- [способы создания виртуального окружения на stackoverflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
