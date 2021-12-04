import { AbstractHttpService, MakeRequestParams } from './AbstractHttpService';
import axios from 'axios';

export class HttpServicce extends AbstractHttpService {
  protected makeRequest({
    url,
    method,
    body,
    responseType,
    withCredentials,
  }: MakeRequestParams): any {
    // const bodyData = body && JSON.stringify(body);
    const headers = {
      'content-type': 'application/json',
    };
    const options = {
      body,
      method,
      headers,
      responseType,
    };

    return axios(url, options)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw new Error(error);
      });
  }
}
