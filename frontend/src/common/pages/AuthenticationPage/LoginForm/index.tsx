import { Formik } from 'formik';
import { loginSchema } from '../validationSchema';
import TextInput from 'common/components/TextInput';
import * as S from '../styles';
import CaracalIcon from 'assets/icons/CaracalLogo.svg';

const LoginForm = () => {
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
          password: '',
        }}
        validationSchema={loginSchema}
        onSubmit={values => console.log(values)}
      >
        {formik => (
          <S.Form onSubmit={formik.handleSubmit}>
            <TextInput name="email" type="text" placeholder="Email" />
            <TextInput name="password" type="text" placeholder="Password" />
            <S.SubmitButton type="submit">Sign in</S.SubmitButton>
          </S.Form>
        )}
      </Formik>
      <S.AuthInformationWrapper>
        <S.AccountMessage>Don't have an account?</S.AccountMessage>
        <S.RedirectLink to="/user/register">Create account</S.RedirectLink>
      </S.AuthInformationWrapper>
    </S.AuthBoxWrapper>
  );
};

export default LoginForm;
