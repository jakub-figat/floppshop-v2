import { backendPort } from 'config/variables';
import { AbstractHttpService } from './AbstractHttpService';
import { MakeRequestParams } from '../types';
import axios, { AxiosResponse } from 'axios';

export class HttpService extends AbstractHttpService {
  protected makeRequest({
    url,
    method,
    body,
  }: MakeRequestParams): Promise<AxiosResponse<any, any>> {
    const concatenatedUrl = HttpService.attachEndpointToPort(backendPort, url);
    const contentType = HttpService.setContentTypeHeader(method);

    const requestConfig = {
      data: body,
      method,
      headers: contentType,
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
