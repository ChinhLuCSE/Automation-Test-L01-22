<div align="center">
    <h2>Automation test website <span><a href="https://school.moodledemo.net/">Moodle</a> </span>
    </h2>
</div>

## 📦 Installation

```
git clone https://github.com/ChinhLuCSE/Automation-Test-L01-22.git
cd Automation-Test-L01-22
python3 -m venv env
source env/bin/activate
pip install -r ./requirements.txt
```

## 🚀 Usage

Go to `src` folder and run the following commands

> Install webdriver package

```sh
python3 -m pip install webdriver-manager --upgrade

python3 -m pip install packaging
```

> Test export calendar

```sh
python run.py test ExportCalendarSuite
```

> Test create event

```sh
python run.py test CreateEventSuite
```

- Read the testcases in folder `testcases`
- Read the result of test in folder `solutions`

Create testcases by changing value in files `ExportCalendarSuite.py` and `CreateEventSuite.py`
