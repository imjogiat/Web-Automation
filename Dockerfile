FROM python:3.9

ADD  main.py .

RUN pip install selenium

RUN pip install webdriver_manager

COPY chromedriver.exe chromedriver.exe

COPY start.sh start.sh

RUN chmod +x start.sh

CMD ["/start.sh"]