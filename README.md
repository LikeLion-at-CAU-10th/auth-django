# How To Run
`pip install -r requirements.txt`
실행에 필요한 라이브러러리를 설치합니다.

`python manage.py runserver`
서버를 실행합니다.

`python manage.py createsuperuser`
유저를 생성합니다.

# API
base url: http://localhost:8000
## 로그인 `POST auth/login`
쿠키에 sessionid를 생성합니다.
`sessionid=avj25mkwmjgeqolcg9noimc2pbvo0a5j; Path=/; HttpOnly; Expires=Mon, 15 Aug 2022 16:54:56 GMT;
`
### Request
```
{
    "username": "test",
    "password": "test"
}
```

### Response
**성공**  
**status** 200  
```
{
    "success": true,
    "message": "로그인 성공",
    "data": {
        "id": 1,
        "email": "puang@likelion.org",
        "user_name": "test",
        "first_name": "김",
        "last_name": "멋사",
        "is_active": true,
        "date_joined": "2022-07-20T05:07:11Z",
        "last_login": "2022-08-03T04:37:42.073Z"
    }
}
```
**실패**  
**status**  403
```
{
    "success": false,
    "message": "로그인 실패"
}
```

## 로그아웃 `POST auth/logout`
쿠키에 sessionid를 제거합니다.
### Response
**성공**  
**status** 200  
```
{
    "success": true,
    "message": "로그아웃 성공"
}
