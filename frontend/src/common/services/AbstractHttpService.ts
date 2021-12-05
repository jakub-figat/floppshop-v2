import { AppEndpoints } from 'config/variables';
import { HttpRequestMethod, MakeRequestParams } from './types';

type GenericHttpRequestParams = {
  url: AppEndpoints;
  responseType?: number;
  withCredentials?: boolean;
};

type HttpGetRequest = GenericHttpRequestParams;
type HttpPostRequest = GenericHttpRequestParams & { body?: unknown };
type HttpPutRequest = GenericHttpRequestParams & { body?: unknown };
type HttpDeleteRequest = GenericHttpRequestParams;

export abstract class AbstractHttpService {
  public get<R>({ url }: HttpGetRequest): Promise<R> {
    return this.makeRequest({
      url,
      method: HttpRequestMethod.GET,
    });
  }

  public post({ url, body }: HttpPostRequest): Promise<any> {
    return this.makeRequest({
      url,
      method: HttpRequestMethod.POST,
      body,
    });
  }

  public put({ url, body }: HttpPutRequest): Promise<any> {
    return this.makeRequest({
      url,
      method: HttpRequestMethod.PUT,
      body,
    });
  }

  public delete({ url }: HttpDeleteRequest): Promise<any> {
    return this.makeRequest({
      url,
      method: HttpRequestMethod.DELETE,
    });
  }

  protected abstract makeRequest({
    url,
    method,
    body,
    responseType,
    withCredentials,
  }: MakeRequestParams): Promise<any>;

  public static attachEndpointToPort = (backendPort: string, url: AppEndpoints): string => {
    return backendPort.concat(url);
  };

  public static setContentTypeHeader(method: HttpRequestMethod): Record<string, string> {
    const isJsonData = method === HttpRequestMethod.POST || HttpRequestMethod.PUT;

    return isJsonData ? { 'content-type': 'application/json' } : {};
  }
}
