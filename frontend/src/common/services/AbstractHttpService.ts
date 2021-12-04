const enum HttpRequestMethod {
    GET = 'GET',
    POST = 'POST',
    PUT = 'PUT',
    DELETE = 'DELETE',
    PATCH = 'PATCH',
}

type GenericHttpRequestParams = {
    url: string,
    responseType?: number,
    withCredentials?: boolean,
}

export type MakeRequestParams = {
    url: string,
    method: HttpRequestMethod,
    body?: unknown;
    responseType?: any
    withCredentials?: boolean;
}

type HttpGetRequest = GenericHttpRequestParams;
type HttpPostRequest = GenericHttpRequestParams & { body?: unknown };
type HttpPutRequest = GenericHttpRequestParams & { body?: unknown };
type HttpDeleteRequest = GenericHttpRequestParams;

export abstract class AbstractHttpService {

    public get({url} : HttpGetRequest) : Promise<any> {
        return this.makeRequest({
            url,
            method: HttpRequestMethod.GET
        })
    }

    public post({url}: HttpPostRequest) : Promise<any> {
        return this.makeRequest({
            url,
            method: HttpRequestMethod.POST
        })
    }

    public put({url}: HttpPutRequest) : Promise<any> {
        return this.makeRequest({
            url,
            method: HttpRequestMethod.PUT
        })
    }

    public delete({url}: HttpDeleteRequest) : Promise<any> {
        return this.makeRequest({
            url,
            method: HttpRequestMethod.DELETE
        })
    }

    protected abstract makeRequest({
        url,
        method,
        responseType,
        withCredentials
}: MakeRequestParams) : Promise<any>


} 