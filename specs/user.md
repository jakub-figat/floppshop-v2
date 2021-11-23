## Users

### User

```ts
type User = {
  id: UUID;
  firstName: string;
  lastName: string;
  username: string;
  email: string;
  dateOfBirth: Time;
  isActive: boolean;
};
```

### Registration

`POST /api/v1/users/register` returns `User`
```ts
type RegisterBody = {
  firstName: string;
  lastName: string;
  username: string;
  email: string;
  dateOfBirth: Time;
  password: string;
  password2: string;
};
```

### List, detail

`GET /api/v1/users` returns `Array<User>`

`GET /api/v1/users/{id}` returns `User`