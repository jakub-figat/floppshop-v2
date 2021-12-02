import styled from 'styled-components';
import { colors, fontSize } from 'styles/stylesConfig';

export const Input = styled.input`
  appearance: none;
  margin: 0.2rem 0;
  padding: 6px 12px;
  width: 100%;
  height: 3rem;
  font-size: ${fontSize.normal};
  font-weight: 400;
  color: #212529;
  background-color: ${colors.white};
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 7px;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  :focus {
    color: #212529;
    background-color: ${colors.white};
    border-color: ${colors.inputBorder};
    outline: 0;
    box-shadow: 0 0 0 0.1rem ${colors.inputBorder};
  }
`;

export const ErrorMessage = styled.div`
  font-size: ${fontSize.xSmall};
  color: ${colors.errorMessage};
  width: 100%;
  text-align: start;
`;
