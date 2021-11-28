import { useParams } from 'react-router';
import RegisterForm from './RegisterForm';
import * as S from './styles';

const AuthenticationPage = () => {
  return (
    <S.PageWrapper>
      <RegisterForm />
    </S.PageWrapper>
  );
};

export default AuthenticationPage;
