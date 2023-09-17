# Демонстрационный проект по тестированию главной страницы сайта компании <a target="_blank" href="https://tensor.ru/">"Тензор"</a>

![This is an image](design/images/homepage.png)

### Стек технологий:
<img src="design/icons/python-original-wordmark.svg" height="40" width="40" />
<img src="design/icons/selenium-original.svg" height="40" width="40" />
<img src="design/icons/Allure_Report.png" height="40" width="40" />
<img src="design/icons/jenkins-original.svg" height="40" width="40" />
<img src="design/icons/Selenoid.png" height="40" width="40" />
<img src="design/icons/Telegram.png" height="40" width="40" />

#### Запуск автотеста производится удаленно на сервере <a target="_blank" href="https://selenoid.autotests.cloud/#/">Selenoid</a> при помощи написанной в Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/Ponomarev_IV_Tensor_Test/">джобы</a>.

### Для запуска автотестов необходимо:
- Открыть подготовленную <a target="_blank" href="https://jenkins.autotests.cloud/job/Ponomarev_IV_Tensor_Test/">джобу</a> в Jenkins
- Нажать "Собрать сейчас" в боковом меню

![This is an image](design/images/jenkins_1.png)

#### *После прохождения автотестов можно зайти в Allure Report и посмотреть отчет по тестовому прогону:*
![This is an image](design/images/allure_1.png)

#### *А так же подробно посмотреть результат прохождения каждого отдельного теста:*
![This is an image](design/images/allure_2.png)

### Для мгновенного получения результатов о тестировании настроено автоматическое оповещение через Telegram.
![This is an image](design/images/telegram.png)

### Ниже на видео представлен пример короткого теста на сервере <a target="_blank" href="https://selenoid.autotests.cloud/#/">Selenoid</a>.
![Watch the video](design/video/test.gif)
