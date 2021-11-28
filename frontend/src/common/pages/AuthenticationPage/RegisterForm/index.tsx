import { Formik } from 'formik';
import { registerSchema, loginSchema } from '../validationSchema';
import TextInput from 'common/components/TextInput';
import CaracalIcon from 'assets/icons/CaracalLogo.svg';
import {
  AuthBoxWrapper,
  FormHeading,
  HeadingWrapper,
  SubHeading,
  Form,
  SubmitButton,
  AuthInformationWrapper,
  AccountMessage,
  RedirectLink,
  Icon,
} from '../styles';

const RegisterForm = () => {
  return (
    <AuthBoxWrapper>
      {/* a place for an cat icon */}
      <Icon src={CaracalIcon} />
      <HeadingWrapper>
        <FormHeading>floppshop</FormHeading>
        <SubHeading>Your favorite pet shop</SubHeading>
      </HeadingWrapper>
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
          <Form onSubmit={formik.handleSubmit}>
            <TextInput name="firstName" type="text" placeholder="First name" />
            <TextInput name="lastName" type="text" placeholder="Last name" />
            <TextInput name="username" type="text" placeholder="Username" />
            <TextInput name="password" type="text" placeholder="Password" />
            <TextInput name="repeatPassword" type="text" placeholder="Repeat password" />
            <SubmitButton type="submit">Sign up</SubmitButton>
          </Form>
        )}
      </Formik>
      <AuthInformationWrapper>
        <AccountMessage>Don't have an account?</AccountMessage>
        <RedirectLink to="/login">Create account</RedirectLink>
      </AuthInformationWrapper>
    </AuthBoxWrapper>
  );
};

export default RegisterForm;

// firstname
// lastname
// username
// 2x password
