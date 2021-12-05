export const backendPort = 'http://localhost:8000';

export enum ApplicationRoutes {
  main = '/',
  register = '/user/register',
  login = '/user/login',
  notFound = '*',
}

export const userEndpoints = {
  register: '/api/users/register',
  login: '/api/users/login',
  getUsers: '/api/users',
  getLoggedUser: '/api/user/me',
  updateUser: '/api/users/me',
} as const;
const productsEndpoints = {
  getProducts: '/api/products',
} as const;

export type ApiMethods = typeof userEndpoints & typeof productsEndpoints;

export type AppEndpoints = ApiMethods[keyof ApiMethods];
