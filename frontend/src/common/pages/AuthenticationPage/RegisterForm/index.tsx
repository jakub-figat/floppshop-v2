import { Formik } from 'formik';
import { registerSchema } from '../validationSchema';
import TextInput from 'common/components/TextInput';
import CaracalIcon from 'assets/icons/CaracalLogo.svg';
import * as S from '../styles';
import { authService } from 'config/rootService';

const RegisterForm = () => {
  const createAccount = (values: any) => {
    console.log('cos');
    authService.register(values).then(response => console.log(response, 'lord pazdan'));
  };

  return (
    <S.AuthBoxWrapper>
      <S.Icon src={CaracalIcon} />
      <S.HeadingWrapper>
        <S.FormHeading>floppshop</S.FormHeading>
        <S.SubHeading>Your favorite pet shop</S.SubHeading>
      </S.HeadingWrapper>
      <Formik
        initialValues={{
          firstName: '',
          lastName: '',
          username: '',
          email: '',
          dateOfBirth: '2021-12-01',
          password: '',
          password2: '',
        }}
        validationSchema={registerSchema}
        onSubmit={values => {
          console.log(values, 'values');
          createAccount(values);
        }}
      >
        {formik => (
          <S.Form onSubmit={formik.handleSubmit}>
            <TextInput name="firstName" type="text" placeholder="First name" />
            <TextInput name="lastName" type="text" placeholder="Last name" />
            <TextInput name="username" type="text" placeholder="Username" />
            <TextInput name="email" type="text" placeholder="Email" />
            <TextInput name="password" type="text" placeholder="Password" />
            <TextInput name="password2" type="text" placeholder="Repeat password" />
            <S.SubmitButton type="submit">Sign up</S.SubmitButton>
          </S.Form>
        )}
      </Formik>
      <S.AuthInformationWrapper>
        <S.AccountMessage>Already have an account?</S.AccountMessage>
        <S.RedirectLink to="/user/login">Log in</S.RedirectLink>
      </S.AuthInformationWrapper>
    </S.AuthBoxWrapper>
  );
};

export default RegisterForm;
