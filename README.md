# pilates
1. Anaconda python 설치

2. 가상환경 생성 및 실행

```python
conda create --name ${가상환경이름} python=3.7 anaconda
conda activate ${가상환경이름}
```
   
3.  패키지 설치

- 사용한 패키지와 버전을 `requirements.txt`에 명시

```python
pip install -r requirements.txt
```

4. 프로젝트 생성하기(이미 생성되어 있으므로 생략)
```python
django-admin startproject config .
```  

5. 서버구동

```python
python manage.py runserver
```

6. 새로운 앱 생성하기 (예시는 게시판)

```python
django-admin startapp board
```

7. 장고로 앱 만들고 최초 실행시 데이터베이스 생성을 위해 다음 명령어를 수행한다.

```python
django-admin migrate
```

8. 장고 관리자를 사용하기 위해서는 장고 관리자 화면에 접속할 수 있는 슈퍼유저(superuser)를 먼저 생성해야 한다. 생성명령어는 다음과 같다.
```python
python manage.py createsuperuser
```

9.  장고 ORM 모델로 migration 작업파일을 생성하는 명령어는 다음과 같다.
```python
python manage.py makemigrations [app_name]
```
뒤에 app_name을 입력하면 해당 app에 대해서만 마이그레이션을 생성하고 app_name을 생략하면 전체 app에 대해서 마이그레이션을 생성

10.  migration 작업파일을 적용하는 명령어는 다음과 같다.
```python
python manage.py migrate [app_name] [migration_name]
```
makemigrations와 같이 app_name을 지정해서 특정 app만 migrate 할 수 있으며 app_name 뒤에 마이그레이션 파일의 이름을 지정하면 해당 번호(버전)의 마이그레이션을 적용(이전버전으로 되돌리기도 가능)


11.  프로젝트의 마이그래이션 적용여부를 확인하는 명령어
```python
python manage.py showmigrations [app_name]
```

12. 데이터베이스 생성 후 django ORM모델로 생성하는 명령어
```python
python manage.py inspectdb > [app_name]/models.py --database 'external' #config/settings.py에 설정된 데이터베이스 이름. java의 JNDI 이름과 비슷하게 생각하면 된다., --database 옵션은 두개이상의 데이터베이스를 사용할 때만 사용한다.
```
* 주의점
  ## 외부 테이블의 Primary Key 를 제대로 못 가져오는 경우가 있다. 그런 경우에는 생성된 모델의 필드에 primary_key=True 를 추가해주면 된다.
  ## 불러온 외부 테이블 구조를 변경하고 싶다면 Meta 클래스의 managed=False 를 managed=True 로 변경해주면 된다.
  ## 몇몇 부분들은 수작업으로 수정해주어야 한다.
