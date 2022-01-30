import { AppEndpoints } from 'config/variables';

export enum HttpRequestMethod {
  GET = 'GET',
  POST = 'POST',
  PUT = 'PUT',
  DELETE = 'DELETE',
  PATCH = 'PATCH',
}

export type MakeRequestParams = {
  url: AppEndpoints;
  method: HttpRequestMethod;
  body?: any;
  responseType?: any;
  withCredentials?: boolean;
};

export interface HttpResponse<T = unknown> {
  headers: Record<string, string>;
  status: number;
  url: string;
  data: T;
}
