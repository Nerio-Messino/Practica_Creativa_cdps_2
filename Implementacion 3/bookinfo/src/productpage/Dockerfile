FROM python:3
# Install git
RUN apt-get update && apt-get install git
RUN git clone https://github.com/Nerio-Messino/Repositorio_Instancias.git
WORKDIR /Repositorio_Instancias
RUN pip3 install -r ./bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "./bookinfo/src/productpage/productpage.py", "9080"]