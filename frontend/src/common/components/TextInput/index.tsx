import { useField } from 'formik';
import * as S from './styles';

interface TextInputProps {
  type: string;
  name: string;
  label?: string;
  placeholder?: string;
}

const TextInput: React.FC<TextInputProps> = ({ ...props }) => {
  const [field, meta] = useField(props);

  return (
    <>
      <S.Input {...field} {...props} />
      {meta.error && meta.touched && <S.ErrorMessage>{meta.error}</S.ErrorMessage>}
    </>
  );
};

export default TextInput;
