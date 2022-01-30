import { AuthService } from 'common/services/AuthService';
import { HttpService } from 'common/services/http';

export const httpService = new HttpService();
export const authService = new AuthService(httpService);
