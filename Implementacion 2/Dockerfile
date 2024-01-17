FROM python:3.7.7-slim
RUN git clone https://github.com/Nerio-Messino/Repositorio_Instancias.git
WORKDIR Repositorio_Instancias
ENV GROUP_NUMBER 'Grupo 03'
RUN pip3 install -r Repositorio_Instancias/bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith.py", "9080"]
