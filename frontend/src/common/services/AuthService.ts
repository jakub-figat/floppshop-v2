import { HttpService } from './http';
import { userEndpoints } from 'config/variables';

export class AuthService {
  constructor(private readonly httpService: HttpService) {}

  public register(body: unknown): Promise<any> {
    return this.httpService
      .post({ url: userEndpoints.register, body })
      .then(response => {
        return response;
      })
      .catch(error => {
        throw new Error(error);
      });
  }

  public login(body: unknown): Promise<any> {
    return this.httpService
      .post({ url: userEndpoints.login, body })
      .then(response => {
        return response;
      })
      .catch(error => {
        throw new Error(error);
      });
  }
}
