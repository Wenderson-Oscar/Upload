# Upload (Consumindo Arquivo)

<img src="pacote_readme/img1.png" alt="exemplo imagem">

> O intuito desse Projeto é carregar um arquivo xlsx, pegar os dados e colocar no banco, e buscar os dados filtrados.

* [Demostração em Vídeo](https://drive.google.com/file/d/16pbhGarpLmSUhkxluq0BqtAS_53I-xN1/view?usp=share_link)

🏫 Atividade acâdemica

## Tecnologias Utilizadas

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">

<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">

## 🚀 Processo de Instalação

Para instalar **Upload**, siga estas etapas:

Linux:
```
git clone https://github.com/Wenderson-Oscar/Upload.git
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

Windows:
```
git clone https://github.com/Wenderson-Oscar/Upload.git
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## ☕ Como Utlizar a Aplicação

Para usar **Upload**, siga estas etapas:

```
python manage.py migrate upload
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

