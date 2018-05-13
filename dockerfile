FROM python:2-onbuild
RUN mkdir /run/wechat
WORKDIR /run/wechat
COPY . .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
CMD [ "python", "__main__.py" ]