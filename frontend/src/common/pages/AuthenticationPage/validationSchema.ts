import * as Yup from 'yup';

export const registerSchema = Yup.object().shape({
  firstName: Yup.string().max(32, '').required(''),
  lastName: Yup.string().max(32, '').required(''),
  email: Yup.string().email('').required(''),
  password: Yup.string().min(8, '').max(32, ''),
  repeatPassword: Yup.string()
    .min(8, '')
    .max(32, '')
    .oneOf([Yup.ref('password'), null], 'Passwords must match'),
});

export const loginSchema = Yup.object({});
