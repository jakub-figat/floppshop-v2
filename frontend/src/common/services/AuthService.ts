import { HttpServicce } from './HttpService';

const url = 'localhost:8000/api/user/register';

export class AuthService {
  constructor(private httpService: HttpServicce) {}

  public register(userData: any): Promise<any> {
    return this.httpService
      .get({ url })
      .then(response => {
        return response;
      })
      .catch(error => {
        throw new Error(error);
      });
  }
}
