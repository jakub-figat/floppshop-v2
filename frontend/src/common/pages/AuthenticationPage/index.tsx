import { useLocation } from 'react-router';
import RegisterForm from './RegisterForm';
import LoginForm from './LoginForm';
import * as S from './styles';

const AuthenticationPage = () => {
  const { pathname } = useLocation();
  return (
    <S.PageWrapper>{pathname === '/user/login' ? <LoginForm /> : <RegisterForm />}</S.PageWrapper>
  );
};

export default AuthenticationPage;
