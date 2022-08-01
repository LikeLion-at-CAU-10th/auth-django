# 로그인 `POST auth/login`
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
    "message": "로그인 성공"
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

# 로그아웃 `POST auth/logout`
쿠키에 sessionid를 제거합니다.
### Response
**성공**  
**status** 200  
```
{
    "success": true,
    "message": "로그아웃 성공"
}