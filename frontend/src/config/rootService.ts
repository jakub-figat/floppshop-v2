import { AuthService } from 'common/services/AuthService';
import { HttpServicce } from 'common/services/HttpService';

export const httpService = new HttpServicce();
export const authService = new AuthService(httpService);
