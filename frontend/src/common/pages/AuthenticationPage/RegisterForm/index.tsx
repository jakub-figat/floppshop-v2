import { Formik } from 'formik';
import { registerSchema, loginSchema } from '../validationSchema';
import TextInput from 'common/components/TextInput';
import CaracalIcon from 'assets/icons/CaracalLogo.svg';
import * as S from '../styles';

const RegisterForm = () => {
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
        validationSchema={registerSchema}
        onSubmit={values => console.log(values)}
      >
        {formik => (
          <S.Form onSubmit={formik.handleSubmit}>
            <TextInput name="firstName" type="text" placeholder="First name" />
            <TextInput name="lastName" type="text" placeholder="Last name" />
            <TextInput name="username" type="text" placeholder="Username" />
            <TextInput name="password" type="text" placeholder="Password" />
            <TextInput name="repeatPassword" type="text" placeholder="Repeat password" />
            <S.SubmitButton type="submit">Sign up</S.SubmitButton>
          </S.Form>
        )}
      </Formik>
      <S.AuthInformationWrapper>
        <S.AccountMessage>Don't have an account?</S.AccountMessage>
        <S.RedirectLink to="/login">Create account</S.RedirectLink>
      </S.AuthInformationWrapper>
    </S.AuthBoxWrapper>
  );
};

export default RegisterForm;
