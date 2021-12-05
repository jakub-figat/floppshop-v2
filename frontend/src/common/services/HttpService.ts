import { backendPort } from 'config/variables';
import { AbstractHttpService } from './AbstractHttpService';
import { MakeRequestParams } from './types';
import axios, { AxiosResponse } from 'axios';

export class HttpServicce extends AbstractHttpService {
  protected makeRequest({
    url,
    method,
    body,
  }: MakeRequestParams): Promise<AxiosResponse<any, any>> {
    const concatenatedUrl = HttpServicce.attachEndpointToPort(backendPort, url);

    const headers = {
      'content-type': 'application/json',
    };

    const requestConfig = {
      body,
      method,
      headers,
    };

    return axios(concatenatedUrl, requestConfig)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw new Error(error);
      });
  }
}
