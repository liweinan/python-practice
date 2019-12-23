安装`pipenv`：

```bash
$ pip install pipenv
```

安装本项目的依赖包：

```bash
$ pipenv install
```

进入到`pipenv`提供的虚拟环境：

```bash
$ pipenv shell
Launching subshell in virtual environment…
 . /Users/weli/.local/share/virtualenvs/python-practice-rOVm0gl7/bin/activate
$  . /Users/weli/.local/share/virtualenvs/python-practice-rOVm0gl7/bin/activate
(python-practice) $
```

试着执行其中的代码：

```bash
(python-practice) $ python structbuf.py
Original: (1, b'ab', 2.7)

ctypes string buffer
Before : b'000000000000000000000000'
After   : b'0100000061620000cdcc2c40'
Unpacked: (1, b'ab', 2.700000047683716)

array
Before : b'000000000000000000000000'
After   : b'0100000061620000cdcc2c40'
Unpacked: (1, b'ab', 2.700000047683716)
(python-practice) $
```






