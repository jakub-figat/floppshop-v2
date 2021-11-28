import styled from 'styled-components';
import { fontSize } from 'styles/stylesConfig';

export const FormWrapper = styled.div`
  width: 30rem;
  height: 40rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
`;

export const FormHeading = styled.h2`
  font-size: ${fontSize.large};
`;

export const SubHeading = styled.p`
  font-size: ${fontSize.normal};
`;
