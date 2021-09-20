# Test_task_for_Tensor
Some autotests for Yandex (Selenium, Pytest).

Did this with PageObject pattern.

For running my tests:

1) Download files from this repository
2) Install all files from requirements.txt(pip install -r requirements.txt) in your shell
3) Write in your terminal: "pytest -s --tb=line --count x test_yandex_search_and_images.py" (without quotes ofc),where x is the number of runs of each test
4) Enjoy!

I'm gonna be so Thankful for your feedback!

email: ilienko030203@gmail.com

Phone: 8 (906) 909-03-49





P.S. Я понимаю, что плохо сделал 7-8 шаг во втором тест-кейсе, объединив шаги, так как тест получился не атомарным.
Но, я не придумал, как по другому делать проверку на соответствие картинки из 8 шага и из 6(Без объявления переменной как глобальной и без занесения ее в атрибуты класса)
.Также пытался сделать проверку через значение атрибута src у картинки, но с вероятностью +- 0.2 вылезала ошибка.
